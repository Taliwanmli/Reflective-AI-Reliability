# Evidence-Grounded and Uncertainty-Calibrated AI for Personal Reflection

A protocol-first research scaffold for studying the reliability of language-model responses to synthetic, non-clinical personal reflections.

> **Status: Protocol development**<br>
> **No study results are reported yet.** The design, materials, and analysis plan remain subject to review and revision.

## Motivation

Personal reflections are a sensitive setting for language models: a short first-person account can support several plausible readings, while an overconfident response can turn a possibility into an apparent fact. This proposed undergraduate project examines whether explicit evidence-grounding and uncertainty-calibration instructions make responses more reliable, and whether any gains persist when the same reflection is phrased differently.

## Research questions

1. How do evidence-grounding instructions affect source grounding, unsupported inference, and emotional or psychological overreach?
2. How do uncertainty-calibration cues affect confidence, directive intensity, and transparency about limitations?
3. Do the two interventions interact, and how robust are their effects across paraphrases and repeated generations?

The full questions and draft hypotheses are in [research questions and hypotheses](docs/research-questions-and-hypotheses.md).

## Proposed design

The benchmark is planned around approximately 120 fictional, non-identifiable, non-clinical base reflections. Each semantic scenario will eventually include meaning-preserving paraphrases and will be evaluated under four conditions:

| Condition | Planned manipulation |
| --- | --- |
| Neutral baseline | Shared task and safety envelope only |
| Evidence-grounded | Explicitly separates supported observations from interpretations |
| Uncertainty-calibrated | Explicitly calibrates confidence and acknowledges ambiguity |
| Combined | Applies both interventions |

Planned evaluation dimensions are source grounding, unsupported inference, uncertainty calibration, directive intensity, emotional or psychological overreach, consistency, robustness to paraphrasing, practical usefulness, and transparency about limitations. The operational definitions are in the [evaluation rubric](docs/evaluation-rubric.md).

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

Before any model run, the study will freeze versioned prompts, dataset hashes, exact model identifiers, generation parameters, repeat counts, exclusion rules, and an analysis plan. Raw responses, annotations, and derived summaries will be linked by stable identifiers. The repository currently performs no API calls; the [API budget](docs/api-budget.md) is a planning document only.

## Privacy and ethics position

The proposed phase uses synthetic reflections only and does not involve research participants. Real diary entries, personal data, and clinical or crisis scenarios are outside the present dataset. Any future human-participant study would be separate and would require consideration of the applicable King's College London ethics and data-governance processes before it began. No ethics approval is claimed here.

## Relationship to InnerMap

This research is informed by InnerMap, a privately developed reflection prototype. The production application and its source code are not included in this repository. The repository is an independent research scaffold, not a public edition of InnerMap and not a medical or therapeutic product.

## Current limitations

- The protocol and annotation rubric have not yet undergone formal methodological review.
- The full synthetic benchmark and paraphrase set have not been created.
- Models, repeat counts, inference settings, and inferential tests are not yet frozen.
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
- LinkedIn profile: URL to be confirmed before publication

The affiliation above identifies the author's course and department; it does not imply institutional sponsorship or endorsement.

## Licensing

Code is licensed under the [MIT License](LICENSE). Synthetic research materials and documentation may be reused with attribution. InnerMap's private code, brand assets, prompts, and proprietary materials are not licensed through this repository. No rights are claimed over OpenAI models, outputs, trademarks, or platform materials.

Contributions are welcome under the privacy and scope rules in [CONTRIBUTING.md](CONTRIBUTING.md).
