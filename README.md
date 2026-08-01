# Evidence-Grounded and Uncertainty-Calibrated AI for Personal Reflection

A protocol-first research scaffold for a proposed independent undergraduate research project on the reliability of language-model responses to synthetic, non-clinical personal reflections.

> **Status: Protocol development**<br>
> **Proposed independent undergraduate research project.** No sponsorship, supervision, approval, funding, or endorsement is claimed.<br>
> **No study results are reported yet.** The design, materials, and analysis plan remain subject to review and revision.

## Motivation

Personal reflections are a sensitive setting for language models: a short first-person account can support several plausible readings, while an overconfident response can turn a possibility into an apparent fact. This proposed independent undergraduate research project examines whether explicit evidence-grounding and uncertainty-calibration instructions make responses more reliable, and whether any gains persist when the same reflection is phrased differently.

## Research questions

1. How do evidence-grounding instructions affect source grounding, unsupported inference, and emotional or psychological overreach?
2. How do uncertainty-calibration cues affect confidence, directive intensity, and transparency about limitations?
3. Do the two interventions interact, and how robust are their effects across paraphrases and repeated generations?

The full questions and draft hypotheses are in [research questions and hypotheses](docs/research-questions-and-hypotheses.md).

## Proposed design

The study is staged so that feasibility is tested before its scope grows:

- **Stage A — pilot:** approximately 30 fictional base scenarios, three variants per scenario (the base plus two meaning-preserving paraphrases), four prompt conditions, one primary OpenAI API model, and two independent generations per cell. This is 720 planned primary requests before retries. The pilot tests manipulation distinctness, scenario ambiguity, paraphrase equivalence, rubric consistency, annotation time, financial and operational feasibility, and whether the proposed statistics fit the resulting data. If the protocol, prompts, rubric, or analysis changes materially, pilot observations remain separate from later confirmatory analysis.
- **Stage B — conditional expansion:** approximately 60–120 base scenarios only if the pilot supports expansion. The final count depends on annotation burden, available time and funding, methodological review, data quality, and the frozen statistical plan. Additional models are staged exploratory comparisons, not part of the primary design by default.

Each eligible semantic scenario has three surface variants and is evaluated under four conditions:

| Condition | Planned manipulation |
| --- | --- |
| Neutral baseline | Shared task and safety envelope only |
| Evidence-grounded | Explicitly separates supported observations from interpretations |
| Uncertainty-calibrated | Explicitly calibrates confidence and acknowledges ambiguity |
| Combined | Applies both interventions |

Planned evaluation dimensions are source grounding, unsupported inference, uncertainty calibration, directive intensity, emotional or psychological overreach, consistency, robustness to paraphrasing, practical usefulness, and transparency about limitations. The pilot is fully annotated. In a larger Stage B, primary outcomes are annotated completely where feasible, detailed secondary dimensions may use a pre-specified stratified sample, and a random subset is re-annotated for intra-rater stability. A second annotator is included only if one becomes available; no inter-rater claim is planned without actual independent annotation. Operational definitions are in the [evaluation rubric](docs/evaluation-rubric.md).

## Repository map

```text
docs/       Draft protocol, hypotheses, rubric, ethics, limitations, and plans
data/       Fictional sample records and data documentation
schemas/    Machine-readable reflection and evaluation record contracts
prompts/    Draft, model-neutral experimental prompt templates
scripts/    Offline dataset validation only
tests/      Standard-library validator tests
.github/    Research issue and pull-request templates
```

## Reproducibility approach

Before any model run, the study will freeze versioned prompts, dataset hashes, exact model identifiers, generation parameters, repeat counts, exclusion rules, and an analysis plan. Raw responses, annotations, and derived summaries will be linked by stable identifiers. The repository currently performs no API calls; the [API budget](docs/api-budget.md) is a planning document only. The evidence base and design implications are summarised in [related work](docs/related-work.md).

## Privacy and ethics position

The proposed phase uses synthetic reflections only and does not involve research participants. Real diary entries, personal data, and clinical or crisis scenarios are outside the present dataset. Any future human-participant study would be separate and would require consideration of the applicable King's College London ethics and data-governance processes before it began. No ethics approval is claimed here.

## Relationship to the private prototype

InnerMap is a privately developed reflection prototype that informed the general research context. Its production application and source code are not included; this independent research repository is not a public edition of InnerMap.

## Current limitations

- The protocol and annotation rubric have not yet undergone formal methodological review.
- The full synthetic benchmark and paraphrase set have not been created.
- The primary model identifier, inference settings, and inferential tests are not yet frozen.
- No reliability estimates, model outputs, participant data, or study results are reported.
- Synthetic scenarios cannot fully represent the language or stakes of real personal reflection.

See [limitations](docs/limitations.md) for the planned validity analysis.

## Planned outputs

Subject to review, the project aims to produce a versioned synthetic benchmark, prompt-condition definitions, an annotated response corpus, reliability and robustness analyses, and a transparent report of both positive and null findings. These are planned outputs, not completed deliverables.

## Citation

Citation metadata is provided in [CITATION.cff](CITATION.cff). Until a versioned release exists, cite the repository URL and the commit or release identifier used. No DOI or publication is claimed.

## Author

**Shiwen Tian**<br>
Computer Science undergraduate, Department of Informatics, King's College London

- [GitHub profile](https://github.com/Taliwanmli)

The affiliation above identifies the author's course and department; it does not imply institutional sponsorship, supervision, approval, or endorsement.

## Licensing

Code is licensed under the [MIT License](LICENSE). Synthetic research materials and documentation may be reused with attribution. Private product code and proprietary materials are not licensed through this repository. No rights are claimed over third-party models, outputs, trademarks, or platform materials.

## Validation

Local checks use Python 3.11 or 3.12 and require no API credentials:

```bash
python3 scripts/validate_dataset.py data/synthetic-examples.sample.jsonl
python3 -m unittest discover -s tests -v
python3 -m json.tool schemas/reflection.schema.json >/dev/null
python3 -m json.tool schemas/evaluation.schema.json >/dev/null
python3 -c "import tomllib; tomllib.load(open('pyproject.toml', 'rb'))"
```

The GitHub Actions validation workflow runs the same checks on both supported Python versions and validates `CITATION.cff` with the pinned `cffconvert` dependency. These checks establish file syntax, schema flags, and validator behaviour only; they cannot establish methodological validity, fictionality, non-identifiability, semantic equivalence, or research quality. The workflow uses no secrets and makes no model or paid API call. No status badge is shown until a successful workflow run has been observed.

Contributions are welcome under the privacy and scope rules in [CONTRIBUTING.md](CONTRIBUTING.md).
