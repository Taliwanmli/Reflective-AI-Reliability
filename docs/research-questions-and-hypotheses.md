# Research questions and draft hypotheses

**Status:** Draft and subject to methodological review. No hypothesis has been tested in this repository.

## Constructs

For this study, **evidence grounding** means that substantive claims can be traced to text supplied in the reflection and that interpretations are marked as interpretations. **Uncertainty calibration** means that expressed confidence matches the support and ambiguity in the input. **Reliability** is treated as a profile of response-level quality and risk measures plus set-level stability; it is not assumed to be one universal score.

## Primary research questions

### RQ1: Evidence grounding

How does an explicit evidence-grounding instruction change source grounding, unsupported inference, and emotional or psychological overreach relative to a neutral baseline?

**H1a:** Evidence-grounded and combined conditions will receive higher source-grounding scores than the neutral baseline.  
**H1b:** Evidence-grounded and combined conditions will receive lower unsupported-inference and overreach risk scores than the neutral baseline.

### RQ2: Uncertainty calibration

How does an explicit uncertainty-calibration cue change uncertainty calibration, directive intensity, and transparency about limitations?

**H2a:** Uncertainty-calibrated and combined conditions will receive higher uncertainty-calibration scores than the neutral baseline.  
**H2b:** They will receive lower directive-intensity risk and higher limitation-transparency scores than the neutral baseline.

### RQ3: Combined intervention

Does combining evidence grounding with uncertainty calibration provide an additive benefit, create a trade-off, or produce no material improvement beyond either intervention alone?

**H3a:** The combined condition will show the strongest pre-specified reliability profile: higher grounding and calibration with lower unsupported inference and overreach.  
**H3b:** Any gain may be accompanied by lower practical-usefulness ratings if responses become excessively hedged or formulaic; this trade-off will be estimated rather than assumed away.

### RQ4: Phrasing robustness

How much do scores and substantive interpretations vary across meaning-preserving paraphrases?

**H4:** Intervention conditions, especially the combined condition, will have less within-scenario variation and fewer substantive contradictions across paraphrases than the neutral baseline.

### RQ5: Repeated-generation consistency

How much do outputs vary across independent generations of the same model, prompt condition, and reflection variant?

**H5:** Explicit intervention conditions will reduce severe within-cell disagreements, although surface wording will remain stochastic.

## Secondary and exploratory questions

- Do effects differ by scenario category, reflection length, writing register, or whether advice is explicitly requested?
- Do compared models respond differently to the same intervention?
- Which error types remain common in the combined condition?
- When does calibrated language become unhelpful boilerplate?

These analyses will be labelled exploratory unless their contrasts and error controls are frozen before the main run.

## Outcome mapping

| Question | Primary outcomes | Unit |
| --- | --- | --- |
| RQ1 | Source grounding; unsupported inference; emotional or psychological overreach | Response |
| RQ2 | Uncertainty calibration; directive intensity; transparency about limitations | Response |
| RQ3 | Pre-specified multi-dimensional profile; practical usefulness | Response |
| RQ4 | Robustness to paraphrasing; score dispersion; contradiction count | Paraphrase set |
| RQ5 | Consistency; score dispersion; contradiction count | Repeat set |

Score directions and anchors are defined in the [evaluation rubric](evaluation-rubric.md). A composite outcome, if used, must be specified before main-study outcome inspection and reported alongside its component dimensions.

## Hypothesis-free integrity checks

The following are quality checks, not evidence for the hypotheses:

- dataset and manifest validation;
- equal planned cell counts or documented missingness;
- prompt-render hashes;
- duplicate-response detection;
- annotation completion and confidence flags; and
- verification that set-level scores use the intended linked records.
