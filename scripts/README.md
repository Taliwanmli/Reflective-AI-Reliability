# Offline dataset validation

`validate_dataset.py` checks JSONL structure and the study's required synthetic-data flags. It uses only the Python standard library and makes no network or API request.

## Requirements

- Python 3.11 or later

## Run the validator

From the repository root:

```bash
python3 scripts/validate_dataset.py data/synthetic-examples.sample.jsonl
```

A valid file prints its record count and exits with status 0. An invalid file prints line-specific errors to standard error and exits with status 1. Missing or unreadable files exit with status 2.

## Run tests

```bash
python3 -m unittest discover -s tests -v
```

## What is checked

- valid JSON object on every non-blank line;
- required and unknown fields;
- identifier and paraphrase-group formats;
- allowed category;
- non-empty reflection text;
- `synthetic` is exactly `true`;
- `contains_personal_data` and `clinical_content` are exactly `false`; and
- reflection identifiers are unique within the file.

## What is not checked

The validator cannot determine whether prose is genuinely fictional, identifiable in context, clinically sensitive, semantically equivalent to a paraphrase, or copied from a private source. Those checks require provenance and human review.
