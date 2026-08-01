# Reproducibility plan

**Status:** Draft. The current repository contains protocol materials and offline validation only.

## Reproducibility goals

The project aims to make it possible to determine exactly which input, prompt condition, model configuration, response, and annotation produced each reported value. Reproducibility does not mean that a stochastic hosted model will return identical text indefinitely; it means that inputs, procedures, versions, and divergence are observable.

## Freeze points

The study will use explicit stages:

1. **Protocol draft:** questions, dimensions, and boundaries remain editable.
2. **Pilot freeze:** pilot dataset, prompt versions, and rubric version are tagged.
3. **Main-run freeze:** benchmark, exclusions, models, repeats, parameters, and analysis plan are locked before main outcomes are inspected.
4. **Analysis release:** deviations, results, annotations, and environment information are released together where permitted.

Each freeze should use a signed or otherwise identifiable Git tag if the maintainer's workflow supports it. No tag will imply publication or peer review.

## Stable identifiers

Planned identifiers include:

- `reflection_id` for one surface text;
- `paraphrase_group` for semantically equivalent variants;
- `condition` for one of the four prompt conditions;
- exact `model` identifier;
- `generation_repeat` for an independent request;
- `response_id` derived from the run manifest, not response content; and
- annotation record identifiers linked to one response or response set.

Identifiers must not encode names, emails, or private source paths.

## Versioned artefacts

The main-run manifest will reference cryptographic hashes for:

- canonical JSONL input;
- JSON Schemas;
- prompt templates and rendered prompts;
- execution configuration;
- raw response files;
- annotation files; and
- analysis code and environment lock files, if added later.

Canonicalisation rules—encoding, newline style, JSON serialisation, and record order—must be documented before hashes are used as evidence of equivalence.

## Inference manifest

Each planned request row should contain at least:

- run and request identifiers;
- reflection and paraphrase identifiers;
- condition and prompt hash;
- model identifier and requested parameters;
- repeat index and random seed where supported;
- planned execution order;
- start and end timestamps in UTC;
- success, refusal, failure, or retry status;
- token-use metadata when returned; and
- raw response location and content hash.

Retries must append an attempt record. They must not silently overwrite a valid but undesirable response.

## Prompt rendering

One deterministic renderer should combine a frozen template and reflection text. It should reject unknown placeholders and record the exact rendered prompt. No private product instructions, previous conversation state, or unversioned examples may be injected at runtime.

The current repository intentionally does not implement this renderer or API execution. Adding them requires a separate reviewed change after the protocol and budget are approved.

## Annotation reproducibility

Annotation releases should include:

- rubric version;
- response or set identifiers;
- integer scores and score direction;
- short rationales and response spans where applicable;
- ambiguity and masking-break flags;
- annotator pseudonym or role;
- original and adjudicated values; and
- timestamps or batches sufficient to reconstruct the process without publishing personal information.

Calibration items must be distinguishable from main-study items. If a rubric change requires re-annotation, mixed versions should not be pooled silently.

## Analysis reproducibility

Before the main run, the analysis plan should define:

- primary contrasts and outcomes;
- response- and set-level units;
- treatment of dependence and missingness;
- effect-size and interval methods;
- multiplicity approach;
- composite construction, if any;
- exclusion and protocol-deviation rules; and
- planned sensitivity and exploratory analyses.

Generated tables and figures should be buildable from versioned machine-readable inputs. Manual changes to reported values are not permitted.

## Environment capture

The validator uses the Python standard library. Future analysis or inference environments should record runtime and dependency versions using an appropriate lock file and include a minimal reproduction command. Hosted API behaviour outside the investigator's control will be described as such.

## Release checklist

Before a research release:

- validate JSONL and schemas;
- run all tests;
- verify hashes and record counts;
- scan for secrets, personal data, and private paths;
- check that model-output redistribution is permitted for the intended release;
- publish the protocol version and deviation log;
- verify that no result is described as peer reviewed, approved, or endorsed without evidence; and
- preserve null and failed outcomes according to the frozen plan.
