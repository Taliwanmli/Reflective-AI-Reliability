# Draft research protocol

**Working title:** Evidence-Grounded and Uncertainty-Calibrated AI for Personal Reflection<br>
**Status:** Protocol development; no study results are reported<br>
**Investigator:** Shiwen Tian, Computer Science undergraduate, Department of Informatics, King's College London<br>
**Protocol version:** 0.1 draft

This document describes a proposed undergraduate research project. It is not a registration, ethics approval, publication, peer-reviewed protocol, or statement of endorsement by King's College London or OpenAI.

## 1. Research problem

Language models can produce fluent interpretations of short personal reflections even when the text supports several meanings. In a reflective context, the distinction between an observation, a plausible interpretation, and an unsupported claim is especially important because the response concerns the writer's experiences, motives, emotions, or choices.

The proposed study asks whether two prompt-level interventions—evidence grounding and uncertainty calibration—improve response reliability without making responses unhelpful or formulaic. It also tests whether observed effects survive natural, meaning-preserving changes in user phrasing.

## 2. Why this context requires care

First-person reflections can contain private material and invite psychological interpretation. A model may:

- restate an inference as though the writer supplied it;
- assign an emotion, motive, trait, or recurring pattern without adequate evidence;
- express unwarranted confidence;
- give directives where reflective, choice-preserving language would be more appropriate; or
- change its interpretation when surface wording changes but meaning does not.

The present phase avoids real user data and clinical scenarios. It studies response behaviour under controlled synthetic inputs, not therapeutic efficacy, mental-health outcomes, or the lived experience of actual users.

## 3. Objectives and research questions

The primary objective is to estimate how the four prompt conditions affect response reliability. The secondary objective is to characterise variation across paraphrases and repeated generations.

The precise questions and directional draft hypotheses are specified in [research questions and hypotheses](research-questions-and-hypotheses.md). In summary:

1. Does evidence grounding improve traceability to the supplied reflection and reduce unsupported inference?
2. Does uncertainty calibration reduce overconfidence and inappropriate direction while preserving usefulness?
3. Does the combined condition outperform either intervention alone on a pre-specified reliability profile?
4. How stable are responses across semantically equivalent paraphrases and repeated generations?

## 4. Study design

### 4.1 Design overview

The proposed benchmark is a blocked, repeated-measures comparison. Every eligible reflection variant will be submitted under each of four experimental conditions:

1. neutral baseline;
2. evidence-grounded;
3. uncertainty-calibrated; and
4. combined evidence-grounded and uncertainty-calibrated.

Condition definitions are in [experimental conditions](experimental-conditions.md). Each text therefore acts as its own comparison block. Model and generation repeat will be recorded rather than pooled invisibly.

### 4.2 Synthetic benchmark

The target is approximately 120 base scenarios, provisionally balanced across eight categories (about 15 per category):

- university and study pressures;
- career choices;
- interpersonal uncertainty;
- habits and personal goals;
- ordinary achievements and setbacks;
- time management;
- confidence and motivation; and
- everyday non-clinical stress.

The exact count and balance will be frozen before the main run. All scenarios will be fictional, non-identifiable, non-clinical first-person reflections. The small file in `data/` demonstrates the record format only; it is not the completed benchmark.

### 4.3 Construction process

Each base scenario will be authored from a scenario specification containing a category, intended facts, deliberately unresolved points, and prohibited inferences. Construction will follow these steps:

1. Draft a short fictional reflection without names, contact details, precise locations, account identifiers, or distinctive biographical combinations.
2. Screen out clinical, medical-treatment, crisis, self-harm, abuse, criminal-conduct, and high-stakes professional-advice content.
3. Record what the text explicitly supports and where more than one interpretation remains plausible.
4. Review for accidental resemblance to genuine diary material and rewrite or exclude any doubtful case.
5. Validate the machine-readable record and retain a versioned content hash.

No private diary entry, user message, product prompt, or production data may be used as a seed.

### 4.4 Paraphrase generation

Each base scenario is planned to have two semantically equivalent paraphrases, giving three surface variants per semantic group. This count is provisional and will be fixed before data collection.

Paraphrases will vary features such as sentence order, register, directness, punctuation, brevity, and everyday wording while preserving:

- the events and facts stated;
- the degree of emotional explicitness;
- unresolved ambiguity;
- temporal relations; and
- whether advice is requested.

Each paraphrase will receive a semantic-equivalence review against the scenario specification. A paraphrase that adds or removes a material claim will be revised or excluded. If model assistance is later used to draft paraphrases, the model, prompt, settings, and human review decision will be recorded; no such generation is performed by this repository at present.

### 4.5 Experimental conditions

All conditions share the same task framing, input placeholder, length target, and non-clinical safety envelope. Only the planned intervention language differs. This limits avoidable confounding by tone or output format. Prompt templates are versioned in `prompts/` and are draft experimental materials, not production prompts.

### 4.6 Models and repeated generations

Publicly available OpenAI API models may be compared, subject to access, budget, and protocol review. Exact model snapshots or dated identifiers will be selected before the main run. The study will not silently substitute a newer model under the same label.

For each model, every reflection variant and condition will receive a pre-specified number of independent generations. A fresh request context will be used for each generation. The following will be frozen and recorded:

- exact model identifier and access date;
- prompt-template commit and rendered prompt hash;
- generation parameters and random seed where the service exposes one;
- requested and observed token usage;
- generation repeat index;
- request status and any retry reason; and
- provider-returned identifiers that are appropriate to retain.

The number of models and repeats remains to be determined. The [API budget](api-budget.md) shows the request formula and spending gates. Running this repository currently makes no API request.

### 4.7 Assignment and execution order

Requests will be generated from a manifest created before inference. Execution order will be randomised within blocks to reduce time-of-run and transient-service confounding. Retries will follow a written rule and will not replace an undesirable but technically valid response. Failed requests will remain visible in the run manifest.

## 5. Evaluation

### 5.1 Units of analysis

Two units are planned:

- **Response level:** one model response to one reflection variant under one condition, model, and repeat.
- **Set level:** linked responses across repeats or paraphrases for the same semantic scenario, condition, and model.

Source grounding, unsupported inference, uncertainty calibration, directive intensity, emotional or psychological overreach, practical usefulness, and transparency are response-level dimensions. Consistency across repeats and robustness to paraphrasing are set-level dimensions.

### 5.2 Annotation process

The investigator will apply the versioned [evaluation rubric](evaluation-rubric.md). The planned process is:

1. Pilot the rubric on a small, separately marked calibration set.
2. Revise ambiguous anchors before freezing the main codebook.
3. Present responses without condition labels and, where practical, without model labels.
4. Annotate each response independently of its siblings before performing set-level comparisons.
5. Record a score, short rationale, cited response span where applicable, confidence flag, and adjudication note.
6. Re-annotate a random subset after a washout interval to estimate intra-rater stability.

A second human annotator has not been confirmed. If one becomes available, the sampling fraction, training procedure, agreement statistic, and adjudication process will be specified before joint annotation. The repository will not imply inter-rater reliability unless it is actually measured.

### 5.3 Investigator annotation and masking limits

Complete masking may be impossible because intervention language can create recognisable response patterns and the investigator develops the protocol. The analysis will record which labels were hidden, whether masking was broken, and which judgments required adjudication. Annotator expectations are a threat to validity rather than something the protocol can eliminate by assertion.

### 5.4 Model-based evaluation

Automated or model-based judging is not part of the initial tooling. If later added, it will be supplementary and validated against held-out human annotations. Risks include preference for fluent answers, sensitivity to judge prompts, shared model-family biases, position effects, scale compression, and leakage of condition cues. Judge outputs will not be treated as ground truth.

## 6. Planned analysis

The final analysis plan will be frozen before inspecting main-study outcomes. The current proposal includes:

- score distributions, missingness, and floor or ceiling effects by condition and model;
- paired condition contrasts within the same reflection variant;
- effect sizes with uncertainty intervals, not significance labels alone;
- ordinal or otherwise scale-appropriate models with semantic scenario treated as a repeated grouping factor;
- condition-by-model interaction estimates, labelled exploratory unless powered and pre-specified;
- within-group dispersion across repeated generations;
- within-group dispersion and substantive disagreement across paraphrases;
- sensitivity analyses excluding ambiguous or protocol-deviating records; and
- qualitative error analysis of unsupported claims, overreach, directives, and useful calibrated responses.

The project will define any composite reliability outcome, score reversals, weighting, multiplicity correction, exclusion rule, and minimum practically relevant effect before the main analysis. If sample size or model assumptions do not support the proposed inferential model, the fallback will emphasise paired descriptive estimates and resampling intervals, with the change documented as a deviation.

## 7. Expected outputs

Planned outputs are:

- a versioned synthetic benchmark and paraphrase set;
- frozen prompt-condition materials;
- a run manifest and machine-readable response records;
- investigator annotations with applicable agreement checks;
- quantitative summaries and qualitative error categories; and
- a report that includes null, mixed, and adverse findings.

None of these outputs is represented as complete in the current repository.

## 8. Threats to validity

Key threats include construct validity of the rubric, investigator expectancy, limited scenario realism, imperfect paraphrase equivalence, prompt-format confounding, model updates, stochastic variability, dependence among variants, multiple comparisons, and limited generalisability beyond the chosen models and non-clinical synthetic scenarios. These are expanded in [limitations](limitations.md).

## 9. Reproducibility and deviations

The [reproducibility plan](reproducibility-plan.md) defines versioning, hashes, manifests, provenance, and release stages. Any change after protocol freeze will be logged with a date, rationale, affected artefacts, and whether outcomes had been inspected. Confirmatory and exploratory analyses will remain distinguishable.

## 10. Ethical and data-governance boundaries

The current proposed phase has no research participants and accepts no real personal reflections. Synthetic-only status does not justify claiming that ethics review is unnecessary. The applicable data-governance and institutional requirements will be considered as the design develops.

Any future human-participant study would be a separate project phase and would require consideration of the applicable King's College London ethics and data-governance processes before recruitment or data collection began. This repository does not claim that approval has been sought or obtained.

Further controls are specified in [data governance and ethics](data-governance-and-ethics.md).

## 11. Boundaries

This study does not evaluate diagnosis, therapy, crisis intervention, medical advice, or clinical outcomes. It does not test a deployed product, involve real diary data, measure long-term user benefit, or establish that a response is safe for every context. It does not claim that prompt instructions alone solve model reliability.
