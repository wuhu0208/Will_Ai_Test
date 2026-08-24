from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
import hashlib
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "question_banks/TMA1_R00_2023KW_C1N.md"
SOURCE = ROOT / "doc/TMA1_R00_2023KW_C1N.pdf"


def question_block(text: str, question_id: str) -> str:
    match = re.search(
        rf"(?ms)^## {re.escape(question_id)}\s*$\n(.*?)(?=^## TMA1-Q-|\Z)",
        text,
    )
    if not match:
        raise AssertionError(f"missing question block: {question_id}")
    return match.group(1)


class Tma1SourceTruthRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = BANK.read_text(encoding="utf-8")

    def test_source_identity_and_question_set_are_frozen(self):
        expected_hash = (
            "f977e61f182c5017a30235b61e7a208ab90152abcd4a473cb608c180bdc22b3c"
        )
        self.assertIn("source_pdf: TMA1_R00_2023KW_C1N.pdf", self.text)
        self.assertIn(f"source_sha256: {expected_hash}", self.text)
        self.assertIn("source_pages: 40", self.text)
        self.assertEqual(hashlib.sha256(SOURCE.read_bytes()).hexdigest(), expected_hash)

        ids = re.findall(r"(?m)^## (TMA1-Q-\d{4})$", self.text)
        self.assertEqual(ids, [f"TMA1-Q-{index:04d}" for index in range(1, 29)])

    def test_question_statistics_match_frozen_types(self):
        expected = {
            "FACT": 3,
            "SPEC_LOOKUP": 2,
            "MODEL": 5,
            "TABLE": 6,
            "CALCULATION": 2,
            "CHART": 2,
            "PROCEDURE": 4,
            "CAUTION": 4,
        }
        actual = Counter(re.findall(r"(?m)^\*\*Type: ([A-Z_]+)\*\*$", self.text))
        self.assertEqual(actual, Counter(expected))
        self.assertIn("- Total: 28", self.text)
        for question_type, count in expected.items():
            self.assertIn(f"- {question_type}: {count}", self.text)

    def test_question_scoring_is_atomic_and_totals_100(self):
        for index in range(1, 29):
            question_id = f"TMA1-Q-{index:04d}"
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
        forward = (Decimal("6.93") * Decimal("22") - Decimal("6.35")) / (
            Decimal("75") - Decimal("24.5")
        )
        pressure = (
            Decimal("5.0") * (Decimal("100") - Decimal("30")) + Decimal("13.26")
        ) / Decimal("13.25")
        rounded_pressure = pressure.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
        back_substitution = (
            Decimal("13.25") * rounded_pressure - Decimal("13.26")
        ) / (Decimal("100") - Decimal("30"))

        self.assertEqual(
            forward.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP), Decimal("2.9")
        )
        self.assertEqual(rounded_pressure, Decimal("27.4"))
        self.assertEqual(
            back_substitution.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP),
            Decimal("5.0"),
        )

        forward_block = question_block(self.text, "TMA1-Q-0010")
        inverse_block = question_block(self.text, "TMA1-Q-0011")
        for required in ("2.893267... kN", "ROUND_HALF_UP", "2.9 kN"):
            self.assertIn(required, forward_block)
        for required in ("27.415849... MPa", "27.4 MPa", "4.997 kN", "5.0 kN"):
            self.assertIn(required, inverse_block)

    def test_chart_gold_keeps_visual_evidence_and_tolerances(self):
        force = question_block(self.text, "TMA1-Q-0012")
        eccentricity = question_block(self.text, "TMA1-Q-0013")

        for block in (force, eccentricity):
            self.assertIn("**Type: CHART**", block)
            self.assertIn("- Evidence type: CHART", block)
            self.assertIn("视觉读取", block)

        for required in ("约 **0.75 kN**", "0.55～0.95 kN", "0.75±0.20 kN"):
            self.assertIn(required, force)
        for required in ("约 **40 mm**", "37～43 mm", "40±3 mm"):
            self.assertIn(required, eccentricity)

    def test_model_grammar_and_document_common_boundaries_are_frozen(self):
        model = question_block(self.text, "TMA1-Q-0001")
        self.assertIn(
            "TMA<本体尺寸><设计编号>-1<配管方式><压板方向>", self.text
        )
        self.assertIn("- Binding: EXACT_MODEL", model)
        self.assertIn("`TMA0400-1CC`", model)

        for question_id in ("TMA1-Q-0021", "TMA1-Q-0023", "TMA1-Q-0024", "TMA1-Q-0025"):
            block = question_block(self.text, question_id)
            self.assertIn("- Binding: DOCUMENT_COMMON", block)
            self.assertIn(
                "- Model / Scope: TMA1_R00_2023KW_C1N.pdf :: ", block
            )

    def test_related_double_acting_tma_rule_does_not_bind_to_tma1(self):
        block = question_block(self.text, "TMA1-Q-0022")
        self.assertIn("- Binding: MODEL_FAMILY", block)
        self.assertIn("KOSMEK TMA 油压复动夹紧器（相关产品）", block)
        self.assertIn("不含 TMA-1 单动式", block)
        self.assertNotIn("- Model / Scope: TMA-1 复动夹紧器", block)
        self.assertIn("复动夹紧器的速度控制回路", block)
        self.assertIn("异常高压", block)
        self.assertIn("漏油或损坏", block)

    def test_high_and_medium_coverage_rows_are_reconciled(self):
        rows = {
            match.group(1): match.group(0)
            for match in re.finditer(r"(?m)^\| (TMA1-SI-\d{3}) \|.*\|$", self.text)
        }
        self.assertEqual(
            sorted(rows), [f"TMA1-SI-{index:03d}" for index in range(1, 19)]
        )
        for row_id, row in rows.items():
            if "| HIGH：" in row or "| MEDIUM：" in row:
                self.assertTrue("TMA1-Q-" in row or "排除" in row, row_id)

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
