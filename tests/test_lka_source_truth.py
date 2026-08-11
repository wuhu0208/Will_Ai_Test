from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "question_banks/LKA_R01_2023KW_C1N.md"


def question_block(text: str, question_id: str) -> str:
    match = re.search(
        rf"^## {re.escape(question_id)}\n(.*?)(?=^## LKA-Q-|\Z)",
        text,
        flags=re.MULTILINE | re.DOTALL,
    )
    return match.group(1) if match else ""


class LkaSourceTruthRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = BANK.read_text(encoding="utf-8")

    def test_clamp_force_formulas_preserve_fulcrum_offset(self):
        block = question_block(self.text, "LKA-Q-0003")
        self.assertIn("F = (11.76 x P) / (L - 18.5)", block)
        self.assertIn("F = (9.20 x P) / (L - 18.5)", block)
        self.assertNotIn("F = (11.76 x P) / L", self.text)
        self.assertNotIn("F = (9.20 x P) / L", self.text)

    def test_clamp_force_gold_uses_offset_and_half_up_rounding(self):
        pressure = Decimal("5.0")
        effective_length = Decimal("60") - Decimal("18.5")
        quantum = Decimal("0.01")
        standard = Decimal("11.76") * pressure / effective_length
        confirmation = Decimal("9.20") * pressure / effective_length

        self.assertEqual(
            standard.quantize(quantum, rounding=ROUND_HALF_UP), Decimal("1.42")
        )
        self.assertEqual(
            confirmation.quantize(quantum, rounding=ROUND_HALF_UP), Decimal("1.11")
        )

        block = question_block(self.text, "LKA-Q-0017")
        for required in (
            "11.76 x 5.0 / (60 - 18.5) = 1.416867... kN",
            "9.20 x 5.0 / (60 - 18.5) = 1.108433... kN",
            "1.42 kN",
            "1.11 kN",
        ):
            self.assertIn(required, block)

    def test_chart_gold_is_visual_read_with_chart_tolerance(self):
        block = question_block(self.text, "LKA-Q-0018")
        self.assertIn("`1.1 kN`", block)
        self.assertIn("CHART: accept 1.0-1.2 kN", block)
        self.assertIn("不作为 Chart Gold 来源", block)

    def test_air_bleeding_limit_is_frozen(self):
        block = question_block(self.text, "LKA-Q-0023")
        self.assertIn("不超过 2 MPa", block)
        self.assertIn("2 MPa or below", block)
        self.assertIn("供油压力超过 2 MPa", block)

    def test_affected_coverage_rows_are_reconciled(self):
        required = {
            "LKA-SI-007": "(L - 18.5)",
            "LKA-SI-008": "1.1 kN",
            "LKA-SI-022": "2 MPa-or-below",
        }
        for inventory_id, value in required.items():
            row = next(
                line
                for line in self.text.splitlines()
                if line.startswith(f"| {inventory_id} |")
            )
            self.assertIn(value, row)


if __name__ == "__main__":
    unittest.main()
