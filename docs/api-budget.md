# API budget and execution gates

**Status:** Planning only. **Current authorised spend: zero.** This repository contains no API client and makes no model request.

## Request-count formula

Let:

- `B` = number of base semantic scenarios;
- `V` = surface variants per scenario, including the base;
- `C` = prompt conditions;
- `M` = model identifiers;
- `R` = independent generations per model-condition-input cell; and
- `A` = additional attempts caused by the pre-specified retry rule.

Planned primary requests are:

```text
primary_requests = B × V × C × M × R
total_attempts = primary_requests + A
```

With the current design targets `B = 120`, `V = 3`, and `C = 4`:

```text
primary_requests = 1,440 × M × R
```

For illustration only, two models and three repeats would require 8,640 primary requests before retries. This is not an approved run size or spending commitment.

## Token and cost formula

Before execution, a pilot will estimate the input and output token distributions using the exact rendered prompts. A conservative upper budget should use high-percentile rather than mean token counts.

For model `m`:

```text
input_cost_m  = input_tokens_m  / 1,000,000 × input_price_m
output_cost_m = output_tokens_m / 1,000,000 × output_price_m
total_cost    = Σ(input_cost_m + output_cost_m) + retry_reserve
```

Prices, model availability, caching rules, batch discounts, taxes, and currency conversion can change. They must be retrieved from authoritative current sources and recorded immediately before approval. This draft intentionally contains no monetary estimate based on stale or assumed prices.

## Execution gates

No API run may begin until all of the following are complete:

1. Protocol, benchmark schema, and condition templates are reviewed.
2. Exact models, repeats, generation parameters, and retry rules are frozen.
3. A small synthetic pilot confirms token estimates and technical validity.
4. Provider data-handling and output-reuse conditions applicable at that time are reviewed.
5. A maximum request count, token ceiling, currency amount, and funding source are approved by the investigator.
6. A hard client-side spending or request cap and a stop condition are implemented and tested without live calls where possible.
7. Credentials are supplied outside version control and logging is checked for reflection text and secrets.

## Staged plan

### Stage 0 — Offline only

Validate records, prompts, manifests, randomisation, hashes, and dry-run cost calculations. Cost: zero.

### Stage 1 — Technical pilot

Use a small, pre-specified subset solely to verify request construction, response capture, token estimates, and failure handling. Pilot responses will not be mixed into confirmatory results.

### Stage 2 — Method pilot

Use a separate subset to calibrate the rubric and assess whether prompt manipulations are distinguishable. Any resulting protocol change will be versioned before the main freeze.

### Stage 3 — Main run

Execute only the frozen manifest within the approved hard cap. Stop automatically on the cost ceiling, unexpected request growth, credential or logging concern, schema mismatch, or material provider change.

## Cost-control options

If the projected total is too high, reduce scope before data collection rather than stopping selectively after seeing outcomes. Options include fewer models, fewer repeats supported by a power or precision analysis, fewer paraphrases, or a staged model comparison. Any change must preserve balanced condition comparisons and be documented.

## Items still to determine

- exact model identifiers;
- number of models and repeats;
- input and output token caps;
- approved currency budget and funding source;
- retry reserve;
- whether a batch service is methodologically and operationally appropriate; and
- the retention and redistribution plan for model outputs.
