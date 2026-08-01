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

For Stage A, `B = 30`, `V = 3`, `C = 4`, `M = 1`, and `R = 2`:

```text
primary_requests = 30 × 3 × 4 × 1 × 2 = 720
```

The 720-request pilot count excludes retries and does not itself authorise spending. A Stage B expansion to 60–120 base scenarios would require a new calculation after the primary model count, repeat count, token observations, retry reserve, and scope are frozen. Additional models are costed as separate staged exploratory runs.

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

1. Protocol, benchmark schema, condition templates, and pilot decision criteria are reviewed.
2. Exact models, repeats, generation parameters, and retry rules are frozen.
3. Offline checks confirm request construction and a separately authorised synthetic pilot remains within the hard request and token caps.
4. Provider data-handling and output-reuse conditions applicable at that time are reviewed.
5. A maximum request count, token ceiling, currency amount, and funding source are approved by the investigator.
6. A hard client-side spending or request cap and a stop condition are implemented and tested without live calls where possible.
7. Credentials are supplied outside version control and logging is checked for reflection text and secrets.

## Staged plan

### Stage 0 — Offline only

Validate records, prompts, manifests, randomisation, hashes, and dry-run cost calculations. Cost: zero.

### Stage A1 — Technical verification

Use a small, pre-specified subset of Stage A solely to verify request construction, response capture, token estimates, and failure handling. These records remain marked as technical checks and are not silently replaced or pooled.

### Stage A2 — Method and feasibility pilot

Complete the frozen 30-scenario pilot to assess manipulation distinctness, ambiguity, paraphrase equivalence, rubric consistency, annotation time, financial and operational feasibility, and statistical appropriateness. If the protocol changes materially, the pilot remains separate from later confirmatory analysis.

### Stage B — Conditional expansion

Expand to approximately 60–120 base scenarios only if the pilot supports it and annotation capacity, time, funding, review, data quality, and the statistical plan make the larger scope credible. Execute only the newly frozen manifest within a newly approved hard cap. Stop automatically on the cost ceiling, unexpected request growth, credential or logging concern, schema mismatch, or material provider change.

## Cost-control options

If the projected total is too high, reduce Stage B before its data collection rather than stopping selectively after seeing outcomes. Options include remaining at the pilot scope, choosing the lower end of 60–120 scenarios, limiting detailed secondary annotation to a pre-specified stratified sample, or deferring additional-model comparisons. Any change must preserve balanced primary condition comparisons and be documented.

## Items still to determine

- exact model identifiers;
- any Stage B repeat count and exploratory model count;
- input and output token caps;
- approved currency budget and funding source;
- retry reserve;
- whether a batch service is methodologically and operationally appropriate; and
- the retention and redistribution plan for model outputs.
