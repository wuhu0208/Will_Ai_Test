from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
import hashlib
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "question_banks/TLA1_R00_2023KW_C1N.md"
SOURCE = ROOT / "doc/TLA1_R00_2023KW_C1N.pdf"


def question_block(text: str, question_id: str) -> str:
    match = re.search(
        rf"(?ms)^## {re.escape(question_id)}\s*$\n(.*?)(?=^## TLA1-Q-|\Z)",
        text,
    )
    if not match:
        raise AssertionError(f"missing question block: {question_id}")
    return match.group(1)


class Tla1SourceTruthRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = BANK.read_text(encoding="utf-8")

    def test_source_identity_and_question_set_are_frozen(self):
        expected_hash = (
            "2fbe3bb3b2c2c6c264f5320f3f88aad56df8ed23af37afd5a1b680bafbb6c9e6"
        )
        self.assertIn("source_pdf: TLA1_R00_2023KW_C1N.pdf", self.text)
        self.assertIn(f"source_sha256: {expected_hash}", self.text)
        self.assertIn("source_pages: 40", self.text)
        self.assertEqual(hashlib.sha256(SOURCE.read_bytes()).hexdigest(), expected_hash)

        ids = re.findall(r"(?m)^## (TLA1-Q-\d{4})$", self.text)
        self.assertEqual(ids, [f"TLA1-Q-{index:04d}" for index in range(1, 29)])

    def test_question_statistics_match_frozen_types(self):
        expected = {
            "FACT": 3,
            "SPEC_LOOKUP": 1,
            "MODEL": 6,
            "TABLE": 7,
            "CALCULATION": 3,
            "CHART": 2,
            "PROCEDURE": 3,
            "CAUTION": 3,
        }
        actual = Counter(re.findall(r"(?m)^\*\*Type: ([A-Z_]+)\*\*$", self.text))
        self.assertEqual(actual, Counter(expected))
        self.assertIn("- Total: 28", self.text)
        for question_type, count in expected.items():
            self.assertIn(f"- {question_type}: {count}", self.text)

    def test_question_scoring_is_atomic_and_totals_100(self):
        for index in range(1, 29):
            question_id = f"TLA1-Q-{index:04d}"
            block = question_block(self.text, question_id)
            scoring = re.search(
                r"(?ms)^### Scoring Standard\s*$\n(.*?)(?=^### Accepted Variants)",
                block,
            )
            self.assertIsNotNone(scoring, question_id)
            points = re.findall(
                r"(?m)^- P(\d+) \[(\d+)]\s*:\s*(\S.*)$", scoring.group(1)
            )
            self.assertTrue(points, question_id)
            self.assertEqual(
                [int(point_id) for point_id, _, _ in points],
                list(range(1, len(points) + 1)),
                question_id,
            )
            self.assertEqual(
                sum(int(weight) for _, weight, _ in points), 100, question_id
            )

    def test_calculation_gold_is_deterministic(self):
        force = (Decimal("25.0") - Decimal("2.19")) / (
            Decimal("5.53") + Decimal("0.0178") * Decimal("80")
        )
        pressure = (
            Decimal("6.0")
            * (Decimal("2.60") + Decimal("0.0059") * Decimal("100"))
            + Decimal("2.00")
        )
        rounded_pressure = pressure.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
        back_substitution = (rounded_pressure - Decimal("2.00")) / Decimal("3.19")
        full_time = Decimal("0.61") * Decimal("22.5") / Decimal("9.5")

        self.assertEqual(
            force.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP), Decimal("3.3")
        )
        self.assertEqual(rounded_pressure, Decimal("21.1"))
        self.assertEqual(
            back_substitution.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP),
            Decimal("6.0"),
        )
        self.assertEqual(
            full_time.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
            Decimal("1.44"),
        )

        required_by_question = {
            "TLA1-Q-0010": ("3.280126... kN", "ROUND_HALF_UP", "3.3 kN"),
            "TLA1-Q-0011": ("21.14 MPa", "21.1 MPa", "5.987460... kN", "6.0 kN"),
            "TLA1-Q-0014": ("1.444736... s", "ROUND_HALF_UP", "1.44 秒"),
        }
        for question_id, required_tokens in required_by_question.items():
            block = question_block(self.text, question_id)
            for token in required_tokens:
                self.assertIn(token, block)

    def test_chart_gold_keeps_visual_evidence_and_tolerances(self):
        force = question_block(self.text, "TLA1-Q-0012")
        action_time = question_block(self.text, "TLA1-Q-0013")
        for block in (force, action_time):
            self.assertIn("**Type: CHART**", block)
            self.assertIn("- Evidence type: CHART", block)
            self.assertIn("视觉", block)

        for required in ("约 **6.6 kN**", "6.3～6.9 kN", "±0.3 kN"):
            self.assertIn(required, force)
        for required in ("约 **0.61 秒**", "0.56～0.66 秒", "±0.05 秒"):
            self.assertIn(required, action_time)

    def test_model_grammar_and_accessory_boundaries_are_frozen(self):
        model = question_block(self.text, "TLA1-Q-0001")
        self.assertIn(
            "TLA<主体尺寸><设计编号>-1<配管方式><夹紧旋转方向>", self.text
        )
        self.assertIn("- Binding: EXACT_MODEL", model)
        self.assertIn("`TLA0802-1CR`", model)

        bzt = question_block(self.text, "TLA1-Q-0026")
        for required in (
            "BZT0101-A",
            "TLA1602-1C□",
            "进油节流",
            "35 MPa",
            "10 MPa",
            "0.04 MPa",
            "2.6 mm²",
            "10 N·m",
        ):
            self.assertIn(required, bzt)

        jzg = question_block(self.text, "TLA1-Q-0027")
        for required in ("JZG010", "G1/8A", "42 MPa", "低压"):
            self.assertIn(required, jzg)

    def test_document_common_and_single_acting_boundaries_are_frozen(self):
        for question_id in (
            "TLA1-Q-0021",
            "TLA1-Q-0022",
            "TLA1-Q-0023",
            "TLA1-Q-0024",
            "TLA1-Q-0025",
        ):
            block = question_block(self.text, question_id)
            self.assertIn("- Binding: DOCUMENT_COMMON", block)
            self.assertIn(
                "- Model / Scope: TLA1_R00_2023KW_C1N.pdf :: ", block
            )

        circuit = question_block(self.text, "TLA1-Q-0022")
        self.assertIn("单动夹紧器", circuit)
        self.assertIn("横向安装释放", circuit)
        self.assertIn("进油节流", circuit)
        self.assertIn("异常高压、漏油或损坏", circuit)

    def test_high_and_medium_coverage_rows_are_reconciled(self):
        rows = {
            match.group(1): match.group(0)
            for match in re.finditer(r"(?m)^\| (TLA1-SI-\d{3}) \|.*\|$", self.text)
        }
        self.assertEqual(
            sorted(rows), [f"TLA1-SI-{index:03d}" for index in range(1, 16)]
        )
        for row_id, row in rows.items():
            if "| HIGH：" in row or "| MEDIUM：" in row:
                self.assertTrue("TLA1-Q-" in row or "排除" in row, row_id)

    def test_delivery_has_no_construction_or_execution_artifacts(self):
        forbidden = (
            "后续构建",
            "初始处置",
            "internal checkpoint",
            "next work package",
            "developer notes",
            "Playwright",
            "Selenium",
            "Timeout",
            "Retry",
            "WP1",
            "WP2",
            "WP3",
            "WP4",
            "WP5",
        )
        for token in forbidden:
            self.assertNotIn(token, self.text)


if __name__ == "__main__":
    unittest.main()
