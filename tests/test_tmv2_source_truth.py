from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
import hashlib
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "question_banks/TMV2_R00_2023KW_C1N.md"
SOURCE = ROOT / "doc/TMV2_R00_2023KW_C1N.pdf"


def question_block(text: str, question_id: str) -> str:
    match = re.search(
        rf"(?ms)^## {re.escape(question_id)}\s*$\n(.*?)(?=^## TMV2-Q-|\Z)", text
    )
    if not match:
        raise AssertionError(f"missing question block: {question_id}")
    return match.group(1)


class Tmv2SourceTruthRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = BANK.read_text(encoding="utf-8")

    def test_source_identity_and_question_set_are_frozen(self):
        expected_hash = (
            "32427e6260cbc6845a58240507b05e36177e94a8cabbe3b391b982115a6973e4"
        )
        self.assertIn("source_pdf: TMV2_R00_2023KW_C1N.pdf", self.text)
        self.assertIn(f"source_sha256: {expected_hash}", self.text)
        self.assertIn("source_pages: 44", self.text)
        self.assertEqual(hashlib.sha256(SOURCE.read_bytes()).hexdigest(), expected_hash)
        ids = re.findall(r"(?m)^## (TMV2-Q-\d{4})$", self.text)
        self.assertEqual(ids, [f"TMV2-Q-{index:04d}" for index in range(1, 29)])

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
            question_id = f"TMV2-Q-{index:04d}"
            block = question_block(self.text, question_id)
            scoring = re.search(
                r"(?ms)^### Scoring Standard\s*$\n(.*?)(?=^### Accepted Variants)",
                block,
            )
            self.assertIsNotNone(scoring, question_id)
            points = re.findall(r"(?m)^- P(\d+) \[(\d+)]\s*:\s*(\S.*)$", scoring.group(1))
            self.assertEqual(
                [int(point_id) for point_id, _, _ in points],
                list(range(1, len(points) + 1)),
                question_id,
            )
            self.assertEqual(sum(int(weight) for _, weight, _ in points), 100, question_id)

    def test_calculation_gold_is_deterministic(self):
        forward = Decimal("8.33") * Decimal("22") / (Decimal("75") - Decimal("24.5"))
        inverse = Decimal("5.0") * (Decimal("100") - Decimal("30")) / Decimal("16.03")
        self.assertEqual(
            forward.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP), Decimal("3.6")
        )
        self.assertEqual(
            inverse.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP), Decimal("21.8")
        )
        for required in ("3.629... kN", "ROUND_HALF_UP", "3.6 kN"):
            self.assertIn(required, question_block(self.text, "TMV2-Q-0011"))
        for required in ("21.833... MPa", "21.8 MPa", "35 MPa"):
            self.assertIn(required, question_block(self.text, "TMV2-Q-0012"))

    def test_model_outputs_and_chart_values_are_frozen(self):
        model = question_block(self.text, "TMV2-Q-0001")
        for required in ("TMV0600-2CCE", "φD=43 mm", "板式配管型", "双向确认型"):
            self.assertIn(required, model)

        states = question_block(self.text, "TMV2-Q-0004")
        self.assertIn("OUT1 ON、OUT2 OFF", states)
        self.assertIn("OUT1 OFF、OUT2 ON", states)

        force = question_block(self.text, "TMV2-Q-0013")
        eccentricity = question_block(self.text, "TMV2-Q-0014")
        self.assertIn("1.1 kN ±0.1 kN", force)
        self.assertIn("40 mm ±2 mm", eccentricity)

    def test_document_common_and_accessory_boundaries_are_frozen(self):
        for index in range(19, 23):
            block = question_block(self.text, f"TMV2-Q-{index:04d}")
            self.assertIn("- Binding: DOCUMENT_COMMON", block)
            self.assertIn("- Model / Scope: TMV2_R00_2023KW_C1N.pdf :: ", block)

        speed = question_block(self.text, "TMV2-Q-0020")
        self.assertIn("两侧都必须采用进油节流", speed)
        self.assertIn("回油节流", speed)

        bzt = question_block(self.text, "TMV2-Q-0023")
        for required in ("BZT0101-A", "G1/8A", "2.6 mm²", "10 N·m", "12 g"):
            self.assertIn(required, bzt)

        sensor = question_block(self.text, "TMV2-Q-0025")
        for required in ("LZV0010-C2HA", "0.200 MPa", "NPN", "E 双向确认型"):
            self.assertIn(required, sensor)

        fitting = question_block(self.text, "TMV2-Q-0027")
        self.assertIn("包层密封件", fitting)
        self.assertIn("O 形圈密封", fitting)

    def test_coverage_rows_and_delivery_are_reconciled(self):
        rows = {
            match.group(1): match.group(0)
            for match in re.finditer(r"(?m)^\| (TMV2-SI-\d{3}) \|.*\|$", self.text)
        }
        self.assertEqual(sorted(rows), [f"TMV2-SI-{index:03d}" for index in range(1, 17)])
        for row_id, row in rows.items():
            if "| HIGH：" in row or "| MEDIUM：" in row:
                self.assertTrue("TMV2-Q-" in row or "排除" in row, row_id)

        for token in ("internal checkpoint", "next work package", "developer notes", "WP1", "WP2", "WP3", "WP4", "WP5"):
            self.assertNotIn(token, self.text)


if __name__ == "__main__":
    unittest.main()
