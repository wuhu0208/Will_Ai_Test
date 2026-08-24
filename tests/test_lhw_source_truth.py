from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
import hashlib
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "question_banks/LHW_R00_2023KW_C1N.md"
SOURCE = ROOT / "doc/LHW_R00_2023KW_C1N.pdf"


def question_block(text: str, question_id: str) -> str:
    match = re.search(
        rf"(?ms)^## {re.escape(question_id)}\s*$\n(.*?)(?=^## LHW-Q-|\Z)", text
    )
    if not match:
        raise AssertionError(f"missing question block: {question_id}")
    return match.group(1)


class LhwSourceTruthRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = BANK.read_text(encoding="utf-8")

    def test_source_identity_and_question_set_are_frozen(self):
        expected_hash = (
            "9d4fe66046dd69a803ca21aca3f35a52d58fe566d10577d5e7a72b5a7a69e27f"
        )
        self.assertIn("source_pdf: LHW_R00_2023KW_C1N.pdf", self.text)
        self.assertIn(f"source_sha256: {expected_hash}", self.text)
        self.assertIn("source_pages: 52", self.text)
        self.assertEqual(hashlib.sha256(SOURCE.read_bytes()).hexdigest(), expected_hash)
        ids = re.findall(r"(?m)^## (LHW-Q-\d{4})$", self.text)
        self.assertEqual(ids, [f"LHW-Q-{index:04d}" for index in range(1, 29)])

    def test_statistics_and_scoring_are_frozen(self):
        expected = {
            "MODEL": 2,
            "FACT": 1,
            "SPEC_LOOKUP": 3,
            "TABLE": 5,
            "CALCULATION": 2,
            "CHART": 2,
            "PROCEDURE": 6,
            "CAUTION": 7,
        }
        actual = Counter(re.findall(r"(?m)^\*\*Type: ([A-Z_]+)\*\*$", self.text))
        self.assertEqual(actual, Counter(expected))
        self.assertIn("- Total: 28", self.text)
        for question_type, count in expected.items():
            self.assertIn(f"- {question_type}: {count}", self.text)

        for index in range(1, 29):
            question_id = f"LHW-Q-{index:04d}"
            block = question_block(self.text, question_id)
            scoring = re.search(
                r"(?ms)^### Scoring Standard\s*$\n(.*?)(?=^### Accepted Variants)", block
            )
            self.assertIsNotNone(scoring, question_id)
            points = re.findall(r"(?m)^- P(\d+) \[(\d+)]\s*:\s*(\S.*)$", scoring.group(1))
            self.assertEqual(
                [int(point_id) for point_id, _, _ in points],
                list(range(1, len(points) + 1)),
                question_id,
            )
            self.assertEqual(sum(int(weight) for _, weight, _ in points), 100, question_id)

    def test_calculation_gold_is_deterministic_and_exact(self):
        forward = Decimal("5.0") * (
            Decimal(1) - Decimal("0.0009") * Decimal("90")
        ) / (Decimal("1.4892") + Decimal("0.0018") * Decimal("90"))
        inverse = Decimal("5.0") * (
            Decimal("0.7822") + Decimal("0.0010") * Decimal("120")
        ) / (Decimal(1) - Decimal("0.0009") * Decimal("120"))
        self.assertEqual(
            forward.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP), Decimal("2.8")
        )
        self.assertEqual(
            inverse.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP), Decimal("5.1")
        )
        back = Decimal("5.1") * (
            Decimal(1) - Decimal("0.0009") * Decimal("120")
        ) / (Decimal("0.7822") + Decimal("0.0010") * Decimal("120"))
        self.assertEqual(
            back.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP), Decimal("5.0")
        )
        forward_block = question_block(self.text, "LHW-Q-0012")
        inverse_block = question_block(self.text, "LHW-Q-0013")
        for required in ("2.7828246124... kN", "2.8 kN", "ROUND_HALF_UP"):
            self.assertIn(required, forward_block)
        for required in ("5.0571748879... MPa", "5.1 MPa", "5.0423409444... kN"):
            self.assertIn(required, inverse_block)

    def test_chart_gold_is_visual_and_toleranced(self):
        force = question_block(self.text, "LHW-Q-0014")
        action = question_block(self.text, "LHW-Q-0015")
        for block in (force, action):
            self.assertIn("**Type: CHART**", block)
            self.assertIn("- Evidence type: CHART", block)
        for required in ("视觉 Gold", "约 3.1 kN", "3.0～3.2 kN", "不能替代"):
            self.assertIn(required, force)
        for required in ("0.44 s", "0.22 s", "0.90 s", "0.45 s", "CHART tolerance"):
            self.assertIn(required, action)

    def test_model_sensor_speed_and_accessory_boundaries_are_frozen(self):
        model = question_block(self.text, "LHW-Q-0001")
        for required in ("LHW0481-CRE-A", "φD=48 mm", "夹紧时顺时针", "快换压板 A 型"):
            self.assertIn(required, model)

        states = question_block(self.text, "LHW-Q-0005")
        for required in ("E 为夹紧和释放", "H 仅确认夹紧", "J 仅确认释放", "夹紧确认 ON"):
            self.assertIn(required, states)

        air = question_block(self.text, "LHW-Q-0006")
        for required in ("ISA3-G", "GPS3-E", "0.1～0.2 MPa", "5 m 以内"):
            self.assertIn(required, air)

        speed = question_block(self.text, "LHW-Q-0026")
        self.assertIn("夹紧侧和释放侧均应采用回油节流", speed)
        self.assertIn("LHW 不在其中", speed)

        bzl = question_block(self.text, "LHW-Q-0023")
        for required in ("BZL0101-B", "BZL0201-B", "0.12 MPa", "2.6 mm²", "5.0 mm²"):
            self.assertIn(required, bzl)

        lzh = question_block(self.text, "LHW-Q-0021")
        for required in ("LZH0550-T", "LZH0550-A", "LZH0551-W", "S50CH"):
            self.assertIn(required, lzh)

    def test_document_common_bindings_are_page_bounded(self):
        for index in range(25, 29):
            block = question_block(self.text, f"LHW-Q-{index:04d}")
            self.assertIn("- Binding: DOCUMENT_COMMON", block)
            self.assertIn("- Model / Scope: LHW_R00_2023KW_C1N.pdf :: ", block)
            self.assertRegex(block, r"- Physical page: 3[1-3]")
            self.assertIn("- Local scope path:", block)

    def test_coverage_rows_and_delivery_are_reconciled(self):
        rows = {
            match.group(1): match.group(0)
            for match in re.finditer(r"(?m)^\| (LHW-SI-\d{3}) \|.*\|$", self.text)
        }
        self.assertEqual(sorted(rows), [f"LHW-SI-{index:03d}" for index in range(1, 15)])
        for row_id, row in rows.items():
            if "| HIGH：" in row or "| MEDIUM：" in row:
                self.assertTrue("LHW-Q-" in row or "排除" in row, row_id)

        for token in (
            "internal checkpoint",
            "next work package",
            "developer notes",
            "WP1",
            "WP2",
            "WP3",
            "WP4",
            "WP5",
        ):
            self.assertNotIn(token, self.text)


if __name__ == "__main__":
    unittest.main()
