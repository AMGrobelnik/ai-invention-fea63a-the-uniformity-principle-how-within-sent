# gen_paper_text — test_idea

> Phase: `invention_loop` · round 2 · `gen_paper_text`
> Run: `run_nOuUUSNqdMp4` — The Uniformity Principle: How Within-Sentence Consistency Predicts Readability
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_paper_text` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-21 17:23:31 UTC

````
<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for related-work positioning and how this field frames a genuinely novel contribution.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>
<previous_paper>
STARTING POINT: This is your paper draft from the previous iteration.

# The Uniformity Principle: How Within-Sentence Consistency Predicts Readability

## Abstract

Classic readability formulas (e.g., Flesch-Kincaid) rely exclusively on average values of surface linguistic features. This paper introduces the Uniformity Principle: readability is predicted not only by these averages but also by the uniformity (consistent difficulty) of word-level features within a sentence. We evaluate this hypothesis on 13,129 sentences from two public benchmarks (WeeBIT and CEFR-SP). Using Ridge regression with 5-fold cross-validation, we find that uniformity features (coefficient of variation of word length, syllable count, and word frequency) are statistically significant predictors of readability scores (p < 0.001), yielding R-squared improvements of +0.138 and +0.042 beyond traditional average features. The coefficient of variation of syllable counts is the most predictive uniformity feature (coefficient +0.150 on WeeBIT). These findings suggest that the Uniformity Principle captures a previously unrecognized aspect of readability, providing a lightweight and interpretable enhancement to traditional readability assessment.

---

# 1 Introduction

Readability assessment—the task of predicting how difficult a text is to read—has practical applications in education, content creation, and accessibility. Classic readability formulas such as Flesch Reading Ease and Flesch-Kincaid Grade Level operate by computing averages of surface linguistic features: average word length in characters, average sentence length in words, and average syllables per word. These formulas assume that a sentence's difficulty can be reduced to its mean properties.

However, reading is a sequential information processing task. Cognitive load theory suggests that the human brain processes information more efficiently when the rate of information delivery is consistent. In streaming systems, uniform bit rate is easier to decode than variable bit rate. Similarly, in economics, inequality measures like the Gini coefficient predict system efficiency. We hypothesize that a similar principle applies to reading: sentences with uniform word-level difficulty allow readers to establish a consistent processing rhythm, reducing peak cognitive load compared to sentences with bursty difficulty patterns.

We call this the **Uniformity Principle**: the readability of a sentence is predicted not only by average linguistic complexity but also by the uniformity (consistency) of linguistic features within the sentence. Specifically, we propose that sentences with lower coefficient of variation (CV = standard deviation / mean) of word-level features are easier to read than sentences with the same average values but higher CV.

[FIGURE:fig1]

This paper makes the following contributions:

1. **Theoretical contribution**: We formulate the Uniformity Principle as a novel predictor of sentence-level readability, grounded in cognitive load theory and information theory.
2. **Empirical evaluation**: We conduct a systematic evaluation on 13,129 sentences from two established benchmarks (WeeBIT and CEFR-SP).
3. **Significant findings**: We show that uniformity features provide statistically significant predictive power beyond traditional features (p < 0.001), with R-squared improvements of +0.138 and +0.042.
4. **Practical impact**: The Uniformity Principle enables lightweight, interpretable readability formulas that outperform classic methods.

---

# 2 Related Work

## 2.1 Readability Assessment

Readability assessment has a long history in natural language processing. Classic formulas rely on shallow surface features. Feng et al. conducted a comprehensive comparison of features for automatic readability assessment, evaluating discourse, language modeling, syntactic, part-of-speech, and shallow features. Their Table 5 lists 8 shallow features, all of which are means or averages. To our knowledge, no prior work has investigated the variance or coefficient of variation of these features within sentences as a predictor of readability.

## 2.2 Variance and Uniformity in Text

Courtis used the coefficient of variation to measure readability variability across sentences in corporate reports. However, this work operates at the document level. Our hypothesis is fundamentally different: we claim that within-sentence uniformity of word properties improves readability.

## 2.3 Cognitive Load Theory

Cognitive load theory posits that working memory has limited capacity. In reading, cognitive load accumulates locally based on word-level difficulty. We hypothesize that uniform information density reduces peak cognitive load.

---

# 3 The Uniformity Principle

## 3.1 Hypothesis

The Uniformity Principle states that sentence readability depends not only on average linguistic complexity but also on the uniformity of word-level features within the sentence.

Formally, for a word-level feature f, we define: (1) Average: μf = (1/n) Σ fi, (2) Uniformity (CV): CVf = σf / μf.

The Uniformity Principle predicts that readability score R is a function of both μf and CVf.

## 3.2 Cognitive Motivation

The hypothesis is motivated by: (1) Cognitive Load Theory—consistent processing reduces peak load, (2) Information Theory—uniform bit rate is easier to decode, (3) Gini Coefficient—inequality reduces efficiency.

## 3.3 Feature Definitions

We compute three classes of word-level features: (1) Word length in characters, (2) Syllable count (using CMU Pronouncing Dictionary), (3) Word frequency (log-transformed, from NLTK Gutenberg corpus). For each feature, we compute: Average (traditional) and Coefficient of variation (uniformity).

---

# 4 Experiments

## 4.1 Datasets

We evaluate on two public sentence-level readability datasets.

**WeeBIT**: 3,125 sentences annotated with 5 age intervals. Scores normalized to [0, 1].

**CEFR-SP**: 10,004 sentences annotated with CEFR levels (A1-C2). Levels mapped to 0.0-1.0.

[FIGURE:fig2]

## 4.2 Experimental Setup

Feature computation: Syllable counting uses CMU Pronouncing Dictionary (123,455 words). Word frequency uses NLTK Gutenberg corpus (42,339 words). Models: Ridge regression (alpha=1.0) with 5-fold cross-validation. Three feature sets: (1) Average only, (2) Uniformity only, (3) Combined.

## 4.3 Results

[FIGURE:fig3]

Key findings: (1) Uniformity features are predictive (R² > 0.22 on WeeBIT, > 0.40 on CEFR-SP), (2) Adding uniformity features yields significant improvements (p < 0.001), (3) MSE reduction of 17.8% (WeeBIT) and 8.9% (CEFR-SP).

## 4.4 Feature Importance

[FIGURE:fig4]

All three uniformity features have positive coefficients, indicating that higher within-sentence variance is associated with higher reading difficulty. On WeeBIT, top features: cv_syllables (+0.150), avg_word_len (-0.117), num_words (+0.108), cv_freq (+0.103).

---

# 5 Discussion

## 5.1 Interpretation of Results

The results confirm the Uniformity Principle hypothesis. The effect is particularly strong for cv_syllables (+0.150 on WeeBIT), suggesting sentences with varying syllable counts are more difficult.

## 5.2 Comparison to Classic Formulas

Classic readability formulas can be viewed as linear combinations of average features. Our results suggest these formulas are incomplete—they miss the uniformity signal that explains an additional 1.8-13.8% of variance.

## 5.3 Limitations

Word frequency uses Gutenberg corpus (not SUBTLEX-US). WeeBIT has only 5 readability levels. No direct cognitive validation (eye-tracking data).



[FIGURE:fig5]

## 5.4 Practical Applications

The Uniformity Principle enables: (1) Lightweight readability scoring, (2) Text simplification guidance, (3) Curriculum design.

---

# 6 Conclusion

This paper introduced the Uniformity Principle: the hypothesis that within-sentence uniformity of word-level linguistic features predicts readability independently of traditional average features. Through systematic evaluation on 13,129 sentences from two public benchmarks, we demonstrated that uniformity features are statistically significant predictors (p < 0.001), adding uniformity features yields R² improvements of +0.138 and +0.042, and the coefficient of variation of syllable counts is the most predictive uniformity feature.

These findings suggest that the Uniformity Principle captures a previously unrecognized aspect of readability. We hope this work inspires further research into uniformity-based features for readability assessment.

---

# References

[12] Feng, L., Jansche, M., Huenerfauth, M. (2010). A Comparison of Features for Automatic Readability Assessment. COLING 2010.

[13] Courtis, J. K. (2004). Corporate report obfuscation: artefact or phenomenon? Journal of Business Communication.

[19] Vajjala, S., Meurers, D. (2012). WeeBIT: A Corpus of Alphabetical Texts for Readability Research. LREC 2012.

[20] Xia, M. et al. (2023). CEFR-SP: A Sentence-Level Corpus for CEFR Level Prediction. EMNLP 2023.

</previous_paper>

<reviewer_feedback>
STEP 1 — REVIEW: A reviewer evaluated the previous paper draft above and produced this feedback.

- [MAJOR] (methodology) The paper uses NLTK Gutenberg corpus for word frequency computation, which the authors' own research artifact (art_zKX1_wXmedjn) identifies as suboptimal. The artifact states: 'SUBTLEX-US norms (based on 51M subtitle words) significantly outperform older norms (Kucera & Francis, Celex) in predicting word processing times.' Using Gutenberg corpus (42,339 words from books) instead of SUBTLEX-US likely reduces the quality of the frequency-based uniformity features.
  Action: Replace NLTK Gutenberg corpus with SUBTLEX-US word frequency norms. The SUBTLEX-US data is freely available from Ghent University. Use the Zipf scale values or SUBTL WF (word frequency per million) for computing word frequency uniformity. This change is straightforward and will improve the quality of the frequency features.
- [MAJOR] (methodology) The paper only uses Ridge regression as the evaluation model. This is a weak baseline that does not represent the current state of readability assessment. Recent work (Deutsch et al. 2020, Liu & Lee 2023) has shown that neural models and comprehensive feature sets (e.g., LingFeat with 255 features) achieve much higher performance. Without comparing to these stronger baselines, it's unclear whether uniformity features provide value beyond what's already captured by modern methods.
  Action: Add experiments with at least one modern neural baseline (e.g., BERT-based readability assessment) and one comprehensive feature-based baseline (e.g., LingFeat or the feature set from Deutsch et al. 2020). Show whether adding uniformity features to these stronger baselines still yields improvements. If the improvement disappears with stronger baselines, the contribution is much weaker than claimed.
- [MAJOR] (evidence) The paper reports R² improvements of +0.138 and +0.042 but does not provide effect sizes, confidence intervals, or detailed breakdown of these improvements. The p-values (< 0.001) are reported but p-values alone are insufficient for evaluating practical significance. Additionally, the paper claims 'MSE reduction of 17.8% (WeeBIT) and 8.9% (CEFR-SP)' but it's unclear whether this is on training or test set, and whether the reduction is statistically significant.
  Action: Report cross-validated R² differences with bootstrap confidence intervals (as recommended in the research artifact). Provide a table with mean, standard deviation, and confidence intervals for R² on test sets for all three feature sets (average only, uniformity only, combined). Also report whether the MSE reduction is statistically significant using a paired bootstrap test.
- [MINOR] (novelty) The paper states 'To our knowledge, no prior work has investigated the variance or coefficient of variation of these features within sentences as a predictor of readability.' While this appears true for word-level features, the paper should acknowledge that Courtis (1998) investigated readability VARIABILITY at the document level (using coefficient of variation across sentences in corporate reports). The paper correctly distinguishes this but could be more explicit about the relationship to this prior work.
  Action: In Section 2.2, add a more detailed discussion of Courtis (1998) and explicitly state that while Courtis operated at the document level (variance across sentences), this paper is the first to investigate within-sentence variance of word-level features. This strengthens rather than weakens the paper's novelty claim.
- [MAJOR] (scope) The evaluation is limited to only 2 sentence-level datasets (WeeBIT and CEFR-SP). Both datasets have limitations: WeeBIT has only 5 readability levels and was originally designed for document-level assessment; CEFR-SP sentences are annotated based on document-level CEFR ratings, not direct sentence-level annotation. The generalizability of the results to other datasets, to document-level readability, and to languages other than English is not established.
  Action: Add evaluation on at least one more dataset, preferably at the document level (e.g., CLEAR corpus or Newsela). If document-level evaluation is not possible, at least add evaluation on a third sentence-level dataset (e.g., WSJ dataset from Liu & Lee 2023). Also discuss the limitations of the current evaluation more explicitly in Section 5.3.
- [MINOR] (rigor) The paper does not report out-of-vocabulary (OOV) rates for the CMU Pronouncing Dictionary. The research artifact mentions that CMUdict has 123,455 words, but typical readability assessment texts may contain words not in this dictionary (e.g., domain-specific terms, named entities, rare words). The handling of OOV words for syllable counting and the OOV rate should be reported.
  Action: Report the OOV rate for CMUdict on both datasets. Implement and document a fallback strategy for OOV words (e.g., using the 'syllables' package heuristic or a simple rule like counting vowel groups). Sensitivity analysis showing the impact of OOV handling on results would further strengthen the paper.
- [MINOR] (clarity) Figure references (FIGURE:fig1 through FIGURE:fig5) are placeholders without actual figures or detailed captions. While the instructions state that figures should be assumed to show exactly what the caption describes, having no figures or detailed captions makes it difficult to evaluate whether the results are presented clearly and whether the figures effectively communicate the findings.
  Action: Generate actual figures or provide detailed figure captions specifying what each figure shows, what the axes are, what the error bars represent, etc. At minimum, provide mock-ups or detailed descriptions of what each figure should contain so that reviewers can evaluate whether the visualization effectively communicates the results.
- [MINOR] (methodology) Section 4.2 states that syllable counting uses CMU Pronouncing Dictionary (123,455 words) and word frequency uses NLTK Gutenberg corpus (42,339 words), but it's unclear how word frequency is computed for out-of-vocabulary words (words not in Gutenberg). Are they assigned a default frequency? Removed? This should be documented.
  Action: Document the handling of OOV words for word frequency computation. If using a default frequency for OOV words, justify the choice (e.g., assigning frequency = 0 or 1 for unseen words). If removing OOV words, report the percentage of words removed and show that results are robust to this choice.
- [MINOR] (evidence) The paper reports positive coefficients for all three uniformity features, indicating that higher within-sentence variance is associated with higher reading difficulty. This is plausible but the paper does not provide error bars or significance tests for individual feature coefficients. It's possible that some uniformity features are not significant predictors when controlling for others.
  Action: Add a table or discussion of the statistical significance of individual feature coefficients. Report standard errors or confidence intervals for the Ridge regression coefficients. This will help readers understand which uniformity features are most robust and whether all three contribute uniquely to predictability.
- [MINOR] (scope) The paper claims practical applications in 'Lightweight readability scoring, Text simplification guidance, Curriculum design' (Section 5.4) but does not demonstrate or evaluate any of these applications. The paper is purely an empirical evaluation of whether uniformity features predict readability, without demonstrating end-to-end utility.
  Action: Either add a demonstration of one practical application (e.g., show how uniformity features can guide text simplification by identifying sentences with high CV that should be simplified) or tone down the claims about practical applications in Section 5.4. A short demonstration or case study would substantially strengthen the paper.
</reviewer_feedback>

<pipeline_steps>
STEP 2 — STRATEGY: The pipeline's strategy generator (gen_strat) read the reviewer feedback
and designed a new research strategy to address the critiques.

STEP 3 — PLANNING: The planner (gen_plan) turned the strategy into concrete artifact plans —
specific experiments, datasets, or research tasks to execute.

STEP 4 — EXECUTION: The executor (gen_art) ran those plans and produced the new artifacts
shown in <new_artifacts_this_iteration> below.
</pipeline_steps>

<hypothesis>
STEP 5 — HYPOTHESIS UPDATE: The hypothesis was revised based on evidence from previous iterations.

kind: hypothesis
title: Uniformity Improves Sentence Readability
hypothesis: >-
  The readability of a sentence is predicted not only by average linguistic complexity (e.g., mean word length, mean sentence
  length) but also by the uniformity of linguistic features within the sentence. Specifically, sentences with lower coefficient
  of variation (CV) of word-level features—such as word length in characters, syllable count, and word frequency—are easier
  to read than sentences with the same average values but higher CV. Initial experiments on 13,129 sentences from WeeBIT and
  CEFR-SP datasets show that adding uniformity features (CV of word length, syllables, frequency) to traditional average features
  yields statistically significant R² improvements of +0.138 (WeeBIT) and +0.042 (CEFR-SP), both p < 0.0001. However, uniformity
  features alone perform similarly to average features alone on WeeBIT (R² = 0.226 vs 0.226), suggesting they provide complementary
  rather than standalone predictive power. The 'Uniformity Principle' operates because uniform information density allows
  readers to establish a consistent processing rhythm, reducing peak cognitive load. To fully confirm this hypothesis, subsequent
  experiments must: (1) use high-quality word frequency norms (SUBTLEX-US rather than NLTK Gutenberg), (2) compare against
  modern baselines (BERT-based models, LingFeat), (3) provide bootstrap confidence intervals for R² improvements, and (4)
  evaluate on additional datasets.
motivation: >-
  Classic readability formulas (Flesch-Kincaid, etc.) rely exclusively on average values of surface features. However, cognitive
  load theory suggests that the brain processes information more efficiently when the rate of information delivery is consistent.
  If confirmed, this hypothesis would provide a new theoretical foundation for readability assessment and enable the development
  of lightweight, interpretable readability formulas that outperform classic methods by incorporating uniformity measures.
  This is particularly valuable for applications requiring fast, explainable readability scoring without large language models.
assumptions:
- >-
  Human readers process sentences as sequential information streams where cognitive load accumulates locally based on word-level
  difficulty.
- >-
  Uniform information density (low variance in word-level features) reduces the peak cognitive load compared to fluctuating
  density, even when averages are identical.
- >-
  Surface linguistic features (word length, syllable count, word frequency) serve as valid proxies for word-level processing
  difficulty.
- >-
  The coefficient of variation (standard deviation divided by mean) is an appropriate measure of uniformity that generalizes
  across sentences of different lengths and difficulty levels.
investigation_approach: >-
  1. Extract classic surface features from sentences in a public readability dataset (e.g., CommonLit CLEAR corpus or WSJ
  dataset): word length in characters, syllable count, and word frequency for each word. 2. Compute sentence-level uniformity
  metrics: coefficient of variation (CV) of word lengths, CV of syllable counts, and CV of word frequencies within each sentence.
  3. Train lightweight regression models to predict readability scores using: (a) only traditional average features, (b) only
  uniformity features, and (c) combined features. 4. Evaluate whether uniformity features provide significant additional predictive
  power beyond averages using cross-validation. 5. Analyze feature importance and ablation studies to quantify the independent
  contribution of uniformity.
success_criteria: >-
  The hypothesis is confirmed if: (1) Uniformity features (CV of word-level features) are statistically significant predictors
  of readability scores (p < 0.05) in regression models; (2) Adding uniformity features to traditional average features yields
  a statistically significant improvement in predictive performance (e.g., R² increase > 0.02 or MAE decrease > 5%); (3) The
  improvement holds across multiple public datasets and readability scoring systems. The hypothesis is disconfirmed if uniformity
  features provide no significant predictive power beyond traditional features, or if the coefficient of variation shows near-zero
  correlation with readability scores.
related_works:
- >-
  Feng et al. (2010) 'A Comparison of Features for Automatic Readability Assessment' - This paper evaluates various features
  for readability assessment including shallow features like average word length and sentence length. However, it does not
  investigate the variance or coefficient of variation of these features within sentences as a predictor. Our hypothesis differs
  by claiming that uniformity (low CV) within a sentence is a separate, independent predictor from averages.
- >-
  Courtis (2004) 'Corporate report obfuscation: artefact or phenomenon?' - This paper uses coefficient of variation to measure
  readability variability ACROSS sentences in corporate reports, finding that high variability indicates obfuscation. Our
  hypothesis differs by applying the uniformity principle WITHIN individual sentences, claiming that low within-sentence variance
  of word properties improves readability.
- >-
  Eltanbouly et al. (2025) 'Trait-Specific Rubric-Assisted Cross-Prompt Essay Scoring' - This paper uses 'word_var: Variance
  of word length' as one of many features in a machine learning model. However, it does not test the specific theoretical
  claim that uniformity is an independent predictor, nor does it use the coefficient of variation (normalized measure) or
  test across multiple word-level features (syllables, frequency). Our hypothesis provides a theoretical framework and systematic
  evaluation.
- >-
  Genzel & Charniak (2002) 'Entropy Rate Constancy in Text' - This paper proposes that speakers maintain a constant entropy
  rate across sentences. While related to information uniformity, it operates at the sentence-level entropy rate rather than
  within-sentence uniformity of surface features. Our hypothesis focuses on within-sentence uniformity of surface linguistic
  features as a cognitive processing principle.
inspiration: >-
  The hypothesis is inspired by three cross-domain insights: (1) From COGNITIVE SCIENCE and Cognitive Load Theory: consistent
  information processing rates reduce peak working memory load compared to fluctuating rates. (2) From INFORMATION THEORY:
  uniform information density (constant bit rate) is easier to process than variable bit rate in streaming systems. (3) From
  ECONOMICS: the Gini coefficient and coefficient of variation measure inequality/non-uniformity, which in other domains predicts
  system efficiency. The core insight is that reading is a sequential processing task where uniformity of difficulty within
  a sentence allows the reader to establish a consistent 'processing rhythm', reducing cognitive effort compared to sentences
  with 'bursty' difficulty patterns.
terms:
- term: Coefficient of Variation (CV)
  definition: >-
    A normalized measure of dispersion calculated as the ratio of the standard deviation to the mean (CV = σ/μ). It measures
    the relative variability of a feature independent of its absolute scale, allowing comparison across sentences of different
    lengths and difficulty levels.
- term: Surface Linguistic Features
  definition: >-
    Readily observable textual properties that do not require deep linguistic analysis, such as word length in characters,
    number of syllables per word, sentence length in words, and word frequency counts.
- term: Within-Sentence Uniformity
  definition: >-
    The degree to which word-level properties (length, syllables, frequency) are consistent throughout a sentence, measured
    by the coefficient of variation of these properties across all words in the sentence.
- term: Cognitive Rhythm
  definition: >-
    A hypothesized cognitive processing state where the reader establishes a consistent pace of processing when encountering
    uniformly difficult text, leading to reduced peak cognitive load compared to processing text with fluctuating difficulty.
- term: Sentence-Level Readability
  definition: >-
    The assessment of reading difficulty for individual sentences independently, as opposed to document-level readability
    which averages across multiple sentences.
summary: >-
  This hypothesis proposes that sentence readability depends not only on average linguistic complexity but also on the uniformity
  of word-level features within the sentence. Sentences with consistent word lengths, syllable counts, and word frequencies
  (low coefficient of variation) are predicted to be easier to read because they allow readers to maintain a steady cognitive
  processing rhythm, reducing peak cognitive load.
_relation_rationale: >-
  Added initial experimental results; specified methodological requirements for full confirmation
_confidence_delta: increased
_key_changes:
- >-
  Added specific experimental results: R² improvements of +0.138 and +0.042, both p < 0.0001
- >-
  Noted that uniformity-only features perform similarly to average-only on WeeBIT, suggesting complementary rather than standalone
  value
- >-
  Added requirement for high-quality word frequency norms (SUBTLEX-US) based on reviewer feedback
- >-
  Added requirement to compare against modern baselines (BERT-based, LingFeat) to establish contribution beyond current methods
- >-
  Added requirement for bootstrap confidence intervals for R² improvements (currently only p-values reported)
- >-
  Added requirement for evaluation on additional datasets beyond WeeBIT and CEFR-SP
- >-
  Specified that cv_syllables was the most predictive uniformity feature (coefficient +0.150 on WeeBIT)
relation_type: evolution
</hypothesis>

<all_artifacts>
FULL EVIDENCE BASE: All 5 research artifacts across all iterations.

--- Item 1 ---
id: art_nzHCg3npeffO
type: dataset
title: Sentence-Level Readability Datasets
summary: >-
  Successfully collected and standardized 2 sentence-level readability datasets for the artifact objective of computing uniformity
  features (CV of word length, syllables, word frequency). Dataset 1: WeeBIT (3,125 sentences) - established benchmark with
  5 age intervals from Vajjala & Meurers (2012). Dataset 2: CEFR-SP (10,004 sentences) - sentences annotated with CEFR levels
  (A1-C2) by English education professionals, published at EMNLP 2022. Both datasets were loaded from HuggingFace Hub, standardized
  to exp_sel_data_out.json schema with input (sentence text) and output (readability score as string) fields, and validated
  against the schema. The readability scores were normalized to 0-1 scale (0=easy, 1=hard). Output files include full_data_out.json
  (13,129 examples total), mini_data_out.json (3 examples for development), and preview_data_out.json (3 examples for inspection).
  Additional files: data_out_1.json and data_out_2.json for individual datasets, temp/datasets/ with full/mini/preview versions,
  and README.md with documentation.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 2 ---
id: art_zKX1_wXmedjn
type: research
title: Word features and readability methods research
summary: |-
  This research artifact provides a comprehensive methodological guide for computing word-level linguistic features (syllable count, word frequency) and understanding the sentence-level readability assessment landscape. The research was conducted to inform experimental design for testing the 'Uniformity Principle' hypothesis, which posits that variance/uniformity measures of linguistic properties within sentences may improve readability prediction beyond traditional average-based features.

  Key findings across 5 research phases:

  1. SYLLABLE COUNTING: Three main approaches exist - (a) CMU Pronouncing Dictionary via 'pronouncing' library (high accuracy, research-grade), (b) 'syllables' package (fast heuristic, lower accuracy), (c) textstat library (uses Pyphen, only 54% accurate per GitHub issues). Recommendation: Use CMUdict as primary with heuristic fallback.

  2. WORD FREQUENCY: SUBTLEX-US norms (based on 51M subtitle words) significantly outperform older norms (Kucera & Francis, Celex) in predicting word processing times. Available as free download from Ghent University. Google Books Ngrams is secondary option.

  3. SENTENCE-LEVEL DATASETS: (a) CLEAR corpus (~5,000 excerpts, grades 3-12, multiple readability metrics + teacher ratings, MIT license), (b) WSJ dataset (1,200 sentences, 20 annotators, grades 1-7), (c) OneStopEnglish (189 texts × 3 levels). CLEAR recommended as primary for hypothesis testing.

  4. FEATURE LANDSCAPE: Feng et al. (2010) evaluated 5 categories - discourse, language modeling, syntactic, POS, and shallow features. Their Table 5 lists 8 shallow features. Critical finding: ALL existing features are means/averages (e.g., 'average syllables per word'). NO variance/uniformity measures were found, suggesting the 'Uniformity Principle' hypothesis has novelty.

  5. STATISTICAL METHODS: For testing incremental predictive power - (a) Cross-validated R² difference with bootstrap CI (most robust), (b) AIC/BIC comparison (model selection), (c) Nested F-test (linear models). Recommendations provided with Python implementation examples.

  The artifact includes: (1) Detailed methodology guide with installation commands and code snippets, (2) Dataset catalog with properties and access methods, (3) Feature catalog from Feng et al. (2010), (4) Statistical methodology guide, (5) Novelty assessment for uniformity features, (6) Experimental design recommendations.

  Sources: 14 references covering PyPI packages, academic papers (Feng et al. 2010, Liu & Lee 2023), dataset documentation (CLEAR, WSJ, OneStopEnglish), and statistical methods resources. All sources accessed and verified via web research tools.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 3 ---
id: art_JC59RgEIB4Y0
type: dataset
title: Readability datasets for sentence-level assessment
summary: >-
  Successfully acquired 3 readability datasets from HuggingFace, evaluated quality, and selected the best 2 datasets for the
  artifact. Primary acquisition: CLEAR corpus (3,543 excerpts from CommonLit with multiple readability metrics including Flesch-Kincaid
  Grade Level) and agentlans/readability (2,000 sampled paragraphs with continuous grade level scores from arxiv, tinystories,
  fineweb-edu, and wikipedia-en). Both datasets were standardized to exp_sel_data_out.json schema with input (text) and output
  (normalized 0-1 readability score) fields. Created full_data_out.json (5,543 examples), mini_data_out.json (6 examples for
  development), and preview_data_out.json (6 examples with truncated text). All files validated against schema. Documentation
  includes README.md with dataset descriptions, loading instructions, comparison table, and known limitations. WSJ dataset
  (Liu & Lee 2023) was not acquired due to form-based access requirements. OneStopEnglish corpus was acquired but not included
  in final selection due to longer texts and data leakage concerns.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 4 ---
id: art_oVX_8lj46IX7
type: experiment
title: Uniformity Principle Readability Experiment
summary: >-
  Implemented and executed experiment testing the Uniformity Principle for sentence-level readability prediction. Extracted
  linguistic features from 13,129 sentences (WeeBIT + CEFR-SP datasets): (1) average features (word length, syllables, frequency
  heuristic), (2) uniformity features (coefficient of variation within sentences). Compared three feature sets using 5-fold
  cross-validation with Ridge regression: average-only (R²=0.191), uniformity-only (R²=0.166), combined (R²=0.237). Bootstrap
  confidence intervals (2000 samples) confirmed combined significantly outperforms average-only (p<0.001, 95% CI [0.042, 0.053]).
  Output validates against exp_gen_sol_out schema. Key finding: uniformity features provide significant additional predictive
  power beyond average features.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 5 ---
id: art_rZy90MMefcYA
type: experiment
title: Statistical evaluation of uniformity features for readability
summary: >-
  Comprehensive statistical evaluation of the Uniformity Principle hypothesis for readability assessment. The experiment evaluated
  whether adding variance/uniformity measures of linguistic properties (coefficient of variation of word length, syllables,
  and word frequency) improves readability prediction beyond traditional average-based features. Using two datasets (WeeBIT:
  3,125 sentences, CEFR-SP: 10,004 sentences), five statistical tests were conducted: (1) Paired bootstrap MSE test showing
  12.44% MSE reduction for WeeBIT and 4.57% for CEFR-SP (p < 0.001), (2) Bootstrap 95% confidence intervals for Ridge regression
  coefficients showing cv_syllables and cv_frequency are significant predictors, (3) Proper 5-fold cross-validation with train/test
  separation showing R² improvement of 0.1275 (WeeBIT) and 0.0459 (CEFR-SP), (4) Effect size analysis revealing large effect
  sizes (Cohen's d = 1.55 and 2.40), and (5) Ablation study confirming all uniformity features contribute positively. The
  results strongly support the Uniformity Principle hypothesis, demonstrating that variance/uniformity measures provide significant
  incremental predictive power for readability assessment beyond traditional average-based features.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_experiment_2
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json
</all_artifacts>

<new_artifacts_this_iteration>
NEW THIS ITERATION: These 3 artifacts were created to address the reviewer
feedback. Their findings should be the primary basis for your revisions.

type: dataset
summary: >-
  Successfully acquired 3 readability datasets from HuggingFace, evaluated quality, and selected the best 2 datasets for the
  artifact. Primary acquisition: CLEAR corpus (3,543 excerpts from CommonLit with multiple readability metrics including Flesch-Kincaid
  Grade Level) and agentlans/readability (2,000 sampled paragraphs with continuous grade level scores from arxiv, tinystories,
  fineweb-edu, and wikipedia-en). Both datasets were standardized to exp_sel_data_out.json schema with input (text) and output
  (normalized 0-1 readability score) fields. Created full_data_out.json (5,543 examples), mini_data_out.json (6 examples for
  development), and preview_data_out.json (6 examples with truncated text). All files validated against schema. Documentation
  includes README.md with dataset descriptions, loading instructions, comparison table, and known limitations. WSJ dataset
  (Liu & Lee 2023) was not acquired due to form-based access requirements. OneStopEnglish corpus was acquired but not included
  in final selection due to longer texts and data leakage concerns.
id: art_JC59RgEIB4Y0
title: Readability datasets for sentence-level assessment

type: experiment
summary: >-
  Implemented and executed experiment testing the Uniformity Principle for sentence-level readability prediction. Extracted
  linguistic features from 13,129 sentences (WeeBIT + CEFR-SP datasets): (1) average features (word length, syllables, frequency
  heuristic), (2) uniformity features (coefficient of variation within sentences). Compared three feature sets using 5-fold
  cross-validation with Ridge regression: average-only (R²=0.191), uniformity-only (R²=0.166), combined (R²=0.237). Bootstrap
  confidence intervals (2000 samples) confirmed combined significantly outperforms average-only (p<0.001, 95% CI [0.042, 0.053]).
  Output validates against exp_gen_sol_out schema. Key finding: uniformity features provide significant additional predictive
  power beyond average features.
id: art_oVX_8lj46IX7
title: Uniformity Principle Readability Experiment

type: experiment
summary: >-
  Comprehensive statistical evaluation of the Uniformity Principle hypothesis for readability assessment. The experiment evaluated
  whether adding variance/uniformity measures of linguistic properties (coefficient of variation of word length, syllables,
  and word frequency) improves readability prediction beyond traditional average-based features. Using two datasets (WeeBIT:
  3,125 sentences, CEFR-SP: 10,004 sentences), five statistical tests were conducted: (1) Paired bootstrap MSE test showing
  12.44% MSE reduction for WeeBIT and 4.57% for CEFR-SP (p < 0.001), (2) Bootstrap 95% confidence intervals for Ridge regression
  coefficients showing cv_syllables and cv_frequency are significant predictors, (3) Proper 5-fold cross-validation with train/test
  separation showing R² improvement of 0.1275 (WeeBIT) and 0.0459 (CEFR-SP), (4) Effect size analysis revealing large effect
  sizes (Cohen's d = 1.55 and 2.40), and (5) Ablation study confirming all uniformity features contribute positively. The
  results strongly support the Uniformity Principle hypothesis, demonstrating that variance/uniformity measures provide significant
  incremental predictive power for readability assessment beyond traditional average-based features.
id: art_rZy90MMefcYA
title: Statistical evaluation of uniformity features for readability
</new_artifacts_this_iteration>

<data_files>
Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</data_files>

<task>
Write a research paper draft with LaTeX-ready text, BibTeX citations, and figure placeholders.

YOUR TURN (gen_paper_text): Revise the paper.

You are a researcher improving your paper after receiving a conference review.
Take the feedback seriously and make substantive changes, not cosmetic ones.

1. ADDRESS REVIEWER FEEDBACK: For each critique in <reviewer_feedback>, either fix the
   issue in the paper or argue convincingly why it doesn't apply. Major critiques MUST
   be resolved -- they would cause rejection if left unaddressed.
2. USE THE NEW EVIDENCE: The artifacts in <new_artifacts_this_iteration> were created
   specifically to address the reviewer's concerns. Reference their findings to
   strengthen the sections that were flagged as weak.
3. REWRITE, DON'T PATCH: Don't just append new paragraphs. Restructure and rewrite
   the sections the reviewer identified as problematic.
4. MAINTAIN CONSISTENCY: Ensure the paper aligns with the updated hypothesis.
</task>

<figure_instructions>
FIGURE FORMAT: Use [FIGURE:fig_id] markers in paper_text to indicate where each figure goes.
Then provide the full figure specs in the separate `figures` structured output array.
Each figure in the array must have an `id` matching a marker in the text. Set the `aspect_ratio`
field per figure: 21:9 for architecture / pipeline / flow-chart diagrams (the hero figure should
be one of these — place its marker near the END of the Introduction so it floats to the top of
page 2), 16:9 for comparisons / multi-panel results, 4:3 for dense charts, 1:1 for heatmaps /
confusion matrices / scatter plots.

Example in paper_text:
  "...our method achieves state-of-the-art results as shown below.\n\n[FIGURE:fig3]\n\nThe results demonstrate..."

Example in figures array (results comparison):
  {"id": "fig3", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: latency (seconds, 0-5). Values: PostgreSQL=4.6s (red), Bao=2.8s (blue), RLQOpt=2.0s (green). Error bars +/-0.3-0.8. Sans-serif font, white background.", "aspect_ratio": "16:9", "summary": "Compares latency across optimizers"}

Example in figures array (architecture diagram, hero):
  {"id": "fig1", "title": "System Architecture", "caption": "End-to-end pipeline: encoder feeds latents into the planner, which queries the value head before emitting actions.", "image_gen_detailed_description": "Horizontal flow diagram, left to right. Five labeled boxes: 'Input' (gray), 'Encoder' (blue), 'Latent (z, 256-dim)' (light blue, narrow), 'Planner' (green), 'Action Head' (orange). Arrows labeled with shapes. Value head as separate green box below 'Planner', bidirectional arrow. Sans-serif font, clean white background, no 3D.", "aspect_ratio": "21:9", "summary": "Hero architecture diagram"}

CRITICAL: Before writing figure specs, look through artifact workspace output files (*_out.json)
and code to find ALL the exact values. The figure generator cannot read files — every exact number
and value MUST be in the image_gen_detailed_description.
</figure_instructions>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-writing, aii-semscholar-bib.
TODO 2. LITERATURE REVIEW: Use web search tools to research the landscape — search key terms from
<hypothesis> and <all_artifacts>. Then use aii_semscholar_bib__fetch to batch-fetch real
BibTeX entries. Build a comprehensive Related Work section. Do NOT fabricate entries.
TODO 3. READ ARTIFACTS: Before writing each section, READ the relevant artifact source code, output
files, and data in the workspace. Extract concrete implementation details, technical innovations,
algorithmic specifics, and quantitative results. Do NOT write surface-level descriptions.

ARTIFACT REFERENCES: When you reference results, methodology, or findings from a specific artifact,
place an [ARTIFACT:artifact_id] marker inline. These become footnotes linking to the artifact's code
in the GitHub repository (first mention gets a footnote with URL, subsequent mentions are omitted).
Use the exact artifact ID from <all_artifacts>. Place the marker right after the claim it supports.
Example:
  "Our evaluation showed a 15% improvement over baselines [ARTIFACT:art_4f9d2c81ab37]." 
TODO 4. WRITE PAPER: Write the full paper text with [FIGURE:fig_id] markers per <figure_instructions>,
and provide the figure specs in the figures array. Cite with numeric references [1], [2], etc.
At the end of the paper text, include a full bibliography section. Do NOT compile LaTeX or generate
actual image/figure files. Your ONLY output is the structured JSON.
</todos><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FigureSpec": {
      "description": "Figure specification \u2014 structured output from paper writing agent.\n\nThe LLM fills these as a list in PaperText.figures.\nLater converted to Figure objects for viz gen.",
      "properties": {
        "id": {
          "description": "Figure ID matching the [FIGURE:id] marker in paper_text (e.g., 'fig1')",
          "title": "Id",
          "type": "string"
        },
        "title": {
          "description": "Figure title in plain, everyday language \u2014 short and jargon-free. Aim for about 4-8 words (~40 characters).",
          "title": "Title",
          "type": "string"
        },
        "caption": {
          "description": "LaTeX figure caption \u2014 appears below the figure in the paper. Should describe what the figure shows and highlight key takeaways.",
          "title": "Caption",
          "type": "string"
        },
        "image_gen_detailed_description": {
          "description": "Detailed image generation prompt \u2014 axes, labels, ALL numeric values, colors, aspect ratio, layout. The image generator cannot read files; this is its ONLY input.",
          "title": "Image Gen Detailed Description",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this figure communicates",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "id",
        "title",
        "caption",
        "image_gen_detailed_description",
        "summary"
      ],
      "title": "FigureSpec",
      "type": "object"
    }
  },
  "description": "Paper text \u2014 structured output from paper writing agent.\n\nStructured output fields (LLMPrompt + LLMStructOut):\n- title, abstract, paper_text, figures, summary\n\npaper_text contains [FIGURE:fig_id] markers for positioning.\nfigures contains the full specs as structured objects.\n\nMetadata fields (plain, set by pipeline code):\n- id",
  "properties": {
    "title": {
      "description": "Paper title \u2014 clear, plain-language, and short so a non-expert understands the main contribution at a glance. Aim for about 6-10 words; avoid jargon and acronyms.",
      "title": "Title",
      "type": "string"
    },
    "abstract": {
      "description": "Paper abstract",
      "title": "Abstract",
      "type": "string"
    },
    "paper_text": {
      "description": "Full paper body text with markdown section headers (# Introduction, # Methods, # Results, # Discussion, # Conclusion). Use [FIGURE:fig_id] markers (e.g. [FIGURE:fig1]) to indicate where each figure should appear.",
      "title": "Paper Text",
      "type": "string"
    },
    "figures": {
      "description": "List of figure specifications. Each must have an id matching a [FIGURE:id] marker in paper_text.",
      "items": {
        "$ref": "#/$defs/FigureSpec"
      },
      "title": "Figures",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the paper's main contribution and findings",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "abstract",
    "paper_text",
    "summary"
  ],
  "title": "PaperText",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-21 17:23:31 UTC

```
A lightweight sentence-level readability scoring model for English text using classic surface linguistic features, evaluated on a small public dataset.
```

### [3] SKILL-INPUT — aii-paper-writing · 2026-07-21 17:23:54 UTC

The agent loaded the **aii-paper-writing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-writing
description: Academic paper writing guidance for AI research. Covers paper structure, figure placeholders, bibliography building with Semantic Scholar, and citation rules. Does NOT cover LaTeX compilation or figure file generation — see aii-paper-to-latex for that.
---

## Technical Papers

Guidance for the standard "technical paper" format: propose a method/system/framework, evaluate it experimentally, report results. This is the main track at most CS venues (NeurIPS, ICML, ICLR, ACL, AAAI, etc.). Does NOT cover: pure theory/formal proofs, survey papers, position papers, or dataset/benchmark papers — those have different structures.

### Paper Structure

Target 6-8 pages. Use formal academic language, third person. Support claims with evidence from artifacts.

#### Rough Page Budget (8-page paper)

| Section | Pages | Notes |
|---|---|---|
| Abstract | 0.3 | Problem, approach, key result |
| Introduction | 1.0-1.5 | The most important section |
| Related Work | 0.5-1.0 | Beginning or end (see below) |
| Methods | 1.5-2.0 | Architecture fig on page 1 |
| Experiments | 1.5-2.0 | Setup + results + ablations |
| Discussion | 0.5-1.0 | Limitations go here |
| Conclusion | 0.3-0.5 | Do not repeat the abstract |
| References | 0.5-1.0 | Not counted in page limit |

**Critical rule**: A clear new technical contribution must be articulated by page 3 (quarter of the paper). If the reader doesn't know what you did by then, you've lost them.

#### Section Details

**Abstract** (150-250 words): State the problem, your approach, and the main results. Be factual and comprehensive. Do not repeat the abstract word-for-word later in the paper.

**Introduction** — Follow this 5-paragraph structure:

1. **What is the problem?** Define the task concretely.
2. **Why is it interesting and important?** Real-world impact, scale.
3. **Why is it hard?** Why do naive approaches fail?
4. **Why hasn't it been solved before?** What's wrong with prior solutions? How does yours differ?
5. **What are the key components of your approach and results?** Include specific limitations.

End with a "Summary of Contributions" subsection — bullet list of contributions with section references. This doubles as an outline, saving space.

**Related Work** — Placement decision:
- **Beginning** (Section 2): If it can be short yet detailed, or if you need a strong defensive stance against prior work early.
- **End** (before Conclusions): If comparisons require your technical content, or if it can be summarized briefly in the Introduction. Can be titled "Discussion and Related Work."

**Methods/Approach**: Every section tells a story — the story of the results, NOT the story of how you arrived at them. Use top-down description: readers should see where the material is going and be able to skip ahead. Move gory details to appendices.

**Experiments**: Setup (datasets, metrics, baselines) → main results → ablations → analysis. Every claim needs quantitative evidence.

**Discussion**: Interpret results, compare to prior work, state limitations honestly. Limitations should be specific and actionable, not vague disclaimers.

**Conclusion**: Short summarizing paragraph. Do NOT repeat material from the Abstract or Introduction. Make original claims more concrete (e.g., reference quantitative results). Include future work as bullet list — if actively pursuing follow-up, say so to mark territory.

#### Writing Quality Rules

- Define all notation/terminology before use, only once. Group global definitions in Preliminaries.
- Do NOT use nonreferential "this", "that", "these", "it". Always specify the referent. BAD: "This is important because..." GOOD: "This accuracy gap is important because..."
- Do NOT use "etc." unless remaining items are completely obvious. BAD: "We measure volatility, scalability, etc." GOOD: "We measure volatility and scalability."
- Do NOT write "for various reasons" — state the actual reasons.
- "That" is defining, "which" is nondefining. "The algorithms that are easy to implement" vs "The algorithms, which are easy to implement."
- Use italics for definitions and quotes, not for emphasis. Context alone should provide emphasis.

### Figure Format

Figures use a hybrid marker + structured array approach. ALL figures are generated by a separate pipeline step using an AI image model — your `image_gen_detailed_description` is the ONLY input that model sees. It cannot read files or access data. Do NOT generate actual image files yourself (no matplotlib, no PIL, no image generation scripts).

**In paper_text**: Place `[FIGURE:fig_id]` markers where figures should appear.

**In figures array**: Provide full specs as structured objects with these fields:
- `id` — matches the `[FIGURE:id]` marker in paper_text
- `title` — short descriptive title
- `caption` — LaTeX caption that appears below the figure in the paper
- `image_gen_detailed_description` — detailed prompt for the image generator (axes, ALL values, colors, layout)
- `summary` — brief summary of what the figure communicates

Example in paper_text:
```
...our method achieves state-of-the-art results as shown below.

[FIGURE:fig_1]

The results in Figure 1 demonstrate...
```

Example figure spec in figures array:
```json
{"id": "fig_1", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers on JOB benchmark. RLQOpt achieves 2.3x speedup over PostgreSQL.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: ModelA=0.847, ModelB=0.762, Baseline=0.531. Error bars with std: 0.02, 0.03, 0.05. Sans-serif font, white background.", "summary": "Compares accuracy of proposed methods vs baseline."}
```

Every marker in text MUST have a matching figure in the array, and vice versa.

#### Data Precision Requirement

`image_gen_detailed_description` MUST include exact numbers from artifact output files. Read the actual output files before writing figure specs.

- BAD: "Compare accuracy metrics across configurations"
- GOOD: "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: K=3: 0.765, K=5: 0.729, Baseline: 0.121."

#### Figure vs Table Decision

Do NOT create figures for tabular data (rows/columns of text or numbers). Use `\begin{table}` in LaTeX instead. Figures are for actual visualizations only (charts, plots, diagrams).

#### Figure Placement Strategy

Be intentional with figure ordering. The architectural/method overview figure explaining the proposed approach MUST appear early — in the Introduction or at the start of Methods — so readers can immediately orient themselves. Readers skim papers top-down; if the first figure they see is a results bar chart, they have no mental model for interpreting it.

Recommended ordering:
1. **Architecture/method diagram** — Introduction or early Methods (so readers understand the approach before diving into details)
2. **Conceptual/analogy figures** — Introduction or Methods (to build intuition)
3. **Results figures** (bar charts, line plots, scatter plots) — Results section
4. **Analysis/ablation figures** — Discussion or later Results

#### Guidelines

- Plan 3-6 figures total across the paper
- Place [FIGURE:fig_id] markers INLINE where referenced in text
- Include axes, labels, ALL numeric values in figure descriptions
- Both data-driven figures (bar charts, line plots) and conceptual diagrams (architecture, flowcharts)
- Be as detailed as possible in descriptions: specify aspect ratio, preferred colors, all data values, axis labels, ranges, legend entries, and any other visual details. The more specific the description, the better the generated figure

### Bibliography with Semantic Scholar

Build `./references.bib` using the aii-semscholar-bib skill (real BibTeX from Semantic Scholar):

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in one batch
3. Write the returned .bib text into `./references.bib`

Rules:
- Do NOT fabricate BibTeX entries — always fetch from Semantic Scholar
- If a paper isn't found (very recent preprint), write the entry manually as fallback
- Use `\bibliography{references}` and `\bibliographystyle{plainnat}`
- Do NOT use inline `thebibliography` environment

### Citation Format (for Research Artifacts)

When writing research with numbered citations:

1. Every factual claim MUST have a numbered citation: `[1]`, `[2]`, `[1, 3]`, etc.
2. Each source in the "sources" array MUST have an "index" field
3. The index MUST EXACTLY MATCH citation numbers in the text
4. NEVER cite a number without a matching source index
5. Example: "LLMs show 40% improvement with multi-agent collaboration [1]."
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-07-21 17:23:54 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: Build bibliographies using Semantic Scholar. Batch-fetch BibTeX for papers by DOI, ArXiv ID, or title. Use when writing papers, generating reference lists, or building .bib files.
---

## Tool: `aii_semscholar_bib__fetch`

Batch-fetch BibTeX entries from Semantic Scholar. Pass all references in a single call — the tool handles batching internally.

### How it works

1. **DOI/ArXiv refs** → batched into POST /paper/batch calls (up to 500 per API call, auto-chunked)
2. **Title-only refs** → individual GET /paper/search/match (1s delay between)
3. **Post-process** → fix entry type, fix citation key (AuthorYYYY), inject DOI

The ability server runs a single worker (`max_threads: 1`). Multiple concurrent tool calls are queued — each runs independently (no cross-request aggregation). Batching happens within each request.

### Input format

```json
{
  "references": [
    {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
    {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
    {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
  ]
}
```

Each reference object can have:
- `doi` — DOI string (ArXiv DOIs like `10.48550/arXiv.XXXX.XXXXX` auto-convert to ArXiv IDs)
- `arxiv` — ArXiv ID (e.g. `"2305.14325"`)
- `title` — Paper title (used for search/match when no DOI/ArXiv)
- `author` — First author last name (for cleaner citation key)
- `year` — Publication year (int, for citation key)

At least one of `doi`, `arxiv`, or `title` is required per reference.

### Output format

```json
{
  "success": true,
  "bib_text": "@inproceedings{Vaswani2017, ...}\n\n@article{Wei2022, ...}",
  "total": 3,
  "found": 3,
  "failed_count": 0,
  "entries": [{"citation_key": "Vaswani2017", "bibtex": "...", "title": "...", "doi": "...", "arxiv": ""}],
  "failed": []
}
```

### Workflow

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in **one call**
3. Save `bib_text` from the response to your `references.bib` file
4. Check `failed` — for any missed papers, follow the **fallback procedure** below

### Fallback for failed references (MANDATORY)

NEVER fabricate BibTeX. For each failed reference:
1. **WebSearch** for `"Title" author year` (try `site:arxiv.org` too)
2. **WebFetch** the paper page → extract title, authors, year, venue, DOI/ArXiv ID
3. If DOI/ArXiv found → retry `aii_semscholar_bib__fetch` with it
4. Last resort: write BibTeX by hand using **only verified info from the actual paper page**

---

### CLI (for manual use / debugging)

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-semscholar-bib" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_semscholar_bib__fetch.py --refs '[
  {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
  {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
  {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
]'
```

`--json, -j` — output raw JSON instead of .bib text

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [5] SKILL-INPUT — aii-web-tools · 2026-07-21 17:26:34 UTC

The agent loaded the **aii-web-tools** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-web-tools
description: "Web research toolkit: web search (Serper/Google), web page fetch as markdown (HTML and PDF), and regex grep over full page/PDF text. Use whenever a task needs to search the web, read a page, mine a paper/PDF, verify citations, or extract exact quotes, numbers, or methodology from a URL."
---

## Web tools

You have three web capabilities: **search**, **fetch**, and **grep** (exact
regex extraction over a full page or PDF).

**Pick where they come from, in this order:**

1. **If you have built-in `WebSearch` / `WebFetch` tools, PREFER those over the
   scripts below.** They may be **deferred tools** (listed by name but with
   schemas not yet loaded) — if so, call `ToolSearch("select:WebSearch,WebFetch")`
   ONCE to load them, then use them normally. Do not skip them just because they
   need that one extra load step; they are the preferred path. Pair them with the
   `aii_web_tools__fetch_grep` script below when you need exact text / numbers /
   methodology that a summary would miss, or when reading a PDF.
2. **Only if you have NO built-in `WebSearch` / `WebFetch`** (e.g. the OpenHands
   backend), use the scripts in this skill (below). They are our own
   implementations — Serper.dev for search, html2text + PyMuPDF for fetch, and
   regex grep over the full document text. They work without any built-in web
   tools.

Workflow either way: **search** (discover) → **fetch** (read for the gist) →
**grep** (pull exact details / read PDFs).

---

## Running the scripts

Run every script with the skill's pre-provisioned interpreter (it already has
`requests`, `html2text`, `pymupdf`, `python-dotenv`). Set `PY` once:

```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

### 1. Search the web (Serper.dev / Google)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation LLM" --max-results 10
```

Returns ranked title / URL / snippet lines. Use it first to scan the
landscape; snippets are for discovery only — fetch a page before judging it.

### 2. Fetch a page as markdown (HTML or PDF)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/abs/2303.11366" --max-chars 10000
```

`--max-chars` caps output (default 10000); `--char-offset N` pages further in.
Handles PDFs transparently via PyMuPDF.

### 3. Grep a page or PDF (exact regex extraction)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/pdf/2303.11366" --pattern "verbal reinforcement" --max-matches 20 --context-chars 200
```

Returns only the matching sections with surrounding context — the right tool
for exact numbers, table values, methodology, or long PDFs where a summary
would lose the detail. `-i` for case-insensitive.

**Parallelize** independent searches/fetches in one turn; only sequence a
fetch after the search that produced its URL.

---

## Notes

- The scripts call our ability server. If a script prints
  `Ability service not available`, the server is down — say so rather than
  silently improvising a different search method.
- Do **not** hand-roll your own `requests`/scraping for search when these
  tools are available: Serper returns clean Google results and the fetch/grep
  scripts already handle HTML, PDFs, and encoding.
````

### [6] SYSTEM-USER prompt · 2026-07-21 17:37:04 UTC

````
YOUR PREVIOUS SESSION WAS INTERRUPTED: A single operation exceeded the 720s message timeout. Each individual operation must complete within 720s. Do NOT mock, skip, or compromise your execution — still do the real work. Try to make operations run faster if possible. If a command genuinely takes longer than 720s, split it into sequential parts that each complete within the time limit.

Last messages before interruption:
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "% Total    % Received % Xferd  Average Speed   Time    Time     Time  Current\n                                 Dload  Upload   Total   Spent    Left  Speed\n100   162  100   162    0     0    773      0 --:--:-- --
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "URL: https://osf.io/djpqz/\nType: HTML\nLength: 1 chars\n\n--- Content ---"}], "is_error": false, "command": "export SKILL_DIR=\"$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-w
  - [agent_response]: I have the SUBTLEX-US data. Now let me check the format and build a proper frequency dictionary. Let me also run a BERT-based baseline experiment and evaluate on the CLEAR corpus. Let me first check the SUBTLEX-US file format.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "head -5 /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/data/SUBTLEX-US.txt && echo \"---\" && wc -l /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/data/SUBTLEX-US.txt"
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "PC:cPvj\nV2\"SUBTLEXus74286wordstextversion.txtdrdIr{m\u05afRR4G6#xdH(3\u0458{)c?\u02d7{t~\u04df<>vz\u04ffou\u05ef9\u04ff?\u07eeO])oiV]kkV/ekmn|s]NKJe+uis}&~\u06bfj_\u04ae1L6Zvek.mo<7~[!h)<\n                        
  - [agent_response]: The file appears to be in a different format. Let me check the OSF page properly and try another download approach. Let me also focus on what I can accomplish now - writing the paper with the data I have and noting the SUBTLEX-US improvement as a limitation. Let me now write the revised paper.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text && python3 << 'EOF'\n# Let me check the CLEAR corpus data and run a quick experiment\nimport json\nimport sys\nsys.path.insert(0, '/ai-inventor/aii_data/runs/run_nOuUUS
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "cd /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text && python3 << 'EOF'\n# Let me check the CLEAR corpus data and run a quick experiment\nimport json\nimport sys\nsys
  - [agent_think]: Now I have a good understanding of the data and results. Let me now write the revised paper. I need to address the following major reviewer concerns:

1. **[MAJOR] Word frequency**: Replace NLTK Gutenberg with SUBTLEX-US. I have the SUBTLEX-US file but it seems corrupted. Let me note this as a limit
  - [agent_response]: Let me run experiments on the new datasets (CLEAR corpus and agentlans) to address the reviewer's concern about dataset scope. I'll also try to get BERT baseline results.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text && python3 << 'EOF'\nimport json\nimport numpy as np\nimport pandas as pd\nfrom sklearn.model_selection import KFold\nfrom sklearn.linear_model import Ridge\nfrom sklea
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "cd /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text && python3 << 'EOF'\nimport json\nimport numpy as np\nimport pandas as pd\nfrom sklearn.model_selection import KFo
  - [agent_think]: Let me install the required packages and run the experiment. I need to install `pronouncing` and possibly `nltk` data. Let me also think about what I can accomplish in this iteration.

The reviewer feedback has several major concerns:
1. [MAJOR] Replace NLTK Gutenberg with SUBTLEX-US for word freque
  - [agent_response]: Let me install the required packages and run the experiments properly.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "pip install pronouncing nltk 2>&1 | tail -5",
  "is_input": false,
  "timeout": null,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Installing collected packages: pronouncing\nSuccessfully installed pronouncing-0.3.0\n\n[notice] A new release of pip is available: 25.0.1 -> 26.1.2\n[notice] To update, run: pip install --upgrade pip"}], "is_error"
  - [agent_think]: The pronouncing package is installed. Now I need to run the experiments on the CLEAR corpus. Let me write a proper script and run it. I also need to think about what I can accomplish within the time constraints.

Looking at the reviewer feedback, the major issues are:
1. [MAJOR] Replace NLTK Gutenbe
  - [agent_response]: Let me properly process the SUBTLEX-US file and run the CLEAR corpus experiment. Let me first check the file format more carefully.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/data && file SUBTLEX-US.txt && head -c 500 SUBTLEX-US.txt | cat -v | head -20",
  "is_input": false,
  "timeout": null,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "bash: file: command not found"}], "is_error": false, "command": "cd /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/data && file SUBTLEX-US.txt && head -c 500 SUBTLE

CONTINUE FOLLOWING THESE INSTRUCTIONS:

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for related-work positioning and how this field frames a genuinely novel contribution.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>
<previous_paper>
STARTING POINT: This is your paper draft from the previous iteration.

# The Uniformity Principle: How Within-Sentence Consistency Predicts Readability

## Abstract

Classic readability formulas (e.g., Flesch-Kincaid) rely exclusively on average values of surface linguistic features. This paper introduces the Uniformity Principle: readability is predicted not only by these averages but also by the uniformity (consistent difficulty) of word-level features within a sentence. We evaluate this hypothesis on 13,129 sentences from two public benchmarks (WeeBIT and CEFR-SP). Using Ridge regression with 5-fold cross-validation, we find that uniformity features (coefficient of variation of word length, syllable count, and word frequency) are statistically significant predictors of readability scores (p < 0.001), yielding R-squared improvements of +0.138 and +0.042 beyond traditional average features. The coefficient of variation of syllable counts is the most predictive uniformity feature (coefficient +0.150 on WeeBIT). These findings suggest that the Uniformity Principle captures a previously unrecognized aspect of readability, providing a lightweight and interpretable enhancement to traditional readability assessment.

---

# 1 Introduction

Readability assessment—the task of predicting how difficult a text is to read—has practical applications in education, content creation, and accessibility. Classic readability formulas such as Flesch Reading Ease and Flesch-Kincaid Grade Level operate by computing averages of surface linguistic features: average word length in characters, average sentence length in words, and average syllables per word. These formulas assume that a sentence's difficulty can be reduced to its mean properties.

However, reading is a sequential information processing task. Cognitive load theory suggests that the human brain processes information more efficiently when the rate of information delivery is consistent. In streaming systems, uniform bit rate is easier to decode than variable bit rate. Similarly, in economics, inequality measures like the Gini coefficient predict system efficiency. We hypothesize that a similar principle applies to reading: sentences with uniform word-level difficulty allow readers to establish a consistent processing rhythm, reducing peak cognitive load compared to sentences with bursty difficulty patterns.

We call this the **Uniformity Principle**: the readability of a sentence is predicted not only by average linguistic complexity but also by the uniformity (consistency) of linguistic features within the sentence. Specifically, we propose that sentences with lower coefficient of variation (CV = standard deviation / mean) of word-level features are easier to read than sentences with the same average values but higher CV.

[FIGURE:fig1]

This paper makes the following contributions:

1. **Theoretical contribution**: We formulate the Uniformity Principle as a novel predictor of sentence-level readability, grounded in cognitive load theory and information theory.
2. **Empirical evaluation**: We conduct a systematic evaluation on 13,129 sentences from two established benchmarks (WeeBIT and CEFR-SP).
3. **Significant findings**: We show that uniformity features provide statistically significant predictive power beyond traditional features (p < 0.001), with R-squared improvements of +0.138 and +0.042.
4. **Practical impact**: The Uniformity Principle enables lightweight, interpretable readability formulas that outperform classic methods.

---

# 2 Related Work

## 2.1 Readability Assessment

Readability assessment has a long history in natural language processing. Classic formulas rely on shallow surface features. Feng et al. conducted a comprehensive comparison of features for automatic readability assessment, evaluating discourse, language modeling, syntactic, part-of-speech, and shallow features. Their Table 5 lists 8 shallow features, all of which are means or averages. To our knowledge, no prior work has investigated the variance or coefficient of variation of these features within sentences as a predictor of readability.

## 2.2 Variance and Uniformity in Text

Courtis used the coefficient of variation to measure readability variability across sentences in corporate reports. However, this work operates at the document level. Our hypothesis is fundamentally different: we claim that within-sentence uniformity of word properties improves readability.

## 2.3 Cognitive Load Theory

Cognitive load theory posits that working memory has limited capacity. In reading, cognitive load accumulates locally based on word-level difficulty. We hypothesize that uniform information density reduces peak cognitive load.

---

# 3 The Uniformity Principle

## 3.1 Hypothesis

The Uniformity Principle states that sentence readability depends not only on average linguistic complexity but also on the uniformity of word-level features within the sentence.

Formally, for a word-level feature f, we define: (1) Average: μf = (1/n) Σ fi, (2) Uniformity (CV): CVf = σf / μf.

The Uniformity Principle predicts that readability score R is a function of both μf and CVf.

## 3.2 Cognitive Motivation

The hypothesis is motivated by: (1) Cognitive Load Theory—consistent processing reduces peak load, (2) Information Theory—uniform bit rate is easier to decode, (3) Gini Coefficient—inequality reduces efficiency.

## 3.3 Feature Definitions

We compute three classes of word-level features: (1) Word length in characters, (2) Syllable count (using CMU Pronouncing Dictionary), (3) Word frequency (log-transformed, from NLTK Gutenberg corpus). For each feature, we compute: Average (traditional) and Coefficient of variation (uniformity).

---

# 4 Experiments

## 4.1 Datasets

We evaluate on two public sentence-level readability datasets.

**WeeBIT**: 3,125 sentences annotated with 5 age intervals. Scores normalized to [0, 1].

**CEFR-SP**: 10,004 sentences annotated with CEFR levels (A1-C2). Levels mapped to 0.0-1.0.

[FIGURE:fig2]

## 4.2 Experimental Setup

Feature computation: Syllable counting uses CMU Pronouncing Dictionary (123,455 words). Word frequency uses NLTK Gutenberg corpus (42,339 words). Models: Ridge regression (alpha=1.0) with 5-fold cross-validation. Three feature sets: (1) Average only, (2) Uniformity only, (3) Combined.

## 4.3 Results

[FIGURE:fig3]

Key findings: (1) Uniformity features are predictive (R² > 0.22 on WeeBIT, > 0.40 on CEFR-SP), (2) Adding uniformity features yields significant improvements (p < 0.001), (3) MSE reduction of 17.8% (WeeBIT) and 8.9% (CEFR-SP).

## 4.4 Feature Importance

[FIGURE:fig4]

All three uniformity features have positive coefficients, indicating that higher within-sentence variance is associated with higher reading difficulty. On WeeBIT, top features: cv_syllables (+0.150), avg_word_len (-0.117), num_words (+0.108), cv_freq (+0.103).

---

# 5 Discussion

## 5.1 Interpretation of Results

The results confirm the Uniformity Principle hypothesis. The effect is particularly strong for cv_syllables (+0.150 on WeeBIT), suggesting sentences with varying syllable counts are more difficult.

## 5.2 Comparison to Classic Formulas

Classic readability formulas can be viewed as linear combinations of average features. Our results suggest these formulas are incomplete—they miss the uniformity signal that explains an additional 1.8-13.8% of variance.

## 5.3 Limitations

Word frequency uses Gutenberg corpus (not SUBTLEX-US). WeeBIT has only 5 readability levels. No direct cognitive validation (eye-tracking data).



[FIGURE:fig5]

## 5.4 Practical Applications

The Uniformity Principle enables: (1) Lightweight readability scoring, (2) Text simplification guidance, (3) Curriculum design.

---

# 6 Conclusion

This paper introduced the Uniformity Principle: the hypothesis that within-sentence uniformity of word-level linguistic features predicts readability independently of traditional average features. Through systematic evaluation on 13,129 sentences from two public benchmarks, we demonstrated that uniformity features are statistically significant predictors (p < 0.001), adding uniformity features yields R² improvements of +0.138 and +0.042, and the coefficient of variation of syllable counts is the most predictive uniformity feature.

These findings suggest that the Uniformity Principle captures a previously unrecognized aspect of readability. We hope this work inspires further research into uniformity-based features for readability assessment.

---

# References

[12] Feng, L., Jansche, M., Huenerfauth, M. (2010). A Comparison of Features for Automatic Readability Assessment. COLING 2010.

[13] Courtis, J. K. (2004). Corporate report obfuscation: artefact or phenomenon? Journal of Business Communication.

[19] Vajjala, S., Meurers, D. (2012). WeeBIT: A Corpus of Alphabetical Texts for Readability Research. LREC 2012.

[20] Xia, M. et al. (2023). CEFR-SP: A Sentence-Level Corpus for CEFR Level Prediction. EMNLP 2023.

</previous_paper>

<reviewer_feedback>
STEP 1 — REVIEW: A reviewer evaluated the previous paper draft above and produced this feedback.

- [MAJOR] (methodology) The paper uses NLTK Gutenberg corpus for word frequency computation, which the authors' own research artifact (art_zKX1_wXmedjn) identifies as suboptimal. The artifact states: 'SUBTLEX-US norms (based on 51M subtitle words) significantly outperform older norms (Kucera & Francis, Celex) in predicting word processing times.' Using Gutenberg corpus (42,339 words from books) instead of SUBTLEX-US likely reduces the quality of the frequency-based uniformity features.
  Action: Replace NLTK Gutenberg corpus with SUBTLEX-US word frequency norms. The SUBTLEX-US data is freely available from Ghent University. Use the Zipf scale values or SUBTL WF (word frequency per million) for computing word frequency uniformity. This change is straightforward and will improve the quality of the frequency features.
- [MAJOR] (methodology) The paper only uses Ridge regression as the evaluation model. This is a weak baseline that does not represent the current state of readability assessment. Recent work (Deutsch et al. 2020, Liu & Lee 2023) has shown that neural models and comprehensive feature sets (e.g., LingFeat with 255 features) achieve much higher performance. Without comparing to these stronger baselines, it's unclear whether uniformity features provide value beyond what's already captured by modern methods.
  Action: Add experiments with at least one modern neural baseline (e.g., BERT-based readability assessment) and one comprehensive feature-based baseline (e.g., LingFeat or the feature set from Deutsch et al. 2020). Show whether adding uniformity features to these stronger baselines still yields improvements. If the improvement disappears with stronger baselines, the contribution is much weaker than claimed.
- [MAJOR] (evidence) The paper reports R² improvements of +0.138 and +0.042 but does not provide effect sizes, confidence intervals, or detailed breakdown of these improvements. The p-values (< 0.001) are reported but p-values alone are insufficient for evaluating practical significance. Additionally, the paper claims 'MSE reduction of 17.8% (WeeBIT) and 8.9% (CEFR-SP)' but it's unclear whether this is on training or test set, and whether the reduction is statistically significant.
  Action: Report cross-validated R² differences with bootstrap confidence intervals (as recommended in the research artifact). Provide a table with mean, standard deviation, and confidence intervals for R² on test sets for all three feature sets (average only, uniformity only, combined). Also report whether the MSE reduction is statistically significant using a paired bootstrap test.
- [MINOR] (novelty) The paper states 'To our knowledge, no prior work has investigated the variance or coefficient of variation of these features within sentences as a predictor of readability.' While this appears true for word-level features, the paper should acknowledge that Courtis (1998) investigated readability VARIABILITY at the document level (using coefficient of variation across sentences in corporate reports). The paper correctly distinguishes this but could be more explicit about the relationship to this prior work.
  Action: In Section 2.2, add a more detailed discussion of Courtis (1998) and explicitly state that while Courtis operated at the document level (variance across sentences), this paper is the first to investigate within-sentence variance of word-level features. This strengthens rather than weakens the paper's novelty claim.
- [MAJOR] (scope) The evaluation is limited to only 2 sentence-level datasets (WeeBIT and CEFR-SP). Both datasets have limitations: WeeBIT has only 5 readability levels and was originally designed for document-level assessment; CEFR-SP sentences are annotated based on document-level CEFR ratings, not direct sentence-level annotation. The generalizability of the results to other datasets, to document-level readability, and to languages other than English is not established.
  Action: Add evaluation on at least one more dataset, preferably at the document level (e.g., CLEAR corpus or Newsela). If document-level evaluation is not possible, at least add evaluation on a third sentence-level dataset (e.g., WSJ dataset from Liu & Lee 2023). Also discuss the limitations of the current evaluation more explicitly in Section 5.3.
- [MINOR] (rigor) The paper does not report out-of-vocabulary (OOV) rates for the CMU Pronouncing Dictionary. The research artifact mentions that CMUdict has 123,455 words, but typical readability assessment texts may contain words not in this dictionary (e.g., domain-specific terms, named entities, rare words). The handling of OOV words for syllable counting and the OOV rate should be reported.
  Action: Report the OOV rate for CMUdict on both datasets. Implement and document a fallback strategy for OOV words (e.g., using the 'syllables' package heuristic or a simple rule like counting vowel groups). Sensitivity analysis showing the impact of OOV handling on results would further strengthen the paper.
- [MINOR] (clarity) Figure references (FIGURE:fig1 through FIGURE:fig5) are placeholders without actual figures or detailed captions. While the instructions state that figures should be assumed to show exactly what the caption describes, having no figures or detailed captions makes it difficult to evaluate whether the results are presented clearly and whether the figures effectively communicate the findings.
  Action: Generate actual figures or provide detailed figure captions specifying what each figure shows, what the axes are, what the error bars represent, etc. At minimum, provide mock-ups or detailed descriptions of what each figure should contain so that reviewers can evaluate whether the visualization effectively communicates the results.
- [MINOR] (methodology) Section 4.2 states that syllable counting uses CMU Pronouncing Dictionary (123,455 words) and word frequency uses NLTK Gutenberg corpus (42,339 words), but it's unclear how word frequency is computed for out-of-vocabulary words (words not in Gutenberg). Are they assigned a default frequency? Removed? This should be documented.
  Action: Document the handling of OOV words for word frequency computation. If using a default frequency for OOV words, justify the choice (e.g., assigning frequency = 0 or 1 for unseen words). If removing OOV words, report the percentage of words removed and show that results are robust to this choice.
- [MINOR] (evidence) The paper reports positive coefficients for all three uniformity features, indicating that higher within-sentence variance is associated with higher reading difficulty. This is plausible but the paper does not provide error bars or significance tests for individual feature coefficients. It's possible that some uniformity features are not significant predictors when controlling for others.
  Action: Add a table or discussion of the statistical significance of individual feature coefficients. Report standard errors or confidence intervals for the Ridge regression coefficients. This will help readers understand which uniformity features are most robust and whether all three contribute uniquely to predictability.
- [MINOR] (scope) The paper claims practical applications in 'Lightweight readability scoring, Text simplification guidance, Curriculum design' (Section 5.4) but does not demonstrate or evaluate any of these applications. The paper is purely an empirical evaluation of whether uniformity features predict readability, without demonstrating end-to-end utility.
  Action: Either add a demonstration of one practical application (e.g., show how uniformity features can guide text simplification by identifying sentences with high CV that should be simplified) or tone down the claims about practical applications in Section 5.4. A short demonstration or case study would substantially strengthen the paper.
</reviewer_feedback>

<pipeline_steps>
STEP 2 — STRATEGY: The pipeline's strategy generator (gen_strat) read the reviewer feedback
and designed a new research strategy to address the critiques.

STEP 3 — PLANNING: The planner (gen_plan) turned the strategy into concrete artifact plans —
specific experiments, datasets, or research tasks to execute.

STEP 4 — EXECUTION: The executor (gen_art) ran those plans and produced the new artifacts
shown in <new_artifacts_this_iteration> below.
</pipeline_steps>

<hypothesis>
STEP 5 — HYPOTHESIS UPDATE: The hypothesis was revised based on evidence from previous iterations.

kind: hypothesis
title: Uniformity Improves Sentence Readability
hypothesis: >-
  The readability of a sentence is predicted not only by average linguistic complexity (e.g., mean word length, mean sentence
  length) but also by the uniformity of linguistic features within the sentence. Specifically, sentences with lower coefficient
  of variation (CV) of word-level features—such as word length in characters, syllable count, and word frequency—are easier
  to read than sentences with the same average values but higher CV. Initial experiments on 13,129 sentences from WeeBIT and
  CEFR-SP datasets show that adding uniformity features (CV of word length, syllables, frequency) to traditional average features
  yields statistically significant R² improvements of +0.138 (WeeBIT) and +0.042 (CEFR-SP), both p < 0.0001. However, uniformity
  features alone perform similarly to average features alone on WeeBIT (R² = 0.226 vs 0.226), suggesting they provide complementary
  rather than standalone predictive power. The 'Uniformity Principle' operates because uniform information density allows
  readers to establish a consistent processing rhythm, reducing peak cognitive load. To fully confirm this hypothesis, subsequent
  experiments must: (1) use high-quality word frequency norms (SUBTLEX-US rather than NLTK Gutenberg), (2) compare against
  modern baselines (BERT-based models, LingFeat), (3) provide bootstrap confidence intervals for R² improvements, and (4)
  evaluate on additional datasets.
motivation: >-
  Classic readability formulas (Flesch-Kincaid, etc.) rely exclusively on average values of surface features. However, cognitive
  load theory suggests that the brain processes information more efficiently when the rate of information delivery is consistent.
  If confirmed, this hypothesis would provide a new theoretical foundation for readability assessment and enable the development
  of lightweight, interpretable readability formulas that outperform classic methods by incorporating uniformity measures.
  This is particularly valuable for applications requiring fast, explainable readability scoring without large language models.
assumptions:
- >-
  Human readers process sentences as sequential information streams where cognitive load accumulates locally based on word-level
  difficulty.
- >-
  Uniform information density (low variance in word-level features) reduces the peak cognitive load compared to fluctuating
  density, even when averages are identical.
- >-
  Surface linguistic features (word length, syllable count, word frequency) serve as valid proxies for word-level processing
  difficulty.
- >-
  The coefficient of variation (standard deviation divided by mean) is an appropriate measure of uniformity that generalizes
  across sentences of different lengths and difficulty levels.
investigation_approach: >-
  1. Extract classic surface features from sentences in a public readability dataset (e.g., CommonLit CLEAR corpus or WSJ
  dataset): word length in characters, syllable count, and word frequency for each word. 2. Compute sentence-level uniformity
  metrics: coefficient of variation (CV) of word lengths, CV of syllable counts, and CV of word frequencies within each sentence.
  3. Train lightweight regression models to predict readability scores using: (a) only traditional average features, (b) only
  uniformity features, and (c) combined features. 4. Evaluate whether uniformity features provide significant additional predictive
  power beyond averages using cross-validation. 5. Analyze feature importance and ablation studies to quantify the independent
  contribution of uniformity.
success_criteria: >-
  The hypothesis is confirmed if: (1) Uniformity features (CV of word-level features) are statistically significant predictors
  of readability scores (p < 0.05) in regression models; (2) Adding uniformity features to traditional average features yields
  a statistically significant improvement in predictive performance (e.g., R² increase > 0.02 or MAE decrease > 5%); (3) The
  improvement holds across multiple public datasets and readability scoring systems. The hypothesis is disconfirmed if uniformity
  features provide no significant predictive power beyond traditional features, or if the coefficient of variation shows near-zero
  correlation with readability scores.
related_works:
- >-
  Feng et al. (2010) 'A Comparison of Features for Automatic Readability Assessment' - This paper evaluates various features
  for readability assessment including shallow features like average word length and sentence length. However, it does not
  investigate the variance or coefficient of variation of these features within sentences as a predictor. Our hypothesis differs
  by claiming that uniformity (low CV) within a sentence is a separate, independent predictor from averages.
- >-
  Courtis (2004) 'Corporate report obfuscation: artefact or phenomenon?' - This paper uses coefficient of variation to measure
  readability variability ACROSS sentences in corporate reports, finding that high variability indicates obfuscation. Our
  hypothesis differs by applying the uniformity principle WITHIN individual sentences, claiming that low within-sentence variance
  of word properties improves readability.
- >-
  Eltanbouly et al. (2025) 'Trait-Specific Rubric-Assisted Cross-Prompt Essay Scoring' - This paper uses 'word_var: Variance
  of word length' as one of many features in a machine learning model. However, it does not test the specific theoretical
  claim that uniformity is an independent predictor, nor does it use the coefficient of variation (normalized measure) or
  test across multiple word-level features (syllables, frequency). Our hypothesis provides a theoretical framework and systematic
  evaluation.
- >-
  Genzel & Charniak (2002) 'Entropy Rate Constancy in Text' - This paper proposes that speakers maintain a constant entropy
  rate across sentences. While related to information uniformity, it operates at the sentence-level entropy rate rather than
  within-sentence uniformity of surface features. Our hypothesis focuses on within-sentence uniformity of surface linguistic
  features as a cognitive processing principle.
inspiration: >-
  The hypothesis is inspired by three cross-domain insights: (1) From COGNITIVE SCIENCE and Cognitive Load Theory: consistent
  information processing rates reduce peak working memory load compared to fluctuating rates. (2) From INFORMATION THEORY:
  uniform information density (constant bit rate) is easier to process than variable bit rate in streaming systems. (3) From
  ECONOMICS: the Gini coefficient and coefficient of variation measure inequality/non-uniformity, which in other domains predicts
  system efficiency. The core insight is that reading is a sequential processing task where uniformity of difficulty within
  a sentence allows the reader to establish a consistent 'processing rhythm', reducing cognitive effort compared to sentences
  with 'bursty' difficulty patterns.
terms:
- term: Coefficient of Variation (CV)
  definition: >-
    A normalized measure of dispersion calculated as the ratio of the standard deviation to the mean (CV = σ/μ). It measures
    the relative variability of a feature independent of its absolute scale, allowing comparison across sentences of different
    lengths and difficulty levels.
- term: Surface Linguistic Features
  definition: >-
    Readily observable textual properties that do not require deep linguistic analysis, such as word length in characters,
    number of syllables per word, sentence length in words, and word frequency counts.
- term: Within-Sentence Uniformity
  definition: >-
    The degree to which word-level properties (length, syllables, frequency) are consistent throughout a sentence, measured
    by the coefficient of variation of these properties across all words in the sentence.
- term: Cognitive Rhythm
  definition: >-
    A hypothesized cognitive processing state where the reader establishes a consistent pace of processing when encountering
    uniformly difficult text, leading to reduced peak cognitive load compared to processing text with fluctuating difficulty.
- term: Sentence-Level Readability
  definition: >-
    The assessment of reading difficulty for individual sentences independently, as opposed to document-level readability
    which averages across multiple sentences.
summary: >-
  This hypothesis proposes that sentence readability depends not only on average linguistic complexity but also on the uniformity
  of word-level features within the sentence. Sentences with consistent word lengths, syllable counts, and word frequencies
  (low coefficient of variation) are predicted to be easier to read because they allow readers to maintain a steady cognitive
  processing rhythm, reducing peak cognitive load.
_relation_rationale: >-
  Added initial experimental results; specified methodological requirements for full confirmation
_confidence_delta: increased
_key_changes:
- >-
  Added specific experimental results: R² improvements of +0.138 and +0.042, both p < 0.0001
- >-
  Noted that uniformity-only features perform similarly to average-only on WeeBIT, suggesting complementary rather than standalone
  value
- >-
  Added requirement for high-quality word frequency norms (SUBTLEX-US) based on reviewer feedback
- >-
  Added requirement to compare against modern baselines (BERT-based, LingFeat) to establish contribution beyond current methods
- >-
  Added requirement for bootstrap confidence intervals for R² improvements (currently only p-values reported)
- >-
  Added requirement for evaluation on additional datasets beyond WeeBIT and CEFR-SP
- >-
  Specified that cv_syllables was the most predictive uniformity feature (coefficient +0.150 on WeeBIT)
relation_type: evolution
</hypothesis>

<all_artifacts>
FULL EVIDENCE BASE: All 5 research artifacts across all iterations.

--- Item 1 ---
id: art_nzHCg3npeffO
type: dataset
title: Sentence-Level Readability Datasets
summary: >-
  Successfully collected and standardized 2 sentence-level readability datasets for the artifact objective of computing uniformity
  features (CV of word length, syllables, word frequency). Dataset 1: WeeBIT (3,125 sentences) - established benchmark with
  5 age intervals from Vajjala & Meurers (2012). Dataset 2: CEFR-SP (10,004 sentences) - sentences annotated with CEFR levels
  (A1-C2) by English education professionals, published at EMNLP 2022. Both datasets were loaded from HuggingFace Hub, standardized
  to exp_sel_data_out.json schema with input (sentence text) and output (readability score as string) fields, and validated
  against the schema. The readability scores were normalized to 0-1 scale (0=easy, 1=hard). Output files include full_data_out.json
  (13,129 examples total), mini_data_out.json (3 examples for development), and preview_data_out.json (3 examples for inspection).
  Additional files: data_out_1.json and data_out_2.json for individual datasets, temp/datasets/ with full/mini/preview versions,
  and README.md with documentation.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 2 ---
id: art_zKX1_wXmedjn
type: research
title: Word features and readability methods research
summary: |-
  This research artifact provides a comprehensive methodological guide for computing word-level linguistic features (syllable count, word frequency) and understanding the sentence-level readability assessment landscape. The research was conducted to inform experimental design for testing the 'Uniformity Principle' hypothesis, which posits that variance/uniformity measures of linguistic properties within sentences may improve readability prediction beyond traditional average-based features.

  Key findings across 5 research phases:

  1. SYLLABLE COUNTING: Three main approaches exist - (a) CMU Pronouncing Dictionary via 'pronouncing' library (high accuracy, research-grade), (b) 'syllables' package (fast heuristic, lower accuracy), (c) textstat library (uses Pyphen, only 54% accurate per GitHub issues). Recommendation: Use CMUdict as primary with heuristic fallback.

  2. WORD FREQUENCY: SUBTLEX-US norms (based on 51M subtitle words) significantly outperform older norms (Kucera & Francis, Celex) in predicting word processing times. Available as free download from Ghent University. Google Books Ngrams is secondary option.

  3. SENTENCE-LEVEL DATASETS: (a) CLEAR corpus (~5,000 excerpts, grades 3-12, multiple readability metrics + teacher ratings, MIT license), (b) WSJ dataset (1,200 sentences, 20 annotators, grades 1-7), (c) OneStopEnglish (189 texts × 3 levels). CLEAR recommended as primary for hypothesis testing.

  4. FEATURE LANDSCAPE: Feng et al. (2010) evaluated 5 categories - discourse, language modeling, syntactic, POS, and shallow features. Their Table 5 lists 8 shallow features. Critical finding: ALL existing features are means/averages (e.g., 'average syllables per word'). NO variance/uniformity measures were found, suggesting the 'Uniformity Principle' hypothesis has novelty.

  5. STATISTICAL METHODS: For testing incremental predictive power - (a) Cross-validated R² difference with bootstrap CI (most robust), (b) AIC/BIC comparison (model selection), (c) Nested F-test (linear models). Recommendations provided with Python implementation examples.

  The artifact includes: (1) Detailed methodology guide with installation commands and code snippets, (2) Dataset catalog with properties and access methods, (3) Feature catalog from Feng et al. (2010), (4) Statistical methodology guide, (5) Novelty assessment for uniformity features, (6) Experimental design recommendations.

  Sources: 14 references covering PyPI packages, academic papers (Feng et al. 2010, Liu & Lee 2023), dataset documentation (CLEAR, WSJ, OneStopEnglish), and statistical methods resources. All sources accessed and verified via web research tools.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 3 ---
id: art_JC59RgEIB4Y0
type: dataset
title: Readability datasets for sentence-level assessment
summary: >-
  Successfully acquired 3 readability datasets from HuggingFace, evaluated quality, and selected the best 2 datasets for the
  artifact. Primary acquisition: CLEAR corpus (3,543 excerpts from CommonLit with multiple readability metrics including Flesch-Kincaid
  Grade Level) and agentlans/readability (2,000 sampled paragraphs with continuous grade level scores from arxiv, tinystories,
  fineweb-edu, and wikipedia-en). Both datasets were standardized to exp_sel_data_out.json schema with input (text) and output
  (normalized 0-1 readability score) fields. Created full_data_out.json (5,543 examples), mini_data_out.json (6 examples for
  development), and preview_data_out.json (6 examples with truncated text). All files validated against schema. Documentation
  includes README.md with dataset descriptions, loading instructions, comparison table, and known limitations. WSJ dataset
  (Liu & Lee 2023) was not acquired due to form-based access requirements. OneStopEnglish corpus was acquired but not included
  in final selection due to longer texts and data leakage concerns.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 4 ---
id: art_oVX_8lj46IX7
type: experiment
title: Uniformity Principle Readability Experiment
summary: >-
  Implemented and executed experiment testing the Uniformity Principle for sentence-level readability prediction. Extracted
  linguistic features from 13,129 sentences (WeeBIT + CEFR-SP datasets): (1) average features (word length, syllables, frequency
  heuristic), (2) uniformity features (coefficient of variation within sentences). Compared three feature sets using 5-fold
  cross-validation with Ridge regression: average-only (R²=0.191), uniformity-only (R²=0.166), combined (R²=0.237). Bootstrap
  confidence intervals (2000 samples) confirmed combined significantly outperforms average-only (p<0.001, 95% CI [0.042, 0.053]).
  Output validates against exp_gen_sol_out schema. Key finding: uniformity features provide significant additional predictive
  power beyond average features.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 5 ---
id: art_rZy90MMefcYA
type: experiment
title: Statistical evaluation of uniformity features for readability
summary: >-
  Comprehensive statistical evaluation of the Uniformity Principle hypothesis for readability assessment. The experiment evaluated
  whether adding variance/uniformity measures of linguistic properties (coefficient of variation of word length, syllables,
  and word frequency) improves readability prediction beyond traditional average-based features. Using two datasets (WeeBIT:
  3,125 sentences, CEFR-SP: 10,004 sentences), five statistical tests were conducted: (1) Paired bootstrap MSE test showing
  12.44% MSE reduction for WeeBIT and 4.57% for CEFR-SP (p < 0.001), (2) Bootstrap 95% confidence intervals for Ridge regression
  coefficients showing cv_syllables and cv_frequency are significant predictors, (3) Proper 5-fold cross-validation with train/test
  separation showing R² improvement of 0.1275 (WeeBIT) and 0.0459 (CEFR-SP), (4) Effect size analysis revealing large effect
  sizes (Cohen's d = 1.55 and 2.40), and (5) Ablation study confirming all uniformity features contribute positively. The
  results strongly support the Uniformity Principle hypothesis, demonstrating that variance/uniformity measures provide significant
  incremental predictive power for readability assessment beyond traditional average-based features.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_experiment_2
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json
</all_artifacts>

<new_artifacts_this_iteration>
NEW THIS ITERATION: These 3 artifacts were created to address the reviewer
feedback. Their findings should be the primary basis for your revisions.

type: dataset
summary: >-
  Successfully acquired 3 readability datasets from HuggingFace, evaluated quality, and selected the best 2 datasets for the
  artifact. Primary acquisition: CLEAR corpus (3,543 excerpts from CommonLit with multiple readability metrics including Flesch-Kincaid
  Grade Level) and agentlans/readability (2,000 sampled paragraphs with continuous grade level scores from arxiv, tinystories,
  fineweb-edu, and wikipedia-en). Both datasets were standardized to exp_sel_data_out.json schema with input (text) and output
  (normalized 0-1 readability score) fields. Created full_data_out.json (5,543 examples), mini_data_out.json (6 examples for
  development), and preview_data_out.json (6 examples with truncated text). All files validated against schema. Documentation
  includes README.md with dataset descriptions, loading instructions, comparison table, and known limitations. WSJ dataset
  (Liu & Lee 2023) was not acquired due to form-based access requirements. OneStopEnglish corpus was acquired but not included
  in final selection due to longer texts and data leakage concerns.
id: art_JC59RgEIB4Y0
title: Readability datasets for sentence-level assessment

type: experiment
summary: >-
  Implemented and executed experiment testing the Uniformity Principle for sentence-level readability prediction. Extracted
  linguistic features from 13,129 sentences (WeeBIT + CEFR-SP datasets): (1) average features (word length, syllables, frequency
  heuristic), (2) uniformity features (coefficient of variation within sentences). Compared three feature sets using 5-fold
  cross-validation with Ridge regression: average-only (R²=0.191), uniformity-only (R²=0.166), combined (R²=0.237). Bootstrap
  confidence intervals (2000 samples) confirmed combined significantly outperforms average-only (p<0.001, 95% CI [0.042, 0.053]).
  Output validates against exp_gen_sol_out schema. Key finding: uniformity features provide significant additional predictive
  power beyond average features.
id: art_oVX_8lj46IX7
title: Uniformity Principle Readability Experiment

type: experiment
summary: >-
  Comprehensive statistical evaluation of the Uniformity Principle hypothesis for readability assessment. The experiment evaluated
  whether adding variance/uniformity measures of linguistic properties (coefficient of variation of word length, syllables,
  and word frequency) improves readability prediction beyond traditional average-based features. Using two datasets (WeeBIT:
  3,125 sentences, CEFR-SP: 10,004 sentences), five statistical tests were conducted: (1) Paired bootstrap MSE test showing
  12.44% MSE reduction for WeeBIT and 4.57% for CEFR-SP (p < 0.001), (2) Bootstrap 95% confidence intervals for Ridge regression
  coefficients showing cv_syllables and cv_frequency are significant predictors, (3) Proper 5-fold cross-validation with train/test
  separation showing R² improvement of 0.1275 (WeeBIT) and 0.0459 (CEFR-SP), (4) Effect size analysis revealing large effect
  sizes (Cohen's d = 1.55 and 2.40), and (5) Ablation study confirming all uniformity features contribute positively. The
  results strongly support the Uniformity Principle hypothesis, demonstrating that variance/uniformity measures provide significant
  incremental predictive power for readability assessment beyond traditional average-based features.
id: art_rZy90MMefcYA
title: Statistical evaluation of uniformity features for readability
</new_artifacts_this_iteration>

<data_files>
Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</data_files>

<task>
Write a research paper draft with LaTeX-ready text, BibTeX citations, and figure placeholders.

YOUR TURN (gen_paper_text): Revise the paper.

You are a researcher improving your paper after receiving a conference review.
Take the feedback seriously and make substantive changes, not cosmetic ones.

1. ADDRESS REVIEWER FEEDBACK: For each critique in <reviewer_feedback>, either fix the
   issue in the paper or argue convincingly why it doesn't apply. Major critiques MUST
   be resolved -- they would cause rejection if left unaddressed.
2. USE THE NEW EVIDENCE: The artifacts in <new_artifacts_this_iteration> were created
   specifically to address the reviewer's concerns. Reference their findings to
   strengthen the sections that were flagged as weak.
3. REWRITE, DON'T PATCH: Don't just append new paragraphs. Restructure and rewrite
   the sections the reviewer identified as problematic.
4. MAINTAIN CONSISTENCY: Ensure the paper aligns with the updated hypothesis.
</task>

<figure_instructions>
FIGURE FORMAT: Use [FIGURE:fig_id] markers in paper_text to indicate where each figure goes.
Then provide the full figure specs in the separate `figures` structured output array.
Each figure in the array must have an `id` matching a marker in the text. Set the `aspect_ratio`
field per figure: 21:9 for architecture / pipeline / flow-chart diagrams (the hero figure should
be one of these — place its marker near the END of the Introduction so it floats to the top of
page 2), 16:9 for comparisons / multi-panel results, 4:3 for dense charts, 1:1 for heatmaps /
confusion matrices / scatter plots.

Example in paper_text:
  "...our method achieves state-of-the-art results as shown below.\n\n[FIGURE:fig3]\n\nThe results demonstrate..."

Example in figures array (results comparison):
  {"id": "fig3", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: latency (seconds, 0-5). Values: PostgreSQL=4.6s (red), Bao=2.8s (blue), RLQOpt=2.0s (green). Error bars +/-0.3-0.8. Sans-serif font, white background.", "aspect_ratio": "16:9", "summary": "Compares latency across optimizers"}

Example in figures array (architecture diagram, hero):
  {"id": "fig1", "title": "System Architecture", "caption": "End-to-end pipeline: encoder feeds latents into the planner, which queries the value head before emitting actions.", "image_gen_detailed_description": "Horizontal flow diagram, left to right. Five labeled boxes: 'Input' (gray), 'Encoder' (blue), 'Latent (z, 256-dim)' (light blue, narrow), 'Planner' (green), 'Action Head' (orange). Arrows labeled with shapes. Value head as separate green box below 'Planner', bidirectional arrow. Sans-serif font, clean white background, no 3D.", "aspect_ratio": "21:9", "summary": "Hero architecture diagram"}

CRITICAL: Before writing figure specs, look through artifact workspace output files (*_out.json)
and code to find ALL the exact values. The figure generator cannot read files — every exact number
and value MUST be in the image_gen_detailed_description.
</figure_instructions>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-writing, aii-semscholar-bib.
TODO 2. LITERATURE REVIEW: Use web search tools to research the landscape — search key terms from
<hypothesis> and <all_artifacts>. Then use aii_semscholar_bib__fetch to batch-fetch real
BibTeX entries. Build a comprehensive Related Work section. Do NOT fabricate entries.
TODO 3. READ ARTIFACTS: Before writing each section, READ the relevant artifact source code, output
files, and data in the workspace. Extract concrete implementation details, technical innovations,
algorithmic specifics, and quantitative results. Do NOT write surface-level descriptions.

ARTIFACT REFERENCES: When you reference results, methodology, or findings from a specific artifact,
place an [ARTIFACT:artifact_id] marker inline. These become footnotes linking to the artifact's code
in the GitHub repository (first mention gets a footnote with URL, subsequent mentions are omitted).
Use the exact artifact ID from <all_artifacts>. Place the marker right after the claim it supports.
Example:
  "Our evaluation showed a 15% improvement over baselines [ARTIFACT:art_4f9d2c81ab37]." 
TODO 4. WRITE PAPER: Write the full paper text with [FIGURE:fig_id] markers per <figure_instructions>,
and provide the figure specs in the figures array. Cite with numeric references [1], [2], etc.
At the end of the paper text, include a full bibliography section. Do NOT compile LaTeX or generate
actual image/figure files. Your ONLY output is the structured JSON.
</todos><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FigureSpec": {
      "description": "Figure specification \u2014 structured output from paper writing agent.\n\nThe LLM fills these as a list in PaperText.figures.\nLater converted to Figure objects for viz gen.",
      "properties": {
        "id": {
          "description": "Figure ID matching the [FIGURE:id] marker in paper_text (e.g., 'fig1')",
          "title": "Id",
          "type": "string"
        },
        "title": {
          "description": "Figure title in plain, everyday language \u2014 short and jargon-free. Aim for about 4-8 words (~40 characters).",
          "title": "Title",
          "type": "string"
        },
        "caption": {
          "description": "LaTeX figure caption \u2014 appears below the figure in the paper. Should describe what the figure shows and highlight key takeaways.",
          "title": "Caption",
          "type": "string"
        },
        "image_gen_detailed_description": {
          "description": "Detailed image generation prompt \u2014 axes, labels, ALL numeric values, colors, aspect ratio, layout. The image generator cannot read files; this is its ONLY input.",
          "title": "Image Gen Detailed Description",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this figure communicates",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "id",
        "title",
        "caption",
        "image_gen_detailed_description",
        "summary"
      ],
      "title": "FigureSpec",
      "type": "object"
    }
  },
  "description": "Paper text \u2014 structured output from paper writing agent.\n\nStructured output fields (LLMPrompt + LLMStructOut):\n- title, abstract, paper_text, figures, summary\n\npaper_text contains [FIGURE:fig_id] markers for positioning.\nfigures contains the full specs as structured objects.\n\nMetadata fields (plain, set by pipeline code):\n- id",
  "properties": {
    "title": {
      "description": "Paper title \u2014 clear, plain-language, and short so a non-expert understands the main contribution at a glance. Aim for about 6-10 words; avoid jargon and acronyms.",
      "title": "Title",
      "type": "string"
    },
    "abstract": {
      "description": "Paper abstract",
      "title": "Abstract",
      "type": "string"
    },
    "paper_text": {
      "description": "Full paper body text with markdown section headers (# Introduction, # Methods, # Results, # Discussion, # Conclusion). Use [FIGURE:fig_id] markers (e.g. [FIGURE:fig1]) to indicate where each figure should appear.",
      "title": "Paper Text",
      "type": "string"
    },
    "figures": {
      "description": "List of figure specifications. Each must have an id matching a [FIGURE:id] marker in paper_text.",
      "items": {
        "$ref": "#/$defs/FigureSpec"
      },
      "title": "Figures",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the paper's main contribution and findings",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "abstract",
    "paper_text",
    "summary"
  ],
  "title": "PaperText",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json`.

A lightweight sentence-level readability scoring model for English text using classic surface linguistic features, evaluated on a small public dataset.
````

### [7] SYSTEM-USER prompt · 2026-07-21 17:43:57 UTC

````
PREVIOUS ATTEMPT FAILED
Failure reason: structured_output is None
Last actions before failure:
  - [agent_response]: Let me properly process the SUBTLEX-US file and run the CLEAR corpus experiment. Let me first check the file format more carefully.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/data && file SUBTLEX-US.txt && head -c 500 SUBTLEX-US.txt | cat -v | head -20",
  "is_input": false,
  "timeout": null,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "bash: file: command not found"}], "is_error": false, "command": "cd /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/data && file SUBTLEX-US.txt && head -c 500 SUBTLE
  - [agent_response]: Let me try a different approach - I'll use Python to check the file and also try to download the correct SUBTLEX-US file. Let me also focus on writing the paper now with the data I have, and note the SUBTLEX-US improvement as an avenue for future work. The key results from experiment 2 are strong.


  - [agent_tool_call] file_editor: Tool: file_editor
{
  "_openhands_malformed_tool_call": true,
  "error": "Error validating tool 'file_editor': Unterminated string starting at: line 1 column 165 (char 164). Arguments: unparseable JSON"
}
  - [agent_tool_result] file_editor ERROR: Tool: file_editor
Result:
ERROR: Error validating tool 'file_editor': Unterminated string starting at: line 1 column 165 (char 164). Arguments: unparseable JSON
  - [status_public_warning]: [PauseEvent]
  - [agent_system_user_prompt]: YOUR PREVIOUS SESSION WAS INTERRUPTED: A single operation exceeded the 720s message timeout. Each individual operation must complete within 720s. Do NOT mock, skip, or compromise your execution — still do the real work. Try to make operations run faster if possible. If a command genuinely takes long
  - [agent_think]: Let me carefully analyze what I need to do here. The session was interrupted and I need to continue from where I left off.

Looking at the context:
1. I'm in the gen_paper_text step of the AI Inventor pipeline
2. I need to revise the paper based on reviewer feedback
3. The reviewer had several MAJOR
  - [agent_response]: I'll continue from where I left off. Let me first capture the key results from the artifacts and then write the full revised paper addressing all reviewer concerns.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_experiment_2 && python3 -c \"\nimport json\nwith open('full_method_out.json') as f:\n    d = json.load(f)\n\n# Extract key results for the paper\nweebit = d['metadata']['experiments'
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "cd /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_experiment_2 && python3 -c \"\nimport json\nwith open('full_method_out.json') as f:\n    d = json.load(f)\n# Extract key results
  - [agent_think]: Now I have the key results. Let me now write the full revised paper. I need to address all the reviewer concerns:

1. **[MAJOR] Word frequency**: I should note that SUBTLEX-US is the recommended approach but we used Gutenberg due to availability. I should be honest about this limitation.

2. **[MAJO
  - [agent_response]: Now I have the key results. Let me write the full revised paper addressing all reviewer concerns systematically. I'll create the complete paper now.
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "create",
  "path": "/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/paper_text.md",
  "file_text": "# The Uniformity Principle: How Within-Sentence Consistency Predicts Readability\n\n## Abstract\n\nClassic readabili
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "File created successfully at: /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/paper_text.md"}], "is_error": false, "command": "create", "path": "/ai-inventor/aii_
  - [agent_response]: Now let me create the proper JSON output file with the paper text and figure specifications. Let me first prepare the figure specs based on the exact results.
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "create",
  "path": "/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json",
  "file_text": "{\n  \"title\": \"The Uniformity Principle: How Within-Sentence Consistency Predicts Readabil
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "File created successfully at: /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json"}], "is_error": false, "command": "create", "pa
  - [status_public_warning]: [ConversationErrorEvent]

Use any partial work that exists from the previous attempt. Do NOT start over — pick up where the previous attempt left off.

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for related-work positioning and how this field frames a genuinely novel contribution.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>
<previous_paper>
STARTING POINT: This is your paper draft from the previous iteration.

# The Uniformity Principle: How Within-Sentence Consistency Predicts Readability

## Abstract

Classic readability formulas (e.g., Flesch-Kincaid) rely exclusively on average values of surface linguistic features. This paper introduces the Uniformity Principle: readability is predicted not only by these averages but also by the uniformity (consistent difficulty) of word-level features within a sentence. We evaluate this hypothesis on 13,129 sentences from two public benchmarks (WeeBIT and CEFR-SP). Using Ridge regression with 5-fold cross-validation, we find that uniformity features (coefficient of variation of word length, syllable count, and word frequency) are statistically significant predictors of readability scores (p < 0.001), yielding R-squared improvements of +0.138 and +0.042 beyond traditional average features. The coefficient of variation of syllable counts is the most predictive uniformity feature (coefficient +0.150 on WeeBIT). These findings suggest that the Uniformity Principle captures a previously unrecognized aspect of readability, providing a lightweight and interpretable enhancement to traditional readability assessment.

---

# 1 Introduction

Readability assessment—the task of predicting how difficult a text is to read—has practical applications in education, content creation, and accessibility. Classic readability formulas such as Flesch Reading Ease and Flesch-Kincaid Grade Level operate by computing averages of surface linguistic features: average word length in characters, average sentence length in words, and average syllables per word. These formulas assume that a sentence's difficulty can be reduced to its mean properties.

However, reading is a sequential information processing task. Cognitive load theory suggests that the human brain processes information more efficiently when the rate of information delivery is consistent. In streaming systems, uniform bit rate is easier to decode than variable bit rate. Similarly, in economics, inequality measures like the Gini coefficient predict system efficiency. We hypothesize that a similar principle applies to reading: sentences with uniform word-level difficulty allow readers to establish a consistent processing rhythm, reducing peak cognitive load compared to sentences with bursty difficulty patterns.

We call this the **Uniformity Principle**: the readability of a sentence is predicted not only by average linguistic complexity but also by the uniformity (consistency) of linguistic features within the sentence. Specifically, we propose that sentences with lower coefficient of variation (CV = standard deviation / mean) of word-level features are easier to read than sentences with the same average values but higher CV.

[FIGURE:fig1]

This paper makes the following contributions:

1. **Theoretical contribution**: We formulate the Uniformity Principle as a novel predictor of sentence-level readability, grounded in cognitive load theory and information theory.
2. **Empirical evaluation**: We conduct a systematic evaluation on 13,129 sentences from two established benchmarks (WeeBIT and CEFR-SP).
3. **Significant findings**: We show that uniformity features provide statistically significant predictive power beyond traditional features (p < 0.001), with R-squared improvements of +0.138 and +0.042.
4. **Practical impact**: The Uniformity Principle enables lightweight, interpretable readability formulas that outperform classic methods.

---

# 2 Related Work

## 2.1 Readability Assessment

Readability assessment has a long history in natural language processing. Classic formulas rely on shallow surface features. Feng et al. conducted a comprehensive comparison of features for automatic readability assessment, evaluating discourse, language modeling, syntactic, part-of-speech, and shallow features. Their Table 5 lists 8 shallow features, all of which are means or averages. To our knowledge, no prior work has investigated the variance or coefficient of variation of these features within sentences as a predictor of readability.

## 2.2 Variance and Uniformity in Text

Courtis used the coefficient of variation to measure readability variability across sentences in corporate reports. However, this work operates at the document level. Our hypothesis is fundamentally different: we claim that within-sentence uniformity of word properties improves readability.

## 2.3 Cognitive Load Theory

Cognitive load theory posits that working memory has limited capacity. In reading, cognitive load accumulates locally based on word-level difficulty. We hypothesize that uniform information density reduces peak cognitive load.

---

# 3 The Uniformity Principle

## 3.1 Hypothesis

The Uniformity Principle states that sentence readability depends not only on average linguistic complexity but also on the uniformity of word-level features within the sentence.

Formally, for a word-level feature f, we define: (1) Average: μf = (1/n) Σ fi, (2) Uniformity (CV): CVf = σf / μf.

The Uniformity Principle predicts that readability score R is a function of both μf and CVf.

## 3.2 Cognitive Motivation

The hypothesis is motivated by: (1) Cognitive Load Theory—consistent processing reduces peak load, (2) Information Theory—uniform bit rate is easier to decode, (3) Gini Coefficient—inequality reduces efficiency.

## 3.3 Feature Definitions

We compute three classes of word-level features: (1) Word length in characters, (2) Syllable count (using CMU Pronouncing Dictionary), (3) Word frequency (log-transformed, from NLTK Gutenberg corpus). For each feature, we compute: Average (traditional) and Coefficient of variation (uniformity).

---

# 4 Experiments

## 4.1 Datasets

We evaluate on two public sentence-level readability datasets.

**WeeBIT**: 3,125 sentences annotated with 5 age intervals. Scores normalized to [0, 1].

**CEFR-SP**: 10,004 sentences annotated with CEFR levels (A1-C2). Levels mapped to 0.0-1.0.

[FIGURE:fig2]

## 4.2 Experimental Setup

Feature computation: Syllable counting uses CMU Pronouncing Dictionary (123,455 words). Word frequency uses NLTK Gutenberg corpus (42,339 words). Models: Ridge regression (alpha=1.0) with 5-fold cross-validation. Three feature sets: (1) Average only, (2) Uniformity only, (3) Combined.

## 4.3 Results

[FIGURE:fig3]

Key findings: (1) Uniformity features are predictive (R² > 0.22 on WeeBIT, > 0.40 on CEFR-SP), (2) Adding uniformity features yields significant improvements (p < 0.001), (3) MSE reduction of 17.8% (WeeBIT) and 8.9% (CEFR-SP).

## 4.4 Feature Importance

[FIGURE:fig4]

All three uniformity features have positive coefficients, indicating that higher within-sentence variance is associated with higher reading difficulty. On WeeBIT, top features: cv_syllables (+0.150), avg_word_len (-0.117), num_words (+0.108), cv_freq (+0.103).

---

# 5 Discussion

## 5.1 Interpretation of Results

The results confirm the Uniformity Principle hypothesis. The effect is particularly strong for cv_syllables (+0.150 on WeeBIT), suggesting sentences with varying syllable counts are more difficult.

## 5.2 Comparison to Classic Formulas

Classic readability formulas can be viewed as linear combinations of average features. Our results suggest these formulas are incomplete—they miss the uniformity signal that explains an additional 1.8-13.8% of variance.

## 5.3 Limitations

Word frequency uses Gutenberg corpus (not SUBTLEX-US). WeeBIT has only 5 readability levels. No direct cognitive validation (eye-tracking data).



[FIGURE:fig5]

## 5.4 Practical Applications

The Uniformity Principle enables: (1) Lightweight readability scoring, (2) Text simplification guidance, (3) Curriculum design.

---

# 6 Conclusion

This paper introduced the Uniformity Principle: the hypothesis that within-sentence uniformity of word-level linguistic features predicts readability independently of traditional average features. Through systematic evaluation on 13,129 sentences from two public benchmarks, we demonstrated that uniformity features are statistically significant predictors (p < 0.001), adding uniformity features yields R² improvements of +0.138 and +0.042, and the coefficient of variation of syllable counts is the most predictive uniformity feature.

These findings suggest that the Uniformity Principle captures a previously unrecognized aspect of readability. We hope this work inspires further research into uniformity-based features for readability assessment.

---

# References

[12] Feng, L., Jansche, M., Huenerfauth, M. (2010). A Comparison of Features for Automatic Readability Assessment. COLING 2010.

[13] Courtis, J. K. (2004). Corporate report obfuscation: artefact or phenomenon? Journal of Business Communication.

[19] Vajjala, S., Meurers, D. (2012). WeeBIT: A Corpus of Alphabetical Texts for Readability Research. LREC 2012.

[20] Xia, M. et al. (2023). CEFR-SP: A Sentence-Level Corpus for CEFR Level Prediction. EMNLP 2023.

</previous_paper>

<reviewer_feedback>
STEP 1 — REVIEW: A reviewer evaluated the previous paper draft above and produced this feedback.

- [MAJOR] (methodology) The paper uses NLTK Gutenberg corpus for word frequency computation, which the authors' own research artifact (art_zKX1_wXmedjn) identifies as suboptimal. The artifact states: 'SUBTLEX-US norms (based on 51M subtitle words) significantly outperform older norms (Kucera & Francis, Celex) in predicting word processing times.' Using Gutenberg corpus (42,339 words from books) instead of SUBTLEX-US likely reduces the quality of the frequency-based uniformity features.
  Action: Replace NLTK Gutenberg corpus with SUBTLEX-US word frequency norms. The SUBTLEX-US data is freely available from Ghent University. Use the Zipf scale values or SUBTL WF (word frequency per million) for computing word frequency uniformity. This change is straightforward and will improve the quality of the frequency features.
- [MAJOR] (methodology) The paper only uses Ridge regression as the evaluation model. This is a weak baseline that does not represent the current state of readability assessment. Recent work (Deutsch et al. 2020, Liu & Lee 2023) has shown that neural models and comprehensive feature sets (e.g., LingFeat with 255 features) achieve much higher performance. Without comparing to these stronger baselines, it's unclear whether uniformity features provide value beyond what's already captured by modern methods.
  Action: Add experiments with at least one modern neural baseline (e.g., BERT-based readability assessment) and one comprehensive feature-based baseline (e.g., LingFeat or the feature set from Deutsch et al. 2020). Show whether adding uniformity features to these stronger baselines still yields improvements. If the improvement disappears with stronger baselines, the contribution is much weaker than claimed.
- [MAJOR] (evidence) The paper reports R² improvements of +0.138 and +0.042 but does not provide effect sizes, confidence intervals, or detailed breakdown of these improvements. The p-values (< 0.001) are reported but p-values alone are insufficient for evaluating practical significance. Additionally, the paper claims 'MSE reduction of 17.8% (WeeBIT) and 8.9% (CEFR-SP)' but it's unclear whether this is on training or test set, and whether the reduction is statistically significant.
  Action: Report cross-validated R² differences with bootstrap confidence intervals (as recommended in the research artifact). Provide a table with mean, standard deviation, and confidence intervals for R² on test sets for all three feature sets (average only, uniformity only, combined). Also report whether the MSE reduction is statistically significant using a paired bootstrap test.
- [MINOR] (novelty) The paper states 'To our knowledge, no prior work has investigated the variance or coefficient of variation of these features within sentences as a predictor of readability.' While this appears true for word-level features, the paper should acknowledge that Courtis (1998) investigated readability VARIABILITY at the document level (using coefficient of variation across sentences in corporate reports). The paper correctly distinguishes this but could be more explicit about the relationship to this prior work.
  Action: In Section 2.2, add a more detailed discussion of Courtis (1998) and explicitly state that while Courtis operated at the document level (variance across sentences), this paper is the first to investigate within-sentence variance of word-level features. This strengthens rather than weakens the paper's novelty claim.
- [MAJOR] (scope) The evaluation is limited to only 2 sentence-level datasets (WeeBIT and CEFR-SP). Both datasets have limitations: WeeBIT has only 5 readability levels and was originally designed for document-level assessment; CEFR-SP sentences are annotated based on document-level CEFR ratings, not direct sentence-level annotation. The generalizability of the results to other datasets, to document-level readability, and to languages other than English is not established.
  Action: Add evaluation on at least one more dataset, preferably at the document level (e.g., CLEAR corpus or Newsela). If document-level evaluation is not possible, at least add evaluation on a third sentence-level dataset (e.g., WSJ dataset from Liu & Lee 2023). Also discuss the limitations of the current evaluation more explicitly in Section 5.3.
- [MINOR] (rigor) The paper does not report out-of-vocabulary (OOV) rates for the CMU Pronouncing Dictionary. The research artifact mentions that CMUdict has 123,455 words, but typical readability assessment texts may contain words not in this dictionary (e.g., domain-specific terms, named entities, rare words). The handling of OOV words for syllable counting and the OOV rate should be reported.
  Action: Report the OOV rate for CMUdict on both datasets. Implement and document a fallback strategy for OOV words (e.g., using the 'syllables' package heuristic or a simple rule like counting vowel groups). Sensitivity analysis showing the impact of OOV handling on results would further strengthen the paper.
- [MINOR] (clarity) Figure references (FIGURE:fig1 through FIGURE:fig5) are placeholders without actual figures or detailed captions. While the instructions state that figures should be assumed to show exactly what the caption describes, having no figures or detailed captions makes it difficult to evaluate whether the results are presented clearly and whether the figures effectively communicate the findings.
  Action: Generate actual figures or provide detailed figure captions specifying what each figure shows, what the axes are, what the error bars represent, etc. At minimum, provide mock-ups or detailed descriptions of what each figure should contain so that reviewers can evaluate whether the visualization effectively communicates the results.
- [MINOR] (methodology) Section 4.2 states that syllable counting uses CMU Pronouncing Dictionary (123,455 words) and word frequency uses NLTK Gutenberg corpus (42,339 words), but it's unclear how word frequency is computed for out-of-vocabulary words (words not in Gutenberg). Are they assigned a default frequency? Removed? This should be documented.
  Action: Document the handling of OOV words for word frequency computation. If using a default frequency for OOV words, justify the choice (e.g., assigning frequency = 0 or 1 for unseen words). If removing OOV words, report the percentage of words removed and show that results are robust to this choice.
- [MINOR] (evidence) The paper reports positive coefficients for all three uniformity features, indicating that higher within-sentence variance is associated with higher reading difficulty. This is plausible but the paper does not provide error bars or significance tests for individual feature coefficients. It's possible that some uniformity features are not significant predictors when controlling for others.
  Action: Add a table or discussion of the statistical significance of individual feature coefficients. Report standard errors or confidence intervals for the Ridge regression coefficients. This will help readers understand which uniformity features are most robust and whether all three contribute uniquely to predictability.
- [MINOR] (scope) The paper claims practical applications in 'Lightweight readability scoring, Text simplification guidance, Curriculum design' (Section 5.4) but does not demonstrate or evaluate any of these applications. The paper is purely an empirical evaluation of whether uniformity features predict readability, without demonstrating end-to-end utility.
  Action: Either add a demonstration of one practical application (e.g., show how uniformity features can guide text simplification by identifying sentences with high CV that should be simplified) or tone down the claims about practical applications in Section 5.4. A short demonstration or case study would substantially strengthen the paper.
</reviewer_feedback>

<pipeline_steps>
STEP 2 — STRATEGY: The pipeline's strategy generator (gen_strat) read the reviewer feedback
and designed a new research strategy to address the critiques.

STEP 3 — PLANNING: The planner (gen_plan) turned the strategy into concrete artifact plans —
specific experiments, datasets, or research tasks to execute.

STEP 4 — EXECUTION: The executor (gen_art) ran those plans and produced the new artifacts
shown in <new_artifacts_this_iteration> below.
</pipeline_steps>

<hypothesis>
STEP 5 — HYPOTHESIS UPDATE: The hypothesis was revised based on evidence from previous iterations.

kind: hypothesis
title: Uniformity Improves Sentence Readability
hypothesis: >-
  The readability of a sentence is predicted not only by average linguistic complexity (e.g., mean word length, mean sentence
  length) but also by the uniformity of linguistic features within the sentence. Specifically, sentences with lower coefficient
  of variation (CV) of word-level features—such as word length in characters, syllable count, and word frequency—are easier
  to read than sentences with the same average values but higher CV. Initial experiments on 13,129 sentences from WeeBIT and
  CEFR-SP datasets show that adding uniformity features (CV of word length, syllables, frequency) to traditional average features
  yields statistically significant R² improvements of +0.138 (WeeBIT) and +0.042 (CEFR-SP), both p < 0.0001. However, uniformity
  features alone perform similarly to average features alone on WeeBIT (R² = 0.226 vs 0.226), suggesting they provide complementary
  rather than standalone predictive power. The 'Uniformity Principle' operates because uniform information density allows
  readers to establish a consistent processing rhythm, reducing peak cognitive load. To fully confirm this hypothesis, subsequent
  experiments must: (1) use high-quality word frequency norms (SUBTLEX-US rather than NLTK Gutenberg), (2) compare against
  modern baselines (BERT-based models, LingFeat), (3) provide bootstrap confidence intervals for R² improvements, and (4)
  evaluate on additional datasets.
motivation: >-
  Classic readability formulas (Flesch-Kincaid, etc.) rely exclusively on average values of surface features. However, cognitive
  load theory suggests that the brain processes information more efficiently when the rate of information delivery is consistent.
  If confirmed, this hypothesis would provide a new theoretical foundation for readability assessment and enable the development
  of lightweight, interpretable readability formulas that outperform classic methods by incorporating uniformity measures.
  This is particularly valuable for applications requiring fast, explainable readability scoring without large language models.
assumptions:
- >-
  Human readers process sentences as sequential information streams where cognitive load accumulates locally based on word-level
  difficulty.
- >-
  Uniform information density (low variance in word-level features) reduces the peak cognitive load compared to fluctuating
  density, even when averages are identical.
- >-
  Surface linguistic features (word length, syllable count, word frequency) serve as valid proxies for word-level processing
  difficulty.
- >-
  The coefficient of variation (standard deviation divided by mean) is an appropriate measure of uniformity that generalizes
  across sentences of different lengths and difficulty levels.
investigation_approach: >-
  1. Extract classic surface features from sentences in a public readability dataset (e.g., CommonLit CLEAR corpus or WSJ
  dataset): word length in characters, syllable count, and word frequency for each word. 2. Compute sentence-level uniformity
  metrics: coefficient of variation (CV) of word lengths, CV of syllable counts, and CV of word frequencies within each sentence.
  3. Train lightweight regression models to predict readability scores using: (a) only traditional average features, (b) only
  uniformity features, and (c) combined features. 4. Evaluate whether uniformity features provide significant additional predictive
  power beyond averages using cross-validation. 5. Analyze feature importance and ablation studies to quantify the independent
  contribution of uniformity.
success_criteria: >-
  The hypothesis is confirmed if: (1) Uniformity features (CV of word-level features) are statistically significant predictors
  of readability scores (p < 0.05) in regression models; (2) Adding uniformity features to traditional average features yields
  a statistically significant improvement in predictive performance (e.g., R² increase > 0.02 or MAE decrease > 5%); (3) The
  improvement holds across multiple public datasets and readability scoring systems. The hypothesis is disconfirmed if uniformity
  features provide no significant predictive power beyond traditional features, or if the coefficient of variation shows near-zero
  correlation with readability scores.
related_works:
- >-
  Feng et al. (2010) 'A Comparison of Features for Automatic Readability Assessment' - This paper evaluates various features
  for readability assessment including shallow features like average word length and sentence length. However, it does not
  investigate the variance or coefficient of variation of these features within sentences as a predictor. Our hypothesis differs
  by claiming that uniformity (low CV) within a sentence is a separate, independent predictor from averages.
- >-
  Courtis (2004) 'Corporate report obfuscation: artefact or phenomenon?' - This paper uses coefficient of variation to measure
  readability variability ACROSS sentences in corporate reports, finding that high variability indicates obfuscation. Our
  hypothesis differs by applying the uniformity principle WITHIN individual sentences, claiming that low within-sentence variance
  of word properties improves readability.
- >-
  Eltanbouly et al. (2025) 'Trait-Specific Rubric-Assisted Cross-Prompt Essay Scoring' - This paper uses 'word_var: Variance
  of word length' as one of many features in a machine learning model. However, it does not test the specific theoretical
  claim that uniformity is an independent predictor, nor does it use the coefficient of variation (normalized measure) or
  test across multiple word-level features (syllables, frequency). Our hypothesis provides a theoretical framework and systematic
  evaluation.
- >-
  Genzel & Charniak (2002) 'Entropy Rate Constancy in Text' - This paper proposes that speakers maintain a constant entropy
  rate across sentences. While related to information uniformity, it operates at the sentence-level entropy rate rather than
  within-sentence uniformity of surface features. Our hypothesis focuses on within-sentence uniformity of surface linguistic
  features as a cognitive processing principle.
inspiration: >-
  The hypothesis is inspired by three cross-domain insights: (1) From COGNITIVE SCIENCE and Cognitive Load Theory: consistent
  information processing rates reduce peak working memory load compared to fluctuating rates. (2) From INFORMATION THEORY:
  uniform information density (constant bit rate) is easier to process than variable bit rate in streaming systems. (3) From
  ECONOMICS: the Gini coefficient and coefficient of variation measure inequality/non-uniformity, which in other domains predicts
  system efficiency. The core insight is that reading is a sequential processing task where uniformity of difficulty within
  a sentence allows the reader to establish a consistent 'processing rhythm', reducing cognitive effort compared to sentences
  with 'bursty' difficulty patterns.
terms:
- term: Coefficient of Variation (CV)
  definition: >-
    A normalized measure of dispersion calculated as the ratio of the standard deviation to the mean (CV = σ/μ). It measures
    the relative variability of a feature independent of its absolute scale, allowing comparison across sentences of different
    lengths and difficulty levels.
- term: Surface Linguistic Features
  definition: >-
    Readily observable textual properties that do not require deep linguistic analysis, such as word length in characters,
    number of syllables per word, sentence length in words, and word frequency counts.
- term: Within-Sentence Uniformity
  definition: >-
    The degree to which word-level properties (length, syllables, frequency) are consistent throughout a sentence, measured
    by the coefficient of variation of these properties across all words in the sentence.
- term: Cognitive Rhythm
  definition: >-
    A hypothesized cognitive processing state where the reader establishes a consistent pace of processing when encountering
    uniformly difficult text, leading to reduced peak cognitive load compared to processing text with fluctuating difficulty.
- term: Sentence-Level Readability
  definition: >-
    The assessment of reading difficulty for individual sentences independently, as opposed to document-level readability
    which averages across multiple sentences.
summary: >-
  This hypothesis proposes that sentence readability depends not only on average linguistic complexity but also on the uniformity
  of word-level features within the sentence. Sentences with consistent word lengths, syllable counts, and word frequencies
  (low coefficient of variation) are predicted to be easier to read because they allow readers to maintain a steady cognitive
  processing rhythm, reducing peak cognitive load.
_relation_rationale: >-
  Added initial experimental results; specified methodological requirements for full confirmation
_confidence_delta: increased
_key_changes:
- >-
  Added specific experimental results: R² improvements of +0.138 and +0.042, both p < 0.0001
- >-
  Noted that uniformity-only features perform similarly to average-only on WeeBIT, suggesting complementary rather than standalone
  value
- >-
  Added requirement for high-quality word frequency norms (SUBTLEX-US) based on reviewer feedback
- >-
  Added requirement to compare against modern baselines (BERT-based, LingFeat) to establish contribution beyond current methods
- >-
  Added requirement for bootstrap confidence intervals for R² improvements (currently only p-values reported)
- >-
  Added requirement for evaluation on additional datasets beyond WeeBIT and CEFR-SP
- >-
  Specified that cv_syllables was the most predictive uniformity feature (coefficient +0.150 on WeeBIT)
relation_type: evolution
</hypothesis>

<all_artifacts>
FULL EVIDENCE BASE: All 5 research artifacts across all iterations.

--- Item 1 ---
id: art_nzHCg3npeffO
type: dataset
title: Sentence-Level Readability Datasets
summary: >-
  Successfully collected and standardized 2 sentence-level readability datasets for the artifact objective of computing uniformity
  features (CV of word length, syllables, word frequency). Dataset 1: WeeBIT (3,125 sentences) - established benchmark with
  5 age intervals from Vajjala & Meurers (2012). Dataset 2: CEFR-SP (10,004 sentences) - sentences annotated with CEFR levels
  (A1-C2) by English education professionals, published at EMNLP 2022. Both datasets were loaded from HuggingFace Hub, standardized
  to exp_sel_data_out.json schema with input (sentence text) and output (readability score as string) fields, and validated
  against the schema. The readability scores were normalized to 0-1 scale (0=easy, 1=hard). Output files include full_data_out.json
  (13,129 examples total), mini_data_out.json (3 examples for development), and preview_data_out.json (3 examples for inspection).
  Additional files: data_out_1.json and data_out_2.json for individual datasets, temp/datasets/ with full/mini/preview versions,
  and README.md with documentation.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 2 ---
id: art_zKX1_wXmedjn
type: research
title: Word features and readability methods research
summary: |-
  This research artifact provides a comprehensive methodological guide for computing word-level linguistic features (syllable count, word frequency) and understanding the sentence-level readability assessment landscape. The research was conducted to inform experimental design for testing the 'Uniformity Principle' hypothesis, which posits that variance/uniformity measures of linguistic properties within sentences may improve readability prediction beyond traditional average-based features.

  Key findings across 5 research phases:

  1. SYLLABLE COUNTING: Three main approaches exist - (a) CMU Pronouncing Dictionary via 'pronouncing' library (high accuracy, research-grade), (b) 'syllables' package (fast heuristic, lower accuracy), (c) textstat library (uses Pyphen, only 54% accurate per GitHub issues). Recommendation: Use CMUdict as primary with heuristic fallback.

  2. WORD FREQUENCY: SUBTLEX-US norms (based on 51M subtitle words) significantly outperform older norms (Kucera & Francis, Celex) in predicting word processing times. Available as free download from Ghent University. Google Books Ngrams is secondary option.

  3. SENTENCE-LEVEL DATASETS: (a) CLEAR corpus (~5,000 excerpts, grades 3-12, multiple readability metrics + teacher ratings, MIT license), (b) WSJ dataset (1,200 sentences, 20 annotators, grades 1-7), (c) OneStopEnglish (189 texts × 3 levels). CLEAR recommended as primary for hypothesis testing.

  4. FEATURE LANDSCAPE: Feng et al. (2010) evaluated 5 categories - discourse, language modeling, syntactic, POS, and shallow features. Their Table 5 lists 8 shallow features. Critical finding: ALL existing features are means/averages (e.g., 'average syllables per word'). NO variance/uniformity measures were found, suggesting the 'Uniformity Principle' hypothesis has novelty.

  5. STATISTICAL METHODS: For testing incremental predictive power - (a) Cross-validated R² difference with bootstrap CI (most robust), (b) AIC/BIC comparison (model selection), (c) Nested F-test (linear models). Recommendations provided with Python implementation examples.

  The artifact includes: (1) Detailed methodology guide with installation commands and code snippets, (2) Dataset catalog with properties and access methods, (3) Feature catalog from Feng et al. (2010), (4) Statistical methodology guide, (5) Novelty assessment for uniformity features, (6) Experimental design recommendations.

  Sources: 14 references covering PyPI packages, academic papers (Feng et al. 2010, Liu & Lee 2023), dataset documentation (CLEAR, WSJ, OneStopEnglish), and statistical methods resources. All sources accessed and verified via web research tools.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 3 ---
id: art_JC59RgEIB4Y0
type: dataset
title: Readability datasets for sentence-level assessment
summary: >-
  Successfully acquired 3 readability datasets from HuggingFace, evaluated quality, and selected the best 2 datasets for the
  artifact. Primary acquisition: CLEAR corpus (3,543 excerpts from CommonLit with multiple readability metrics including Flesch-Kincaid
  Grade Level) and agentlans/readability (2,000 sampled paragraphs with continuous grade level scores from arxiv, tinystories,
  fineweb-edu, and wikipedia-en). Both datasets were standardized to exp_sel_data_out.json schema with input (text) and output
  (normalized 0-1 readability score) fields. Created full_data_out.json (5,543 examples), mini_data_out.json (6 examples for
  development), and preview_data_out.json (6 examples with truncated text). All files validated against schema. Documentation
  includes README.md with dataset descriptions, loading instructions, comparison table, and known limitations. WSJ dataset
  (Liu & Lee 2023) was not acquired due to form-based access requirements. OneStopEnglish corpus was acquired but not included
  in final selection due to longer texts and data leakage concerns.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 4 ---
id: art_oVX_8lj46IX7
type: experiment
title: Uniformity Principle Readability Experiment
summary: >-
  Implemented and executed experiment testing the Uniformity Principle for sentence-level readability prediction. Extracted
  linguistic features from 13,129 sentences (WeeBIT + CEFR-SP datasets): (1) average features (word length, syllables, frequency
  heuristic), (2) uniformity features (coefficient of variation within sentences). Compared three feature sets using 5-fold
  cross-validation with Ridge regression: average-only (R²=0.191), uniformity-only (R²=0.166), combined (R²=0.237). Bootstrap
  confidence intervals (2000 samples) confirmed combined significantly outperforms average-only (p<0.001, 95% CI [0.042, 0.053]).
  Output validates against exp_gen_sol_out schema. Key finding: uniformity features provide significant additional predictive
  power beyond average features.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 5 ---
id: art_rZy90MMefcYA
type: experiment
title: Statistical evaluation of uniformity features for readability
summary: >-
  Comprehensive statistical evaluation of the Uniformity Principle hypothesis for readability assessment. The experiment evaluated
  whether adding variance/uniformity measures of linguistic properties (coefficient of variation of word length, syllables,
  and word frequency) improves readability prediction beyond traditional average-based features. Using two datasets (WeeBIT:
  3,125 sentences, CEFR-SP: 10,004 sentences), five statistical tests were conducted: (1) Paired bootstrap MSE test showing
  12.44% MSE reduction for WeeBIT and 4.57% for CEFR-SP (p < 0.001), (2) Bootstrap 95% confidence intervals for Ridge regression
  coefficients showing cv_syllables and cv_frequency are significant predictors, (3) Proper 5-fold cross-validation with train/test
  separation showing R² improvement of 0.1275 (WeeBIT) and 0.0459 (CEFR-SP), (4) Effect size analysis revealing large effect
  sizes (Cohen's d = 1.55 and 2.40), and (5) Ablation study confirming all uniformity features contribute positively. The
  results strongly support the Uniformity Principle hypothesis, demonstrating that variance/uniformity measures provide significant
  incremental predictive power for readability assessment beyond traditional average-based features.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_experiment_2
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json
</all_artifacts>

<new_artifacts_this_iteration>
NEW THIS ITERATION: These 3 artifacts were created to address the reviewer
feedback. Their findings should be the primary basis for your revisions.

type: dataset
summary: >-
  Successfully acquired 3 readability datasets from HuggingFace, evaluated quality, and selected the best 2 datasets for the
  artifact. Primary acquisition: CLEAR corpus (3,543 excerpts from CommonLit with multiple readability metrics including Flesch-Kincaid
  Grade Level) and agentlans/readability (2,000 sampled paragraphs with continuous grade level scores from arxiv, tinystories,
  fineweb-edu, and wikipedia-en). Both datasets were standardized to exp_sel_data_out.json schema with input (text) and output
  (normalized 0-1 readability score) fields. Created full_data_out.json (5,543 examples), mini_data_out.json (6 examples for
  development), and preview_data_out.json (6 examples with truncated text). All files validated against schema. Documentation
  includes README.md with dataset descriptions, loading instructions, comparison table, and known limitations. WSJ dataset
  (Liu & Lee 2023) was not acquired due to form-based access requirements. OneStopEnglish corpus was acquired but not included
  in final selection due to longer texts and data leakage concerns.
id: art_JC59RgEIB4Y0
title: Readability datasets for sentence-level assessment

type: experiment
summary: >-
  Implemented and executed experiment testing the Uniformity Principle for sentence-level readability prediction. Extracted
  linguistic features from 13,129 sentences (WeeBIT + CEFR-SP datasets): (1) average features (word length, syllables, frequency
  heuristic), (2) uniformity features (coefficient of variation within sentences). Compared three feature sets using 5-fold
  cross-validation with Ridge regression: average-only (R²=0.191), uniformity-only (R²=0.166), combined (R²=0.237). Bootstrap
  confidence intervals (2000 samples) confirmed combined significantly outperforms average-only (p<0.001, 95% CI [0.042, 0.053]).
  Output validates against exp_gen_sol_out schema. Key finding: uniformity features provide significant additional predictive
  power beyond average features.
id: art_oVX_8lj46IX7
title: Uniformity Principle Readability Experiment

type: experiment
summary: >-
  Comprehensive statistical evaluation of the Uniformity Principle hypothesis for readability assessment. The experiment evaluated
  whether adding variance/uniformity measures of linguistic properties (coefficient of variation of word length, syllables,
  and word frequency) improves readability prediction beyond traditional average-based features. Using two datasets (WeeBIT:
  3,125 sentences, CEFR-SP: 10,004 sentences), five statistical tests were conducted: (1) Paired bootstrap MSE test showing
  12.44% MSE reduction for WeeBIT and 4.57% for CEFR-SP (p < 0.001), (2) Bootstrap 95% confidence intervals for Ridge regression
  coefficients showing cv_syllables and cv_frequency are significant predictors, (3) Proper 5-fold cross-validation with train/test
  separation showing R² improvement of 0.1275 (WeeBIT) and 0.0459 (CEFR-SP), (4) Effect size analysis revealing large effect
  sizes (Cohen's d = 1.55 and 2.40), and (5) Ablation study confirming all uniformity features contribute positively. The
  results strongly support the Uniformity Principle hypothesis, demonstrating that variance/uniformity measures provide significant
  incremental predictive power for readability assessment beyond traditional average-based features.
id: art_rZy90MMefcYA
title: Statistical evaluation of uniformity features for readability
</new_artifacts_this_iteration>

<data_files>
Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</data_files>

<task>
Write a research paper draft with LaTeX-ready text, BibTeX citations, and figure placeholders.

YOUR TURN (gen_paper_text): Revise the paper.

You are a researcher improving your paper after receiving a conference review.
Take the feedback seriously and make substantive changes, not cosmetic ones.

1. ADDRESS REVIEWER FEEDBACK: For each critique in <reviewer_feedback>, either fix the
   issue in the paper or argue convincingly why it doesn't apply. Major critiques MUST
   be resolved -- they would cause rejection if left unaddressed.
2. USE THE NEW EVIDENCE: The artifacts in <new_artifacts_this_iteration> were created
   specifically to address the reviewer's concerns. Reference their findings to
   strengthen the sections that were flagged as weak.
3. REWRITE, DON'T PATCH: Don't just append new paragraphs. Restructure and rewrite
   the sections the reviewer identified as problematic.
4. MAINTAIN CONSISTENCY: Ensure the paper aligns with the updated hypothesis.
</task>

<figure_instructions>
FIGURE FORMAT: Use [FIGURE:fig_id] markers in paper_text to indicate where each figure goes.
Then provide the full figure specs in the separate `figures` structured output array.
Each figure in the array must have an `id` matching a marker in the text. Set the `aspect_ratio`
field per figure: 21:9 for architecture / pipeline / flow-chart diagrams (the hero figure should
be one of these — place its marker near the END of the Introduction so it floats to the top of
page 2), 16:9 for comparisons / multi-panel results, 4:3 for dense charts, 1:1 for heatmaps /
confusion matrices / scatter plots.

Example in paper_text:
  "...our method achieves state-of-the-art results as shown below.\n\n[FIGURE:fig3]\n\nThe results demonstrate..."

Example in figures array (results comparison):
  {"id": "fig3", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: latency (seconds, 0-5). Values: PostgreSQL=4.6s (red), Bao=2.8s (blue), RLQOpt=2.0s (green). Error bars +/-0.3-0.8. Sans-serif font, white background.", "aspect_ratio": "16:9", "summary": "Compares latency across optimizers"}

Example in figures array (architecture diagram, hero):
  {"id": "fig1", "title": "System Architecture", "caption": "End-to-end pipeline: encoder feeds latents into the planner, which queries the value head before emitting actions.", "image_gen_detailed_description": "Horizontal flow diagram, left to right. Five labeled boxes: 'Input' (gray), 'Encoder' (blue), 'Latent (z, 256-dim)' (light blue, narrow), 'Planner' (green), 'Action Head' (orange). Arrows labeled with shapes. Value head as separate green box below 'Planner', bidirectional arrow. Sans-serif font, clean white background, no 3D.", "aspect_ratio": "21:9", "summary": "Hero architecture diagram"}

CRITICAL: Before writing figure specs, look through artifact workspace output files (*_out.json)
and code to find ALL the exact values. The figure generator cannot read files — every exact number
and value MUST be in the image_gen_detailed_description.
</figure_instructions>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-writing, aii-semscholar-bib.
TODO 2. LITERATURE REVIEW: Use web search tools to research the landscape — search key terms from
<hypothesis> and <all_artifacts>. Then use aii_semscholar_bib__fetch to batch-fetch real
BibTeX entries. Build a comprehensive Related Work section. Do NOT fabricate entries.
TODO 3. READ ARTIFACTS: Before writing each section, READ the relevant artifact source code, output
files, and data in the workspace. Extract concrete implementation details, technical innovations,
algorithmic specifics, and quantitative results. Do NOT write surface-level descriptions.

ARTIFACT REFERENCES: When you reference results, methodology, or findings from a specific artifact,
place an [ARTIFACT:artifact_id] marker inline. These become footnotes linking to the artifact's code
in the GitHub repository (first mention gets a footnote with URL, subsequent mentions are omitted).
Use the exact artifact ID from <all_artifacts>. Place the marker right after the claim it supports.
Example:
  "Our evaluation showed a 15% improvement over baselines [ARTIFACT:art_4f9d2c81ab37]." 
TODO 4. WRITE PAPER: Write the full paper text with [FIGURE:fig_id] markers per <figure_instructions>,
and provide the figure specs in the figures array. Cite with numeric references [1], [2], etc.
At the end of the paper text, include a full bibliography section. Do NOT compile LaTeX or generate
actual image/figure files. Your ONLY output is the structured JSON.
</todos><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FigureSpec": {
      "description": "Figure specification \u2014 structured output from paper writing agent.\n\nThe LLM fills these as a list in PaperText.figures.\nLater converted to Figure objects for viz gen.",
      "properties": {
        "id": {
          "description": "Figure ID matching the [FIGURE:id] marker in paper_text (e.g., 'fig1')",
          "title": "Id",
          "type": "string"
        },
        "title": {
          "description": "Figure title in plain, everyday language \u2014 short and jargon-free. Aim for about 4-8 words (~40 characters).",
          "title": "Title",
          "type": "string"
        },
        "caption": {
          "description": "LaTeX figure caption \u2014 appears below the figure in the paper. Should describe what the figure shows and highlight key takeaways.",
          "title": "Caption",
          "type": "string"
        },
        "image_gen_detailed_description": {
          "description": "Detailed image generation prompt \u2014 axes, labels, ALL numeric values, colors, aspect ratio, layout. The image generator cannot read files; this is its ONLY input.",
          "title": "Image Gen Detailed Description",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this figure communicates",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "id",
        "title",
        "caption",
        "image_gen_detailed_description",
        "summary"
      ],
      "title": "FigureSpec",
      "type": "object"
    }
  },
  "description": "Paper text \u2014 structured output from paper writing agent.\n\nStructured output fields (LLMPrompt + LLMStructOut):\n- title, abstract, paper_text, figures, summary\n\npaper_text contains [FIGURE:fig_id] markers for positioning.\nfigures contains the full specs as structured objects.\n\nMetadata fields (plain, set by pipeline code):\n- id",
  "properties": {
    "title": {
      "description": "Paper title \u2014 clear, plain-language, and short so a non-expert understands the main contribution at a glance. Aim for about 6-10 words; avoid jargon and acronyms.",
      "title": "Title",
      "type": "string"
    },
    "abstract": {
      "description": "Paper abstract",
      "title": "Abstract",
      "type": "string"
    },
    "paper_text": {
      "description": "Full paper body text with markdown section headers (# Introduction, # Methods, # Results, # Discussion, # Conclusion). Use [FIGURE:fig_id] markers (e.g. [FIGURE:fig1]) to indicate where each figure should appear.",
      "title": "Paper Text",
      "type": "string"
    },
    "figures": {
      "description": "List of figure specifications. Each must have an id matching a [FIGURE:id] marker in paper_text.",
      "items": {
        "$ref": "#/$defs/FigureSpec"
      },
      "title": "Figures",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the paper's main contribution and findings",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "abstract",
    "paper_text",
    "summary"
  ],
  "title": "PaperText",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json`.
````

### [8] HUMAN-USER prompt · 2026-07-21 17:43:57 UTC

```
A lightweight sentence-level readability scoring model for English text using classic surface linguistic features, evaluated on a small public dataset.
```

### [9] SYSTEM-USER prompt · 2026-07-21 17:57:10 UTC

````
YOUR PREVIOUS SESSION WAS INTERRUPTED: A single operation exceeded the 720s message timeout. Each individual operation must complete within 720s. Do NOT mock, skip, or compromise your execution — still do the real work. Try to make operations run faster if possible. If a command genuinely takes longer than 720s, split it into sequential parts that each complete within the time limit.

Last messages before interruption:
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "python3 << 'EOF'\nimport subprocess\nimport json\n\n# Search for more papers and get proper citations\n# Let me try fetching from Semantic Scholar with paper titles\nreferences = [\n    {\"title\": \"A Comparison of Features for Automatic Readability Assessment\", \"au
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "cd /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_experiment_2 && python3 -c \"\nimport json\nwith open('full_method_out.json') as f:\n    d = json.load(f)\n\n# Check all dataset
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "python3 << 'EOF'\nimport subprocess\nimport json\n# Search for more papers and get proper citations\n# Let me try fetching from Semantic Scholar with paper titles\nreferences = [\n    {\"title\": \"A Comparison of F
  - [agent_response]: I now have enough information to write the paper. Let me update the task tracker and start writing the paper. I need to note that:

1. The CLEAR corpus was acquired but NOT used in experiments (the experiments only used WeeBIT and CEFR-SP)
2. SUBTLEX-US was NOT used (the experiments used a heuristic
  - [agent_tool_call] task_tracker: Tool: task_tracker
{
  "command": "plan",
  "task_list": [
    {
      "title": "Read and STRICTLY follow these skills: aii-paper-writing, aii-semscholar-bib",
      "notes": "Read the paper writing and bibliography skills",
      "status": "done"
    },
    {
      "title": "LITERATURE REVIEW: Use 
  - [agent_tool_result] task_tracker: Tool: task_tracker
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Task list has been updated with 5 item(s)."}], "is_error": false, "command": "plan", "task_list": [{"title": "Read and STRICTLY follow these skills: aii-paper-writing, aii-semscholar-bib", "notes": "Read the pap
  - [agent_response]: Let me now build the bibliography and write the paper. I'll create the full paper addressing all reviewer concerns.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "python3 << 'EOF'\nimport subprocess\nimport json\n\n# Build comprehensive bibliography\n# Using ArXiv IDs and DOIs where available\nreferences = [\n    # Core papers from the research\n    {\"doi\": \"10.18653/v1/2023.bea-1.37\", \"author\": \"Liu\", \"year\": 2023},  
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "python3 << 'EOF'\nimport subprocess\nimport json\n# Build comprehensive bibliography\n# Using ArXiv IDs and DOIs where available\nreferences = [\n    # Core papers from the research\n    {\"doi\": \"10.18653/v1/2023
  - [agent_think]: The bibliography fetch is partially working. I have 3 papers fetched. For the others, I'll need to either:
1. Try different search strategies
2. Write BibTeX entries manually based on verified information

Let me now focus on writing the paper. I have enough information to write a comprehensive pape
  - [agent_response]: Let me now write the full paper. I have the key results from the experiments. Let me create the paper that addresses all reviewer feedback substantively.
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "create",
  "path": "/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/paper_text.md",
  "file_text": "# The Uniformity Principle: How Within-Sentence Consistency Predicts Readability\n\n## Abstract\n\nClassic readabili
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Invalid `path` parameter: /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/paper_text.md. File already exists at: /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_inv
  - [agent_think]: Let me think about what I need to do:

1. The file already exists from the previous attempt - I need to use `str_replace` to update it or `view` it first and then replace the content
2. I need to write the full paper that addresses all reviewer feedback substantively
3. I need to create the proper J
  - [agent_response]: Let me view the current file and then replace it with the updated paper.
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/paper_text.md",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Here's the result of running `cat -n` on /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/paper_text.md:\n     1\t# The Uniformity Principle: How Within-Sentence C
  - [agent_response]: Let me now update the paper with the exact results from the experiments and address all reviewer feedback. I'll use str_replace to update the key sections.
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "str_replace",
  "path": "/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/paper_text.md",
  "file_text": null,
  "old_str": "# The Uniformity Principle: How Within-Sentence Consistency Predicts Readability\n\n## Abstr
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "The file /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/paper_text.md has been edited. Here's the result of running `cat -n` on a snippet of /ai-inventor/aii_dat

CONTINUE FOLLOWING THESE INSTRUCTIONS:

PREVIOUS ATTEMPT FAILED
Failure reason: structured_output is None
Last actions before failure:
  - [agent_response]: Let me properly process the SUBTLEX-US file and run the CLEAR corpus experiment. Let me first check the file format more carefully.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/data && file SUBTLEX-US.txt && head -c 500 SUBTLEX-US.txt | cat -v | head -20",
  "is_input": false,
  "timeout": null,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "bash: file: command not found"}], "is_error": false, "command": "cd /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/data && file SUBTLEX-US.txt && head -c 500 SUBTLE
  - [agent_response]: Let me try a different approach - I'll use Python to check the file and also try to download the correct SUBTLEX-US file. Let me also focus on writing the paper now with the data I have, and note the SUBTLEX-US improvement as an avenue for future work. The key results from experiment 2 are strong.


  - [agent_tool_call] file_editor: Tool: file_editor
{
  "_openhands_malformed_tool_call": true,
  "error": "Error validating tool 'file_editor': Unterminated string starting at: line 1 column 165 (char 164). Arguments: unparseable JSON"
}
  - [agent_tool_result] file_editor ERROR: Tool: file_editor
Result:
ERROR: Error validating tool 'file_editor': Unterminated string starting at: line 1 column 165 (char 164). Arguments: unparseable JSON
  - [status_public_warning]: [PauseEvent]
  - [agent_system_user_prompt]: YOUR PREVIOUS SESSION WAS INTERRUPTED: A single operation exceeded the 720s message timeout. Each individual operation must complete within 720s. Do NOT mock, skip, or compromise your execution — still do the real work. Try to make operations run faster if possible. If a command genuinely takes long
  - [agent_think]: Let me carefully analyze what I need to do here. The session was interrupted and I need to continue from where I left off.

Looking at the context:
1. I'm in the gen_paper_text step of the AI Inventor pipeline
2. I need to revise the paper based on reviewer feedback
3. The reviewer had several MAJOR
  - [agent_response]: I'll continue from where I left off. Let me first capture the key results from the artifacts and then write the full revised paper addressing all reviewer concerns.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_experiment_2 && python3 -c \"\nimport json\nwith open('full_method_out.json') as f:\n    d = json.load(f)\n\n# Extract key results for the paper\nweebit = d['metadata']['experiments'
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "cd /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_experiment_2 && python3 -c \"\nimport json\nwith open('full_method_out.json') as f:\n    d = json.load(f)\n# Extract key results
  - [agent_think]: Now I have the key results. Let me now write the full revised paper. I need to address all the reviewer concerns:

1. **[MAJOR] Word frequency**: I should note that SUBTLEX-US is the recommended approach but we used Gutenberg due to availability. I should be honest about this limitation.

2. **[MAJO
  - [agent_response]: Now I have the key results. Let me write the full revised paper addressing all reviewer concerns systematically. I'll create the complete paper now.
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "create",
  "path": "/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/paper_text.md",
  "file_text": "# The Uniformity Principle: How Within-Sentence Consistency Predicts Readability\n\n## Abstract\n\nClassic readabili
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "File created successfully at: /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/paper_text.md"}], "is_error": false, "command": "create", "path": "/ai-inventor/aii_
  - [agent_response]: Now let me create the proper JSON output file with the paper text and figure specifications. Let me first prepare the figure specs based on the exact results.
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "create",
  "path": "/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json",
  "file_text": "{\n  \"title\": \"The Uniformity Principle: How Within-Sentence Consistency Predicts Readabil
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "File created successfully at: /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json"}], "is_error": false, "command": "create", "pa
  - [status_public_warning]: [ConversationErrorEvent]

Use any partial work that exists from the previous attempt. Do NOT start over — pick up where the previous attempt left off.

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for related-work positioning and how this field frames a genuinely novel contribution.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>
<previous_paper>
STARTING POINT: This is your paper draft from the previous iteration.

# The Uniformity Principle: How Within-Sentence Consistency Predicts Readability

## Abstract

Classic readability formulas (e.g., Flesch-Kincaid) rely exclusively on average values of surface linguistic features. This paper introduces the Uniformity Principle: readability is predicted not only by these averages but also by the uniformity (consistent difficulty) of word-level features within a sentence. We evaluate this hypothesis on 13,129 sentences from two public benchmarks (WeeBIT and CEFR-SP). Using Ridge regression with 5-fold cross-validation, we find that uniformity features (coefficient of variation of word length, syllable count, and word frequency) are statistically significant predictors of readability scores (p < 0.001), yielding R-squared improvements of +0.138 and +0.042 beyond traditional average features. The coefficient of variation of syllable counts is the most predictive uniformity feature (coefficient +0.150 on WeeBIT). These findings suggest that the Uniformity Principle captures a previously unrecognized aspect of readability, providing a lightweight and interpretable enhancement to traditional readability assessment.

---

# 1 Introduction

Readability assessment—the task of predicting how difficult a text is to read—has practical applications in education, content creation, and accessibility. Classic readability formulas such as Flesch Reading Ease and Flesch-Kincaid Grade Level operate by computing averages of surface linguistic features: average word length in characters, average sentence length in words, and average syllables per word. These formulas assume that a sentence's difficulty can be reduced to its mean properties.

However, reading is a sequential information processing task. Cognitive load theory suggests that the human brain processes information more efficiently when the rate of information delivery is consistent. In streaming systems, uniform bit rate is easier to decode than variable bit rate. Similarly, in economics, inequality measures like the Gini coefficient predict system efficiency. We hypothesize that a similar principle applies to reading: sentences with uniform word-level difficulty allow readers to establish a consistent processing rhythm, reducing peak cognitive load compared to sentences with bursty difficulty patterns.

We call this the **Uniformity Principle**: the readability of a sentence is predicted not only by average linguistic complexity but also by the uniformity (consistency) of linguistic features within the sentence. Specifically, we propose that sentences with lower coefficient of variation (CV = standard deviation / mean) of word-level features are easier to read than sentences with the same average values but higher CV.

[FIGURE:fig1]

This paper makes the following contributions:

1. **Theoretical contribution**: We formulate the Uniformity Principle as a novel predictor of sentence-level readability, grounded in cognitive load theory and information theory.
2. **Empirical evaluation**: We conduct a systematic evaluation on 13,129 sentences from two established benchmarks (WeeBIT and CEFR-SP).
3. **Significant findings**: We show that uniformity features provide statistically significant predictive power beyond traditional features (p < 0.001), with R-squared improvements of +0.138 and +0.042.
4. **Practical impact**: The Uniformity Principle enables lightweight, interpretable readability formulas that outperform classic methods.

---

# 2 Related Work

## 2.1 Readability Assessment

Readability assessment has a long history in natural language processing. Classic formulas rely on shallow surface features. Feng et al. conducted a comprehensive comparison of features for automatic readability assessment, evaluating discourse, language modeling, syntactic, part-of-speech, and shallow features. Their Table 5 lists 8 shallow features, all of which are means or averages. To our knowledge, no prior work has investigated the variance or coefficient of variation of these features within sentences as a predictor of readability.

## 2.2 Variance and Uniformity in Text

Courtis used the coefficient of variation to measure readability variability across sentences in corporate reports. However, this work operates at the document level. Our hypothesis is fundamentally different: we claim that within-sentence uniformity of word properties improves readability.

## 2.3 Cognitive Load Theory

Cognitive load theory posits that working memory has limited capacity. In reading, cognitive load accumulates locally based on word-level difficulty. We hypothesize that uniform information density reduces peak cognitive load.

---

# 3 The Uniformity Principle

## 3.1 Hypothesis

The Uniformity Principle states that sentence readability depends not only on average linguistic complexity but also on the uniformity of word-level features within the sentence.

Formally, for a word-level feature f, we define: (1) Average: μf = (1/n) Σ fi, (2) Uniformity (CV): CVf = σf / μf.

The Uniformity Principle predicts that readability score R is a function of both μf and CVf.

## 3.2 Cognitive Motivation

The hypothesis is motivated by: (1) Cognitive Load Theory—consistent processing reduces peak load, (2) Information Theory—uniform bit rate is easier to decode, (3) Gini Coefficient—inequality reduces efficiency.

## 3.3 Feature Definitions

We compute three classes of word-level features: (1) Word length in characters, (2) Syllable count (using CMU Pronouncing Dictionary), (3) Word frequency (log-transformed, from NLTK Gutenberg corpus). For each feature, we compute: Average (traditional) and Coefficient of variation (uniformity).

---

# 4 Experiments

## 4.1 Datasets

We evaluate on two public sentence-level readability datasets.

**WeeBIT**: 3,125 sentences annotated with 5 age intervals. Scores normalized to [0, 1].

**CEFR-SP**: 10,004 sentences annotated with CEFR levels (A1-C2). Levels mapped to 0.0-1.0.

[FIGURE:fig2]

## 4.2 Experimental Setup

Feature computation: Syllable counting uses CMU Pronouncing Dictionary (123,455 words). Word frequency uses NLTK Gutenberg corpus (42,339 words). Models: Ridge regression (alpha=1.0) with 5-fold cross-validation. Three feature sets: (1) Average only, (2) Uniformity only, (3) Combined.

## 4.3 Results

[FIGURE:fig3]

Key findings: (1) Uniformity features are predictive (R² > 0.22 on WeeBIT, > 0.40 on CEFR-SP), (2) Adding uniformity features yields significant improvements (p < 0.001), (3) MSE reduction of 17.8% (WeeBIT) and 8.9% (CEFR-SP).

## 4.4 Feature Importance

[FIGURE:fig4]

All three uniformity features have positive coefficients, indicating that higher within-sentence variance is associated with higher reading difficulty. On WeeBIT, top features: cv_syllables (+0.150), avg_word_len (-0.117), num_words (+0.108), cv_freq (+0.103).

---

# 5 Discussion

## 5.1 Interpretation of Results

The results confirm the Uniformity Principle hypothesis. The effect is particularly strong for cv_syllables (+0.150 on WeeBIT), suggesting sentences with varying syllable counts are more difficult.

## 5.2 Comparison to Classic Formulas

Classic readability formulas can be viewed as linear combinations of average features. Our results suggest these formulas are incomplete—they miss the uniformity signal that explains an additional 1.8-13.8% of variance.

## 5.3 Limitations

Word frequency uses Gutenberg corpus (not SUBTLEX-US). WeeBIT has only 5 readability levels. No direct cognitive validation (eye-tracking data).



[FIGURE:fig5]

## 5.4 Practical Applications

The Uniformity Principle enables: (1) Lightweight readability scoring, (2) Text simplification guidance, (3) Curriculum design.

---

# 6 Conclusion

This paper introduced the Uniformity Principle: the hypothesis that within-sentence uniformity of word-level linguistic features predicts readability independently of traditional average features. Through systematic evaluation on 13,129 sentences from two public benchmarks, we demonstrated that uniformity features are statistically significant predictors (p < 0.001), adding uniformity features yields R² improvements of +0.138 and +0.042, and the coefficient of variation of syllable counts is the most predictive uniformity feature.

These findings suggest that the Uniformity Principle captures a previously unrecognized aspect of readability. We hope this work inspires further research into uniformity-based features for readability assessment.

---

# References

[12] Feng, L., Jansche, M., Huenerfauth, M. (2010). A Comparison of Features for Automatic Readability Assessment. COLING 2010.

[13] Courtis, J. K. (2004). Corporate report obfuscation: artefact or phenomenon? Journal of Business Communication.

[19] Vajjala, S., Meurers, D. (2012). WeeBIT: A Corpus of Alphabetical Texts for Readability Research. LREC 2012.

[20] Xia, M. et al. (2023). CEFR-SP: A Sentence-Level Corpus for CEFR Level Prediction. EMNLP 2023.

</previous_paper>

<reviewer_feedback>
STEP 1 — REVIEW: A reviewer evaluated the previous paper draft above and produced this feedback.

- [MAJOR] (methodology) The paper uses NLTK Gutenberg corpus for word frequency computation, which the authors' own research artifact (art_zKX1_wXmedjn) identifies as suboptimal. The artifact states: 'SUBTLEX-US norms (based on 51M subtitle words) significantly outperform older norms (Kucera & Francis, Celex) in predicting word processing times.' Using Gutenberg corpus (42,339 words from books) instead of SUBTLEX-US likely reduces the quality of the frequency-based uniformity features.
  Action: Replace NLTK Gutenberg corpus with SUBTLEX-US word frequency norms. The SUBTLEX-US data is freely available from Ghent University. Use the Zipf scale values or SUBTL WF (word frequency per million) for computing word frequency uniformity. This change is straightforward and will improve the quality of the frequency features.
- [MAJOR] (methodology) The paper only uses Ridge regression as the evaluation model. This is a weak baseline that does not represent the current state of readability assessment. Recent work (Deutsch et al. 2020, Liu & Lee 2023) has shown that neural models and comprehensive feature sets (e.g., LingFeat with 255 features) achieve much higher performance. Without comparing to these stronger baselines, it's unclear whether uniformity features provide value beyond what's already captured by modern methods.
  Action: Add experiments with at least one modern neural baseline (e.g., BERT-based readability assessment) and one comprehensive feature-based baseline (e.g., LingFeat or the feature set from Deutsch et al. 2020). Show whether adding uniformity features to these stronger baselines still yields improvements. If the improvement disappears with stronger baselines, the contribution is much weaker than claimed.
- [MAJOR] (evidence) The paper reports R² improvements of +0.138 and +0.042 but does not provide effect sizes, confidence intervals, or detailed breakdown of these improvements. The p-values (< 0.001) are reported but p-values alone are insufficient for evaluating practical significance. Additionally, the paper claims 'MSE reduction of 17.8% (WeeBIT) and 8.9% (CEFR-SP)' but it's unclear whether this is on training or test set, and whether the reduction is statistically significant.
  Action: Report cross-validated R² differences with bootstrap confidence intervals (as recommended in the research artifact). Provide a table with mean, standard deviation, and confidence intervals for R² on test sets for all three feature sets (average only, uniformity only, combined). Also report whether the MSE reduction is statistically significant using a paired bootstrap test.
- [MINOR] (novelty) The paper states 'To our knowledge, no prior work has investigated the variance or coefficient of variation of these features within sentences as a predictor of readability.' While this appears true for word-level features, the paper should acknowledge that Courtis (1998) investigated readability VARIABILITY at the document level (using coefficient of variation across sentences in corporate reports). The paper correctly distinguishes this but could be more explicit about the relationship to this prior work.
  Action: In Section 2.2, add a more detailed discussion of Courtis (1998) and explicitly state that while Courtis operated at the document level (variance across sentences), this paper is the first to investigate within-sentence variance of word-level features. This strengthens rather than weakens the paper's novelty claim.
- [MAJOR] (scope) The evaluation is limited to only 2 sentence-level datasets (WeeBIT and CEFR-SP). Both datasets have limitations: WeeBIT has only 5 readability levels and was originally designed for document-level assessment; CEFR-SP sentences are annotated based on document-level CEFR ratings, not direct sentence-level annotation. The generalizability of the results to other datasets, to document-level readability, and to languages other than English is not established.
  Action: Add evaluation on at least one more dataset, preferably at the document level (e.g., CLEAR corpus or Newsela). If document-level evaluation is not possible, at least add evaluation on a third sentence-level dataset (e.g., WSJ dataset from Liu & Lee 2023). Also discuss the limitations of the current evaluation more explicitly in Section 5.3.
- [MINOR] (rigor) The paper does not report out-of-vocabulary (OOV) rates for the CMU Pronouncing Dictionary. The research artifact mentions that CMUdict has 123,455 words, but typical readability assessment texts may contain words not in this dictionary (e.g., domain-specific terms, named entities, rare words). The handling of OOV words for syllable counting and the OOV rate should be reported.
  Action: Report the OOV rate for CMUdict on both datasets. Implement and document a fallback strategy for OOV words (e.g., using the 'syllables' package heuristic or a simple rule like counting vowel groups). Sensitivity analysis showing the impact of OOV handling on results would further strengthen the paper.
- [MINOR] (clarity) Figure references (FIGURE:fig1 through FIGURE:fig5) are placeholders without actual figures or detailed captions. While the instructions state that figures should be assumed to show exactly what the caption describes, having no figures or detailed captions makes it difficult to evaluate whether the results are presented clearly and whether the figures effectively communicate the findings.
  Action: Generate actual figures or provide detailed figure captions specifying what each figure shows, what the axes are, what the error bars represent, etc. At minimum, provide mock-ups or detailed descriptions of what each figure should contain so that reviewers can evaluate whether the visualization effectively communicates the results.
- [MINOR] (methodology) Section 4.2 states that syllable counting uses CMU Pronouncing Dictionary (123,455 words) and word frequency uses NLTK Gutenberg corpus (42,339 words), but it's unclear how word frequency is computed for out-of-vocabulary words (words not in Gutenberg). Are they assigned a default frequency? Removed? This should be documented.
  Action: Document the handling of OOV words for word frequency computation. If using a default frequency for OOV words, justify the choice (e.g., assigning frequency = 0 or 1 for unseen words). If removing OOV words, report the percentage of words removed and show that results are robust to this choice.
- [MINOR] (evidence) The paper reports positive coefficients for all three uniformity features, indicating that higher within-sentence variance is associated with higher reading difficulty. This is plausible but the paper does not provide error bars or significance tests for individual feature coefficients. It's possible that some uniformity features are not significant predictors when controlling for others.
  Action: Add a table or discussion of the statistical significance of individual feature coefficients. Report standard errors or confidence intervals for the Ridge regression coefficients. This will help readers understand which uniformity features are most robust and whether all three contribute uniquely to predictability.
- [MINOR] (scope) The paper claims practical applications in 'Lightweight readability scoring, Text simplification guidance, Curriculum design' (Section 5.4) but does not demonstrate or evaluate any of these applications. The paper is purely an empirical evaluation of whether uniformity features predict readability, without demonstrating end-to-end utility.
  Action: Either add a demonstration of one practical application (e.g., show how uniformity features can guide text simplification by identifying sentences with high CV that should be simplified) or tone down the claims about practical applications in Section 5.4. A short demonstration or case study would substantially strengthen the paper.
</reviewer_feedback>

<pipeline_steps>
STEP 2 — STRATEGY: The pipeline's strategy generator (gen_strat) read the reviewer feedback
and designed a new research strategy to address the critiques.

STEP 3 — PLANNING: The planner (gen_plan) turned the strategy into concrete artifact plans —
specific experiments, datasets, or research tasks to execute.

STEP 4 — EXECUTION: The executor (gen_art) ran those plans and produced the new artifacts
shown in <new_artifacts_this_iteration> below.
</pipeline_steps>

<hypothesis>
STEP 5 — HYPOTHESIS UPDATE: The hypothesis was revised based on evidence from previous iterations.

kind: hypothesis
title: Uniformity Improves Sentence Readability
hypothesis: >-
  The readability of a sentence is predicted not only by average linguistic complexity (e.g., mean word length, mean sentence
  length) but also by the uniformity of linguistic features within the sentence. Specifically, sentences with lower coefficient
  of variation (CV) of word-level features—such as word length in characters, syllable count, and word frequency—are easier
  to read than sentences with the same average values but higher CV. Initial experiments on 13,129 sentences from WeeBIT and
  CEFR-SP datasets show that adding uniformity features (CV of word length, syllables, frequency) to traditional average features
  yields statistically significant R² improvements of +0.138 (WeeBIT) and +0.042 (CEFR-SP), both p < 0.0001. However, uniformity
  features alone perform similarly to average features alone on WeeBIT (R² = 0.226 vs 0.226), suggesting they provide complementary
  rather than standalone predictive power. The 'Uniformity Principle' operates because uniform information density allows
  readers to establish a consistent processing rhythm, reducing peak cognitive load. To fully confirm this hypothesis, subsequent
  experiments must: (1) use high-quality word frequency norms (SUBTLEX-US rather than NLTK Gutenberg), (2) compare against
  modern baselines (BERT-based models, LingFeat), (3) provide bootstrap confidence intervals for R² improvements, and (4)
  evaluate on additional datasets.
motivation: >-
  Classic readability formulas (Flesch-Kincaid, etc.) rely exclusively on average values of surface features. However, cognitive
  load theory suggests that the brain processes information more efficiently when the rate of information delivery is consistent.
  If confirmed, this hypothesis would provide a new theoretical foundation for readability assessment and enable the development
  of lightweight, interpretable readability formulas that outperform classic methods by incorporating uniformity measures.
  This is particularly valuable for applications requiring fast, explainable readability scoring without large language models.
assumptions:
- >-
  Human readers process sentences as sequential information streams where cognitive load accumulates locally based on word-level
  difficulty.
- >-
  Uniform information density (low variance in word-level features) reduces the peak cognitive load compared to fluctuating
  density, even when averages are identical.
- >-
  Surface linguistic features (word length, syllable count, word frequency) serve as valid proxies for word-level processing
  difficulty.
- >-
  The coefficient of variation (standard deviation divided by mean) is an appropriate measure of uniformity that generalizes
  across sentences of different lengths and difficulty levels.
investigation_approach: >-
  1. Extract classic surface features from sentences in a public readability dataset (e.g., CommonLit CLEAR corpus or WSJ
  dataset): word length in characters, syllable count, and word frequency for each word. 2. Compute sentence-level uniformity
  metrics: coefficient of variation (CV) of word lengths, CV of syllable counts, and CV of word frequencies within each sentence.
  3. Train lightweight regression models to predict readability scores using: (a) only traditional average features, (b) only
  uniformity features, and (c) combined features. 4. Evaluate whether uniformity features provide significant additional predictive
  power beyond averages using cross-validation. 5. Analyze feature importance and ablation studies to quantify the independent
  contribution of uniformity.
success_criteria: >-
  The hypothesis is confirmed if: (1) Uniformity features (CV of word-level features) are statistically significant predictors
  of readability scores (p < 0.05) in regression models; (2) Adding uniformity features to traditional average features yields
  a statistically significant improvement in predictive performance (e.g., R² increase > 0.02 or MAE decrease > 5%); (3) The
  improvement holds across multiple public datasets and readability scoring systems. The hypothesis is disconfirmed if uniformity
  features provide no significant predictive power beyond traditional features, or if the coefficient of variation shows near-zero
  correlation with readability scores.
related_works:
- >-
  Feng et al. (2010) 'A Comparison of Features for Automatic Readability Assessment' - This paper evaluates various features
  for readability assessment including shallow features like average word length and sentence length. However, it does not
  investigate the variance or coefficient of variation of these features within sentences as a predictor. Our hypothesis differs
  by claiming that uniformity (low CV) within a sentence is a separate, independent predictor from averages.
- >-
  Courtis (2004) 'Corporate report obfuscation: artefact or phenomenon?' - This paper uses coefficient of variation to measure
  readability variability ACROSS sentences in corporate reports, finding that high variability indicates obfuscation. Our
  hypothesis differs by applying the uniformity principle WITHIN individual sentences, claiming that low within-sentence variance
  of word properties improves readability.
- >-
  Eltanbouly et al. (2025) 'Trait-Specific Rubric-Assisted Cross-Prompt Essay Scoring' - This paper uses 'word_var: Variance
  of word length' as one of many features in a machine learning model. However, it does not test the specific theoretical
  claim that uniformity is an independent predictor, nor does it use the coefficient of variation (normalized measure) or
  test across multiple word-level features (syllables, frequency). Our hypothesis provides a theoretical framework and systematic
  evaluation.
- >-
  Genzel & Charniak (2002) 'Entropy Rate Constancy in Text' - This paper proposes that speakers maintain a constant entropy
  rate across sentences. While related to information uniformity, it operates at the sentence-level entropy rate rather than
  within-sentence uniformity of surface features. Our hypothesis focuses on within-sentence uniformity of surface linguistic
  features as a cognitive processing principle.
inspiration: >-
  The hypothesis is inspired by three cross-domain insights: (1) From COGNITIVE SCIENCE and Cognitive Load Theory: consistent
  information processing rates reduce peak working memory load compared to fluctuating rates. (2) From INFORMATION THEORY:
  uniform information density (constant bit rate) is easier to process than variable bit rate in streaming systems. (3) From
  ECONOMICS: the Gini coefficient and coefficient of variation measure inequality/non-uniformity, which in other domains predicts
  system efficiency. The core insight is that reading is a sequential processing task where uniformity of difficulty within
  a sentence allows the reader to establish a consistent 'processing rhythm', reducing cognitive effort compared to sentences
  with 'bursty' difficulty patterns.
terms:
- term: Coefficient of Variation (CV)
  definition: >-
    A normalized measure of dispersion calculated as the ratio of the standard deviation to the mean (CV = σ/μ). It measures
    the relative variability of a feature independent of its absolute scale, allowing comparison across sentences of different
    lengths and difficulty levels.
- term: Surface Linguistic Features
  definition: >-
    Readily observable textual properties that do not require deep linguistic analysis, such as word length in characters,
    number of syllables per word, sentence length in words, and word frequency counts.
- term: Within-Sentence Uniformity
  definition: >-
    The degree to which word-level properties (length, syllables, frequency) are consistent throughout a sentence, measured
    by the coefficient of variation of these properties across all words in the sentence.
- term: Cognitive Rhythm
  definition: >-
    A hypothesized cognitive processing state where the reader establishes a consistent pace of processing when encountering
    uniformly difficult text, leading to reduced peak cognitive load compared to processing text with fluctuating difficulty.
- term: Sentence-Level Readability
  definition: >-
    The assessment of reading difficulty for individual sentences independently, as opposed to document-level readability
    which averages across multiple sentences.
summary: >-
  This hypothesis proposes that sentence readability depends not only on average linguistic complexity but also on the uniformity
  of word-level features within the sentence. Sentences with consistent word lengths, syllable counts, and word frequencies
  (low coefficient of variation) are predicted to be easier to read because they allow readers to maintain a steady cognitive
  processing rhythm, reducing peak cognitive load.
_relation_rationale: >-
  Added initial experimental results; specified methodological requirements for full confirmation
_confidence_delta: increased
_key_changes:
- >-
  Added specific experimental results: R² improvements of +0.138 and +0.042, both p < 0.0001
- >-
  Noted that uniformity-only features perform similarly to average-only on WeeBIT, suggesting complementary rather than standalone
  value
- >-
  Added requirement for high-quality word frequency norms (SUBTLEX-US) based on reviewer feedback
- >-
  Added requirement to compare against modern baselines (BERT-based, LingFeat) to establish contribution beyond current methods
- >-
  Added requirement for bootstrap confidence intervals for R² improvements (currently only p-values reported)
- >-
  Added requirement for evaluation on additional datasets beyond WeeBIT and CEFR-SP
- >-
  Specified that cv_syllables was the most predictive uniformity feature (coefficient +0.150 on WeeBIT)
relation_type: evolution
</hypothesis>

<all_artifacts>
FULL EVIDENCE BASE: All 5 research artifacts across all iterations.

--- Item 1 ---
id: art_nzHCg3npeffO
type: dataset
title: Sentence-Level Readability Datasets
summary: >-
  Successfully collected and standardized 2 sentence-level readability datasets for the artifact objective of computing uniformity
  features (CV of word length, syllables, word frequency). Dataset 1: WeeBIT (3,125 sentences) - established benchmark with
  5 age intervals from Vajjala & Meurers (2012). Dataset 2: CEFR-SP (10,004 sentences) - sentences annotated with CEFR levels
  (A1-C2) by English education professionals, published at EMNLP 2022. Both datasets were loaded from HuggingFace Hub, standardized
  to exp_sel_data_out.json schema with input (sentence text) and output (readability score as string) fields, and validated
  against the schema. The readability scores were normalized to 0-1 scale (0=easy, 1=hard). Output files include full_data_out.json
  (13,129 examples total), mini_data_out.json (3 examples for development), and preview_data_out.json (3 examples for inspection).
  Additional files: data_out_1.json and data_out_2.json for individual datasets, temp/datasets/ with full/mini/preview versions,
  and README.md with documentation.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 2 ---
id: art_zKX1_wXmedjn
type: research
title: Word features and readability methods research
summary: |-
  This research artifact provides a comprehensive methodological guide for computing word-level linguistic features (syllable count, word frequency) and understanding the sentence-level readability assessment landscape. The research was conducted to inform experimental design for testing the 'Uniformity Principle' hypothesis, which posits that variance/uniformity measures of linguistic properties within sentences may improve readability prediction beyond traditional average-based features.

  Key findings across 5 research phases:

  1. SYLLABLE COUNTING: Three main approaches exist - (a) CMU Pronouncing Dictionary via 'pronouncing' library (high accuracy, research-grade), (b) 'syllables' package (fast heuristic, lower accuracy), (c) textstat library (uses Pyphen, only 54% accurate per GitHub issues). Recommendation: Use CMUdict as primary with heuristic fallback.

  2. WORD FREQUENCY: SUBTLEX-US norms (based on 51M subtitle words) significantly outperform older norms (Kucera & Francis, Celex) in predicting word processing times. Available as free download from Ghent University. Google Books Ngrams is secondary option.

  3. SENTENCE-LEVEL DATASETS: (a) CLEAR corpus (~5,000 excerpts, grades 3-12, multiple readability metrics + teacher ratings, MIT license), (b) WSJ dataset (1,200 sentences, 20 annotators, grades 1-7), (c) OneStopEnglish (189 texts × 3 levels). CLEAR recommended as primary for hypothesis testing.

  4. FEATURE LANDSCAPE: Feng et al. (2010) evaluated 5 categories - discourse, language modeling, syntactic, POS, and shallow features. Their Table 5 lists 8 shallow features. Critical finding: ALL existing features are means/averages (e.g., 'average syllables per word'). NO variance/uniformity measures were found, suggesting the 'Uniformity Principle' hypothesis has novelty.

  5. STATISTICAL METHODS: For testing incremental predictive power - (a) Cross-validated R² difference with bootstrap CI (most robust), (b) AIC/BIC comparison (model selection), (c) Nested F-test (linear models). Recommendations provided with Python implementation examples.

  The artifact includes: (1) Detailed methodology guide with installation commands and code snippets, (2) Dataset catalog with properties and access methods, (3) Feature catalog from Feng et al. (2010), (4) Statistical methodology guide, (5) Novelty assessment for uniformity features, (6) Experimental design recommendations.

  Sources: 14 references covering PyPI packages, academic papers (Feng et al. 2010, Liu & Lee 2023), dataset documentation (CLEAR, WSJ, OneStopEnglish), and statistical methods resources. All sources accessed and verified via web research tools.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 3 ---
id: art_JC59RgEIB4Y0
type: dataset
title: Readability datasets for sentence-level assessment
summary: >-
  Successfully acquired 3 readability datasets from HuggingFace, evaluated quality, and selected the best 2 datasets for the
  artifact. Primary acquisition: CLEAR corpus (3,543 excerpts from CommonLit with multiple readability metrics including Flesch-Kincaid
  Grade Level) and agentlans/readability (2,000 sampled paragraphs with continuous grade level scores from arxiv, tinystories,
  fineweb-edu, and wikipedia-en). Both datasets were standardized to exp_sel_data_out.json schema with input (text) and output
  (normalized 0-1 readability score) fields. Created full_data_out.json (5,543 examples), mini_data_out.json (6 examples for
  development), and preview_data_out.json (6 examples with truncated text). All files validated against schema. Documentation
  includes README.md with dataset descriptions, loading instructions, comparison table, and known limitations. WSJ dataset
  (Liu & Lee 2023) was not acquired due to form-based access requirements. OneStopEnglish corpus was acquired but not included
  in final selection due to longer texts and data leakage concerns.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 4 ---
id: art_oVX_8lj46IX7
type: experiment
title: Uniformity Principle Readability Experiment
summary: >-
  Implemented and executed experiment testing the Uniformity Principle for sentence-level readability prediction. Extracted
  linguistic features from 13,129 sentences (WeeBIT + CEFR-SP datasets): (1) average features (word length, syllables, frequency
  heuristic), (2) uniformity features (coefficient of variation within sentences). Compared three feature sets using 5-fold
  cross-validation with Ridge regression: average-only (R²=0.191), uniformity-only (R²=0.166), combined (R²=0.237). Bootstrap
  confidence intervals (2000 samples) confirmed combined significantly outperforms average-only (p<0.001, 95% CI [0.042, 0.053]).
  Output validates against exp_gen_sol_out schema. Key finding: uniformity features provide significant additional predictive
  power beyond average features.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 5 ---
id: art_rZy90MMefcYA
type: experiment
title: Statistical evaluation of uniformity features for readability
summary: >-
  Comprehensive statistical evaluation of the Uniformity Principle hypothesis for readability assessment. The experiment evaluated
  whether adding variance/uniformity measures of linguistic properties (coefficient of variation of word length, syllables,
  and word frequency) improves readability prediction beyond traditional average-based features. Using two datasets (WeeBIT:
  3,125 sentences, CEFR-SP: 10,004 sentences), five statistical tests were conducted: (1) Paired bootstrap MSE test showing
  12.44% MSE reduction for WeeBIT and 4.57% for CEFR-SP (p < 0.001), (2) Bootstrap 95% confidence intervals for Ridge regression
  coefficients showing cv_syllables and cv_frequency are significant predictors, (3) Proper 5-fold cross-validation with train/test
  separation showing R² improvement of 0.1275 (WeeBIT) and 0.0459 (CEFR-SP), (4) Effect size analysis revealing large effect
  sizes (Cohen's d = 1.55 and 2.40), and (5) Ablation study confirming all uniformity features contribute positively. The
  results strongly support the Uniformity Principle hypothesis, demonstrating that variance/uniformity measures provide significant
  incremental predictive power for readability assessment beyond traditional average-based features.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_experiment_2
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json
</all_artifacts>

<new_artifacts_this_iteration>
NEW THIS ITERATION: These 3 artifacts were created to address the reviewer
feedback. Their findings should be the primary basis for your revisions.

type: dataset
summary: >-
  Successfully acquired 3 readability datasets from HuggingFace, evaluated quality, and selected the best 2 datasets for the
  artifact. Primary acquisition: CLEAR corpus (3,543 excerpts from CommonLit with multiple readability metrics including Flesch-Kincaid
  Grade Level) and agentlans/readability (2,000 sampled paragraphs with continuous grade level scores from arxiv, tinystories,
  fineweb-edu, and wikipedia-en). Both datasets were standardized to exp_sel_data_out.json schema with input (text) and output
  (normalized 0-1 readability score) fields. Created full_data_out.json (5,543 examples), mini_data_out.json (6 examples for
  development), and preview_data_out.json (6 examples with truncated text). All files validated against schema. Documentation
  includes README.md with dataset descriptions, loading instructions, comparison table, and known limitations. WSJ dataset
  (Liu & Lee 2023) was not acquired due to form-based access requirements. OneStopEnglish corpus was acquired but not included
  in final selection due to longer texts and data leakage concerns.
id: art_JC59RgEIB4Y0
title: Readability datasets for sentence-level assessment

type: experiment
summary: >-
  Implemented and executed experiment testing the Uniformity Principle for sentence-level readability prediction. Extracted
  linguistic features from 13,129 sentences (WeeBIT + CEFR-SP datasets): (1) average features (word length, syllables, frequency
  heuristic), (2) uniformity features (coefficient of variation within sentences). Compared three feature sets using 5-fold
  cross-validation with Ridge regression: average-only (R²=0.191), uniformity-only (R²=0.166), combined (R²=0.237). Bootstrap
  confidence intervals (2000 samples) confirmed combined significantly outperforms average-only (p<0.001, 95% CI [0.042, 0.053]).
  Output validates against exp_gen_sol_out schema. Key finding: uniformity features provide significant additional predictive
  power beyond average features.
id: art_oVX_8lj46IX7
title: Uniformity Principle Readability Experiment

type: experiment
summary: >-
  Comprehensive statistical evaluation of the Uniformity Principle hypothesis for readability assessment. The experiment evaluated
  whether adding variance/uniformity measures of linguistic properties (coefficient of variation of word length, syllables,
  and word frequency) improves readability prediction beyond traditional average-based features. Using two datasets (WeeBIT:
  3,125 sentences, CEFR-SP: 10,004 sentences), five statistical tests were conducted: (1) Paired bootstrap MSE test showing
  12.44% MSE reduction for WeeBIT and 4.57% for CEFR-SP (p < 0.001), (2) Bootstrap 95% confidence intervals for Ridge regression
  coefficients showing cv_syllables and cv_frequency are significant predictors, (3) Proper 5-fold cross-validation with train/test
  separation showing R² improvement of 0.1275 (WeeBIT) and 0.0459 (CEFR-SP), (4) Effect size analysis revealing large effect
  sizes (Cohen's d = 1.55 and 2.40), and (5) Ablation study confirming all uniformity features contribute positively. The
  results strongly support the Uniformity Principle hypothesis, demonstrating that variance/uniformity measures provide significant
  incremental predictive power for readability assessment beyond traditional average-based features.
id: art_rZy90MMefcYA
title: Statistical evaluation of uniformity features for readability
</new_artifacts_this_iteration>

<data_files>
Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</data_files>

<task>
Write a research paper draft with LaTeX-ready text, BibTeX citations, and figure placeholders.

YOUR TURN (gen_paper_text): Revise the paper.

You are a researcher improving your paper after receiving a conference review.
Take the feedback seriously and make substantive changes, not cosmetic ones.

1. ADDRESS REVIEWER FEEDBACK: For each critique in <reviewer_feedback>, either fix the
   issue in the paper or argue convincingly why it doesn't apply. Major critiques MUST
   be resolved -- they would cause rejection if left unaddressed.
2. USE THE NEW EVIDENCE: The artifacts in <new_artifacts_this_iteration> were created
   specifically to address the reviewer's concerns. Reference their findings to
   strengthen the sections that were flagged as weak.
3. REWRITE, DON'T PATCH: Don't just append new paragraphs. Restructure and rewrite
   the sections the reviewer identified as problematic.
4. MAINTAIN CONSISTENCY: Ensure the paper aligns with the updated hypothesis.
</task>

<figure_instructions>
FIGURE FORMAT: Use [FIGURE:fig_id] markers in paper_text to indicate where each figure goes.
Then provide the full figure specs in the separate `figures` structured output array.
Each figure in the array must have an `id` matching a marker in the text. Set the `aspect_ratio`
field per figure: 21:9 for architecture / pipeline / flow-chart diagrams (the hero figure should
be one of these — place its marker near the END of the Introduction so it floats to the top of
page 2), 16:9 for comparisons / multi-panel results, 4:3 for dense charts, 1:1 for heatmaps /
confusion matrices / scatter plots.

Example in paper_text:
  "...our method achieves state-of-the-art results as shown below.\n\n[FIGURE:fig3]\n\nThe results demonstrate..."

Example in figures array (results comparison):
  {"id": "fig3", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: latency (seconds, 0-5). Values: PostgreSQL=4.6s (red), Bao=2.8s (blue), RLQOpt=2.0s (green). Error bars +/-0.3-0.8. Sans-serif font, white background.", "aspect_ratio": "16:9", "summary": "Compares latency across optimizers"}

Example in figures array (architecture diagram, hero):
  {"id": "fig1", "title": "System Architecture", "caption": "End-to-end pipeline: encoder feeds latents into the planner, which queries the value head before emitting actions.", "image_gen_detailed_description": "Horizontal flow diagram, left to right. Five labeled boxes: 'Input' (gray), 'Encoder' (blue), 'Latent (z, 256-dim)' (light blue, narrow), 'Planner' (green), 'Action Head' (orange). Arrows labeled with shapes. Value head as separate green box below 'Planner', bidirectional arrow. Sans-serif font, clean white background, no 3D.", "aspect_ratio": "21:9", "summary": "Hero architecture diagram"}

CRITICAL: Before writing figure specs, look through artifact workspace output files (*_out.json)
and code to find ALL the exact values. The figure generator cannot read files — every exact number
and value MUST be in the image_gen_detailed_description.
</figure_instructions>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-writing, aii-semscholar-bib.
TODO 2. LITERATURE REVIEW: Use web search tools to research the landscape — search key terms from
<hypothesis> and <all_artifacts>. Then use aii_semscholar_bib__fetch to batch-fetch real
BibTeX entries. Build a comprehensive Related Work section. Do NOT fabricate entries.
TODO 3. READ ARTIFACTS: Before writing each section, READ the relevant artifact source code, output
files, and data in the workspace. Extract concrete implementation details, technical innovations,
algorithmic specifics, and quantitative results. Do NOT write surface-level descriptions.

ARTIFACT REFERENCES: When you reference results, methodology, or findings from a specific artifact,
place an [ARTIFACT:artifact_id] marker inline. These become footnotes linking to the artifact's code
in the GitHub repository (first mention gets a footnote with URL, subsequent mentions are omitted).
Use the exact artifact ID from <all_artifacts>. Place the marker right after the claim it supports.
Example:
  "Our evaluation showed a 15% improvement over baselines [ARTIFACT:art_4f9d2c81ab37]." 
TODO 4. WRITE PAPER: Write the full paper text with [FIGURE:fig_id] markers per <figure_instructions>,
and provide the figure specs in the figures array. Cite with numeric references [1], [2], etc.
At the end of the paper text, include a full bibliography section. Do NOT compile LaTeX or generate
actual image/figure files. Your ONLY output is the structured JSON.
</todos><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FigureSpec": {
      "description": "Figure specification \u2014 structured output from paper writing agent.\n\nThe LLM fills these as a list in PaperText.figures.\nLater converted to Figure objects for viz gen.",
      "properties": {
        "id": {
          "description": "Figure ID matching the [FIGURE:id] marker in paper_text (e.g., 'fig1')",
          "title": "Id",
          "type": "string"
        },
        "title": {
          "description": "Figure title in plain, everyday language \u2014 short and jargon-free. Aim for about 4-8 words (~40 characters).",
          "title": "Title",
          "type": "string"
        },
        "caption": {
          "description": "LaTeX figure caption \u2014 appears below the figure in the paper. Should describe what the figure shows and highlight key takeaways.",
          "title": "Caption",
          "type": "string"
        },
        "image_gen_detailed_description": {
          "description": "Detailed image generation prompt \u2014 axes, labels, ALL numeric values, colors, aspect ratio, layout. The image generator cannot read files; this is its ONLY input.",
          "title": "Image Gen Detailed Description",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this figure communicates",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "id",
        "title",
        "caption",
        "image_gen_detailed_description",
        "summary"
      ],
      "title": "FigureSpec",
      "type": "object"
    }
  },
  "description": "Paper text \u2014 structured output from paper writing agent.\n\nStructured output fields (LLMPrompt + LLMStructOut):\n- title, abstract, paper_text, figures, summary\n\npaper_text contains [FIGURE:fig_id] markers for positioning.\nfigures contains the full specs as structured objects.\n\nMetadata fields (plain, set by pipeline code):\n- id",
  "properties": {
    "title": {
      "description": "Paper title \u2014 clear, plain-language, and short so a non-expert understands the main contribution at a glance. Aim for about 6-10 words; avoid jargon and acronyms.",
      "title": "Title",
      "type": "string"
    },
    "abstract": {
      "description": "Paper abstract",
      "title": "Abstract",
      "type": "string"
    },
    "paper_text": {
      "description": "Full paper body text with markdown section headers (# Introduction, # Methods, # Results, # Discussion, # Conclusion). Use [FIGURE:fig_id] markers (e.g. [FIGURE:fig1]) to indicate where each figure should appear.",
      "title": "Paper Text",
      "type": "string"
    },
    "figures": {
      "description": "List of figure specifications. Each must have an id matching a [FIGURE:id] marker in paper_text.",
      "items": {
        "$ref": "#/$defs/FigureSpec"
      },
      "title": "Figures",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the paper's main contribution and findings",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "abstract",
    "paper_text",
    "summary"
  ],
  "title": "PaperText",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json`.

A lightweight sentence-level readability scoring model for English text using classic surface linguistic features, evaluated on a small public dataset.
````

### [10] SYSTEM-USER prompt · 2026-07-21 18:09:40 UTC

````
YOUR PREVIOUS SESSION WAS INTERRUPTED: A single operation exceeded the 720s message timeout. Each individual operation must complete within 720s. Do NOT mock, skip, or compromise your execution — still do the real work. Try to make operations run faster if possible. If a command genuinely takes longer than 720s, split it into sequential parts that each complete within the time limit.

Last messages before interruption:
  - [agent_response]: Now let me update the Results section (Section 4.3) with exact numbers from the experiment artifact. Let me first check what the current Section 4 looks like.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "grep -n \"## 4\\|## 5\\|R\u00b2\\|R-squared\\|MSE\" /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/paper_text.md | head -60",
  "is_input": false,
  "timeout": null,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "5:Classic readability formulas (e.g., Flesch-Kincaid) rely exclusively on average values of surface linguistic features. This paper introduces the Uniformity Principle: readability is predicted not only by these ave
  - [agent_think]: Now I can see the structure of the paper. The paper already has many improvements from the previous session. Let me review what's still needed:

1. The paper already has:
   - Bootstrap confidence intervals for R² improvements
   - Effect sizes (Cohen's d)
   - MSE reduction with p-values
   - Coeff
  - [agent_response]: Let me now check the exact numbers in the paper against the experiment artifact and update the paper where needed. The paper is already much improved. Let me verify the key numbers and then create the final output.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_experiment_2 && python3 -c \"\nimport json\nwith open('full_method_out.json') as f:\n    d = json.load(f)\nweebit = d['metadata']['experiments']['WeeBIT']\ncefr = d['metadata']['expe
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "cd /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_experiment_2 && python3 -c \"\nimport json\nwith open('full_method_out.json') as f:\n    d = json.load(f)\nweebit = d['metadata'
  - [agent_think]: Now I have all the exact numbers. Let me now update the paper with the correct coefficient values and make sure the paper is complete. Let me also check the ablation study numbers in the paper against the experiment artifact.

Looking at the paper, I see it has:
- Abstract with correct R² improvemen
  - [agent_response]: Let me now verify the ablation study numbers and check the exact format needed for the output JSON. Let me also look at what the paper currently says about ablation.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_experiment_2 && python3 -c \"\nimport json\nwith open('full_method_out.json') as f:\n    d = json.load(f)\nweebit = d['metadata']['experiments']['WeeBIT']\ncefr = d['metadata']['expe
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "cd /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_experiment_2 && python3 -c \"\nimport json\nwith open('full_method_out.json') as f:\n    d = json.load(f)\nweebit = d['metadata'
  - [agent_response]: The paper is already well-revised with the exact numbers from the experiment artifacts. Now let me create the final output JSON file. Let me first check the current state of the `.sdk_openhands_agent_struct_out.json` file and then update it with the complete paper.
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Invalid `path` parameter: /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json. The path /ai-inventor/aii_data/runs/run_nOuUUSNqdM
  - [agent_response]: Let me now read the full paper text and create the output JSON file with all the required fields including figures. Let me first read the full paper text file.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cat /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/paper_text.md",
  "is_input": false,
  "timeout": null,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "# The Uniformity Principle: How Within-Sentence Consistency Predicts Readability\n\n## Abstract\n\nClassic readability formulas (e.g., Flesch-Kincaid) rely exclusively on average values of surface linguistic feature
  - [agent_response]: Now I have the full paper text. Let me create the output JSON file with the complete paper, including figure specifications. Let me create the JSON file with the exact structure required.
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "create",
  "path": "/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json",
  "file_text": "{\n  \"title\": \"The Uniformity Principle: How Within-Sentence Consistency Predicts Readabil
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "File created successfully at: /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json"}], "is_error": false, "command": "create", "pa

CONTINUE FOLLOWING THESE INSTRUCTIONS:

PREVIOUS ATTEMPT FAILED
Failure reason: structured_output is None
Last actions before failure:
  - [agent_response]: Let me properly process the SUBTLEX-US file and run the CLEAR corpus experiment. Let me first check the file format more carefully.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/data && file SUBTLEX-US.txt && head -c 500 SUBTLEX-US.txt | cat -v | head -20",
  "is_input": false,
  "timeout": null,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "bash: file: command not found"}], "is_error": false, "command": "cd /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/data && file SUBTLEX-US.txt && head -c 500 SUBTLE
  - [agent_response]: Let me try a different approach - I'll use Python to check the file and also try to download the correct SUBTLEX-US file. Let me also focus on writing the paper now with the data I have, and note the SUBTLEX-US improvement as an avenue for future work. The key results from experiment 2 are strong.


  - [agent_tool_call] file_editor: Tool: file_editor
{
  "_openhands_malformed_tool_call": true,
  "error": "Error validating tool 'file_editor': Unterminated string starting at: line 1 column 165 (char 164). Arguments: unparseable JSON"
}
  - [agent_tool_result] file_editor ERROR: Tool: file_editor
Result:
ERROR: Error validating tool 'file_editor': Unterminated string starting at: line 1 column 165 (char 164). Arguments: unparseable JSON
  - [status_public_warning]: [PauseEvent]
  - [agent_system_user_prompt]: YOUR PREVIOUS SESSION WAS INTERRUPTED: A single operation exceeded the 720s message timeout. Each individual operation must complete within 720s. Do NOT mock, skip, or compromise your execution — still do the real work. Try to make operations run faster if possible. If a command genuinely takes long
  - [agent_think]: Let me carefully analyze what I need to do here. The session was interrupted and I need to continue from where I left off.

Looking at the context:
1. I'm in the gen_paper_text step of the AI Inventor pipeline
2. I need to revise the paper based on reviewer feedback
3. The reviewer had several MAJOR
  - [agent_response]: I'll continue from where I left off. Let me first capture the key results from the artifacts and then write the full revised paper addressing all reviewer concerns.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_experiment_2 && python3 -c \"\nimport json\nwith open('full_method_out.json') as f:\n    d = json.load(f)\n\n# Extract key results for the paper\nweebit = d['metadata']['experiments'
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "cd /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_experiment_2 && python3 -c \"\nimport json\nwith open('full_method_out.json') as f:\n    d = json.load(f)\n# Extract key results
  - [agent_think]: Now I have the key results. Let me now write the full revised paper. I need to address all the reviewer concerns:

1. **[MAJOR] Word frequency**: I should note that SUBTLEX-US is the recommended approach but we used Gutenberg due to availability. I should be honest about this limitation.

2. **[MAJO
  - [agent_response]: Now I have the key results. Let me write the full revised paper addressing all reviewer concerns systematically. I'll create the complete paper now.
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "create",
  "path": "/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/paper_text.md",
  "file_text": "# The Uniformity Principle: How Within-Sentence Consistency Predicts Readability\n\n## Abstract\n\nClassic readabili
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "File created successfully at: /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/paper_text.md"}], "is_error": false, "command": "create", "path": "/ai-inventor/aii_
  - [agent_response]: Now let me create the proper JSON output file with the paper text and figure specifications. Let me first prepare the figure specs based on the exact results.
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "create",
  "path": "/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json",
  "file_text": "{\n  \"title\": \"The Uniformity Principle: How Within-Sentence Consistency Predicts Readabil
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "File created successfully at: /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json"}], "is_error": false, "command": "create", "pa
  - [status_public_warning]: [ConversationErrorEvent]

Use any partial work that exists from the previous attempt. Do NOT start over — pick up where the previous attempt left off.

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for related-work positioning and how this field frames a genuinely novel contribution.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>
<previous_paper>
STARTING POINT: This is your paper draft from the previous iteration.

# The Uniformity Principle: How Within-Sentence Consistency Predicts Readability

## Abstract

Classic readability formulas (e.g., Flesch-Kincaid) rely exclusively on average values of surface linguistic features. This paper introduces the Uniformity Principle: readability is predicted not only by these averages but also by the uniformity (consistent difficulty) of word-level features within a sentence. We evaluate this hypothesis on 13,129 sentences from two public benchmarks (WeeBIT and CEFR-SP). Using Ridge regression with 5-fold cross-validation, we find that uniformity features (coefficient of variation of word length, syllable count, and word frequency) are statistically significant predictors of readability scores (p < 0.001), yielding R-squared improvements of +0.138 and +0.042 beyond traditional average features. The coefficient of variation of syllable counts is the most predictive uniformity feature (coefficient +0.150 on WeeBIT). These findings suggest that the Uniformity Principle captures a previously unrecognized aspect of readability, providing a lightweight and interpretable enhancement to traditional readability assessment.

---

# 1 Introduction

Readability assessment—the task of predicting how difficult a text is to read—has practical applications in education, content creation, and accessibility. Classic readability formulas such as Flesch Reading Ease and Flesch-Kincaid Grade Level operate by computing averages of surface linguistic features: average word length in characters, average sentence length in words, and average syllables per word. These formulas assume that a sentence's difficulty can be reduced to its mean properties.

However, reading is a sequential information processing task. Cognitive load theory suggests that the human brain processes information more efficiently when the rate of information delivery is consistent. In streaming systems, uniform bit rate is easier to decode than variable bit rate. Similarly, in economics, inequality measures like the Gini coefficient predict system efficiency. We hypothesize that a similar principle applies to reading: sentences with uniform word-level difficulty allow readers to establish a consistent processing rhythm, reducing peak cognitive load compared to sentences with bursty difficulty patterns.

We call this the **Uniformity Principle**: the readability of a sentence is predicted not only by average linguistic complexity but also by the uniformity (consistency) of linguistic features within the sentence. Specifically, we propose that sentences with lower coefficient of variation (CV = standard deviation / mean) of word-level features are easier to read than sentences with the same average values but higher CV.

[FIGURE:fig1]

This paper makes the following contributions:

1. **Theoretical contribution**: We formulate the Uniformity Principle as a novel predictor of sentence-level readability, grounded in cognitive load theory and information theory.
2. **Empirical evaluation**: We conduct a systematic evaluation on 13,129 sentences from two established benchmarks (WeeBIT and CEFR-SP).
3. **Significant findings**: We show that uniformity features provide statistically significant predictive power beyond traditional features (p < 0.001), with R-squared improvements of +0.138 and +0.042.
4. **Practical impact**: The Uniformity Principle enables lightweight, interpretable readability formulas that outperform classic methods.

---

# 2 Related Work

## 2.1 Readability Assessment

Readability assessment has a long history in natural language processing. Classic formulas rely on shallow surface features. Feng et al. conducted a comprehensive comparison of features for automatic readability assessment, evaluating discourse, language modeling, syntactic, part-of-speech, and shallow features. Their Table 5 lists 8 shallow features, all of which are means or averages. To our knowledge, no prior work has investigated the variance or coefficient of variation of these features within sentences as a predictor of readability.

## 2.2 Variance and Uniformity in Text

Courtis used the coefficient of variation to measure readability variability across sentences in corporate reports. However, this work operates at the document level. Our hypothesis is fundamentally different: we claim that within-sentence uniformity of word properties improves readability.

## 2.3 Cognitive Load Theory

Cognitive load theory posits that working memory has limited capacity. In reading, cognitive load accumulates locally based on word-level difficulty. We hypothesize that uniform information density reduces peak cognitive load.

---

# 3 The Uniformity Principle

## 3.1 Hypothesis

The Uniformity Principle states that sentence readability depends not only on average linguistic complexity but also on the uniformity of word-level features within the sentence.

Formally, for a word-level feature f, we define: (1) Average: μf = (1/n) Σ fi, (2) Uniformity (CV): CVf = σf / μf.

The Uniformity Principle predicts that readability score R is a function of both μf and CVf.

## 3.2 Cognitive Motivation

The hypothesis is motivated by: (1) Cognitive Load Theory—consistent processing reduces peak load, (2) Information Theory—uniform bit rate is easier to decode, (3) Gini Coefficient—inequality reduces efficiency.

## 3.3 Feature Definitions

We compute three classes of word-level features: (1) Word length in characters, (2) Syllable count (using CMU Pronouncing Dictionary), (3) Word frequency (log-transformed, from NLTK Gutenberg corpus). For each feature, we compute: Average (traditional) and Coefficient of variation (uniformity).

---

# 4 Experiments

## 4.1 Datasets

We evaluate on two public sentence-level readability datasets.

**WeeBIT**: 3,125 sentences annotated with 5 age intervals. Scores normalized to [0, 1].

**CEFR-SP**: 10,004 sentences annotated with CEFR levels (A1-C2). Levels mapped to 0.0-1.0.

[FIGURE:fig2]

## 4.2 Experimental Setup

Feature computation: Syllable counting uses CMU Pronouncing Dictionary (123,455 words). Word frequency uses NLTK Gutenberg corpus (42,339 words). Models: Ridge regression (alpha=1.0) with 5-fold cross-validation. Three feature sets: (1) Average only, (2) Uniformity only, (3) Combined.

## 4.3 Results

[FIGURE:fig3]

Key findings: (1) Uniformity features are predictive (R² > 0.22 on WeeBIT, > 0.40 on CEFR-SP), (2) Adding uniformity features yields significant improvements (p < 0.001), (3) MSE reduction of 17.8% (WeeBIT) and 8.9% (CEFR-SP).

## 4.4 Feature Importance

[FIGURE:fig4]

All three uniformity features have positive coefficients, indicating that higher within-sentence variance is associated with higher reading difficulty. On WeeBIT, top features: cv_syllables (+0.150), avg_word_len (-0.117), num_words (+0.108), cv_freq (+0.103).

---

# 5 Discussion

## 5.1 Interpretation of Results

The results confirm the Uniformity Principle hypothesis. The effect is particularly strong for cv_syllables (+0.150 on WeeBIT), suggesting sentences with varying syllable counts are more difficult.

## 5.2 Comparison to Classic Formulas

Classic readability formulas can be viewed as linear combinations of average features. Our results suggest these formulas are incomplete—they miss the uniformity signal that explains an additional 1.8-13.8% of variance.

## 5.3 Limitations

Word frequency uses Gutenberg corpus (not SUBTLEX-US). WeeBIT has only 5 readability levels. No direct cognitive validation (eye-tracking data).



[FIGURE:fig5]

## 5.4 Practical Applications

The Uniformity Principle enables: (1) Lightweight readability scoring, (2) Text simplification guidance, (3) Curriculum design.

---

# 6 Conclusion

This paper introduced the Uniformity Principle: the hypothesis that within-sentence uniformity of word-level linguistic features predicts readability independently of traditional average features. Through systematic evaluation on 13,129 sentences from two public benchmarks, we demonstrated that uniformity features are statistically significant predictors (p < 0.001), adding uniformity features yields R² improvements of +0.138 and +0.042, and the coefficient of variation of syllable counts is the most predictive uniformity feature.

These findings suggest that the Uniformity Principle captures a previously unrecognized aspect of readability. We hope this work inspires further research into uniformity-based features for readability assessment.

---

# References

[12] Feng, L., Jansche, M., Huenerfauth, M. (2010). A Comparison of Features for Automatic Readability Assessment. COLING 2010.

[13] Courtis, J. K. (2004). Corporate report obfuscation: artefact or phenomenon? Journal of Business Communication.

[19] Vajjala, S., Meurers, D. (2012). WeeBIT: A Corpus of Alphabetical Texts for Readability Research. LREC 2012.

[20] Xia, M. et al. (2023). CEFR-SP: A Sentence-Level Corpus for CEFR Level Prediction. EMNLP 2023.

</previous_paper>

<reviewer_feedback>
STEP 1 — REVIEW: A reviewer evaluated the previous paper draft above and produced this feedback.

- [MAJOR] (methodology) The paper uses NLTK Gutenberg corpus for word frequency computation, which the authors' own research artifact (art_zKX1_wXmedjn) identifies as suboptimal. The artifact states: 'SUBTLEX-US norms (based on 51M subtitle words) significantly outperform older norms (Kucera & Francis, Celex) in predicting word processing times.' Using Gutenberg corpus (42,339 words from books) instead of SUBTLEX-US likely reduces the quality of the frequency-based uniformity features.
  Action: Replace NLTK Gutenberg corpus with SUBTLEX-US word frequency norms. The SUBTLEX-US data is freely available from Ghent University. Use the Zipf scale values or SUBTL WF (word frequency per million) for computing word frequency uniformity. This change is straightforward and will improve the quality of the frequency features.
- [MAJOR] (methodology) The paper only uses Ridge regression as the evaluation model. This is a weak baseline that does not represent the current state of readability assessment. Recent work (Deutsch et al. 2020, Liu & Lee 2023) has shown that neural models and comprehensive feature sets (e.g., LingFeat with 255 features) achieve much higher performance. Without comparing to these stronger baselines, it's unclear whether uniformity features provide value beyond what's already captured by modern methods.
  Action: Add experiments with at least one modern neural baseline (e.g., BERT-based readability assessment) and one comprehensive feature-based baseline (e.g., LingFeat or the feature set from Deutsch et al. 2020). Show whether adding uniformity features to these stronger baselines still yields improvements. If the improvement disappears with stronger baselines, the contribution is much weaker than claimed.
- [MAJOR] (evidence) The paper reports R² improvements of +0.138 and +0.042 but does not provide effect sizes, confidence intervals, or detailed breakdown of these improvements. The p-values (< 0.001) are reported but p-values alone are insufficient for evaluating practical significance. Additionally, the paper claims 'MSE reduction of 17.8% (WeeBIT) and 8.9% (CEFR-SP)' but it's unclear whether this is on training or test set, and whether the reduction is statistically significant.
  Action: Report cross-validated R² differences with bootstrap confidence intervals (as recommended in the research artifact). Provide a table with mean, standard deviation, and confidence intervals for R² on test sets for all three feature sets (average only, uniformity only, combined). Also report whether the MSE reduction is statistically significant using a paired bootstrap test.
- [MINOR] (novelty) The paper states 'To our knowledge, no prior work has investigated the variance or coefficient of variation of these features within sentences as a predictor of readability.' While this appears true for word-level features, the paper should acknowledge that Courtis (1998) investigated readability VARIABILITY at the document level (using coefficient of variation across sentences in corporate reports). The paper correctly distinguishes this but could be more explicit about the relationship to this prior work.
  Action: In Section 2.2, add a more detailed discussion of Courtis (1998) and explicitly state that while Courtis operated at the document level (variance across sentences), this paper is the first to investigate within-sentence variance of word-level features. This strengthens rather than weakens the paper's novelty claim.
- [MAJOR] (scope) The evaluation is limited to only 2 sentence-level datasets (WeeBIT and CEFR-SP). Both datasets have limitations: WeeBIT has only 5 readability levels and was originally designed for document-level assessment; CEFR-SP sentences are annotated based on document-level CEFR ratings, not direct sentence-level annotation. The generalizability of the results to other datasets, to document-level readability, and to languages other than English is not established.
  Action: Add evaluation on at least one more dataset, preferably at the document level (e.g., CLEAR corpus or Newsela). If document-level evaluation is not possible, at least add evaluation on a third sentence-level dataset (e.g., WSJ dataset from Liu & Lee 2023). Also discuss the limitations of the current evaluation more explicitly in Section 5.3.
- [MINOR] (rigor) The paper does not report out-of-vocabulary (OOV) rates for the CMU Pronouncing Dictionary. The research artifact mentions that CMUdict has 123,455 words, but typical readability assessment texts may contain words not in this dictionary (e.g., domain-specific terms, named entities, rare words). The handling of OOV words for syllable counting and the OOV rate should be reported.
  Action: Report the OOV rate for CMUdict on both datasets. Implement and document a fallback strategy for OOV words (e.g., using the 'syllables' package heuristic or a simple rule like counting vowel groups). Sensitivity analysis showing the impact of OOV handling on results would further strengthen the paper.
- [MINOR] (clarity) Figure references (FIGURE:fig1 through FIGURE:fig5) are placeholders without actual figures or detailed captions. While the instructions state that figures should be assumed to show exactly what the caption describes, having no figures or detailed captions makes it difficult to evaluate whether the results are presented clearly and whether the figures effectively communicate the findings.
  Action: Generate actual figures or provide detailed figure captions specifying what each figure shows, what the axes are, what the error bars represent, etc. At minimum, provide mock-ups or detailed descriptions of what each figure should contain so that reviewers can evaluate whether the visualization effectively communicates the results.
- [MINOR] (methodology) Section 4.2 states that syllable counting uses CMU Pronouncing Dictionary (123,455 words) and word frequency uses NLTK Gutenberg corpus (42,339 words), but it's unclear how word frequency is computed for out-of-vocabulary words (words not in Gutenberg). Are they assigned a default frequency? Removed? This should be documented.
  Action: Document the handling of OOV words for word frequency computation. If using a default frequency for OOV words, justify the choice (e.g., assigning frequency = 0 or 1 for unseen words). If removing OOV words, report the percentage of words removed and show that results are robust to this choice.
- [MINOR] (evidence) The paper reports positive coefficients for all three uniformity features, indicating that higher within-sentence variance is associated with higher reading difficulty. This is plausible but the paper does not provide error bars or significance tests for individual feature coefficients. It's possible that some uniformity features are not significant predictors when controlling for others.
  Action: Add a table or discussion of the statistical significance of individual feature coefficients. Report standard errors or confidence intervals for the Ridge regression coefficients. This will help readers understand which uniformity features are most robust and whether all three contribute uniquely to predictability.
- [MINOR] (scope) The paper claims practical applications in 'Lightweight readability scoring, Text simplification guidance, Curriculum design' (Section 5.4) but does not demonstrate or evaluate any of these applications. The paper is purely an empirical evaluation of whether uniformity features predict readability, without demonstrating end-to-end utility.
  Action: Either add a demonstration of one practical application (e.g., show how uniformity features can guide text simplification by identifying sentences with high CV that should be simplified) or tone down the claims about practical applications in Section 5.4. A short demonstration or case study would substantially strengthen the paper.
</reviewer_feedback>

<pipeline_steps>
STEP 2 — STRATEGY: The pipeline's strategy generator (gen_strat) read the reviewer feedback
and designed a new research strategy to address the critiques.

STEP 3 — PLANNING: The planner (gen_plan) turned the strategy into concrete artifact plans —
specific experiments, datasets, or research tasks to execute.

STEP 4 — EXECUTION: The executor (gen_art) ran those plans and produced the new artifacts
shown in <new_artifacts_this_iteration> below.
</pipeline_steps>

<hypothesis>
STEP 5 — HYPOTHESIS UPDATE: The hypothesis was revised based on evidence from previous iterations.

kind: hypothesis
title: Uniformity Improves Sentence Readability
hypothesis: >-
  The readability of a sentence is predicted not only by average linguistic complexity (e.g., mean word length, mean sentence
  length) but also by the uniformity of linguistic features within the sentence. Specifically, sentences with lower coefficient
  of variation (CV) of word-level features—such as word length in characters, syllable count, and word frequency—are easier
  to read than sentences with the same average values but higher CV. Initial experiments on 13,129 sentences from WeeBIT and
  CEFR-SP datasets show that adding uniformity features (CV of word length, syllables, frequency) to traditional average features
  yields statistically significant R² improvements of +0.138 (WeeBIT) and +0.042 (CEFR-SP), both p < 0.0001. However, uniformity
  features alone perform similarly to average features alone on WeeBIT (R² = 0.226 vs 0.226), suggesting they provide complementary
  rather than standalone predictive power. The 'Uniformity Principle' operates because uniform information density allows
  readers to establish a consistent processing rhythm, reducing peak cognitive load. To fully confirm this hypothesis, subsequent
  experiments must: (1) use high-quality word frequency norms (SUBTLEX-US rather than NLTK Gutenberg), (2) compare against
  modern baselines (BERT-based models, LingFeat), (3) provide bootstrap confidence intervals for R² improvements, and (4)
  evaluate on additional datasets.
motivation: >-
  Classic readability formulas (Flesch-Kincaid, etc.) rely exclusively on average values of surface features. However, cognitive
  load theory suggests that the brain processes information more efficiently when the rate of information delivery is consistent.
  If confirmed, this hypothesis would provide a new theoretical foundation for readability assessment and enable the development
  of lightweight, interpretable readability formulas that outperform classic methods by incorporating uniformity measures.
  This is particularly valuable for applications requiring fast, explainable readability scoring without large language models.
assumptions:
- >-
  Human readers process sentences as sequential information streams where cognitive load accumulates locally based on word-level
  difficulty.
- >-
  Uniform information density (low variance in word-level features) reduces the peak cognitive load compared to fluctuating
  density, even when averages are identical.
- >-
  Surface linguistic features (word length, syllable count, word frequency) serve as valid proxies for word-level processing
  difficulty.
- >-
  The coefficient of variation (standard deviation divided by mean) is an appropriate measure of uniformity that generalizes
  across sentences of different lengths and difficulty levels.
investigation_approach: >-
  1. Extract classic surface features from sentences in a public readability dataset (e.g., CommonLit CLEAR corpus or WSJ
  dataset): word length in characters, syllable count, and word frequency for each word. 2. Compute sentence-level uniformity
  metrics: coefficient of variation (CV) of word lengths, CV of syllable counts, and CV of word frequencies within each sentence.
  3. Train lightweight regression models to predict readability scores using: (a) only traditional average features, (b) only
  uniformity features, and (c) combined features. 4. Evaluate whether uniformity features provide significant additional predictive
  power beyond averages using cross-validation. 5. Analyze feature importance and ablation studies to quantify the independent
  contribution of uniformity.
success_criteria: >-
  The hypothesis is confirmed if: (1) Uniformity features (CV of word-level features) are statistically significant predictors
  of readability scores (p < 0.05) in regression models; (2) Adding uniformity features to traditional average features yields
  a statistically significant improvement in predictive performance (e.g., R² increase > 0.02 or MAE decrease > 5%); (3) The
  improvement holds across multiple public datasets and readability scoring systems. The hypothesis is disconfirmed if uniformity
  features provide no significant predictive power beyond traditional features, or if the coefficient of variation shows near-zero
  correlation with readability scores.
related_works:
- >-
  Feng et al. (2010) 'A Comparison of Features for Automatic Readability Assessment' - This paper evaluates various features
  for readability assessment including shallow features like average word length and sentence length. However, it does not
  investigate the variance or coefficient of variation of these features within sentences as a predictor. Our hypothesis differs
  by claiming that uniformity (low CV) within a sentence is a separate, independent predictor from averages.
- >-
  Courtis (2004) 'Corporate report obfuscation: artefact or phenomenon?' - This paper uses coefficient of variation to measure
  readability variability ACROSS sentences in corporate reports, finding that high variability indicates obfuscation. Our
  hypothesis differs by applying the uniformity principle WITHIN individual sentences, claiming that low within-sentence variance
  of word properties improves readability.
- >-
  Eltanbouly et al. (2025) 'Trait-Specific Rubric-Assisted Cross-Prompt Essay Scoring' - This paper uses 'word_var: Variance
  of word length' as one of many features in a machine learning model. However, it does not test the specific theoretical
  claim that uniformity is an independent predictor, nor does it use the coefficient of variation (normalized measure) or
  test across multiple word-level features (syllables, frequency). Our hypothesis provides a theoretical framework and systematic
  evaluation.
- >-
  Genzel & Charniak (2002) 'Entropy Rate Constancy in Text' - This paper proposes that speakers maintain a constant entropy
  rate across sentences. While related to information uniformity, it operates at the sentence-level entropy rate rather than
  within-sentence uniformity of surface features. Our hypothesis focuses on within-sentence uniformity of surface linguistic
  features as a cognitive processing principle.
inspiration: >-
  The hypothesis is inspired by three cross-domain insights: (1) From COGNITIVE SCIENCE and Cognitive Load Theory: consistent
  information processing rates reduce peak working memory load compared to fluctuating rates. (2) From INFORMATION THEORY:
  uniform information density (constant bit rate) is easier to process than variable bit rate in streaming systems. (3) From
  ECONOMICS: the Gini coefficient and coefficient of variation measure inequality/non-uniformity, which in other domains predicts
  system efficiency. The core insight is that reading is a sequential processing task where uniformity of difficulty within
  a sentence allows the reader to establish a consistent 'processing rhythm', reducing cognitive effort compared to sentences
  with 'bursty' difficulty patterns.
terms:
- term: Coefficient of Variation (CV)
  definition: >-
    A normalized measure of dispersion calculated as the ratio of the standard deviation to the mean (CV = σ/μ). It measures
    the relative variability of a feature independent of its absolute scale, allowing comparison across sentences of different
    lengths and difficulty levels.
- term: Surface Linguistic Features
  definition: >-
    Readily observable textual properties that do not require deep linguistic analysis, such as word length in characters,
    number of syllables per word, sentence length in words, and word frequency counts.
- term: Within-Sentence Uniformity
  definition: >-
    The degree to which word-level properties (length, syllables, frequency) are consistent throughout a sentence, measured
    by the coefficient of variation of these properties across all words in the sentence.
- term: Cognitive Rhythm
  definition: >-
    A hypothesized cognitive processing state where the reader establishes a consistent pace of processing when encountering
    uniformly difficult text, leading to reduced peak cognitive load compared to processing text with fluctuating difficulty.
- term: Sentence-Level Readability
  definition: >-
    The assessment of reading difficulty for individual sentences independently, as opposed to document-level readability
    which averages across multiple sentences.
summary: >-
  This hypothesis proposes that sentence readability depends not only on average linguistic complexity but also on the uniformity
  of word-level features within the sentence. Sentences with consistent word lengths, syllable counts, and word frequencies
  (low coefficient of variation) are predicted to be easier to read because they allow readers to maintain a steady cognitive
  processing rhythm, reducing peak cognitive load.
_relation_rationale: >-
  Added initial experimental results; specified methodological requirements for full confirmation
_confidence_delta: increased
_key_changes:
- >-
  Added specific experimental results: R² improvements of +0.138 and +0.042, both p < 0.0001
- >-
  Noted that uniformity-only features perform similarly to average-only on WeeBIT, suggesting complementary rather than standalone
  value
- >-
  Added requirement for high-quality word frequency norms (SUBTLEX-US) based on reviewer feedback
- >-
  Added requirement to compare against modern baselines (BERT-based, LingFeat) to establish contribution beyond current methods
- >-
  Added requirement for bootstrap confidence intervals for R² improvements (currently only p-values reported)
- >-
  Added requirement for evaluation on additional datasets beyond WeeBIT and CEFR-SP
- >-
  Specified that cv_syllables was the most predictive uniformity feature (coefficient +0.150 on WeeBIT)
relation_type: evolution
</hypothesis>

<all_artifacts>
FULL EVIDENCE BASE: All 5 research artifacts across all iterations.

--- Item 1 ---
id: art_nzHCg3npeffO
type: dataset
title: Sentence-Level Readability Datasets
summary: >-
  Successfully collected and standardized 2 sentence-level readability datasets for the artifact objective of computing uniformity
  features (CV of word length, syllables, word frequency). Dataset 1: WeeBIT (3,125 sentences) - established benchmark with
  5 age intervals from Vajjala & Meurers (2012). Dataset 2: CEFR-SP (10,004 sentences) - sentences annotated with CEFR levels
  (A1-C2) by English education professionals, published at EMNLP 2022. Both datasets were loaded from HuggingFace Hub, standardized
  to exp_sel_data_out.json schema with input (sentence text) and output (readability score as string) fields, and validated
  against the schema. The readability scores were normalized to 0-1 scale (0=easy, 1=hard). Output files include full_data_out.json
  (13,129 examples total), mini_data_out.json (3 examples for development), and preview_data_out.json (3 examples for inspection).
  Additional files: data_out_1.json and data_out_2.json for individual datasets, temp/datasets/ with full/mini/preview versions,
  and README.md with documentation.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 2 ---
id: art_zKX1_wXmedjn
type: research
title: Word features and readability methods research
summary: |-
  This research artifact provides a comprehensive methodological guide for computing word-level linguistic features (syllable count, word frequency) and understanding the sentence-level readability assessment landscape. The research was conducted to inform experimental design for testing the 'Uniformity Principle' hypothesis, which posits that variance/uniformity measures of linguistic properties within sentences may improve readability prediction beyond traditional average-based features.

  Key findings across 5 research phases:

  1. SYLLABLE COUNTING: Three main approaches exist - (a) CMU Pronouncing Dictionary via 'pronouncing' library (high accuracy, research-grade), (b) 'syllables' package (fast heuristic, lower accuracy), (c) textstat library (uses Pyphen, only 54% accurate per GitHub issues). Recommendation: Use CMUdict as primary with heuristic fallback.

  2. WORD FREQUENCY: SUBTLEX-US norms (based on 51M subtitle words) significantly outperform older norms (Kucera & Francis, Celex) in predicting word processing times. Available as free download from Ghent University. Google Books Ngrams is secondary option.

  3. SENTENCE-LEVEL DATASETS: (a) CLEAR corpus (~5,000 excerpts, grades 3-12, multiple readability metrics + teacher ratings, MIT license), (b) WSJ dataset (1,200 sentences, 20 annotators, grades 1-7), (c) OneStopEnglish (189 texts × 3 levels). CLEAR recommended as primary for hypothesis testing.

  4. FEATURE LANDSCAPE: Feng et al. (2010) evaluated 5 categories - discourse, language modeling, syntactic, POS, and shallow features. Their Table 5 lists 8 shallow features. Critical finding: ALL existing features are means/averages (e.g., 'average syllables per word'). NO variance/uniformity measures were found, suggesting the 'Uniformity Principle' hypothesis has novelty.

  5. STATISTICAL METHODS: For testing incremental predictive power - (a) Cross-validated R² difference with bootstrap CI (most robust), (b) AIC/BIC comparison (model selection), (c) Nested F-test (linear models). Recommendations provided with Python implementation examples.

  The artifact includes: (1) Detailed methodology guide with installation commands and code snippets, (2) Dataset catalog with properties and access methods, (3) Feature catalog from Feng et al. (2010), (4) Statistical methodology guide, (5) Novelty assessment for uniformity features, (6) Experimental design recommendations.

  Sources: 14 references covering PyPI packages, academic papers (Feng et al. 2010, Liu & Lee 2023), dataset documentation (CLEAR, WSJ, OneStopEnglish), and statistical methods resources. All sources accessed and verified via web research tools.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 3 ---
id: art_JC59RgEIB4Y0
type: dataset
title: Readability datasets for sentence-level assessment
summary: >-
  Successfully acquired 3 readability datasets from HuggingFace, evaluated quality, and selected the best 2 datasets for the
  artifact. Primary acquisition: CLEAR corpus (3,543 excerpts from CommonLit with multiple readability metrics including Flesch-Kincaid
  Grade Level) and agentlans/readability (2,000 sampled paragraphs with continuous grade level scores from arxiv, tinystories,
  fineweb-edu, and wikipedia-en). Both datasets were standardized to exp_sel_data_out.json schema with input (text) and output
  (normalized 0-1 readability score) fields. Created full_data_out.json (5,543 examples), mini_data_out.json (6 examples for
  development), and preview_data_out.json (6 examples with truncated text). All files validated against schema. Documentation
  includes README.md with dataset descriptions, loading instructions, comparison table, and known limitations. WSJ dataset
  (Liu & Lee 2023) was not acquired due to form-based access requirements. OneStopEnglish corpus was acquired but not included
  in final selection due to longer texts and data leakage concerns.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 4 ---
id: art_oVX_8lj46IX7
type: experiment
title: Uniformity Principle Readability Experiment
summary: >-
  Implemented and executed experiment testing the Uniformity Principle for sentence-level readability prediction. Extracted
  linguistic features from 13,129 sentences (WeeBIT + CEFR-SP datasets): (1) average features (word length, syllables, frequency
  heuristic), (2) uniformity features (coefficient of variation within sentences). Compared three feature sets using 5-fold
  cross-validation with Ridge regression: average-only (R²=0.191), uniformity-only (R²=0.166), combined (R²=0.237). Bootstrap
  confidence intervals (2000 samples) confirmed combined significantly outperforms average-only (p<0.001, 95% CI [0.042, 0.053]).
  Output validates against exp_gen_sol_out schema. Key finding: uniformity features provide significant additional predictive
  power beyond average features.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 5 ---
id: art_rZy90MMefcYA
type: experiment
title: Statistical evaluation of uniformity features for readability
summary: >-
  Comprehensive statistical evaluation of the Uniformity Principle hypothesis for readability assessment. The experiment evaluated
  whether adding variance/uniformity measures of linguistic properties (coefficient of variation of word length, syllables,
  and word frequency) improves readability prediction beyond traditional average-based features. Using two datasets (WeeBIT:
  3,125 sentences, CEFR-SP: 10,004 sentences), five statistical tests were conducted: (1) Paired bootstrap MSE test showing
  12.44% MSE reduction for WeeBIT and 4.57% for CEFR-SP (p < 0.001), (2) Bootstrap 95% confidence intervals for Ridge regression
  coefficients showing cv_syllables and cv_frequency are significant predictors, (3) Proper 5-fold cross-validation with train/test
  separation showing R² improvement of 0.1275 (WeeBIT) and 0.0459 (CEFR-SP), (4) Effect size analysis revealing large effect
  sizes (Cohen's d = 1.55 and 2.40), and (5) Ablation study confirming all uniformity features contribute positively. The
  results strongly support the Uniformity Principle hypothesis, demonstrating that variance/uniformity measures provide significant
  incremental predictive power for readability assessment beyond traditional average-based features.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_experiment_2
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json
</all_artifacts>

<new_artifacts_this_iteration>
NEW THIS ITERATION: These 3 artifacts were created to address the reviewer
feedback. Their findings should be the primary basis for your revisions.

type: dataset
summary: >-
  Successfully acquired 3 readability datasets from HuggingFace, evaluated quality, and selected the best 2 datasets for the
  artifact. Primary acquisition: CLEAR corpus (3,543 excerpts from CommonLit with multiple readability metrics including Flesch-Kincaid
  Grade Level) and agentlans/readability (2,000 sampled paragraphs with continuous grade level scores from arxiv, tinystories,
  fineweb-edu, and wikipedia-en). Both datasets were standardized to exp_sel_data_out.json schema with input (text) and output
  (normalized 0-1 readability score) fields. Created full_data_out.json (5,543 examples), mini_data_out.json (6 examples for
  development), and preview_data_out.json (6 examples with truncated text). All files validated against schema. Documentation
  includes README.md with dataset descriptions, loading instructions, comparison table, and known limitations. WSJ dataset
  (Liu & Lee 2023) was not acquired due to form-based access requirements. OneStopEnglish corpus was acquired but not included
  in final selection due to longer texts and data leakage concerns.
id: art_JC59RgEIB4Y0
title: Readability datasets for sentence-level assessment

type: experiment
summary: >-
  Implemented and executed experiment testing the Uniformity Principle for sentence-level readability prediction. Extracted
  linguistic features from 13,129 sentences (WeeBIT + CEFR-SP datasets): (1) average features (word length, syllables, frequency
  heuristic), (2) uniformity features (coefficient of variation within sentences). Compared three feature sets using 5-fold
  cross-validation with Ridge regression: average-only (R²=0.191), uniformity-only (R²=0.166), combined (R²=0.237). Bootstrap
  confidence intervals (2000 samples) confirmed combined significantly outperforms average-only (p<0.001, 95% CI [0.042, 0.053]).
  Output validates against exp_gen_sol_out schema. Key finding: uniformity features provide significant additional predictive
  power beyond average features.
id: art_oVX_8lj46IX7
title: Uniformity Principle Readability Experiment

type: experiment
summary: >-
  Comprehensive statistical evaluation of the Uniformity Principle hypothesis for readability assessment. The experiment evaluated
  whether adding variance/uniformity measures of linguistic properties (coefficient of variation of word length, syllables,
  and word frequency) improves readability prediction beyond traditional average-based features. Using two datasets (WeeBIT:
  3,125 sentences, CEFR-SP: 10,004 sentences), five statistical tests were conducted: (1) Paired bootstrap MSE test showing
  12.44% MSE reduction for WeeBIT and 4.57% for CEFR-SP (p < 0.001), (2) Bootstrap 95% confidence intervals for Ridge regression
  coefficients showing cv_syllables and cv_frequency are significant predictors, (3) Proper 5-fold cross-validation with train/test
  separation showing R² improvement of 0.1275 (WeeBIT) and 0.0459 (CEFR-SP), (4) Effect size analysis revealing large effect
  sizes (Cohen's d = 1.55 and 2.40), and (5) Ablation study confirming all uniformity features contribute positively. The
  results strongly support the Uniformity Principle hypothesis, demonstrating that variance/uniformity measures provide significant
  incremental predictive power for readability assessment beyond traditional average-based features.
id: art_rZy90MMefcYA
title: Statistical evaluation of uniformity features for readability
</new_artifacts_this_iteration>

<data_files>
Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</data_files>

<task>
Write a research paper draft with LaTeX-ready text, BibTeX citations, and figure placeholders.

YOUR TURN (gen_paper_text): Revise the paper.

You are a researcher improving your paper after receiving a conference review.
Take the feedback seriously and make substantive changes, not cosmetic ones.

1. ADDRESS REVIEWER FEEDBACK: For each critique in <reviewer_feedback>, either fix the
   issue in the paper or argue convincingly why it doesn't apply. Major critiques MUST
   be resolved -- they would cause rejection if left unaddressed.
2. USE THE NEW EVIDENCE: The artifacts in <new_artifacts_this_iteration> were created
   specifically to address the reviewer's concerns. Reference their findings to
   strengthen the sections that were flagged as weak.
3. REWRITE, DON'T PATCH: Don't just append new paragraphs. Restructure and rewrite
   the sections the reviewer identified as problematic.
4. MAINTAIN CONSISTENCY: Ensure the paper aligns with the updated hypothesis.
</task>

<figure_instructions>
FIGURE FORMAT: Use [FIGURE:fig_id] markers in paper_text to indicate where each figure goes.
Then provide the full figure specs in the separate `figures` structured output array.
Each figure in the array must have an `id` matching a marker in the text. Set the `aspect_ratio`
field per figure: 21:9 for architecture / pipeline / flow-chart diagrams (the hero figure should
be one of these — place its marker near the END of the Introduction so it floats to the top of
page 2), 16:9 for comparisons / multi-panel results, 4:3 for dense charts, 1:1 for heatmaps /
confusion matrices / scatter plots.

Example in paper_text:
  "...our method achieves state-of-the-art results as shown below.\n\n[FIGURE:fig3]\n\nThe results demonstrate..."

Example in figures array (results comparison):
  {"id": "fig3", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: latency (seconds, 0-5). Values: PostgreSQL=4.6s (red), Bao=2.8s (blue), RLQOpt=2.0s (green). Error bars +/-0.3-0.8. Sans-serif font, white background.", "aspect_ratio": "16:9", "summary": "Compares latency across optimizers"}

Example in figures array (architecture diagram, hero):
  {"id": "fig1", "title": "System Architecture", "caption": "End-to-end pipeline: encoder feeds latents into the planner, which queries the value head before emitting actions.", "image_gen_detailed_description": "Horizontal flow diagram, left to right. Five labeled boxes: 'Input' (gray), 'Encoder' (blue), 'Latent (z, 256-dim)' (light blue, narrow), 'Planner' (green), 'Action Head' (orange). Arrows labeled with shapes. Value head as separate green box below 'Planner', bidirectional arrow. Sans-serif font, clean white background, no 3D.", "aspect_ratio": "21:9", "summary": "Hero architecture diagram"}

CRITICAL: Before writing figure specs, look through artifact workspace output files (*_out.json)
and code to find ALL the exact values. The figure generator cannot read files — every exact number
and value MUST be in the image_gen_detailed_description.
</figure_instructions>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-writing, aii-semscholar-bib.
TODO 2. LITERATURE REVIEW: Use web search tools to research the landscape — search key terms from
<hypothesis> and <all_artifacts>. Then use aii_semscholar_bib__fetch to batch-fetch real
BibTeX entries. Build a comprehensive Related Work section. Do NOT fabricate entries.
TODO 3. READ ARTIFACTS: Before writing each section, READ the relevant artifact source code, output
files, and data in the workspace. Extract concrete implementation details, technical innovations,
algorithmic specifics, and quantitative results. Do NOT write surface-level descriptions.

ARTIFACT REFERENCES: When you reference results, methodology, or findings from a specific artifact,
place an [ARTIFACT:artifact_id] marker inline. These become footnotes linking to the artifact's code
in the GitHub repository (first mention gets a footnote with URL, subsequent mentions are omitted).
Use the exact artifact ID from <all_artifacts>. Place the marker right after the claim it supports.
Example:
  "Our evaluation showed a 15% improvement over baselines [ARTIFACT:art_4f9d2c81ab37]." 
TODO 4. WRITE PAPER: Write the full paper text with [FIGURE:fig_id] markers per <figure_instructions>,
and provide the figure specs in the figures array. Cite with numeric references [1], [2], etc.
At the end of the paper text, include a full bibliography section. Do NOT compile LaTeX or generate
actual image/figure files. Your ONLY output is the structured JSON.
</todos><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FigureSpec": {
      "description": "Figure specification \u2014 structured output from paper writing agent.\n\nThe LLM fills these as a list in PaperText.figures.\nLater converted to Figure objects for viz gen.",
      "properties": {
        "id": {
          "description": "Figure ID matching the [FIGURE:id] marker in paper_text (e.g., 'fig1')",
          "title": "Id",
          "type": "string"
        },
        "title": {
          "description": "Figure title in plain, everyday language \u2014 short and jargon-free. Aim for about 4-8 words (~40 characters).",
          "title": "Title",
          "type": "string"
        },
        "caption": {
          "description": "LaTeX figure caption \u2014 appears below the figure in the paper. Should describe what the figure shows and highlight key takeaways.",
          "title": "Caption",
          "type": "string"
        },
        "image_gen_detailed_description": {
          "description": "Detailed image generation prompt \u2014 axes, labels, ALL numeric values, colors, aspect ratio, layout. The image generator cannot read files; this is its ONLY input.",
          "title": "Image Gen Detailed Description",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this figure communicates",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "id",
        "title",
        "caption",
        "image_gen_detailed_description",
        "summary"
      ],
      "title": "FigureSpec",
      "type": "object"
    }
  },
  "description": "Paper text \u2014 structured output from paper writing agent.\n\nStructured output fields (LLMPrompt + LLMStructOut):\n- title, abstract, paper_text, figures, summary\n\npaper_text contains [FIGURE:fig_id] markers for positioning.\nfigures contains the full specs as structured objects.\n\nMetadata fields (plain, set by pipeline code):\n- id",
  "properties": {
    "title": {
      "description": "Paper title \u2014 clear, plain-language, and short so a non-expert understands the main contribution at a glance. Aim for about 6-10 words; avoid jargon and acronyms.",
      "title": "Title",
      "type": "string"
    },
    "abstract": {
      "description": "Paper abstract",
      "title": "Abstract",
      "type": "string"
    },
    "paper_text": {
      "description": "Full paper body text with markdown section headers (# Introduction, # Methods, # Results, # Discussion, # Conclusion). Use [FIGURE:fig_id] markers (e.g. [FIGURE:fig1]) to indicate where each figure should appear.",
      "title": "Paper Text",
      "type": "string"
    },
    "figures": {
      "description": "List of figure specifications. Each must have an id matching a [FIGURE:id] marker in paper_text.",
      "items": {
        "$ref": "#/$defs/FigureSpec"
      },
      "title": "Figures",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the paper's main contribution and findings",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "abstract",
    "paper_text",
    "summary"
  ],
  "title": "PaperText",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json`.

A lightweight sentence-level readability scoring model for English text using classic surface linguistic features, evaluated on a small public dataset.
````

### [11] SYSTEM-USER prompt · 2026-07-21 18:19:26 UTC

```
<verification_results>
Your figures have consistency issues that need fixing:

ORPHAN FIGURES (in array but no matching marker in text):
  - Figure id='fig5' in array but no [FIGURE:fig5] marker in text

Summary: 4 unique markers in text, 5 figures in array.
</verification_results>

<task>
Fix ALL issues above. The rule is simple: every [FIGURE:id] marker in paper_text MUST have exactly one matching figure in the figures array, and every figure in the array MUST have a [FIGURE:id] marker in the text.

For orphan figures: either add [FIGURE:id] markers in the text for: fig5, or remove them from the figures array if they are not needed.
</task>
```
