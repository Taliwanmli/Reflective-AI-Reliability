# Data governance and ethics

**Status:** Draft planning document. The current proposed phase uses synthetic materials only and has no research participants.

## Scope

This repository is designed for a controlled benchmark of language-model responses to fictional, non-identifiable, non-clinical reflections. Synthetic data reduces exposure of personal information but does not remove the need for careful provenance, access control, documentation, or institutional consideration.

## Data classes

| Class | Present now? | Release position |
| --- | --- | --- |
| Draft protocol and prompts | Yes | Public, versioned |
| Synthetic sample reflections | Yes | Public after validation |
| Full synthetic benchmark | No; planned | Public after provenance and safety review |
| Model responses | No; planned | Release decision after content and licence review |
| Investigator annotations | No; planned | Release with pseudonymous annotator IDs where appropriate |
| Real reflections or participant data | No; prohibited in this phase | Not accepted |
| Clinical or crisis scenarios | No; prohibited in this phase | Not accepted |

## Synthetic-data requirements

Every reflection record must:

- be newly authored or have documented, reviewable synthetic provenance;
- be labelled `synthetic: true`;
- be labelled `contains_personal_data: false` and `clinical_content: false`;
- avoid names, contact details, precise locations, identifiers, and distinctive biographies;
- avoid self-harm, suicide, crisis, diagnosis, abuse, criminal conduct, and medical-treatment content;
- avoid high-stakes legal, medical, financial, or safety decisions; and
- contain no copied private diary, user-message, or product material.

The validator enforces required flags and basic structure. It cannot establish that prose is truly fictional or safe; human review remains required.

## Provenance

Each dataset release should include:

- authoring method and dates;
- whether any model assisted drafting or paraphrasing;
- model and prompt details for any such assistance;
- human review outcome and exclusion reason codes;
- schema version and file hash; and
- a statement that no real personal reflections were intentionally used.

Material with uncertain provenance will be excluded rather than assumed safe.

## Minimisation and separation

The benchmark should contain only the text and metadata needed for the research questions. Synthetic source data, generated model responses, annotation records, and analysis outputs will use separate files linked by non-personal identifiers. Prompts and logs must not contain private product context or production credentials.

## Model-provider transmission

No API request is implemented now. Before a future run, the investigator will document what text and metadata would leave the local environment, the provider terms and retention controls applicable at that time, permitted logging, access roles, deletion procedures, and whether the planned use is consistent with applicable institutional requirements. Secrets must be supplied outside version control and never written to run artefacts.

## Access and retention

Public draft materials remain in Git history. Pre-release run artefacts should use least-privilege access and a written retention rule. Failed requests, excluded items, and annotation changes should be retained in a non-sensitive audit manifest when methodologically relevant, rather than silently erased. Any file containing accidental personal data must be quarantined and handled as an incident, not normal research data.

## Ethical boundaries

The benchmark does not test therapy, diagnosis, crisis response, clinical safety, or treatment. It does not establish that an AI response is appropriate for an individual. Synthetic examples should not be described as participant testimony or user evidence.

The current phase has no recruitment, consent process, or interaction with participants. The repository does not claim that ethics approval has been obtained, that review is unnecessary, or that King's College London endorses the project.

Any future human-participant study would be separate. Before it began, the investigator would need to consider the applicable King's College London ethics and data-governance processes, define recruitment and consent, establish lawful and secure handling, assess withdrawal and deletion, and obtain any approvals required for that design.

## Release review

Before publishing a dataset or response corpus, a human reviewer should confirm:

1. provenance is complete;
2. prohibited topics and personal data are absent;
3. licence and provider-output reuse terms have been checked for the intended release;
4. no private prompts, source code, configuration, or product assets are present;
5. hashes and schema versions match the release manifest; and
6. limitations are published beside the artefacts.

## Incident handling

Potential personal-data or private-source exposure must be reported through the private process in `SECURITY.md`. A later deletion commit does not remove the material from earlier history; remediation may require history rewriting, cache review, and replacement of any exposed credential.
