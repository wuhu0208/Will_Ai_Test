from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "question_banks/LSA_LSE_R00_2023KW_C1N.md"


def question_block(text: str, question_id: str) -> str:
    match = re.search(
        rf"^## {re.escape(question_id)}\n(.*?)(?=^## LSA-LSE-Q-|\Z)",
        text,
        flags=re.MULTILINE | re.DOTALL,
    )
    return match.group(1) if match else ""


class LsaLseSourceTruthRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = BANK.read_text(encoding="utf-8")

    def test_calculation_gold_applies_lse_holding_cap(self):
        quantum = Decimal("0.01")
        lsa = Decimal("0.394") * Decimal("5.8")
        lse_clamp = Decimal("0.601") * Decimal("4.8")
        lse_hold_raw = Decimal("0.953") * Decimal("4.8")
        lse_hold = min(lse_hold_raw, Decimal("3.62"))

        self.assertEqual(
            lsa.quantize(quantum, rounding=ROUND_HALF_UP), Decimal("2.29")
        )
        self.assertEqual(
            lse_clamp.quantize(quantum, rounding=ROUND_HALF_UP), Decimal("2.88")
        )
        self.assertEqual(
            lse_hold.quantize(quantum, rounding=ROUND_HALF_UP), Decimal("3.62")
        )

        block = question_block(self.text, "LSA-LSE-Q-0009")
        for required in ("2.2852 kN", "2.8848 kN", "4.5744 kN", "3.62 kN"):
            self.assertIn(required, block)
        self.assertIn("不能报告为 4.57 kN", block)
        self.assertIn("Evidence type: FORMULA + TABLE", block)
        self.assertNotIn("Evidence type: FORMULA + TABLE + CHART", block)

    def test_bzl_chart_gold_is_visual_and_qualitative(self):
        block = question_block(self.text, "LSA-LSE-Q-0010")
        self.assertIn("**Type: CHART**", block)
        self.assertIn("Physical page: 23-24", block)
        self.assertIn("Evidence type: CHART + TEXT", block)
        self.assertIn("本题为定性图表读取，不要求数值插值", block)
        self.assertIn("不接受凭公式推导", block)

    def test_lse_wildcard_target_uses_model_family_binding(self):
        block = question_block(self.text, "LSA-LSE-Q-0012")
        self.assertIn("- Binding: MODEL_FAMILY", block)
        self.assertNotIn("- Binding: EXACT_MODEL", block)
        self.assertIn("LSE0360-C□", block)

    def test_model_grammar_keeps_legal_and_illegal_examples(self):
        for required in (
            "LSA0360-CL",
            "LSE0360-CR",
            "LSA0400-CR",
            "LSE0361-CR",
            "LSA0360-RC",
            "LSE0360-CR-A",
            "BZL0101-C",
            "BZL0110-A",
            "BZS0101",
            "BZS0100-A",
        ):
            self.assertIn(required, self.text)

    def test_delivery_has_no_construction_only_inventory_or_checkpoint(self):
        forbidden = (
            "Source-first inventory",
            "coverage dispositions",
            "Inventory ID",
            "LSA-LSE-SI-",
            "初始处置",
            "覆盖处置",
            "developer notes",
            "internal checkpoint",
            "next work package",
        )
        for marker in forbidden:
            self.assertNotIn(marker, self.text)

        question_ids = re.findall(r"^## (LSA-LSE-Q-\d{4})$", self.text, re.MULTILINE)
        self.assertEqual(question_ids, [f"LSA-LSE-Q-{index:04d}" for index in range(1, 16)])


if __name__ == "__main__":
    unittest.main()
