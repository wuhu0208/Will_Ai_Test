from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
import hashlib
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "question_banks/TC_R00_2026KW_C1N.md"
SOURCE = ROOT / "doc/TC_R00_2026KW_C1N.pdf"


def question_block(text: str, question_id: str) -> str:
    match = re.search(
        rf"(?ms)^## {re.escape(question_id)}\s*$\n(.*?)(?=^## TC-Q-|\Z)",
        text,
    )
    if not match:
        raise AssertionError(f"missing question block: {question_id}")
    return match.group(1)


class TcSourceTruthRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = BANK.read_text(encoding="utf-8")

    def test_source_identity_and_question_set_are_frozen(self):
        expected_hash = (
            "ca6161e78975a8c8a65799dcda590bab3101f3885c8b98cac8839ba03c3aaca1"
        )
        self.assertIn("source_pdf: TC_R00_2026KW_C1N.pdf", self.text)
        self.assertIn(f"source_sha256: {expected_hash}", self.text)
        self.assertIn("source_pages: 48", self.text)
        self.assertEqual(hashlib.sha256(SOURCE.read_bytes()).hexdigest(), expected_hash)
        ids = re.findall(r"(?m)^## (TC-Q-\d{4})$", self.text)
        self.assertEqual(ids, [f"TC-Q-{index:04d}" for index in range(1, 25)])

    def test_statistics_match_frozen_question_types(self):
        expected = Counter(
            {
                "MODEL": 2,
                "SPEC_LOOKUP": 5,
                "TABLE": 4,
                "CALCULATION": 2,
                "CHART": 1,
                "PROCEDURE": 4,
                "CAUTION": 6,
            }
        )
        actual = Counter(re.findall(r"(?m)^\*\*Type: ([A-Z_]+)\*\*$", self.text))
        self.assertEqual(actual, expected)
        self.assertIn("- Total: 24", self.text)
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
        for index in range(1, 25):
            question_id = f"TC-Q-{index:04d}"
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

    def test_calculation_gold_is_deterministic(self):
        support = Decimal("1.86") * Decimal("18") - Decimal("6.51")
        self.assertEqual(support, Decimal("26.97"))
        self.assertEqual(
            support.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP),
            Decimal("27.0"),
        )

        pi = Decimal("3.141592653589793")
        air_force = Decimal("0.25") * Decimal("25") ** 2 * pi / Decimal("4")
        lower = (air_force + Decimal("12.4")).quantize(
            Decimal("0.1"), rounding=ROUND_HALF_UP
        )
        upper = (air_force + Decimal("18.8")).quantize(
            Decimal("0.1"), rounding=ROUND_HALF_UP
        )
        self.assertEqual(lower, Decimal("135.1"))
        self.assertEqual(upper, Decimal("141.5"))

        for question_id, tokens in {
            "TC-Q-0006": ("26.97 kN", "27.0 kN", "ROUND_HALF_UP"),
            "TC-Q-0009": ("122.718... N", "135.1～141.5 N", "ROUND_HALF_UP"),
        }.items():
            block = question_block(self.text, question_id)
            for token in tokens:
                self.assertIn(token, block)

    def test_chart_question_uses_visual_evidence_and_resolution_tolerance(self):
        block = question_block(self.text, "TC-Q-0024")
        for token in (
            "**Type: CHART**",
            "约为 **55 μm**",
            "50～60 μm",
            "视觉读图公差",
            "- Evidence type: CHART",
        ):
            self.assertIn(token, block)
        self.assertIn("不以公式", self.text)

    def test_source_inventory_covers_all_physical_pages_with_disposition(self):
        rows = {
            match.group(1): match.group(0)
            for match in re.finditer(r"(?m)^\| (TC-SI-\d{3}) \|.*\|$", self.text)
        }
        self.assertEqual(
            sorted(rows), [f"TC-SI-{index:03d}" for index in range(1, 14)]
        )
        for row_id, row in rows.items():
            self.assertTrue(
                "TC-Q-" in row
                or "EXCLUDED" in row
                or "清单保留" in row
                or "排除" in row,
                row_id,
            )
        for page_range in (
            "1-2",
            "3-6",
            "7-8",
            "9-12",
            "13-20",
            "21-22",
            "23-24",
            "25-28",
            "29-32",
            "33-34",
            "35-42",
            "43-46",
            "47-48",
        ):
            self.assertIn(f"| {page_range} |", self.text)

    def test_model_installation_and_accessory_boundaries_remain_bound(self):
        model = question_block(self.text, "TC-Q-0002")
        for token in ("液压上升标准型", "液压上升行程加长型", "无活塞杆中空型", "S-M", "M-Q"):
            self.assertIn(token, model)

        hollow = question_block(self.text, "TC-Q-0013")
        for token in ("箭头向下", "HRC60", "硬质镀铬", "倒角"):
            self.assertIn(token, hollow)

        speed = question_block(self.text, "TC-Q-0022")
        for token in ("进油节流", "35 MPa", "0.04 MPa", "TC0553", "TC0403、TC0483"):
            self.assertIn(token, speed)

        vent = question_block(self.text, "TC-Q-0023")
        for token in ("BZX010", "42 MPa", "G1/8A", "不得旋松堵头超过 2 周"):
            self.assertIn(token, vent)


if __name__ == "__main__":
    unittest.main()
