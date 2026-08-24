from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
import hashlib
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "question_banks/LHV_R00_2023KW_C1N.md"
SOURCE = ROOT / "doc/LHV_R00_2023KW_C1N.pdf"


def question_block(text: str, question_id: str) -> str:
    match = re.search(
        rf"(?ms)^## {re.escape(question_id)}\s*$\n(.*?)(?=^## LHV-Q-|\Z)", text
    )
    if not match:
        raise AssertionError(f"missing question block: {question_id}")
    return match.group(1)


class LhvSourceTruthRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = BANK.read_text(encoding="utf-8")

    def test_source_identity_and_question_set_are_frozen(self):
        expected_hash = (
            "c137f9f1c4ce25d500d5e185311e8efe083a18bc08557bdaaac4b86288476f10"
        )
        self.assertIn("source_pdf: LHV_R00_2023KW_C1N.pdf", self.text)
        self.assertIn(f"source_sha256: {expected_hash}", self.text)
        self.assertIn("source_pages: 52", self.text)
        self.assertEqual(hashlib.sha256(SOURCE.read_bytes()).hexdigest(), expected_hash)
        ids = re.findall(r"(?m)^## (LHV-Q-\d{4})$", self.text)
        self.assertEqual(ids, [f"LHV-Q-{index:04d}" for index in range(1, 29)])

    def test_statistics_and_scoring_are_frozen(self):
        expected = {
            "FACT": 3,
            "SPEC_LOOKUP": 3,
            "MODEL": 3,
            "TABLE": 4,
            "CALCULATION": 2,
            "CHART": 2,
            "PROCEDURE": 6,
            "CAUTION": 5,
        }
        actual = Counter(re.findall(r"(?m)^\*\*Type: ([A-Z_]+)\*\*$", self.text))
        self.assertEqual(actual, Counter(expected))
        self.assertIn("- Total: 28", self.text)
        for question_type, count in expected.items():
            self.assertIn(f"- {question_type}: {count}", self.text)

        for index in range(1, 29):
            question_id = f"LHV-Q-{index:04d}"
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
        forward = Decimal("5.5") / (
            Decimal("1.7183") + Decimal("0.0058") * Decimal("90")
        )
        inverse = Decimal("5.0") * (
            Decimal("0.7958") + Decimal("0.0024") * Decimal("120")
        )
        self.assertEqual(
            forward.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP), Decimal("2.5")
        )
        self.assertEqual(
            inverse.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP), Decimal("5.4")
        )
        forward_block = question_block(self.text, "LHV-Q-0011")
        inverse_block = question_block(self.text, "LHV-Q-0012")
        for required in ("2.455028... kN", "必须精确为 2.5 kN"):
            self.assertIn(required, forward_block)
        for required in ("5.41900 MPa", "必须精确为 5.4 MPa", "4.982... kN"):
            self.assertIn(required, inverse_block)
        self.assertNotIn("±0.05", forward_block)
        self.assertNotIn("±0.05", inverse_block)

    def test_chart_gold_is_visual_and_toleranced(self):
        force = question_block(self.text, "LHV-Q-0013")
        action = question_block(self.text, "LHV-Q-0014")
        for block in (force, action):
            self.assertIn("**Type: CHART**", block)
            self.assertIn("- Evidence type: CHART", block)
            self.assertIn("视觉", block)
        for required in ("Gold: 2.6 kN", "2.4-2.8 kN", "公式仅用于检查视觉 Gold"):
            self.assertIn(required, force)
        for required in ("Gold 0.50 s", "0.45-0.55 s", "Gold 0.25 s", "0.22-0.28 s"):
            self.assertIn(required, action)

    def test_model_state_speed_and_accessory_boundaries_are_frozen(self):
        model = question_block(self.text, "LHV-Q-0001")
        for required in ("LHV0480-CRE-A", "φD=48 mm", "夹紧时顺时针", "快换压板 A 型"):
            self.assertIn(required, model)

        states = question_block(self.text, "LHV-Q-0004")
        self.assertIn("OUT1 ON、OUT2 OFF", states)
        self.assertIn("OUT1 OFF、OUT2 ON", states)

        for index in range(19, 23):
            block = question_block(self.text, f"LHV-Q-{index:04d}")
            self.assertIn("- Binding: DOCUMENT_COMMON", block)
            self.assertIn("- Model / Scope: LHV_R00_2023KW_C1N.pdf :: ", block)

        speed = question_block(self.text, "LHV-Q-0020")
        self.assertIn("两侧均采用回油节流", speed)
        self.assertIn("不得套用 TLA/TLV/TMV", speed)

        bzl = question_block(self.text, "LHV-Q-0023")
        for required in ("BZL0101-B", "0.12 MPa", "2.6 mm²", "10 N·m", "12 g"):
            self.assertIn(required, bzl)

        bzl_caution = question_block(self.text, "LHV-Q-0024")
        self.assertIn("不得换装到其他夹紧器上重复使用", bzl_caution)
        self.assertIn("不得把跨夹紧器限制扩大", bzl_caution)

        sensor = question_block(self.text, "LHV-Q-0025")
        for required in ("LZV0010-C3HA", "0.200 MPa", "NPN", "3 台 LHV"):
            self.assertIn(required, sensor)

    def test_coverage_rows_and_delivery_are_reconciled(self):
        rows = {
            match.group(1): match.group(0)
            for match in re.finditer(r"(?m)^\| (LHV-SI-\d{3}) \|.*\|$", self.text)
        }
        self.assertEqual(sorted(rows), [f"LHV-SI-{index:03d}" for index in range(1, 17)])
        for row_id, row in rows.items():
            if "| HIGH：" in row or "| MEDIUM：" in row:
                self.assertTrue("LHV-Q-" in row or "排除" in row, row_id)

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
