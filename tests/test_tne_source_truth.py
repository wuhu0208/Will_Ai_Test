from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
import hashlib
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "question_banks/TNE_R01_2026KW_C1N.md"
SOURCE = ROOT / "doc/TNE_R01_2026KW_C1N.pdf"


def question_block(text: str, question_id: str) -> str:
    match = re.search(
        rf"(?ms)^## {re.escape(question_id)}\s*$\n(.*?)(?=^## TNE-Q-|\Z)",
        text,
    )
    if not match:
        raise AssertionError(f"missing question block: {question_id}")
    return match.group(1)


class TneSourceTruthRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = BANK.read_text(encoding="utf-8")

    def test_source_identity_and_question_set_are_frozen(self):
        expected_hash = (
            "898ac3440cc8b798790b20e0ed804d1f2f99ba6c5fe3697c161ad3bd01e81f16"
        )
        self.assertIn("source_pdf: TNE_R01_2026KW_C1N.pdf", self.text)
        self.assertIn(f"source_sha256: {expected_hash}", self.text)
        self.assertIn("source_pages: 40", self.text)
        self.assertEqual(hashlib.sha256(SOURCE.read_bytes()).hexdigest(), expected_hash)
        ids = re.findall(r"(?m)^## (TNE-Q-\d{4})$", self.text)
        self.assertEqual(ids, [f"TNE-Q-{index:04d}" for index in range(1, 26)])

    def test_statistics_match_frozen_question_types(self):
        expected = Counter(
            {
                "MODEL": 2,
                "SPEC_LOOKUP": 7,
                "TABLE": 4,
                "CALCULATION": 2,
                "CHART": 1,
                "PROCEDURE": 5,
                "CAUTION": 4,
            }
        )
        actual = Counter(re.findall(r"(?m)^\*\*Type: ([A-Z_]+)\*\*$", self.text))
        self.assertEqual(actual, expected)
        self.assertIn("- Total: 25", self.text)
        for question_type, count in expected.items():
            self.assertIn(f"- {question_type}: {count}", self.text)

    def test_every_question_has_atomic_hundred_point_scoring(self):
        required = (
            "### Target",
            "### Question",
            "### Standard Answer",
            "### Scoring Standard",
            "### Accepted Variants",
            "### Forbidden Errors",
            "### Tolerance",
            "### Source",
        )
        for index in range(1, 26):
            question_id = f"TNE-Q-{index:04d}"
            block = question_block(self.text, question_id)
            for heading in required:
                self.assertIn(heading, block, question_id)
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
            self.assertEqual(sum(int(weight) for _, weight, _ in points), 100)

    def test_contact_force_gold_is_deterministic(self):
        pi = Decimal("3.141592653589793")
        sensor_air = Decimal("0.10") * Decimal("16") ** 2 * pi / Decimal("4")
        cleaning_air = Decimal("0.25") * Decimal("25") ** 2 * pi / Decimal("4")
        quantum = Decimal("0.1")

        self.assertEqual(
            (sensor_air + Decimal("9.0")).quantize(
                quantum, rounding=ROUND_HALF_UP
            ),
            Decimal("29.1"),
        )
        self.assertEqual(
            (sensor_air + Decimal("13.5")).quantize(
                quantum, rounding=ROUND_HALF_UP
            ),
            Decimal("33.6"),
        )
        self.assertEqual(
            (cleaning_air + Decimal("11.8")).quantize(
                quantum, rounding=ROUND_HALF_UP
            ),
            Decimal("134.5"),
        )
        self.assertEqual(
            (cleaning_air + Decimal("18.6")).quantize(
                quantum, rounding=ROUND_HALF_UP
            ),
            Decimal("141.3"),
        )

        expected = {
            "TNE-Q-0014": ("20.106... N", "29.1～33.6 N", "ROUND_HALF_UP"),
            "TNE-Q-0016": ("122.718... N", "134.5～141.3 N", "ROUND_HALF_UP"),
        }
        for question_id, tokens in expected.items():
            block = question_block(self.text, question_id)
            for token in tokens:
                self.assertIn(token, block)

    def test_chart_question_uses_visual_evidence_and_resolution_tolerance(self):
        block = question_block(self.text, "TNE-Q-0025")
        for token in (
            "**Type: CHART**",
            "约为 44 μm",
            "40～48 μm",
            "视觉读图公差",
            "- Evidence type: CHART",
        ):
            self.assertIn(token, block)
        self.assertNotIn("表列支撑力作为变位答案", block)

    def test_source_inventory_covers_all_physical_pages_with_disposition(self):
        rows = {
            match.group(1): match.group(0)
            for match in re.finditer(r"(?m)^\| (TNE-SI-\d{3}) \|.*\|$", self.text)
        }
        self.assertEqual(
            sorted(rows), [f"TNE-SI-{index:03d}" for index in range(1, 14)]
        )
        for row_id, row in rows.items():
            self.assertTrue(
                "TNE-Q-" in row
                or "EXCLUDED" in row
                or "清单保留" in row
                or "排除" in row,
                row_id,
            )
        for page_range in (
            "1-2",
            "3-4",
            "5-6",
            "7-8",
            "9-12",
            "13-20",
            "21-22",
            "23-24",
            "25-28",
            "29-32",
            "33-34",
            "35-38",
            "39-40",
        ):
            self.assertIn(f"| {page_range} |", self.text)

    def test_model_sensor_and_installation_boundaries_remain_bound(self):
        model = question_block(self.text, "TNE-Q-0002")
        for token in ("液压上升标准型", "液压上升行程加长型", "弹簧上升型", "M-Q、M-EQ"):
            self.assertIn(token, model)

        sensor = question_block(self.text, "TNE-Q-0011")
        for token in ("0.05～0.15 MPa", "1～4 台", "ISA3-G", "GPS3-E"):
            self.assertIn(token, sensor)

        installation = question_block(self.text, "TNE-Q-0018")
        for token in ("水平密接", "底面承受载荷", "浮起", "变位量"):
            self.assertIn(token, installation)

        accessory = question_block(self.text, "TNE-Q-0023")
        for token in ("TNEZ-S", "TNEZ-SQ", "不适用于 TNE-Q", "不适用于 TNE-EQ"):
            self.assertIn(token, accessory)


if __name__ == "__main__":
    unittest.main()
