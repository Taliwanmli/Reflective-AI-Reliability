# Synthetic reflection data

This directory contains fictional, non-identifiable, non-clinical research inputs. It must never contain real diary entries, participant data, copied private messages, or production product data.

## Current contents

`synthetic-examples.sample.jsonl` is a small format and validator fixture. It is not the planned benchmark and must not be described as collected data or study evidence.

Each line is one UTF-8 JSON object with:

| Field | Meaning |
| --- | --- |
| `reflection_id` | Stable identifier for one surface form |
| `category` | One planned non-clinical topic category |
| `text` | Fictional first-person reflection |
| `synthetic` | Must be `true` |
| `contains_personal_data` | Must be `false` |
| `clinical_content` | Must be `false` |
| `paraphrase_group` | Identifier linking eventual meaning-equivalent variants |
| `notes` | Non-sensitive provenance or review note |

The authoritative machine-readable contract is `schemas/reflection.schema.json`. The offline validator also performs duplicate-ID and required-flag checks.

## Planned benchmark

The target is approximately 120 base semantic scenarios across eight categories, with a provisional total of three surface variants per scenario (one base and two paraphrases). Exact counts will be frozen before the main run. The sample file contains base seeds only; paraphrase construction is future work.

## Authoring rules

- Write every scenario as fiction from a scenario specification, not from memory of a real person's entry.
- Use no names, contact details, usernames, precise locations, organisations tied to an event, or distinctive personal histories.
- Exclude self-harm, suicide, crisis, diagnosis, abuse, criminal conduct, medical treatment, and high-stakes professional advice.
- Keep scenarios non-clinical even when they concern ordinary stress, confidence, or uncertainty.
- Record material ambiguity rather than forcing one “correct” psychological interpretation.
- Exclude anything whose provenance or identifiability is doubtful.

## Validation

From the repository root:

```bash
python3 scripts/validate_dataset.py data/synthetic-examples.sample.jsonl
python3 -m unittest discover -s tests -v
```

Passing validation confirms structure and required flags only. Human review is still required for fictionality, identifiability, clinical boundaries, and semantic equivalence.

## Release provenance

A future benchmark release should state who or what drafted each item, whether model assistance was used, the human review procedure, exclusions, schema version, record count, and cryptographic hash. Dataset changes after a protocol freeze must be logged.
