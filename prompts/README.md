# Draft experimental prompt templates

These four files are model-neutral research materials for the proposed benchmark. They are not production application prompts and are not copied from the private product repository.

## Conditions

| ID | File | Manipulation |
| --- | --- | --- |
| C0 | `baseline.md` | Shared task and safety envelope only |
| C1 | `evidence-grounded.md` | Adds source discipline |
| C2 | `uncertainty-calibrated.md` | Adds confidence and ambiguity calibration |
| C3 | `combined.md` | Adds both intervention blocks |

`{{REFLECTION_TEXT}}` is a placeholder for one validated synthetic reflection. It must never be replaced with real personal data in the current study phase.

## Versioning rules

- Keep shared wording identical across conditions.
- Change one intervention block at a time and document the reason.
- Assign a prompt version and hash the rendered prompt before a run.
- Use a fresh request context for every generation.
- Do not add product memory, examples that reveal desired answers, or previous outputs.

The repository intentionally provides no API execution code. See `docs/experimental-conditions.md` for the manipulation design and `docs/api-budget.md` for execution gates.
