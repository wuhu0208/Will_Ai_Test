from pathlib import Path
import unittest

from tools.validate_question_bank import validate_question_bank


ROOT = Path(__file__).resolve().parent
VALID = ROOT / "fixtures/valid/SAMPLE.md"
SOURCE_ROOT = ROOT / "fixtures/valid"


class QuestionBankValidationTests(unittest.TestCase):
    def invalid_errors(self, fixture: str) -> list[str]:
        path = ROOT / f"fixtures/invalid/{fixture}/SAMPLE.md"
        return validate_question_bank(path, SOURCE_ROOT)

    def test_valid_fixture_passes(self):
        self.assertEqual(validate_question_bank(VALID, SOURCE_ROOT), [])

    def test_missing_standard_answer_fails(self):
        errors = self.invalid_errors("missing_standard_answer")
        self.assertTrue(any("missing section Standard Answer" in error for error in errors))

    def test_duplicate_id_fails(self):
        errors = self.invalid_errors("duplicate_id")
        self.assertTrue(any("duplicate question IDs" in error for error in errors))

    def test_bad_weight_fails(self):
        errors = self.invalid_errors("bad_weight")
        self.assertTrue(any("sum to 90" in error for error in errors))

    def test_missing_target_fails(self):
        errors = self.invalid_errors("missing_target")
        self.assertTrue(any("missing section Target" in error for error in errors))

    def test_missing_source_fails(self):
        errors = self.invalid_errors("missing_source")
        self.assertTrue(any("missing section Source" in error for error in errors))

    def test_valid_looking_wrong_source_hash_fails(self):
        errors = self.invalid_errors("wrong_hash")
        self.assertTrue(any("does not match actual source PDF" in error for error in errors))

    def test_missing_product_fails(self):
        errors = self.invalid_errors("missing_product")
        self.assertTrue(any("requires non-empty Product" in error for error in errors))

    def test_missing_model_scope_fails(self):
        errors = self.invalid_errors("missing_model_scope")
        self.assertTrue(any("requires non-empty Model / Scope" in error for error in errors))

    def test_ambiguous_document_common_fails(self):
        errors = self.invalid_errors("ambiguous_document_common")
        self.assertTrue(
            any("DOCUMENT_COMMON Model / Scope" in error for error in errors)
        )

    def test_workflow_status_front_matter_fails(self):
        errors = self.invalid_errors("workflow_status")
        self.assertTrue(any("workflow field is forbidden" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
