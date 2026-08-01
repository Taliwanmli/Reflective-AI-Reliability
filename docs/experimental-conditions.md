# Experimental conditions

**Status:** Draft experimental materials. These conditions are model-neutral and are not production application prompts.

## Design principle

The four conditions should differ only in the reliability intervention. Task, input, output length, audience, and non-clinical safety boundaries should remain constant. This reduces the risk that a tone or formatting change is mistaken for an evidence-grounding or calibration effect.

## Shared task envelope

Every condition will:

- receive one synthetic, non-clinical first-person reflection;
- request one concise, respectful response intended to support reflection;
- prohibit diagnosis, clinical framing, claims of professional authority, and dependency-seeking language;
- avoid making high-stakes decisions for the writer;
- preserve the writer's control over interpretation and action; and
- use the same target length and output format.

The shared envelope is an ethical boundary, not an experimental intervention. It is included in the neutral baseline as well as the other conditions.

## Conditions

### C0 — Neutral baseline

Uses only the shared task envelope. It does not explicitly request claim-to-source tracing, separation of observation from interpretation, confidence labels, or uncertainty cues.

**Purpose:** Estimate response behaviour under a minimal, safety-bounded reflective instruction.

### C1 — Evidence-grounded

Adds instructions to:

- base factual observations only on the supplied reflection;
- distinguish observations from interpretations;
- avoid introducing events, emotions, motives, patterns, or traits not supported by the text; and
- keep any interpretation traceable to the relevant input evidence.

**Manipulated construct:** Evidence grounding.<br>
**Not intentionally manipulated:** Degree of hedging or confidence language beyond what follows from source discipline.

### C2 — Uncertainty-calibrated

Adds instructions to:

- match confidence to the amount and clarity of evidence;
- mark plausible interpretations as possibilities;
- acknowledge material ambiguity or insufficient information; and
- avoid certainty, fixed labels, and directives when the reflection does not justify them.

**Manipulated construct:** Uncertainty calibration.<br>
**Not intentionally manipulated:** Explicit claim-to-source tracing.

### C3 — Combined

Adds both C1 and C2 intervention blocks without introducing a third task or extra content requirement.

**Manipulated constructs:** Evidence grounding and uncertainty calibration.<br>
**Purpose:** Estimate joint effects and possible usefulness or verbosity trade-offs.

## Condition matrix

| Feature | C0 | C1 | C2 | C3 |
| --- | :---: | :---: | :---: | :---: |
| Shared safety envelope | Yes | Yes | Yes | Yes |
| Explicit source discipline | No | Yes | No | Yes |
| Observation/interpretation distinction | No | Yes | No | Yes |
| Explicit confidence calibration | No | No | Yes | Yes |
| Explicit ambiguity acknowledgement | No | No | Yes | Yes |

## Prompt implementation

The draft templates live in `prompts/`. Before use, they will be rendered through one deterministic procedure. The run manifest will store:

- condition identifier;
- template version and Git commit;
- normalised rendered-prompt hash;
- reflection identifier and semantic group;
- exact model identifier and parameters; and
- generation repeat index.

No condition may contain hidden product context, personal history, prior conversation state, or examples that reveal the preferred answer.

## Assignment and blocking

Every eligible reflection variant is planned to appear in every condition. Requests will be randomised within a manifest while retaining identifiers that support paired analysis. A fresh context will be used for each request so that one condition cannot influence another.

## Pre-run manipulation check

Before the main run, an independent prompt review should confirm that:

1. C1 and C3 contain the same evidence-grounding block.
2. C2 and C3 contain the same uncertainty-calibration block.
3. Shared wording is otherwise identical.
4. Output length and format are constant.
5. No condition names or expected outcomes are shown to the model.

A small pilot may test whether the manipulations are detectable without using pilot responses as confirmatory results. Any prompt revision after viewing pilot outputs will be versioned and the pilot will remain excluded from the main analysis.

## Known design tension

The safety envelope itself discourages some forms of overreach, which may reduce differences between conditions. Removing it would create a less responsible baseline and would test a different question. The study will therefore interpret condition effects as incremental improvements over a common minimum safety boundary.
