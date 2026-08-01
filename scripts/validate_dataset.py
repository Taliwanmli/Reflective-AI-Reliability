#!/usr/bin/env python3
"""Validate synthetic reflection JSONL without network access."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = {
    "reflection_id",
    "category",
    "text",
    "synthetic",
    "contains_personal_data",
    "clinical_content",
    "paraphrase_group",
    "notes",
}

ALLOWED_CATEGORIES = {
    "university_and_study_pressures",
    "career_choices",
    "interpersonal_uncertainty",
    "habits_and_personal_goals",
    "ordinary_achievements_and_setbacks",
    "time_management",
    "confidence_and_motivation",
    "everyday_non_clinical_stress",
}

REFLECTION_ID_PATTERN = re.compile(r"^syn-[0-9]{3}(?:-p[0-9]{2})?$")
PARAPHRASE_GROUP_PATTERN = re.compile(r"^pg-[0-9]{3}$")


def _field_error(line_number: int, field: str, message: str) -> str:
    return f"line {line_number}: field '{field}' {message}"


def validate_record(record: Any, line_number: int) -> list[str]:
    """Return validation errors for one decoded JSON value."""
    if not isinstance(record, dict):
        return [f"line {line_number}: record must be a JSON object"]

    errors: list[str] = []
    fields = set(record)
    missing = sorted(REQUIRED_FIELDS - fields)
    unknown = sorted(fields - REQUIRED_FIELDS)

    if missing:
        errors.append(
            f"line {line_number}: missing required fields: {', '.join(missing)}"
        )
    if unknown:
        errors.append(f"line {line_number}: unknown fields: {', '.join(unknown)}")

    reflection_id = record.get("reflection_id")
    if not isinstance(reflection_id, str) or not REFLECTION_ID_PATTERN.fullmatch(
        reflection_id
    ):
        errors.append(
            _field_error(
                line_number,
                "reflection_id",
                "must match 'syn-000' or 'syn-000-p00'",
            )
        )

    category = record.get("category")
    if category not in ALLOWED_CATEGORIES:
        errors.append(
            _field_error(line_number, "category", "is not an allowed category")
        )

    text = record.get("text")
    if not isinstance(text, str) or not text.strip():
        errors.append(
            _field_error(line_number, "text", "must be a non-empty string")
        )
    elif len(text) > 2000:
        errors.append(
            _field_error(line_number, "text", "must be at most 2000 characters")
        )

    if record.get("synthetic") is not True:
        errors.append(_field_error(line_number, "synthetic", "must be true"))
    if record.get("contains_personal_data") is not False:
        errors.append(
            _field_error(line_number, "contains_personal_data", "must be false")
        )
    if record.get("clinical_content") is not False:
        errors.append(
            _field_error(line_number, "clinical_content", "must be false")
        )

    paraphrase_group = record.get("paraphrase_group")
    if not isinstance(
        paraphrase_group, str
    ) or not PARAPHRASE_GROUP_PATTERN.fullmatch(paraphrase_group):
        errors.append(
            _field_error(
                line_number, "paraphrase_group", "must match 'pg-000'"
            )
        )

    notes = record.get("notes")
    if not isinstance(notes, str):
        errors.append(_field_error(line_number, "notes", "must be a string"))
    elif len(notes) > 500:
        errors.append(
            _field_error(line_number, "notes", "must be at most 500 characters")
        )

    return errors


def validate_dataset(path: Path) -> tuple[int, list[str]]:
    """Validate a JSONL file and return (decoded record count, errors)."""
    errors: list[str] = []
    record_count = 0
    seen_ids: dict[str, int] = {}

    with path.open("r", encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            if not raw_line.strip():
                errors.append(f"line {line_number}: blank lines are not allowed")
                continue

            try:
                record = json.loads(raw_line)
            except json.JSONDecodeError as exc:
                errors.append(
                    f"line {line_number}: invalid JSON at column {exc.colno}: {exc.msg}"
                )
                continue

            record_count += 1
            errors.extend(validate_record(record, line_number))

            if isinstance(record, dict):
                reflection_id = record.get("reflection_id")
                if isinstance(reflection_id, str):
                    first_line = seen_ids.get(reflection_id)
                    if first_line is None:
                        seen_ids[reflection_id] = line_number
                    else:
                        errors.append(
                            f"line {line_number}: duplicate reflection_id "
                            f"'{reflection_id}' first seen on line {first_line}"
                        )

    if record_count == 0:
        errors.append("dataset contains no JSON records")

    return record_count, errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate a synthetic reflection JSONL dataset offline."
    )
    parser.add_argument("dataset", type=Path, help="path to the JSONL dataset")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    try:
        record_count, errors = validate_dataset(args.dataset)
    except (OSError, UnicodeError) as exc:
        print(f"Could not read {args.dataset}: {exc}", file=sys.stderr)
        return 2

    if errors:
        print(
            f"Validation failed for {args.dataset} with {len(errors)} error(s):",
            file=sys.stderr,
        )
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {record_count} records in {args.dataset}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
