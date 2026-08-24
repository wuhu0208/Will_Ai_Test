from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
import hashlib
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "question_banks/LKW_R01_2023KW_C1N.md"
SOURCE = ROOT / "doc/LKW_R01_2023KW_C1N.pdf"


def question_block(text: str, question_id: str) -> str:
    match = re.search(
        rf"(?ms)^## {re.escape(question_id)}\s*$\n(.*?)(?=^## LKW-Q-|\Z)",
        text,
    )
    if not match:
        raise AssertionError(f"missing question block: {question_id}")
    return match.group(1)


class LkwSourceTruthRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = BANK.read_text(encoding="utf-8")

    def test_source_identity_and_question_set_are_frozen(self):
        expected_hash = (
            "fa9aeec4f6e0372cfcea2feeca751948b84f2d1e25609b677f8f2cb278c43064"
        )
        self.assertIn("source_pdf: LKW_R01_2023KW_C1N.pdf", self.text)
        self.assertIn(f"source_sha256: {expected_hash}", self.text)
        self.assertIn("source_pages: 52", self.text)
        self.assertEqual(hashlib.sha256(SOURCE.read_bytes()).hexdigest(), expected_hash)

        ids = re.findall(r"(?m)^## (LKW-Q-\d{4})$", self.text)
        expected_ids = [f"LKW-Q-{index:04d}" for index in range(1, 20)]
        self.assertEqual(ids, expected_ids)

    def test_question_statistics_match_frozen_types(self):
        expected = {
            "FACT": 3,
            "SPEC_LOOKUP": 3,
            "TABLE": 2,
            "MODEL": 2,
            "CALCULATION": 1,
            "CHART": 2,
            "PROCEDURE": 2,
            "CAUTION": 4,
        }
        actual = Counter(re.findall(r"(?m)^\*\*Type: ([A-Z_]+)\*\*$", self.text))
        self.assertEqual(actual, Counter(expected))
        self.assertIn("- Total: 19", self.text)
        for question_type, count in expected.items():
            self.assertIn(f"- {question_type}: {count}", self.text)

    def test_business_question_answer_and_scoring_blocks_are_chinese(self):
        for heading in ("Question", "Standard Answer", "Scoring Standard"):
            blocks = re.findall(
                rf"(?ms)^### {heading}\s*$\n(.*?)(?=^### |^## LKW-Q-|\Z)",
                self.text,
            )
            self.assertEqual(len(blocks), 19)
            self.assertTrue(all(re.search(r"[\u3400-\u9fff]", block) for block in blocks))

    def test_question_scoring_is_atomic_and_totals_100(self):
        for index in range(1, 20):
            question_id = f"LKW-Q-{index:04d}"
            block = question_block(self.text, question_id)
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
            self.assertEqual(
                sum(int(weight) for _, weight, _ in points), 100, question_id
            )

    def test_calculation_gold_is_deterministic(self):
        force = Decimal("18.18") * Decimal("5.0") / (
            Decimal("50") - Decimal("21")
        )
        rounded = force.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        back_substitution = force * Decimal("29") / Decimal("18.18")

        self.assertEqual(rounded, Decimal("3.13"))
        self.assertLessEqual(abs(back_substitution - Decimal("5.0")), Decimal("1e-24"))

        block = question_block(self.text, "LKW-Q-0010")
        for required in (
            "F=(18.18×P)/(L-21)",
            "3.134482758620689655... kN",
            "ROUND_HALF_UP",
            "3.13 kN",
            "反算",
            "5.00 MPa",
        ):
            self.assertIn(required, block)

    def test_chart_gold_keeps_visual_evidence_and_tolerances(self):
        force = question_block(self.text, "LKW-Q-0011")
        eccentricity = question_block(self.text, "LKW-Q-0012")

        for block in (force, eccentricity):
            self.assertIn("**Type: CHART**", block)
            self.assertIn("CHART 容差", block)
            self.assertIn("- Evidence type: CHART", block)

        self.assertIn("约为 **`1.6 kN`**", force)
        self.assertIn("`1.45-1.75 kN`", force)
        self.assertIn("视觉读数", force)
        self.assertIn("读图来源", force)
        self.assertIn("约为 **`17 mm`**", eccentricity)
        self.assertIn("约为\n**`69 mm`**", eccentricity)
        self.assertIn("标准/A/K 型 `15-19 mm`", eccentricity)
        self.assertIn("H 型 `67-71 mm`", eccentricity)

    def test_model_grammar_and_binding_boundaries_are_frozen(self):
        model = question_block(self.text, "LKW-Q-0001")
        wildcard = question_block(self.text, "LKW-Q-0006")

        for required in (
            "LKW<主体尺寸>1-C<压板方向><传感阀符号>[-<选配件>]",
            "传感阀字段中的 `H` 表示夹紧动作确认型",
            "末尾选配件 `H` 表示高强度链接板型",
        ):
            self.assertIn(required, self.text if required.startswith("LKW<") else model)

        self.assertIn("- Binding: MODEL_FAMILY", wildcard)
        self.assertIn("`LKW0551-C□E-□`", wildcard)

    def test_document_common_binding_is_page_bounded(self):
        block = question_block(self.text, "LKW-Q-0018")
        self.assertIn("- Binding: DOCUMENT_COMMON", block)
        self.assertIn(
            "- Model / Scope: LKW_R01_2023KW_C1N.pdf :: ", block
        )
        self.assertIn("- Physical page: 33-34", block)
        self.assertIn("- Printed page: 1727-1728", block)

    def test_state_air_and_accessory_boundaries_are_frozen(self):
        state = question_block(self.text, "LKW-Q-0013")
        air = question_block(self.text, "LKW-Q-0014")
        bzl = question_block(self.text, "LKW-Q-0019")

        self.assertIn("仅 `LKW0401`", state)
        self.assertIn("SMC `AKH` 系列、开启压力 `0.005 MPa`", air)
        self.assertIn("基准为 `5 m` 以内", air)
        self.assertIn("`BZL0101-B` 的本体推荐紧固力矩为 `10 N·m`", bzl)
        self.assertIn("`BZL0201-B` 为 `25 N·m`", bzl)
        self.assertIn("已使用过的 BZL 不得再装到其他夹紧器", bzl)

    def test_delivery_has_no_construction_artifacts(self):
        forbidden = (
            "来源覆盖索引",
            "Coverage ID",
            "LKW-SI-",
            "初始处置",
            "artifacts/",
            "runs/",
            "checkpoint",
            "next work package",
            "developer notes",
            "Playwright",
            "Selenium",
            "WP1",
            "WP2",
            "WP3",
            "WP4",
            "WP5",
        )
        for token in forbidden:
            self.assertNotIn(token, self.text)


if __name__ == "__main__":
    unittest.main()
