from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
import hashlib
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "question_banks/TLV2_R00_2023KW_C1N.md"
SOURCE = ROOT / "doc/TLV2_R00_2023KW_C1N.pdf"


def question_block(text: str, question_id: str) -> str:
    match = re.search(
        rf"(?ms)^## {re.escape(question_id)}\s*$\n(.*?)(?=^## TLV2-Q-|\Z)",
        text,
    )
    if not match:
        raise AssertionError(f"missing question block: {question_id}")
    return match.group(1)


class Tlv2SourceTruthRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = BANK.read_text(encoding="utf-8")

    def test_source_identity_and_question_set_are_frozen(self):
        expected_hash = (
            "05a17554660e3d2b4ce0f0e9f4cbadb1c3e41edffaa8043103ea89ea2e446317"
        )
        self.assertIn("source_pdf: TLV2_R00_2023KW_C1N.pdf", self.text)
        self.assertIn(f"source_sha256: {expected_hash}", self.text)
        self.assertIn("source_pages: 46", self.text)
        self.assertEqual(hashlib.sha256(SOURCE.read_bytes()).hexdigest(), expected_hash)
        ids = re.findall(r"(?m)^## (TLV2-Q-\d{4})$", self.text)
        self.assertEqual(ids, [f"TLV2-Q-{index:04d}" for index in range(1, 22)])

    def test_statistics_match_question_types(self):
        expected = Counter(
            {
                "MODEL": 4,
                "FACT": 3,
                "TABLE": 4,
                "CALCULATION": 3,
                "CHART": 1,
                "PROCEDURE": 2,
                "CAUTION": 4,
            }
        )
        actual = Counter(re.findall(r"(?m)^\*\*Type: ([A-Z_]+)\*\*$", self.text))
        self.assertEqual(actual, expected)
        self.assertIn("- Total: 21", self.text)
        for question_type, count in expected.items():
            self.assertIn(f"- {question_type}: {count}", self.text)

    def test_every_question_has_required_sections_and_atomic_scoring(self):
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
        for index in range(1, 22):
            question_id = f"TLV2-Q-{index:04d}"
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
            self.assertRegex(block, r"- Binding: [A-Z_]+")
            self.assertIn("- Model / Scope:", block)
            self.assertIn("- Evidence type:", block)

    def test_calculation_gold_is_deterministic(self):
        force = Decimal("25") / (
            Decimal("3.566") + Decimal("0.0181") * Decimal("50")
        )
        pressure = Decimal("8") * (
            Decimal("2.398") + Decimal("0.0095") * Decimal("100")
        )
        rounded_pressure = pressure.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
        back_substitution = rounded_pressure / Decimal("3.348")
        full_time = Decimal("0.43") * Decimal("24") / Decimal("11")

        self.assertEqual(
            force.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP), Decimal("5.6")
        )
        self.assertEqual(pressure, Decimal("26.784"))
        self.assertEqual(rounded_pressure, Decimal("26.8"))
        self.assertEqual(
            back_substitution.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP),
            Decimal("8.0"),
        )
        self.assertEqual(
            full_time.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
            Decimal("0.94"),
        )

        required_by_question = {
            "TLV2-Q-0009": ("5.591... kN", "ROUND_HALF_UP", "5.6 kN"),
            "TLV2-Q-0010": ("26.784 MPa", "26.8 MPa", "8.004... kN", "8.0 kN"),
            "TLV2-Q-0013": ("0.93818... s", "ROUND_HALF_UP", "0.94 s"),
        }
        for question_id, tokens in required_by_question.items():
            block = question_block(self.text, question_id)
            for token in tokens:
                self.assertIn(token, block)

    def test_table_and_chart_classifications_match_source_evidence(self):
        force = question_block(self.text, "TLV2-Q-0011")
        action = question_block(self.text, "TLV2-Q-0012")
        self.assertIn("**Type: TABLE**", force)
        self.assertRegex(force, r"- Evidence type: TABLE")
        for token in ("离散表", "**2.9 kN**", "必须精确为 2.9 kN"):
            self.assertIn(token, force)
        self.assertNotIn("视觉读图公差", force)
        self.assertIn("**Type: CHART**", action)
        self.assertRegex(action, r"- Evidence type: CHART")
        self.assertIn("视觉", action)
        for token in ("约 **0.43 秒以上**", "0.38～0.48 秒", "±0.05 秒"):
            self.assertIn(token, action)

    def test_calculation_tolerances_are_exact_rounding_rules(self):
        expected = {
            "TLV2-Q-0009": ("ROUND_HALF_UP", "0.1 kN"),
            "TLV2-Q-0010": ("ROUND_HALF_UP", "0.1 MPa", "0.1 kN"),
            "TLV2-Q-0013": ("ROUND_HALF_UP", "0.01 s"),
        }
        for question_id, tokens in expected.items():
            block = question_block(self.text, question_id)
            tolerance = re.search(
                r"(?ms)^### Tolerance\s*$\n(.*?)(?=^### Source)", block
            ).group(1)
            self.assertNotRegex(tolerance, r"±0\.0")
            for token in tokens:
                self.assertIn(token, tolerance)

    def test_reviewed_atomic_repairs_remain_split(self):
        arm = question_block(self.text, "TLV2-Q-0015")
        self.assertIn("- P3 [30]: 自制连接螺栓最低为 12.9 级", arm)
        self.assertNotIn("明确是 12.9 级以上", arm)

        maintenance = question_block(self.text, "TLV2-Q-0018")
        self.assertIn("- P10 [3]: 定期清扫活塞杆周围", maintenance)
        self.assertIn("- P11 [3]: 定期检查配管和紧固件是否松动", maintenance)

        sensor = question_block(self.text, "TLV2-Q-0020")
        for token in (
            "- P9 [4]: H 对应 0.200 MPa",
            "- P10 [3]: M 对应 0.150 MPa",
            "- P11 [3]: L 对应 0.100 MPa",
        ):
            self.assertIn(token, sensor)

    def test_source_inventory_is_complete_and_mapped(self):
        rows = {
            match.group(1): match.group(0)
            for match in re.finditer(r"(?m)^\| (TLV2-SI-\d{3}) \|.*\|$", self.text)
        }
        self.assertEqual(
            sorted(rows), [f"TLV2-SI-{index:03d}" for index in range(1, 17)]
        )
        for row_id, row in rows.items():
            self.assertTrue(
                "TLV2-Q-" in row
                or "排除" in row
                or "清单保留" in row
                or "EXCLUDED" in row,
                row_id,
            )
        for page_range in ("5-6", "7-8", "9-10", "11-12", "13-14", "15-16", "17-18", "19-20", "21-24", "25-28", "29-30", "31-36", "37-40", "41-44", "45-46"):
            self.assertIn(f"| {page_range} |", self.text)

    def test_model_and_circuit_boundaries_are_frozen(self):
        model = question_block(self.text, "TLV2-Q-0001")
        for token in ("TLV0800-2CRE", "φD=36 mm", "C 为板式配管", "R 为夹紧时顺时针"):
            self.assertIn(token, model)
        sensing = question_block(self.text, "TLV2-Q-0006")
        for token in ("持续供气", "释放状态", "0.005 MPa", "外径 φ6", "内径 φ4"):
            self.assertIn(token, sensing)
        circuit = question_block(self.text, "TLV2-Q-0018")
        for token in ("夹紧侧采用进油节流", "释放侧采用进油节流", "异常高压", "漏油或损坏"):
            self.assertIn(token, circuit)
        grammar = question_block(self.text, "TLV2-Q-0021")
        for token in (
            "TLV0800-2CRE",
            "TLV1600-2CLJ",
            "TLV1000-2BRE",
            "TLV2000-2CRK",
            "TLV0801-2CRE",
        ):
            self.assertIn(token, grammar)


if __name__ == "__main__":
    unittest.main()
