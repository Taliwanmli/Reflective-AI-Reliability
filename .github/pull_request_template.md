## Summary

Describe the research or tooling change and why it is needed.

## Scope

- Protocol or hypotheses:
- Data or schemas:
- Prompt conditions:
- Evaluation rubric or analysis:
- Offline tooling:

## Integrity and privacy checklist

- [ ] The study is described as proposed, planned, draft, or in development where applicable.
- [ ] No completed result, statistic, publication, approval, funding, supervision, or endorsement is fabricated or implied.
- [ ] All reflection examples are fictional, non-identifiable, non-clinical, and labelled synthetic.
- [ ] No real diary entry, participant data, personal identifier, or sensitive private path is included.
- [ ] No private product code, prompt, architecture, asset, configuration, credential, endpoint, or roadmap is included.
- [ ] No API call, model judging, or paid operation was added without separate review and an approved budget gate.

## Reproducibility impact

State whether this changes a schema, prompt version, dataset hash, rubric version, analysis unit, exclusion rule, or freeze point.

## Validation performed

```text
python3 scripts/validate_dataset.py data/synthetic-examples.sample.jsonl
python3 -m unittest discover -s tests -v
```

Add any other checks and their outcomes.

## Limitations and human review

List unresolved methodological questions, facts requiring confirmation, and any artefact that needs human provenance or safety review before merge.
