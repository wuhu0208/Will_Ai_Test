from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
import hashlib
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "question_banks/VSVT_R00_2023KW_C1N.md"
SOURCE = ROOT / "doc/VSVT_R00_2023KW_C1N.pdf"


def question_block(text: str, question_id: str) -> str:
    match = re.search(
        rf"(?ms)^## {re.escape(question_id)}\s*$\n(.*?)(?=^## VSVT-Q-|\Z)",
        text,
    )
    if not match:
        raise AssertionError(f"missing question block: {question_id}")
    return match.group(1)


class VsvtSourceTruthRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = BANK.read_text(encoding="utf-8")

    def test_source_identity_and_single_canonical_delivery_are_frozen(self):
        expected_hash = (
            "9584362162a9808ca4c05899055f68d839d4676c154e43a6f30940be77b4885f"
        )
        self.assertIn("source_pdf: VSVT_R00_2023KW_C1N.pdf", self.text)
        self.assertIn(f"source_sha256: {expected_hash}", self.text)
        self.assertIn("source_pages: 42", self.text)
        self.assertEqual(hashlib.sha256(SOURCE.read_bytes()).hexdigest(), expected_hash)
        self.assertEqual(
            sorted(path.name for path in (ROOT / "question_banks").glob("VSVT*.md")),
            ["VSVT_R00_2023KW_C1N.md"],
        )
        for scope in ("VS", "VT", "VSB", "VSJ", "VZ"):
            self.assertIn(scope, self.text)

    def test_question_set_and_statistics_are_frozen(self):
        ids = re.findall(r"(?m)^## (VSVT-Q-\d{4})$", self.text)
        self.assertEqual(ids, [f"VSVT-Q-{index:04d}" for index in range(1, 25)])
        expected = Counter(
            {
                "MODEL": 3,
                "SPEC_LOOKUP": 5,
                "TABLE": 2,
                "CALCULATION": 2,
                "CHART": 2,
                "PROCEDURE": 5,
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
            1: 11,
            2: 10,
            3: 12,
            4: 19,
            5: 9,
            6: 10,
            7: 10,
            8: 7,
            9: 8,
            10: 5,
            11: 8,
            12: 4,
            13: 4,
            14: 11,
            15: 10,
            16: 10,
            17: 8,
            18: 8,
            19: 7,
            20: 9,
            21: 6,
            22: 10,
            23: 11,
            24: 6,
        }
        for index, expected_count in expected_counts.items():
            question_id = f"VSVT-Q-{index:04d}"
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

        scoring_sections = "\n".join(
            re.findall(
                r"(?ms)^### Scoring Standard\s*$\n(.*?)(?=^### Accepted Variants)",
                self.text,
            )
        )
        for forbidden_compound in (
            "`G` 承担导向并夹紧",
            "`D` 表示锥销并承担定位、夹紧",
            "`F` 不提供定位或导向",
            "检查异常声音和动作",
            "夹紧侧和释放侧均采用回油节流",
        ):
            self.assertNotIn(forbidden_compound, scoring_sections)

    def test_source_inventory_covers_all_physical_pages_with_disposition(self):
        rows = {
            match.group(1): match.group(0)
            for match in re.finditer(r"(?m)^\| (VSVT-SI-\d{3}) \|.*\|$", self.text)
        }
        self.assertEqual(
            sorted(rows), [f"VSVT-SI-{index:03d}" for index in range(1, 19)]
        )
        for row_id, row in rows.items():
            self.assertTrue(
                "VSVT-Q-" in row
                or "EXCLUDED" in row
                or "清单保留" in row,
                row_id,
            )
        for page_range in (
            "1-2",
            "3-4",
            "5-6",
            "7-8",
            "9-10",
            "11-12",
            "13-14",
            "15-16",
            "17-18",
            "19-20",
            "21-22",
            "23-26",
            "27-28",
            "29-30",
            "31-32",
            "33-34",
            "35-38",
            "39-42",
        ):
            self.assertIn(f"| {page_range} |", self.text)

    def test_vs_vt_model_and_compatibility_boundaries_remain_bound(self):
        expected_tokens = {
            "VSVT-Q-0001": ("VS0060-MD", "6.0 kN", "单动弹簧夹紧器", "直导销"),
            "VSVT-Q-0002": ("VT0060-MD-A", "7 MPa", "6.2 kN", "圆形", "方形"),
            "VSVT-Q-0003": ("VSB060-D", "VSJ060-D", "切割套", "通用套"),
            "VSVT-Q-0004": ("VS0250", "VS0400", "没有对应 VT 型号"),
            "VSVT-Q-0021": ("只有 `C` 套", "`G` 套只能与 `MG`", "+0.010 mm"),
            "VSVT-Q-0024": ("`-VS1`", "不适用于 VT", "±0.025 mm"),
        }
        for question_id, tokens in expected_tokens.items():
            block = question_block(self.text, question_id)
            for token in tokens:
                self.assertIn(token, block, question_id)

    def test_table_and_calculation_gold_are_deterministic(self):
        self.assertIn("VS0400 为 40.0 kN", question_block(self.text, "VSVT-Q-0008"))
        vt = question_block(self.text, "VSVT-Q-0009")
        for token in ("VT0040", "2.9 kN", "VT0160", "7.3 kN"):
            self.assertIn(token, vt)

        total = Decimal("4") * Decimal("6.0")
        self.assertEqual(total, Decimal("24.0"))
        vertical_limit = (Decimal("16.0") * Decimal("0.10")).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
        self.assertEqual(vertical_limit, Decimal("1.60"))
        for question_id, tokens in {
            "VSVT-Q-0010": ("24.0 kN", "ROUND_HALF_UP"),
            "VSVT-Q-0011": ("1.60 kN", "10%", "7 MPa", "ROUND_HALF_UP"),
        }.items():
            block = question_block(self.text, question_id)
            for token in tokens:
                self.assertIn(token, block, question_id)

    def test_chart_questions_use_visual_evidence_and_resolution_tolerance(self):
        force = question_block(self.text, "VSVT-Q-0012")
        for token in ("VT0100", "6.0 MPa", "8.5 kN", "5.6 kN", "±0.25 kN"):
            self.assertIn(token, force)
        displacement = question_block(self.text, "VSVT-Q-0013")
        for token in ("VS0100", "Y 轴", "L=350 mm", "F=10 kN", "±1.0 μm"):
            self.assertIn(token, displacement)
        self.assertEqual(self.text.count("- Evidence type: CHART"), 2)

    def test_procedure_and_document_common_boundaries_remain_bound(self):
        expected_tokens = {
            "VSVT-Q-0006": ("释放压力", "钢球", "气密传感器"),
            "VSVT-Q-0014": ("运输保护环", "平行升起", "零件飞散"),
            "VSVT-Q-0015": ("磨削垫片", "复测", "±0.003 mm"),
            "VSVT-Q-0018": ("带单向阀", "回油节流", "分开设置"),
            "VSVT-Q-0019": ("2 MPa 以下", "约一圈", "无气泡"),
            "VSVT-Q-0020": ("1～2 个螺纹牙", "ISO VG32", "动作不良"),
            "VSVT-Q-0023": ("液压油老化", "异常声音", "制造商"),
        }
        for question_id, tokens in expected_tokens.items():
            block = question_block(self.text, question_id)
            for token in tokens:
                self.assertIn(token, block, question_id)
        for question_id in (18, 19, 20, 23):
            block = question_block(self.text, f"VSVT-Q-{question_id:04d}")
            self.assertIn("- Binding: DOCUMENT_COMMON", block)
            self.assertIn("VSVT_R00_2023KW_C1N.pdf ::", block)


if __name__ == "__main__":
    unittest.main()
