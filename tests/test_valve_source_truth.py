from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
import hashlib
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "question_banks/VALVE_R00_2023KW_C1N.md"
SOURCE = ROOT / "doc/VALVE_R00_2023KW_C1N.pdf"


def question_block(text: str, question_id: str) -> str:
    match = re.search(
        rf"(?ms)^## {re.escape(question_id)}\s*$\n(.*?)(?=^## VALVE-Q-|\Z)",
        text,
    )
    if not match:
        raise AssertionError(f"missing question block: {question_id}")
    return match.group(1)


class ValveSourceTruthRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = BANK.read_text(encoding="utf-8")

    def test_source_identity_and_single_canonical_delivery_are_frozen(self):
        expected_hash = (
            "aa85a41bd6a3d29a7a1a0544426d4f1140aa496a99f2e41287f82f49531a3961"
        )
        self.assertIn("source_pdf: VALVE_R00_2023KW_C1N.pdf", self.text)
        self.assertIn(f"source_sha256: {expected_hash}", self.text)
        self.assertIn("source_pages: 88", self.text)
        self.assertEqual(hashlib.sha256(SOURCE.read_bytes()).hexdigest(), expected_hash)
        self.assertEqual(
            sorted(path.name for path in (ROOT / "question_banks").glob("VALVE*.md")),
            ["VALVE_R00_2023KW_C1N.md"],
        )
        for scope in ("BLG", "BLS", "BMA", "BMG"):
            self.assertIn(scope, self.text)

    def test_question_set_and_statistics_are_frozen(self):
        ids = re.findall(r"(?m)^## (VALVE-Q-\d{4})$", self.text)
        self.assertEqual(ids, [f"VALVE-Q-{index:04d}" for index in range(1, 25)])
        expected = Counter(
            {
                "MODEL": 5,
                "SPEC_LOOKUP": 5,
                "TABLE": 2,
                "CALCULATION": 1,
                "CHART": 2,
                "PROCEDURE": 4,
                "CAUTION": 5,
            }
        )
        actual = Counter(re.findall(r"(?m)^\*\*Type: ([A-Z_]+)\*\*$", self.text))
        self.assertEqual(actual, expected)
        self.assertIn("- Total: 24", self.text)
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
        expected_counts = {
            1: 13,
            2: 6,
            3: 12,
            4: 10,
            5: 15,
            6: 6,
            7: 6,
            8: 7,
            9: 12,
            10: 10,
            11: 14,
            12: 5,
            13: 6,
            14: 10,
            15: 11,
            16: 7,
            17: 13,
            18: 5,
            19: 6,
            20: 8,
            21: 7,
            22: 7,
            23: 10,
            24: 16,
        }
        for index, expected_count in expected_counts.items():
            question_id = f"VALVE-Q-{index:04d}"
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
            self.assertEqual(len(points), expected_count, question_id)
            self.assertEqual(
                [int(point_id) for point_id, _, _ in points],
                list(range(1, expected_count + 1)),
                question_id,
            )
            self.assertEqual(sum(int(weight) for _, weight, _ in points), 100)

        for forbidden_compound in (
            "GA 为板式后面连接，GB 为板式底面连接",
            "BMA 约 1.5 kg，BMG 约 0.8 kg",
            "BU5030 设定 2.3～6.7、输出 9.0～25.2",
            "摇动配管并排出含气液压油",
            "检查异常声音和异常动作",
        ):
            scoring_sections = re.findall(
                r"(?ms)^### Scoring Standard\s*$\n(.*?)(?=^### Accepted Variants)",
                self.text,
            )
            self.assertNotIn(forbidden_compound, "\n".join(scoring_sections))

    def test_source_inventory_covers_all_pages_with_disposition(self):
        rows = {
            match.group(1): match.group(0)
            for match in re.finditer(r"(?m)^\| (VALVE-SI-\d{3}) \|.*\|$", self.text)
        }
        self.assertEqual(
            sorted(rows), [f"VALVE-SI-{index:03d}" for index in range(1, 18)]
        )
        for row_id, row in rows.items():
            self.assertTrue(
                "VALVE-Q-" in row
                or "EXCLUDED" in row
                or "清单保留" in row,
                row_id,
            )
        for page_range in (
            "1-2",
            "3-6",
            "7-10",
            "11-14",
            "15-18",
            "19-20",
            "21-26",
            "27-30",
            "31-40",
            "41-44",
            "45-50",
            "51-58",
            "59-64",
            "65-70",
            "71-80",
            "81-86",
            "87-88",
        ):
            self.assertIn(f"| {page_range} |", self.text)

    def test_core_model_and_pressure_boundaries_remain_bound(self):
        expected_tokens = {
            "VALVE-Q-0001": ("GA", "GB", "GC", "GS", "Rc1/4", "Rc3/8"),
            "VALVE-Q-0002": ("BEQ0220", "2.0～7.0 MPa", "GA", "GB"),
            "VALVE-Q-0003": ("BLS", "BLG", "8～20 MPa", "5～18 MPa"),
            "VALVE-Q-0004": ("BMA", "BMG", "1～6 MPa", "6～27 MPa"),
            "VALVE-Q-0009": ("BK22", "BK25", "BK32", "37.5 MPa"),
            "VALVE-Q-0010": ("BEQ0250", "0.07 MPa", "5.5", "0.3 MPa"),
            "VALVE-Q-0013": ("至少相差 1 MPa", "并联 BLS", "并联 BLG"),
            "VALVE-Q-0014": ("2～7 MPa", "3～14 MPa", "6～27 MPa", "23.3 cm²"),
        }
        for question_id, tokens in expected_tokens.items():
            block = question_block(self.text, question_id)
            for token in tokens:
                self.assertIn(token, block, question_id)

    def test_calculation_gold_is_deterministic(self):
        drop = Decimal("0.69") * Decimal("8")
        remaining = Decimal("20.00") - drop
        self.assertEqual(drop, Decimal("5.52"))
        self.assertEqual(
            remaining.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
            Decimal("14.48"),
        )
        block = question_block(self.text, "VALVE-Q-0007")
        for token in ("0.69 MPa/℃", "5.52 MPa", "14.48 MPa", "ROUND_HALF_UP"):
            self.assertIn(token, block)

    def test_chart_questions_use_visual_evidence_and_resolution_tolerance(self):
        reliability = question_block(self.text, "VALVE-Q-0008")
        for token in ("45.2", "115.8", "19 ℃", "16.5 MPa", "视觉读图公差"):
            self.assertIn(token, reliability)
        booster = question_block(self.text, "VALVE-Q-0018")
        for token in ("BU5030", "约为 15 MPa", "14.5～15.5 MPa", "视觉读图"):
            self.assertIn(token, booster)
        self.assertEqual(self.text.count("- Evidence type: CHART"), 2)

    def test_operation_and_common_safety_boundaries_remain_bound(self):
        expected_tokens = {
            "VALVE-Q-0019": ("A、B 与 T 连通", "A/B 封闭", "完全释放"),
            "VALVE-Q-0020": ("输出流量会下降", "内部泄漏", "蓄能器", "P1 与 T/D"),
            "VALVE-Q-0021": ("防误操作", "±45°", "NN"),
            "VALVE-Q-0022": ("空气电磁阀", "自动卸压", "YY"),
            "VALVE-Q-0023": ("保留 1～2 个螺纹", "2 MPa 以下", "松开约一圈"),
            "VALVE-Q-0024": ("液压压力和电源均为零", "定期排气", "禁止擅自改造"),
        }
        for question_id, tokens in expected_tokens.items():
            block = question_block(self.text, question_id)
            for token in tokens:
                self.assertIn(token, block, question_id)


if __name__ == "__main__":
    unittest.main()
