from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_dataset import validate_dataset, validate_record


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_DATASET = REPOSITORY_ROOT / "data" / "synthetic-examples.sample.jsonl"


def valid_record() -> dict[str, object]:
    return {
        "reflection_id": "syn-900",
        "category": "time_management",
        "text": "I planned three small tasks and completed two of them.",
        "synthetic": True,
        "contains_personal_data": False,
        "clinical_content": False,
        "paraphrase_group": "pg-900",
        "notes": "Fictional test fixture.",
    }


class RecordValidationTests(unittest.TestCase):
    def test_valid_record_has_no_errors(self) -> None:
        self.assertEqual(validate_record(valid_record(), 1), [])

    def test_required_field_is_reported(self) -> None:
        record = valid_record()
        del record["text"]
        errors = validate_record(record, 7)
        self.assertTrue(any("line 7" in error and "text" in error for error in errors))

    def test_safety_flags_must_be_exact_booleans(self) -> None:
        cases = {
            "synthetic": False,
            "contains_personal_data": True,
            "clinical_content": True,
        }
        for field, invalid_value in cases.items():
            with self.subTest(field=field):
                record = valid_record()
                record[field] = invalid_value
                errors = validate_record(record, 1)
                self.assertTrue(any(field in error for error in errors))

    def test_unknown_field_is_rejected(self) -> None:
        record = valid_record()
        record["private_note"] = "not allowed"
        errors = validate_record(record, 1)
        self.assertTrue(any("unknown fields: private_note" in error for error in errors))


class DatasetValidationTests(unittest.TestCase):
    def write_lines(self, lines: list[str]) -> tuple[tempfile.TemporaryDirectory[str], Path]:
        temporary_directory = tempfile.TemporaryDirectory()
        path = Path(temporary_directory.name) / "dataset.jsonl"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return temporary_directory, path

    def test_repository_sample_is_valid(self) -> None:
        count, errors = validate_dataset(SAMPLE_DATASET)
        self.assertEqual(count, 12)
        self.assertEqual(errors, [])

    def test_invalid_json_has_line_and_column(self) -> None:
        temporary_directory, path = self.write_lines(["{not-json}"])
        self.addCleanup(temporary_directory.cleanup)
        count, errors = validate_dataset(path)
        self.assertEqual(count, 0)
        self.assertTrue(any("line 1" in error and "column" in error for error in errors))

    def test_duplicate_identifier_is_rejected(self) -> None:
        first = valid_record()
        second = valid_record()
        temporary_directory, path = self.write_lines(
            [json.dumps(first), json.dumps(second)]
        )
        self.addCleanup(temporary_directory.cleanup)
        count, errors = validate_dataset(path)
        self.assertEqual(count, 2)
        self.assertTrue(any("duplicate reflection_id" in error for error in errors))

    def test_blank_line_is_rejected(self) -> None:
        temporary_directory, path = self.write_lines(
            [json.dumps(valid_record()), "", json.dumps({**valid_record(), "reflection_id": "syn-901"})]
        )
        self.addCleanup(temporary_directory.cleanup)
        count, errors = validate_dataset(path)
        self.assertEqual(count, 2)
        self.assertTrue(any("blank lines are not allowed" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
