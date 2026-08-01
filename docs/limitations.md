# Limitations and threats to validity

**Status:** Prospective analysis. No observed limitation is being inferred from study results because no study has been run.

## Construct validity

The nine evaluation dimensions are operational choices, not complete definitions of “reliability” or “usefulness.” Scores may overlap: unsupported inference can affect grounding, calibration, overreach, and usefulness at once. The pilot must test whether annotators can distinguish the constructs, and reports should show component outcomes rather than relying only on a composite.

Warmth, brevity, style, and fluency may influence usefulness ratings even when they are not experimental targets. A fluent response may be overvalued, while a cautious response may be penalised as generic. Anchor examples and masked presentation can reduce but not remove this problem.

## Synthetic-data validity

Synthetic reflections provide control and privacy but may be cleaner, shorter, and less culturally or linguistically complex than real reflections. They cannot reproduce the stakes, ambiguity, personal history, or consent expectations of real users. Results therefore will not establish real-world safety, therapeutic value, user trust, or long-term benefit.

Scenario authors may accidentally embed their own assumptions or make the intended interpretation unusually obvious. A scenario specification and review process can expose some of this bias, but the benchmark remains constructed.

## Paraphrase validity

A surface variant may unintentionally change emotional explicitness, advice-seeking, temporal order, or emphasis. Model differences could then be valid responses to changed meaning rather than failures of robustness. Paraphrases require equivalence review, and doubtful groups should be flagged before inference.

## Annotation validity

The investigator designs the protocol and may also annotate responses, creating expectancy and confirmation risks. Condition masking may be broken by recognisable response style. Intra-rater checks do not replace independent agreement, and a second annotator is not yet confirmed.

Annotation scales are ordinal. Treating intervals as equal without sensitivity analysis could overstate precision. Ambiguous scores, missing responses, and adjudication changes must remain visible.

## Model and platform validity

Model behaviour can change with snapshots, routing, safety systems, service updates, and undocumented platform components. A result tied only to a marketing model name may not reproduce later. Exact available identifiers, dates, parameters, and response metadata should be recorded, but provider-side behaviour may still be only partly observable.

Stage A uses one primary publicly available OpenAI API model. Any additional models are conditional exploratory comparisons. Findings would not automatically generalise to other providers, local models, future versions, conversational sessions, tools, retrieval systems, or production applications.

## Experimental validity

The shared safety envelope may already reduce overreach, compressing differences between conditions. Conversely, the combined condition is longer and may attract more model attention simply because it has more instructions. Prompt length, wording, and output format should be reported as possible confounds.

Repeated requests may experience time-of-day or transient-service effects. Randomised execution order and blocked analyses help, but cannot guarantee identical backend conditions.

## Statistical validity

Reflection variants from the same semantic group are dependent. Repeated generations are also nested within a model, condition, and input. Analyses that treat all outputs as independent would underestimate uncertainty.

Nine dimensions, four conditions, categories, and possible exploratory model comparisons create multiplicity. Confirmatory contrasts, score direction, exclusions, and any composite must be frozen before outcome inspection in the relevant stage. A 30-scenario pilot and small category cells may not support stable inferential or subgroup conclusions; feasibility estimates and paired descriptive summaries may be more appropriate.

Annotation capacity constrains credible scope. The pilot can receive full annotation, but a 60–120-scenario Stage B may require complete coverage only for primary outcomes and a pre-specified stratified sample for detailed secondary dimensions. Such sampling reduces precision and limits claims about unannotated outcomes. Intra-rater checks do not establish inter-rater reliability, and no such claim is warranted unless a second annotator actually contributes independent ratings.

Missing or refused responses may be informative rather than random. Reporting only valid generations could bias comparisons, so failure types and retry rules must be included.

## Scope boundaries

This project does not evaluate:

- clinical, diagnostic, therapeutic, or crisis performance;
- responses to real participants or real diary entries;
- downstream behavioural or wellbeing outcomes;
- privacy or security of a deployed application;
- multimodal, voice, memory, retrieval, or long-conversation systems;
- whether a prompt intervention prevents every unsafe output; or
- institutional, regulatory, or product compliance.

## Interpretation rule

Any future conclusion should be limited to the tested synthetic benchmark, prompt versions, model identifiers, generation settings, and evaluation procedure. Null, mixed, and adverse results should be reported with the same visibility as favourable results.
