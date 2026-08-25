from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
import hashlib
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "question_banks/TLA2_R00_2023KW_C1N.md"
SOURCE = ROOT / "doc/TLA2_R00_2023KW_C1N.pdf"


def question_block(text: str, question_id: str) -> str:
    match = re.search(
        rf"(?ms)^## {re.escape(question_id)}\s*$\n(.*?)(?=^## TLA2-Q-|\Z)",
        text,
    )
    if not match:
        raise AssertionError(f"missing question block: {question_id}")
    return match.group(1)


class Tla2SourceTruthRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = BANK.read_text(encoding="utf-8")

    def test_source_identity_and_question_set_are_frozen(self):
        expected_hash = (
            "414d0144f4c15755021f6da818150daf8f63d3fa4249a59cefd01f130a3bb0b4"
        )
        self.assertIn("source_pdf: TLA2_R00_2023KW_C1N.pdf", self.text)
        self.assertIn(f"source_sha256: {expected_hash}", self.text)
        self.assertIn("source_pages: 52", self.text)
        self.assertEqual(hashlib.sha256(SOURCE.read_bytes()).hexdigest(), expected_hash)

        ids = re.findall(r"(?m)^## (TLA2-Q-\d{4})$", self.text)
        self.assertEqual(ids, [f"TLA2-Q-{index:04d}" for index in range(1, 31)])

    def test_question_statistics_match_frozen_types(self):
        expected = {
            "FACT": 3,
            "SPEC_LOOKUP": 2,
            "MODEL": 6,
            "TABLE": 6,
            "CALCULATION": 3,
            "CHART": 2,
            "PROCEDURE": 3,
            "CAUTION": 5,
        }
        actual = Counter(re.findall(r"(?m)^\*\*Type: ([A-Z_]+)\*\*$", self.text))
        self.assertEqual(actual, Counter(expected))
        self.assertIn("- Total: 30", self.text)
        for question_type, count in expected.items():
            self.assertIn(f"- {question_type}: {count}", self.text)

    def test_question_scoring_is_atomic_and_totals_100(self):
        for index in range(1, 31):
            question_id = f"TLA2-Q-{index:04d}"
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
        standard_force = Decimal("25.0") / (
            Decimal("5.53") + Decimal("0.0147") * Decimal("80")
        )
        pressure = Decimal("7.5") * (
            Decimal("2.59") + Decimal("0.0046") * Decimal("100")
        )
        rounded_pressure = pressure.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
        back_substitution = rounded_pressure / Decimal("3.05")
        f1 = Decimal("120") / Decimal("200") * Decimal("0.417") * Decimal("25")
        f2 = Decimal("80") / Decimal("200") * Decimal("0.417") * Decimal("25")

        self.assertEqual(
            standard_force.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP),
            Decimal("3.7"),
        )
        self.assertEqual(pressure, Decimal("22.875"))
        self.assertEqual(rounded_pressure, Decimal("22.9"))
        self.assertEqual(
            back_substitution.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP),
            Decimal("7.5"),
        )
        self.assertEqual(
            f1.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP), Decimal("6.3")
        )
        self.assertEqual(
            f2.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP), Decimal("4.2")
        )

        required_by_question = {
            "TLA2-Q-0010": ("3.727... kN", "ROUND_HALF_UP", "3.7 kN"),
            "TLA2-Q-0011": ("22.875 MPa", "22.9 MPa", "7.508... kN", "7.5 kN"),
            "TLA2-Q-0012": ("6.255 kN", "6.3 kN", "4.170 kN", "4.2 kN"),
        }
        for question_id, required_tokens in required_by_question.items():
            block = question_block(self.text, question_id)
            for token in required_tokens:
                self.assertIn(token, block)

    def test_chart_gold_keeps_visual_evidence_and_tolerances(self):
        force = question_block(self.text, "TLA2-Q-0013")
        action_time = question_block(self.text, "TLA2-Q-0014")
        for block in (force, action_time):
            self.assertIn("**Type: CHART**", block)
            self.assertRegex(block, r"- Evidence type: CHART")
            self.assertIn("视觉", block)

        for required in ("约 **7.5 kN**", "7.2～7.8 kN", "±0.3 kN"):
            self.assertIn(required, force)
        for required in ("约 **0.43 秒以上**", "0.38～0.48 秒", "±0.05 秒"):
            self.assertIn(required, action_time)

    def test_model_options_and_double_acting_boundaries_are_frozen(self):
        model = question_block(self.text, "TLA2-Q-0001")
        self.assertIn(
            "TLA<主体尺寸><设计编号>-2<配管方式><夹紧旋转方向>-<选项>", self.text
        )
        self.assertIn("`TLA0801-2CR-Q`", model)

        options = question_block(self.text, "TLA2-Q-0006")
        for required in ("P 为双压板", "Q 为长行程", "Y30", "Y45", "Y60"):
            self.assertIn(required, options)

        circuit = question_block(self.text, "TLA2-Q-0025")
        for required in ("夹紧侧", "释放侧", "进油节流", "异常高压", "漏油或损坏"):
            self.assertIn(required, circuit)
        self.assertNotIn("单动夹紧器的速度控制", circuit)

    def test_option_specific_source_truth_is_frozen(self):
        double_arm = question_block(self.text, "TLA2-Q-0012")
        self.assertIn("P 双压板专用公式", double_arm)
        self.assertIn("F1 使用 L2/L3", double_arm)
        self.assertIn("F2 使用 L1/L3", double_arm)

        long_stroke = question_block(self.text, "TLA2-Q-0019")
        for required in ("36/11/25 mm", "15.0/32.7 cm³", "2.1 kg"):
            self.assertIn(required, long_stroke)

        special_angle = question_block(self.text, "TLA2-Q-0020")
        for required in ("19.5/6.5/13 mm", "20.6/7.6/13 mm", "21.7/8.7/13 mm"):
            self.assertIn(required, special_angle)

    def test_accessory_boundaries_are_frozen(self):
        bzt = question_block(self.text, "TLA2-Q-0028")
        for required in (
            "BZT0101-A",
            "TLA1601-2C□-□",
            "进油节流",
            "35/10 MPa",
            "0.04 MPa",
            "2.6 mm²",
            "10 N·m",
        ):
            self.assertIn(required, bzt)

        jzg = question_block(self.text, "TLA2-Q-0029")
        for required in ("JZG010", "G1/8A", "42 MPa", "低压"):
            self.assertIn(required, jzg)

        fitting = question_block(self.text, "TLA2-Q-0030")
        for required in ("9UKC00601E", "9UKP0C0001", "包层密封件"):
            self.assertIn(required, fitting)

    def test_document_common_bindings_and_coverage_are_reconciled(self):
        for question_id in (
            "TLA2-Q-0022",
            "TLA2-Q-0023",
            "TLA2-Q-0024",
            "TLA2-Q-0025",
            "TLA2-Q-0026",
            "TLA2-Q-0027",
        ):
            block = question_block(self.text, question_id)
            self.assertIn("- Binding: DOCUMENT_COMMON", block)
            self.assertIn("- Model / Scope: TLA2_R00_2023KW_C1N.pdf :: ", block)

        rows = {
            match.group(1): match.group(0)
            for match in re.finditer(r"(?m)^\| (TLA2-SI-\d{3}) \|.*\|$", self.text)
        }
        self.assertEqual(
            sorted(rows), [f"TLA2-SI-{index:03d}" for index in range(1, 18)]
        )
        for row_id, row in rows.items():
            if "| HIGH：" in row or "| MEDIUM：" in row:
                self.assertTrue("TLA2-Q-" in row or "排除" in row, row_id)

    def test_delivery_has_no_execution_artifacts(self):
        forbidden = (
            "后续构建",
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
