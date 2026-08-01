# Related work

**Status:** Focused background review for a proposed independent undergraduate research project. Sources were checked against publisher, proceedings, journal, or institutional pages. This page does not claim that the proposed study is novel, complete, registered, or peer reviewed.

## Prompt sensitivity

Meaning-preserving prompt changes can materially change measured model behaviour. Sclar et al. show sensitivity to prompt formatting and argue that evaluation should account for plausible prompt variants rather than relying on one arbitrary format. This supports freezing exact templates and hashes, holding the shared envelope constant across conditions, testing whether the manipulations are distinct, and treating prompt length and formatting as potential confounds rather than as neutral implementation details.

## Expressed uncertainty and calibration

Yona et al. distinguish a model's internal uncertainty from how decisively it expresses claims, including both insufficient and excessive hedging. Zhou et al. connect reluctance to express uncertainty with user reliance and show that simply asking for confidence does not guarantee calibrated communication. These findings motivate separate rubric dimensions for uncertainty calibration, directive intensity, and usefulness; they do not establish that the proposed prompt intervention will work in reflective text.

## Grounding and hallucination

Ji et al. survey hallucination across natural-language generation tasks and distinguish generated content that is unsupported by a source from content that conflicts with wider factual knowledge. The present study narrows that broad problem to traceability against one supplied synthetic reflection. It therefore scores unsupported interpretation and source grounding but does not claim to measure general factual accuracy or eliminate hallucination.

## Sycophancy and preference matching

Sharma et al. study sycophancy as responses that match a user's stated views even when those views are inaccurate. Reflective responses may face an adjacent risk: fluent agreement can reinforce an interpretation that the input does not support. This motivates claim-to-source tracing and overreach checks, while the synthetic and non-clinical design avoids treating the benchmark as a test of actual user belief change.

## Human overreliance

Buçinca et al. show that people can accept incorrect AI recommendations and that cognitive-forcing interventions can reduce overreliance, although user experience may worsen. Zhou et al. likewise find substantial reliance on model answers regardless of expressed certainty. The proposed study measures properties of model responses only; it does not measure reliance, trust, behaviour, or wellbeing. Practical-usefulness scoring is retained so that caution is not automatically treated as cost-free.

## Reflective and mental-health-adjacent AI

The World Health Organization's guidance for large multi-modal models in health emphasises governance, evidence, stakeholder involvement, and post-deployment oversight. Miner et al.'s study of smartphone conversational agents found inconsistent and incomplete responses to standardised health and crisis questions. These sources support a conservative boundary: the current benchmark is synthetic, non-clinical, and excludes crisis content, diagnosis, treatment, participants, therapeutic efficacy, and clinical claims. They are governance context, not evidence that the proposed reflective prompt conditions are safe or effective.

## Human evaluation and model judging

Zheng et al. document position, verbosity, self-enhancement, and reasoning limitations in LLM-as-a-judge evaluation, even while finding useful agreement in their specific benchmarks. The initial design therefore uses human annotation, records masking limitations, and treats any future model-based judge as supplementary rather than ground truth. A second human annotator is not assumed; without independent ratings the project will report only intra-rater checks, not inter-rater reliability.

## Reproducibility of hosted models

Chen et al. report substantial behavioural changes between dated versions of hosted models. Exact model identifiers, dates, prompt hashes, parameters, run manifests, and retained outputs are therefore necessary but cannot make a hosted service permanently reproducible. Stage A tests operational variability, and later reports must limit claims to the observed model version and collection period.

## Design implication

Together, this literature supports a small staged design rather than an immediate broad comparison. Stage A tests whether the proposed constructs, paraphrases, rubric, annotation workload, API budget, and dependence-aware statistics are workable. Stage B is conditional, and additional models remain exploratory unless a later frozen plan justifies a broader confirmatory design.

## Verified references

1. Melanie Sclar, Yejin Choi, Yulia Tsvetkov, and Alane Suhr. “Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design or: How I learned to start worrying about prompt formatting.” *International Conference on Learning Representations (ICLR)*, 2024. [Official proceedings](https://proceedings.iclr.cc/paper_files/paper/2024/hash/6c0e99d736da621403018ca7b32b1a4d-Abstract-Conference.html).
2. Gal Yona, Roee Aharoni, and Mor Geva. “Can Large Language Models Faithfully Express Their Intrinsic Uncertainty in Words?” *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing*, 2024, pp. 7752–7764. [ACL Anthology](https://aclanthology.org/2024.emnlp-main.443/). [DOI: 10.18653/v1/2024.emnlp-main.443](https://doi.org/10.18653/v1/2024.emnlp-main.443).
3. Kaitlyn Zhou, Jena D. Hwang, Xiang Ren, and Maarten Sap. “Relying on the Unreliable: The Impact of Language Models’ Reluctance to Express Uncertainty.” *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, 2024, pp. 3623–3643. [ACL Anthology](https://aclanthology.org/2024.acl-long.198/). [DOI: 10.18653/v1/2024.acl-long.198](https://doi.org/10.18653/v1/2024.acl-long.198).
4. Ziwei Ji, Nayeon Lee, Rita Frieske, Tiezheng Yu, Dan Su, Yan Xu, Etsuko Ishii, Yejin Bang, Andrea Madotto, and Pascale Fung. “Survey of Hallucination in Natural Language Generation.” *ACM Computing Surveys*, 55(12), Article 248, 2023, pp. 1–38. [DOI: 10.1145/3571730](https://doi.org/10.1145/3571730).
5. Mrinank Sharma, Meg Tong, Tomek Korbak, David Duvenaud, Amanda Askell, Sam Bowman, Esin Durmus, Zac Hatfield-Dodds, Scott Johnston, Shauna Kravec, Timothy Maxwell, Sam McCandlish, Kamal Ndousse, Oliver Rausch, Nicholas Schiefer, Da Yan, Miranda Zhang, and Ethan Perez. “Towards Understanding Sycophancy in Language Models.” *International Conference on Learning Representations (ICLR)*, 2024. [Official proceedings](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0105f7972202c1d4fb817da9f21a9663-Abstract-Conference.html).
6. Zana Buçinca, Maja Barbara Malaya, and Krzysztof Z. Gajos. “To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.” *Proceedings of the ACM on Human-Computer Interaction*, 5(CSCW1), Article 188, 2021, pp. 1–21. [DOI: 10.1145/3449287](https://doi.org/10.1145/3449287).
7. World Health Organization. *Ethics and governance of artificial intelligence for health: Guidance on large multi-modal models*. World Health Organization, 2024. ISBN 978-92-4-008475-9. [Official publication](https://www.who.int/publications/i/item/9789240084759).
8. Adam S. Miner, Arnold Milstein, Stephen Schueller, Roshini Hegde, Christina Mangurian, and Eleni Linos. “Smartphone-Based Conversational Agents and Responses to Questions About Mental Health, Interpersonal Violence, and Physical Health.” *JAMA Internal Medicine*, 176(5), 2016, pp. 619–625. [Official journal page](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2500043). [DOI: 10.1001/jamainternmed.2016.0400](https://doi.org/10.1001/jamainternmed.2016.0400).
9. Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric P. Xing, Hao Zhang, Joseph E. Gonzalez, and Ion Stoica. “Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.” *Advances in Neural Information Processing Systems 36, Datasets and Benchmarks Track*, 2023. [Official proceedings](https://proceedings.neurips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html).
10. Lingjiao Chen, Matei Zaharia, and James Zou. “How Is ChatGPT’s Behavior Changing Over Time?” *Harvard Data Science Review*, 6(2), 2024. [Journal article](https://hdsr.mitpress.mit.edu/pub/y95zitmz/release/2). [DOI: 10.1162/99608f92.5317da47](https://doi.org/10.1162/99608f92.5317da47).
