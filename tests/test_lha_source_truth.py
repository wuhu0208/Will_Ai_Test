from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
BANK = ROOT / "question_banks/LHA_R00_2023KW_C1N.md"


def question_block(text: str, question_id: str) -> str:
    match = re.search(
        rf"(?ms)^## {re.escape(question_id)}\s*$\n(.*?)(?=^## LHA-Q-|\Z)",
        text,
    )
    if not match:
        raise AssertionError(f"missing question block: {question_id}")
    return match.group(1)


class LhaSourceTruthRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = BANK.read_text(encoding="utf-8")

    def test_source_identity_and_representative_set_are_frozen(self):
        self.assertIn("source_pdf: LHA_R00_2023KW_C1N.pdf", self.text)
        self.assertIn(
            "source_sha256: 662f538ada8c6b218e89e59b519079738cde290a3e1c1657116ef3618113947f",
            self.text,
        )
        self.assertIn("source_pages: 68", self.text)
        ids = re.findall(r"(?m)^## (LHA-Q-\d{4})$", self.text)
        self.assertEqual(len(ids), 127)
        self.assertEqual(len(ids), len(set(ids)))

    def test_business_question_answer_and_scoring_blocks_are_chinese(self):
        for heading in ("Question", "Standard Answer", "Scoring Standard"):
            blocks = re.findall(
                rf"(?ms)^### {heading}\s*$\n(.*?)(?=^### |^## LHA-Q-|\Z)",
                self.text,
            )
            self.assertEqual(len(blocks), 127)
            self.assertTrue(all(re.search(r"[\u3400-\u9fff]", block) for block in blocks))

    def test_model_grammar_keeps_order_and_combination_boundary(self):
        self.assertIn("`LHA0480-CL`", self.text)
        self.assertIn("`LHA0550-CR-P`", self.text)
        self.assertIn("不得写成 `LHA0550-C-R-P`", self.text)
        block = question_block(self.text, "LHA-Q-0028")
        self.assertIn("不能", block)
        self.assertIn("另行垂询确认", block)

    def test_calculation_gold_keeps_formula_rounding_and_back_substitution(self):
        forward = question_block(self.text, "LHA-Q-0203")
        inverse = question_block(self.text, "LHA-Q-0206")
        self.assertIn("F=P×(1-0.0011×L)/(1.0039+0.0011×L)", forward)
        self.assertIn("3.288 kN", forward)
        self.assertIn("ROUND_HALF_UP", forward)
        self.assertIn("所需压力=6.900 MPa", inverse)
        self.assertIn("可行性结论为可行", inverse)
        self.assertIn("ROUND_HALF_UP", inverse)

    def test_chart_gold_keeps_visual_evidence_and_tolerance(self):
        expected = {
            "LHA-Q-0199": ("约0.5 kN", "0.25至0.75 kN", "±0.25 kN"),
            "LHA-Q-0200": ("约2.1 kN", "1.6至2.6 kN", "±0.5 kN"),
            "LHA-Q-0201": ("约4.6 kN", "4.1至5.1 kN", "±0.5 kN"),
        }
        for question_id, (expected_read, expected_range, expected_tolerance) in expected.items():
            block = question_block(self.text, question_id)
            self.assertIn("- Evidence type: CHART", block)
            self.assertIn(expected_read, block)
            self.assertIn(expected_range, block)
            self.assertIn(
                f"- 图表读数允许误差：{expected_tolerance}。",
                block,
            )
            evidence = block.split("- Evidence: ", 1)[1]
            self.assertIn(f"图表读数容差为{expected_tolerance}", evidence)

        self.assertNotIn("±0.5 kN", question_block(self.text, "LHA-Q-0199"))
        for question_id in ("LHA-Q-0200", "LHA-Q-0201"):
            self.assertNotIn("±0.25 kN", question_block(self.text, question_id))

    def test_document_common_binding_is_limited_to_true_common_material(self):
        common_ids = {
            question_id
            for question_id in re.findall(r"(?m)^## (LHA-Q-\d{4})$", self.text)
            if "- Binding: DOCUMENT_COMMON" in question_block(self.text, question_id)
        }
        self.assertEqual(
            common_ids,
            {
                "LHA-Q-0063",
                "LHA-Q-0064",
                "LHA-Q-0065",
                "LHA-Q-0066",
                "LHA-Q-0120",
                "LHA-Q-0123",
                "LHA-Q-0178",
                "LHA-Q-0179",
                "LHA-Q-0180",
                "LHA-Q-0181",
                "LHA-Q-0182",
                "LHA-Q-0183",
                "LHA-Q-0184",
                "LHA-Q-0185",
                "LHA-Q-0186",
                "LHA-Q-0187",
                "LHA-Q-0188",
                "LHA-Q-0189",
                "LHA-Q-0190",
                "LHA-Q-0192",
            },
        )
        self.assertNotIn("LHA/液压通用", self.text)

    def test_lha_and_accessory_targets_keep_local_identity(self):
        expected = {
            "LHA-Q-0167": ("MODEL_FAMILY", "LHA-M 系列"),
            "LHA-Q-0169": ("PRODUCT_SERIES", "LHA 系列"),
            "LHA-Q-0175": ("MODEL_FAMILY", "LHA-D 系列"),
            "LHA-Q-0191": ("EXACT_MODEL", "BZS0200"),
            "LHA-Q-0193": ("MODEL_FAMILY", "LZ-MP 系列"),
            "LHA-Q-0194": ("MODEL_FAMILY", "LHA0650-D 系列"),
        }
        for question_id, (binding, scope) in expected.items():
            block = question_block(self.text, question_id)
            self.assertIn(f"- Binding: {binding}", block)
            self.assertIn(f"- Model / Scope: {scope}", block)
            self.assertNotIn("KOSMEK 液压产品通用内容", block)

    def test_reviewed_source_evidence_binds_scored_fact(self):
        expected = {
            "LHA-Q-0118": ("Physical page: 38", "快换压板F型用安装螺栓", "LZH□-B"),
            "LHA-Q-0131": ("Model BZT", "速度控制阀（高压用）", "35 MPa"),
            "LHA-Q-0169": ("焊渣", "动作不正常", "漏油"),
            "LHA-Q-0185": ("活塞杆和柱塞周围", "密封材料", "漏油"),
            "LHA-Q-0193": ("LZ-MP", "LC、TC", "板式安装座适用型号"),
        }
        for question_id, phrases in expected.items():
            block = question_block(self.text, question_id)
            for phrase in phrases:
                self.assertIn(phrase, block)

    def test_document_common_evidence_covers_scored_facts(self):
        expected = {
            "LHA-Q-0063": ("动作时间异常变长", "2 MPa以下", "排净后紧固"),
            "LHA-Q-0064": ("ISO VG 32",),
            "LHA-Q-0065": ("不要擅自", "分解或改造"),
            "LHA-Q-0066": ("异物或切削屑", "漏油", "动作不良", "彻底清洁"),
            "LHA-Q-0120": ("Rz 25", "Ra 6.3"),
            "LHA-Q-0123": ("OR NBR-70-1 P7-N", "1AP7"),
            "LHA-Q-0178": ("1至2个螺纹牙", "漏油", "动作不正常"),
            "LHA-Q-0179": ("配管作业后", "泵油箱排空", "排气"),
            "LHA-Q-0180": ("内置单向阀", "释放动作脉动", "异常变长"),
            "LHA-Q-0181": ("回油节流回路", "空气", "速度控制"),
            "LHA-Q-0182": ("进油节流回路", "异常高压", "漏油或损坏"),
            "LHA-Q-0183": ("切断压力源和电源", "压力均为零"),
            "LHA-Q-0184": ("严禁接触动作中的夹紧器", "手指夹伤"),
            "LHA-Q-0185": ("定期清扫", "损伤密封材料", "漏油"),
            "LHA-Q-0186": (
                "配管、安装螺栓、螺母、固定环和夹紧器",
                "及时加固",
            ),
            "LHA-Q-0187": ("发货后1年半", "开始使用后1年", "较短者"),
            "LHA-Q-0188": ("本公司责任", "更换或修理"),
            "LHA-Q-0189": ("定期检查维护", "判断失误", "第三方", "产品质量", "改造、修理", "自然灾害", "磨损老化"),
            "LHA-Q-0190": ("间接损失", "不在质保范围"),
            "LHA-Q-0192": ("NBR-70-1", "NBR-90", "P：滑动用", "N：一般用"),
        }
        for question_id, phrases in expected.items():
            evidence = question_block(self.text, question_id).split("- Evidence: ", 1)[1]
            for phrase in phrases:
                self.assertIn(phrase, evidence)

    def test_q0066_matches_common_page_predicate_and_consequence(self):
        block = question_block(self.text, "LHA-Q-0066")
        self.assertIn("异物或切削屑会导致漏油", block)
        self.assertIn("异物或切削屑会导致动作不良", block)
        self.assertIn("配管、管接头及配件油孔在使用前彻底清洁", block)
        self.assertNotIn("阀和夹紧器动作不良或损伤", block)

    def test_q0189_evidence_contains_all_seven_warranty_exclusions(self):
        block = question_block(self.text, "LHA-Q-0189")
        evidence = block.split("- Evidence: ", 1)[1]
        for phrase in (
            "定期检查维护",
            "判断失误或使用不当",
            "用户或第三方不当使用",
            "非本公司产品质量原因",
            "未经本公司同意改造、修理",
            "自然灾害等非本公司责任",
            "磨损老化备件及其更换费用",
        ):
            self.assertIn(phrase, evidence)

    def test_scope_statistics_match_rebound_targets(self):
        self.assertIn("- Direct LHA: 72", self.text)
        self.assertIn("- Accessory / Related Product: 35", self.text)
        self.assertIn("- Document Common: 20", self.text)

    def test_scope_excludes_nontechnical_contact_questions(self):
        self.assertNotIn("LHA-Q-0068", self.text)
        self.assertNotIn("LHA-Q-0069", self.text)
        self.assertIn("公司地址、销售网点等非技术联系信息不收录", self.text)

    def test_delivery_has_no_construction_artifacts(self):
        forbidden = (
            "artifacts/",
            "runs/",
            "checkpoint",
            "next work package",
            "developer notes",
            "Playwright",
            "Selenium",
        )
        for token in forbidden:
            self.assertNotIn(token, self.text)


if __name__ == "__main__":
    unittest.main()
