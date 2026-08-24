from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
import hashlib
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "question_banks/TMA2_R00_2026KW_C1N.md"
SOURCE = ROOT / "doc/TMA2_R00_2026KW_C1N.pdf"


def question_block(text: str, question_id: str) -> str:
    match = re.search(
        rf"(?ms)^## {re.escape(question_id)}\s*$\n(.*?)(?=^## TMA2-Q-|\Z)",
        text,
    )
    if not match:
        raise AssertionError(f"missing question block: {question_id}")
    return match.group(1)


class Tma2SourceTruthRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = BANK.read_text(encoding="utf-8")

    def test_source_identity_and_question_set_are_frozen(self):
        expected_hash = (
            "3398e3fd6425ecdc85d2f187fa8f44b9f7c19c356e262faab65bdc3010dd6851"
        )
        self.assertIn("source_pdf: TMA2_R00_2026KW_C1N.pdf", self.text)
        self.assertIn(f"source_sha256: {expected_hash}", self.text)
        self.assertIn("source_pages: 38", self.text)
        self.assertEqual(hashlib.sha256(SOURCE.read_bytes()).hexdigest(), expected_hash)

        ids = re.findall(r"(?m)^## (TMA2-Q-\d{4})$", self.text)
        self.assertEqual(ids, [f"TMA2-Q-{index:04d}" for index in range(1, 26)])

    def test_question_statistics_match_frozen_types(self):
        expected = {
            "FACT": 3,
            "SPEC_LOOKUP": 2,
            "MODEL": 2,
            "TABLE": 5,
            "CALCULATION": 2,
            "CHART": 2,
            "PROCEDURE": 5,
            "CAUTION": 4,
        }
        actual = Counter(re.findall(r"(?m)^\*\*Type: ([A-Z_]+)\*\*$", self.text))
        self.assertEqual(actual, Counter(expected))
        self.assertIn("- Total: 25", self.text)
        for question_type, count in expected.items():
            self.assertIn(f"- {question_type}: {count}", self.text)

    def test_question_scoring_is_atomic_and_totals_100(self):
        for index in range(1, 26):
            question_id = f"TMA2-Q-{index:04d}"
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
        forward = Decimal("8.38") * Decimal("22") / (
            Decimal("75") - Decimal("24.5")
        )
        pressure = (
            Decimal("5.0") * (Decimal("100") - Decimal("30")) / Decimal("16.63")
        )
        rounded_pressure = pressure.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
        back_substitution = (
            Decimal("16.63") * rounded_pressure / (Decimal("100") - Decimal("30"))
        )

        self.assertEqual(
            forward.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP), Decimal("3.7")
        )
        self.assertEqual(rounded_pressure, Decimal("21.0"))
        self.assertEqual(
            back_substitution.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP),
            Decimal("5.0"),
        )

        forward_block = question_block(self.text, "TMA2-Q-0011")
        inverse_block = question_block(self.text, "TMA2-Q-0012")
        for required in ("3.650693... kN", "ROUND_HALF_UP", "3.7 kN"):
            self.assertIn(required, forward_block)
        for required in ("21.046301... MPa", "21.0 MPa", "4.989 kN", "5.0 kN"):
            self.assertIn(required, inverse_block)

    def test_chart_gold_keeps_visual_evidence_and_tolerances(self):
        force = question_block(self.text, "TMA2-Q-0013")
        eccentricity = question_block(self.text, "TMA2-Q-0014")

        for block in (force, eccentricity):
            self.assertIn("**Type: CHART**", block)
            self.assertIn("- Evidence type: CHART", block)
            self.assertIn("视觉读取", block)

        for required in ("约为 **1.1 kN**", "0.9-1.3 kN", "Gold: 1.1 kN"):
            self.assertIn(required, force)
        for required in ("约为 **40 mm**", "37-43 mm", "Gold: 40 mm"):
            self.assertIn(required, eccentricity)

    def test_model_grammar_and_document_common_boundaries_are_frozen(self):
        model = question_block(self.text, "TMA2-Q-0001")
        self.assertIn(
            "TMA<本体尺寸><设计编号>-2<配管方式><压板方向>", self.text
        )
        self.assertIn("- Binding: EXACT_MODEL", model)
        self.assertIn("`TMA0401-2CC`", model)

        for question_id in (
            "TMA2-Q-0019",
            "TMA2-Q-0021",
            "TMA2-Q-0024",
            "TMA2-Q-0025",
        ):
            block = question_block(self.text, question_id)
            self.assertIn("- Binding: DOCUMENT_COMMON", block)
            self.assertIn("- Model / Scope: TMA2_R00_2026KW_C1N.pdf :: ", block)

    def test_tma_and_accessory_boundaries_are_frozen(self):
        speed = question_block(self.text, "TMA2-Q-0020")
        self.assertIn("- Binding: PRODUCT_SERIES", speed)
        self.assertIn("夹紧侧和释放侧都必须采用进油节流", speed)
        self.assertIn("禁止采用回油节流", speed)

        bzt = question_block(self.text, "TMA2-Q-0022")
        for required in ("`BZT0101-A`", "`TMA1001-2C□`", "G1/8A", "35 MPa", "10 MPa"):
            self.assertIn(required, bzt)

        tmz = question_block(self.text, "TMA2-Q-0023")
        for required in (
            "`TMZ0400-2MB`",
            "`TMA0401-2`",
            "A=16 mm",
            "B=61 mm",
            "L=75 mm",
            "`OR NBR-90 P5-N`",
        ):
            self.assertIn(required, tmz)

        fitting = question_block(self.text, "TMA2-Q-0024")
        self.assertIn("包层密封件", fitting)
        self.assertIn("使用 O 形密封圈", fitting)
        self.assertIn("不能采用本页所示的 G 螺纹接头密封方式", fitting)

    def test_high_and_medium_coverage_rows_are_reconciled(self):
        rows = {
            match.group(1): match.group(0)
            for match in re.finditer(r"(?m)^\| (TMA2-SI-\d{3}) \|.*\|$", self.text)
        }
        self.assertEqual(
            sorted(rows), [f"TMA2-SI-{index:03d}" for index in range(1, 16)]
        )
        for row_id, row in rows.items():
            if "| HIGH：" in row or "| MEDIUM：" in row:
                self.assertTrue("TMA2-Q-" in row or "排除" in row, row_id)

        self.assertIn("控制阀 > 全般与种类", rows["TMA2-SI-011"])
        self.assertNotIn("标示变更通知", rows["TMA2-SI-011"])

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
