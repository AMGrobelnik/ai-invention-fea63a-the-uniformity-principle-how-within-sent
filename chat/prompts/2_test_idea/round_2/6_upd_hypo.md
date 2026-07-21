# upd_hypo — test_idea

> Phase: `invention_loop` · round 2 · `upd_hypo`
> Run: `run_nOuUUSNqdMp4` — The Uniformity Principle: How Within-Sentence Consistency Predicts Readability
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `upd_hypo` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-21 18:28:24 UTC

````
<current_hypothesis>
The hypothesis as it stands. Revise it based on the evidence below.

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
</current_hypothesis>

<all_artifacts>
Complete set of research artifacts across all iterations.

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
in_dependencies:
- id: art_nzHCg3npeffO
  label: uses
- id: art_zKX1_wXmedjn
  label: methodology
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
in_dependencies:
- id: art_nzHCg3npeffO
  label: uses
- id: art_zKX1_wXmedjn
  label: methodology
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
These 3 artifacts were created THIS iteration.

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

id: art_oVX_8lj46IX7
type: experiment
in_dependencies:
- id: art_nzHCg3npeffO
  label: uses
- id: art_zKX1_wXmedjn
  label: methodology
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

id: art_rZy90MMefcYA
type: experiment
in_dependencies:
- id: art_nzHCg3npeffO
  label: uses
- id: art_zKX1_wXmedjn
  label: methodology
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
</new_artifacts_this_iteration>

<current_paper>
The paper draft from this iteration — represents the current state of the research story.

# The Uniformity Principle: How Within-Sentence Consistency Predicts Readability

## Abstract

Classic readability formulas (e.g., Flesch-Kincaid) rely exclusively on average values of surface linguistic features. This paper introduces the Uniformity Principle: readability is predicted not only by these averages but also by the uniformity (consistent difficulty) of word-level features within a sentence. We evaluate this hypothesis on 13,129 sentences from two public benchmarks (WeeBIT and CEFR-SP) using five-fold cross-validation with Ridge regression. Uniformity features (coefficient of variation of word length, syllable count, and word frequency) are statistically significant predictors of readability scores (p < 0.001), yielding R-squared improvements of +0.127 (95% CI [0.091, 0.153]) on WeeBIT and +0.046 (95% CI [0.037, 0.053]) on CEFR-SP beyond traditional average features. Bootstrap effect sizes are large (Cohen's d = 1.55 and 2.40). The coefficient of variation of syllable counts is the most predictive uniformity feature (coefficient +0.141 on WeeBIT, p < 0.001). These findings support the Uniformity Principle as a previously unrecognized aspect of readability, providing a lightweight and interpretable enhancement to traditional readability assessment.

---

# 1 Introduction

Readability assessment—the task of predicting how difficult a text is to read—has practical applications in education, content creation, and accessibility. Classic readability formulas such as Flesch Reading Ease [1] and Flesch-Kincaid Grade Level [2] operate by computing averages of surface linguistic features: average word length in characters, average sentence length in words, and average syllables per word. These formulas assume that a sentence's difficulty can be reduced to its mean properties.

However, reading is a sequential information processing task. Cognitive load theory suggests that the human brain processes information more efficiently when the rate of information delivery is consistent [3]. In streaming systems, uniform bit rate is easier to decode than variable bit rate. Similarly, in economics, inequality measures like the Gini coefficient predict system efficiency. We hypothesize that a similar principle applies to reading: sentences with uniform word-level difficulty allow readers to establish a consistent processing rhythm, reducing peak cognitive load compared to sentences with bursty difficulty patterns.

We call this the **Uniformity Principle**: the readability of a sentence is predicted not only by average linguistic complexity but also by the uniformity (consistency) of linguistic features within the sentence. Specifically, we propose that sentences with lower coefficient of variation (CV = standard deviation / mean) of word-level features are easier to read than sentences with the same average values but higher CV.

This paper makes the following contributions:

1. **Theoretical contribution**: We formulate the Uniformity Principle as a novel predictor of sentence-level readability, grounded in cognitive load theory and information theory.
2. **Empirical evaluation**: We conduct a systematic evaluation on 13,129 sentences from two established benchmarks (WeeBIT and CEFR-SP) with rigorous statistical testing.
3. **Significant findings**: We show that uniformity features provide statistically significant predictive power beyond traditional features (p < 0.001), with R² improvements of +0.127 (95% CI [0.091, 0.153]) and +0.046 (95% CI [0.037, 0.053]), large effect sizes (Cohen's d = 1.55 and 2.40), and 12.4% and 4.6% MSE reductions [ARTIFACT:art_rZy90MMefcYA].
4. **Feature analysis**: Bootstrap confidence intervals for regression coefficients confirm that cv_syllables and cv_frequency are significant independent predictors; ablation studies quantify each feature's unique contribution.

[FIGURE:fig1]

---

# 2 Related Work

## 2.1 Readability Assessment

Readability assessment has a long history in natural language processing. Classic formulas rely on shallow surface features [1, 2]. Feng et al. [4] conducted a comprehensive comparison of features for automatic readability assessment, evaluating discourse, language modeling, syntactic, part-of-speech, and shallow features. Their Table 5 lists 8 shallow features, all of which are means or averages. To our knowledge, no prior work has investigated the variance or coefficient of variation of these features *within sentences* as a predictor of readability.

Recent work has moved beyond simple formulas. Deutsch et al. [5] evaluated pre-trained transformer models and 255 hand-crafted linguistic features for readability assessment, showing that transformer-based models achieve state-of-the-art performance. Liu and Lee [6] proposed hybrid models combining neural and feature-based approaches for sentence-level readability assessment on the WSJ dataset. However, these modern approaches use traditional average-based features; none incorporate within-sentence uniformity measures.

## 2.2 Variance and Uniformity in Text

Courtis [7] used the coefficient of variation to measure readability variability *across sentences* in corporate reports, finding that high variability indicates obfuscation. This work operates at the document level—measuring how much sentence-level readability varies within a document. Our hypothesis is fundamentally different: we claim that *within-sentence* uniformity of word properties improves readability. While Courtis (2004) showed that documents with variable sentence difficulty are harder to read, we show that sentences with variable word-level difficulty are harder to read. These are complementary findings operating at different levels of text granularity. We are the first to investigate within-sentence variance of word-level features as a predictor of readability.

## 2.3 Cognitive Load Theory

Cognitive load theory posits that working memory has limited capacity [3]. In reading, cognitive load accumulates locally based on word-level difficulty. We hypothesize that uniform information density reduces peak cognitive load. This is consistent with findings from information theory, where uniform bit rate transmission reduces decoding errors [11].

---

# 3 The Uniformity Principle

## 3.1 Hypothesis

The Uniformity Principle states that sentence readability depends not only on average linguistic complexity but also on the uniformity of word-level features within the sentence.

Formally, for a word-level feature *f*, we define:
1. **Average**: μ_f = (1/n) Σ f_i
2. **Uniformity (CV)**: CV_f = σ_f / μ_f

The Uniformity Principle predicts that readability score *R* is a function of both μ_f and CV_f.

## 3.2 Cognitive Motivation

The hypothesis is motivated by three cross-domain principles:
1. **Cognitive Load Theory**: Consistent processing reduces peak working memory load.
2. **Information Theory**: Uniform information density is easier to process than variable density.
3. **Economic Efficiency**: Inequality (measured by Gini or CV) reduces system efficiency.

## 3.3 Feature Definitions

We compute three classes of word-level features:
1. **Word length** in characters
2. **Syllable count** (using CMU Pronouncing Dictionary with heuristic fallback)
3. **Word frequency** (log-transformed, from NLTK Gutenberg corpus)

For each feature, we compute:
- **Average** (traditional readability feature)
- **Coefficient of variation** (uniformity feature)

**Out-of-vocabulary handling**: For syllable counting, we use the CMU Pronouncing Dictionary (123,455 words) as the primary source, with a heuristic fallback that counts vowel groups for out-of-vocabulary (OOV) words. Analysis of both datasets shows OOV rates of 8.2% for WeeBIT and 6.7% for CEFR-SP. For word frequency, words not in the Gutenberg corpus (42,339 words) are assigned a default frequency of 0 (log(1+0) = 0), resulting in OOV rates of 31.4% and 28.9% respectively. Using SUBTLEX-US norms [8] (based on 51M subtitle words) would reduce OOV rates to approximately 5% and improve frequency feature quality; we identify this as an important direction for future work [ARTIFACT:art_zKX1_wXmedjn].

---

# 4 Experiments

## 4.1 Datasets

We evaluate on two public sentence-level readability datasets.

**WeeBIT**: 3,125 sentences from educational materials (Weekly Reader, BBC Bitesize) annotated with 5 age intervals (9-15 years) [9]. Scores normalized to [0, 1] where 0 = easiest.

**CEFR-SP**: 10,004 sentences annotated with CEFR levels (A1-C2) by English education professionals [10]. CEFR levels mapped to 0.0-1.0 (A1=0.0, C2=1.0).

**Dataset statistics**: Combined, the datasets contain 13,129 sentences with mean readability scores of 0.51 (WeeBIT) and 0.49 (CEFR-SP). Sentence lengths range from 3 to 68 words (mean = 18.3, SD = 8.7).

[FIGURE:fig2]

## 4.2 Experimental Setup

**Feature computation**: Syllable counting uses the CMU Pronouncing Dictionary via the `pronouncing` library, with a heuristic fallback for OOV words that counts vowel groups (y-handling, silent-e adjustment). Word frequency uses the NLTK Gutenberg corpus (42,339 words from literary texts), with OOV words assigned frequency = 0.

**Models**: We use Ridge regression (α = 1.0) with 5-fold cross-validation. Ridge regression is appropriate for this feature space (7 features) as it handles potential multicollinearity between average and uniformity features.

**Feature sets compared**:
1. **Average only**: avg_word_length, avg_syllables, avg_frequency, sentence_length
2. **Uniformity only**: cv_word_length, cv_syllables, cv_frequency
3. **Combined**: All 7 features

**Statistical evaluation**: We employ five complementary statistical tests [ARTIFACT:art_rZy90MMefcYA]:
1. **Paired bootstrap MSE test** (5,000 samples) for significance of MSE reduction
2. **Bootstrap 95% confidence intervals** for Ridge regression coefficients
3. **Proper 5-fold cross-validation** with train/test separation
4. **Effect size analysis** with Cohen's d and 95% CI for R² difference
5. **Ablation study** (add-one-in, remove-one-out) for feature contribution

## 4.3 Results

### 4.3.1 Main Results

Table 1 shows the cross-validated R² and MSE for all feature sets on both datasets.

[FIGURE:fig3]

**WeeBIT** (n = 3,125):
- Average only: R² = 0.248 ± 0.027
- Uniformity only: R² = 0.198 ± 0.021
- Combined: R² = 0.376 ± 0.035
- R² improvement (combined vs. average): +0.127 (95% CI [0.091, 0.153])
- MSE reduction: 12.44% (p < 0.001, one-sided bootstrap test)
- Cohen's d: 1.55 (large effect)

**CEFR-SP** (n = 10,004):
- Average only: R² = 0.544 ± 0.009
- Uniformity only: R² = 0.487 ± 0.011
- Combined: R² = 0.590 ± 0.006
- R² improvement (combined vs. average): +0.046 (95% CI [0.037, 0.053])
- MSE reduction: 4.57% (p < 0.001, one-sided bootstrap test)
- Cohen's d: 2.40 (large effect)

### 4.3.2 Coefficient Significance

Bootstrap 95% confidence intervals (5,000 samples) for Ridge regression coefficients on the combined model show:

**WeeBIT significant predictors** (CI does not include 0):
- cv_syllables: β = 0.141 (95% CI [0.125, 0.157])
- sentence_length: β = 0.108 (95% CI [0.099, 0.117])
- avg_word_length: β = -0.127 (95% CI [-0.152, -0.102])
- cv_frequency: β = 0.104 (95% CI [0.069, 0.138])

**CEFR-SP significant predictors**:
- cv_word_length: β = 0.017 (95% CI [0.014, 0.021])
- cv_syllables: β = 0.018 (95% CI [0.014, 0.021])
- cv_frequency: β = 0.066 (95% CI [0.060, 0.072])
- sentence_length: β = 0.087 (95% CI [0.084, 0.089])
- avg_word_length: β = 0.043 (95% CI [0.037, 0.049])

All three uniformity features (cv_syllables, cv_word_length, cv_frequency) are significant predictors on CEFR-SP. On WeeBIT, cv_syllables and cv_frequency are significant; cv_word_length is not significant when controlling for other features.

[FIGURE:fig5]

### 4.3.3 Ablation Study

The ablation study (Table 2) quantifies each uniformity feature's unique contribution by adding features one-at-a-time to the average-only baseline.

**WeeBIT R² improvements over baseline (ΔR²)**:
- + cv_syllables: +0.116 (largest contribution)
- + cv_frequency: +0.025
- + cv_word_length: +0.038

**CEFR-SP R² improvements over baseline (ΔR²)**:
- + cv_frequency: +0.032 (largest contribution)
- + cv_word_length: +0.022
- + cv_syllables: +0.014

Remove-one-out analysis confirms these findings: removing cv_syllables from the combined model reduces R² by 0.080 on WeeBIT and 0.003 on CEFR-SP.

[FIGURE:fig4]

---

# 5 Discussion

## 5.1 Interpretation of Results

The results strongly confirm the Uniformity Principle hypothesis. Adding uniformity features significantly improves readability prediction on both datasets, with large effect sizes (Cohen's d > 1.5). The improvement is particularly strong for cv_syllables on WeeBIT (β = 0.141, 95% CI [0.125, 0.157]), suggesting that sentences with varying syllable counts are substantially more difficult to read.

The positive coefficients for all uniformity features indicate that higher within-sentence variance (less uniformity) is associated with higher reading difficulty. This supports our cognitive motivation: non-uniform information density increases peak cognitive load.

## 5.2 Comparison to Prior Work

Our finding that all existing readability formulas use only average features [4] positions the Uniformity Principle as a novel enhancement. Classic formulas like Flesch-Kincaid can be viewed as linear combinations of average features; our results show these formulas miss the uniformity signal that explains an additional 4.6-12.8% of variance.

Compared to modern neural approaches [5, 6], our method is intentionally simpler and more interpretable. While BERT-based models achieve higher absolute R² on these datasets (reported R² ≈ 0.65-0.75 on WeeBIT [5]), our lightweight approach offers advantages in explainability, computational efficiency, and domains where neural models are impractical. Future work should investigate whether adding uniformity features to neural baselines yields further improvements.

## 5.3 Limitations

**Word frequency norms**: This study uses the NLTK Gutenberg corpus for word frequency, which our earlier research identified as suboptimal compared to SUBTLEX-US norms [8]. SUBTLEX-US is based on 51 million words from film subtitles and better predicts word processing times. Using SUBTLEX-US would likely improve the quality of frequency-based uniformity features and increase R² improvements [ARTIFACT:art_zKX1_wXmedjn].

**Dataset scope**: Evaluation is limited to two sentence-level datasets. WeeBIT has only 5 readability levels and was originally designed for document-level assessment. CEFR-SP sentences are annotated based on document-level CEFR ratings rather than direct sentence-level annotation. A third dataset (CLEAR corpus, 3,543 excerpts with continuous grade-level scores [13]) was acquired but not included in the current experiments due to time constraints [ARTIFACT:art_JC59RgEIB4Y0]. The generalizability of results to document-level readability and to other languages is not yet established.

**Baseline comparison**: While Ridge regression with uniformity features significantly outperforms Ridge regression with average features, we have not compared against modern neural baselines (e.g., BERT-based readability assessment [5]) or comprehensive feature sets (e.g., LingFeat with 255 features [11]). It is possible that neural models already capture uniformity information implicitly through their learned representations. We consider this an important avenue for future work.

**Out-of-vocabulary rates**: CMUdict OOV rates (6.7-8.2%) are handled with a heuristic fallback; SUBTLEX-US OOV rates would be lower (~5%). Gutenberg corpus OOV rates (28.9-31.4%) are high, supporting the case for SUBTLEX-US adoption.

## 5.4 Practical Applications

The Uniformity Principle enables several practical applications:

1. **Lightweight readability scoring**: Uniformity features add only 3 features to traditional formulas, maintaining computational efficiency while improving accuracy.

2. **Text simplification guidance**: Identifying sentences with high CV (low uniformity) provides actionable targets for simplification. For example, a sentence with high cv_syllables could be revised to use more consistent syllable patterns.

3. **Curriculum design**: Educators can use uniformity metrics to select texts with appropriate consistency levels for different learner stages.

A demonstration of text simplification guidance is provided in Appendix A, showing how uniformity analysis identifies revision targets in sample sentences.

---

# 6 Conclusion

This paper introduced the Uniformity Principle: the hypothesis that within-sentence uniformity of word-level linguistic features predicts readability independently of traditional average features. Through systematic evaluation on 13,129 sentences from two public benchmarks with rigorous statistical testing, we demonstrated that:

1. Uniformity features are statistically significant predictors (p < 0.001)
2. Adding uniformity features yields R² improvements of +0.127 and +0.046 with large effect sizes (Cohen's d = 1.55 and 2.40)
3. cv_syllables and cv_frequency are significant independent predictors with bootstrap 95% CIs excluding zero
4. Ablation studies confirm each uniformity feature contributes uniquely to predictive performance

These findings suggest that the Uniformity Principle captures a previously unrecognized aspect of readability. We hope this work inspires further research into uniformity-based features for readability assessment, including adoption of SUBTLEX-US frequency norms, evaluation on document-level corpora, and investigation of whether neural readability models benefit from explicit uniformity features.

---

# Acknowledgments

We thank the anonymous reviewers for their constructive feedback.

---

# References

[1] Flesch, R. (1948). A new readability yardstick. *Journal of Applied Psychology*, 32(3), 221-233.

[2] Kincaid, J. P., Fishburne, R. P., Rogers, R. L., & Chissom, B. S. (1975). Derivation of new readability formulas (Automated Readability Index, Fog Count and Flesch Reading Ease Formula) for Navy enlisted personnel. *Naval Technical Training Command*.

[3] Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science*, 12(2), 257-285.

[4] Feng, L., Jansche, M., Huenerfauth, M., & Elhadad, N. (2010). A comparison of features for automatic readability assessment. In *Coling 2010: Posters* (pp. 276-284).

[5] Deutsch, T., Jasbi, M., & Shieber, S. M. (2020). Linguistic features for readability assessment. In *Proceedings of the 15th Workshop on Innovative Use of NLP for Building Educational Applications* (pp. 1-17).

[6] Liu, F., & Lee, J. (2023). Hybrid models for sentence readability assessment. In *Proceedings of the 18th Workshop on Innovative Use of NLP for Building Educational Applications* (pp. 37-48).

[7] Courtis, J. K. (2004). Corporate report obfuscation: artefact or phenomenon? *Journal of Business Communication*, 41(2), 141-163.

[8] Brysbaert, M., & New, B. (2009). Moving beyond Kučera and Francis: A critical evaluation of current word frequency norms and the introduction of a new and improved word frequency measure for American English. *Behavior Research Methods*, 41(4), 977-990.

[9] Vajjala, S., & Meurers, D. (2012). WeeBIT: A corpus of alphabetically sorted texts for readability research. In *Proceedings of the Eighth International Conference on Language Resources and Evaluation (LREC'12)*.

[10] Xia, M., Kochmar, E., & Briscoe, T. (2023). CEFR-SP: A sentence-level corpus for CEFR level prediction. In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing*.

[11] Lee, B., & Lee, J. (2021). LingFeat: A Python toolkit for exhaustive linguistic feature extraction. *GitHub repository*.

---

# Appendix A: Text Simplification Demonstration

To demonstrate practical application, we analyze three sentences from the WeeBIT dataset with high cv_syllables values:

**Original**: "Photosynthesis is a process used by plants to convert light energy into chemical energy." (cv_syllables = 0.47, predicted readability = 0.71)

**Simplified**: "Plants use photosynthesis to turn light into chemical energy." (cv_syllables = 0.21, predicted readability = 0.52)

The simplification reduces syllable count variance by replacing polysyllabic words ("process," "convert," "energy" × 2) with more uniform alternatives, demonstrating how uniformity analysis guides revision.

---

# Figure Captions

**Figure 1**: Conceptual illustration of the Uniformity Principle. Left: A sentence with uniform word difficulty (low CV) allows consistent processing rhythm. Right: A sentence with variable word difficulty (high CV) creates peak cognitive load spikes. The figure shows a hypothetical cognitive load trace over time for each case.

**Figure 2**: Dataset characteristics. (a) Distribution of readability scores for WeeBIT (5 levels, n=3,125) and CEFR-SP (6 levels mapped to continuous, n=10,004). (b) Sentence length distributions. (c) Word length distributions. All figures show the combined 13,129 sentences used in experiments.

**Figure 3**: Main results. Bar chart showing cross-validated R² for three feature sets (average only, uniformity only, combined) on both datasets. Error bars show ±1 SD across 5 folds. Combined significantly outperforms average only on both datasets (p < 0.001, bootstrap test). WeeBIT: R² = 0.248 → 0.376 (+0.127). CEFR-SP: R² = 0.544 → 0.590 (+0.046).

**Figure 4**: Ablation study results. Bar chart showing R² improvement from adding each uniformity feature to the average-only baseline. WeeBIT: cv_syllables contributes +0.116, cv_frequency +0.025, cv_word_length +0.038. CEFR-SP: cv_frequency contributes +0.032, cv_word_length +0.022, cv_syllables +0.014. Error bars show ±1 SD.

**Figure 5**: Bootstrap coefficient confidence intervals. Forest plot showing 95% CIs for Ridge regression coefficients on the combined model. WeeBIT (top): cv_syllables (β=0.141, CI[0.125,0.157]) and cv_frequency (β=0.104, CI[0.069,0.138]) are significant predictors. CEFR-SP (bottom): all three uniformity features are significant. Coefficients > 0 indicate higher CV (less uniformity) predicts higher difficulty.
</current_paper>

<reviewer_feedback>
Feedback from the paper reviewer this iteration.

- [MAJOR] (methodology) The paper uses NLTK Gutenberg corpus (42,339 words from literary texts) for word frequency computation, which the authors' own research artifact (art_zKX1_wXmedjn) identifies as suboptimal. The artifact states: 'SUBTLEX-US norms (based on 51M subtitle words) significantly outperform older norms in predicting word processing times.' Using Gutenberg corpus likely reduces the quality of the frequency-based uniformity features, potentially understating the Uniformity Principle's effectiveness.
  Action: Replace NLTK Gutenberg corpus with SUBTLEX-US word frequency norms. The SUBTLEX-US data is freely available from Ghent University (http://crr.ugent.be/archives/1423). Use the Zipf scale values or SUBTL WF (word frequency per million) for computing word frequency uniformity. This change is straightforward and will improve the quality of the frequency features. The OOV rate should drop from ~30% to ~5%, substantially improving cv_frequency quality.
- [MAJOR] (methodology) The paper only uses Ridge regression as the evaluation model. This is a weak baseline that does not represent the current state of readability assessment. Recent work (Deutsch et al. 2020, Liu & Lee 2023) has shown that neural models and comprehensive feature sets achieve much higher performance. Without comparing to these stronger baselines, it's unclear whether uniformity features provide value beyond what's already captured by modern methods. It's possible that BERT-based models already capture uniformity information implicitly.
  Action: Add experiments with at least one modern neural baseline (e.g., BERT-based readability assessment as in Deutsch et al. 2020) and one comprehensive feature-based baseline (e.g., LingFeat or the 255 features from Deutsch et al. 2020). Show whether adding uniformity features to these stronger baselines still yields improvements. If the improvement disappears with stronger baselines, the contribution is much weaker than claimed. At minimum, discuss this limitation more explicitly in Section 5.3.
- [MAJOR] (scope) The evaluation is limited to only 2 sentence-level datasets (WeeBIT and CEFR-SP). Both datasets have limitations: WeeBIT has only 5 readability levels and was originally designed for document-level assessment; CEFR-SP sentences are annotated based on document-level CEFR ratings, not direct sentence-level annotation. The generalizability of the results to other datasets, to document-level readability, and to languages other than English is not established. The CLEAR corpus (3,543 excerpts) was acquired (per art_JC59RgEIB4Y0) but not included.
  Action: Add evaluation on at least one more dataset. The CLEAR corpus has been acquired (per the supplementary materials) and should be included - it has continuous grade-level scores which are better suited for regression. Alternatively, evaluate on a document-level dataset to test whether the Uniformity Principle generalizes beyond sentence-level assessment. Also discuss the limitations of the current evaluation more explicitly in Section 5.3.
- [MINOR] (novelty) The paper states 'To our knowledge, no prior work has investigated the variance or coefficient of variation of these features within sentences as a predictor of readability.' While this appears true for word-level features, the relationship to Courtis (2004) could be clearer. Courtis investigated readability VARIABILITY at the document level (using coefficient of variation across sentences in corporate reports). The paper correctly distinguishes this but could be more explicit about the relationship to prior work at the beginning of Section 2.2.
  Action: In Section 2.2, add a more detailed discussion of Courtis (2004) and explicitly state that while Courtis operated at the document level (variance across sentences), this paper is the first to investigate within-sentence variance of word-level features. This strengthens rather than weakens the paper's novelty claim by showing awareness of related concepts at other levels of granularity.
- [MINOR] (rigor) The paper does not report out-of-vocabulary (OOV) rates for the CMU Pronouncing Dictionary, nor does it provide sensitivity analysis for the heuristic fallback in syllable counting. The research artifact mentions that CMUdict has 123,455 words, but typical readability assessment texts may contain words not in this dictionary (e.g., domain-specific terms, named entities, rare words).
  Action: Report the OOV rate for CMUdict on both datasets. The heuristic fallback (counting vowel groups) should be documented more clearly in Section 4.2. A brief sensitivity analysis showing the impact of OOV handling on results would further strengthen the paper. For example, compare results when OOV words are excluded vs. when the heuristic is used.
- [MINOR] (clarity) Figure references (FIGURE:fig1 through FIGURE:fig5) are placeholders without actual figures. While the instructions state that figures should be assumed to show exactly what the caption describes, having no figures makes it difficult to evaluate whether the results are presented clearly and whether the figures effectively communicate the findings. The figure captions in the paper are detailed, but actual visualizations would substantially improve readability.
  Action: Generate actual figures for all 5 figures. At minimum, provide detailed specifications including what each figure shows, what the axes are, what the error bars represent, etc. The figures are critical for communicating the R² improvements, ablation results, and coefficient confidence intervals. Consider using matplotlib or seaborn to create bar charts for Figures 3 and 4, and a forest plot for Figure 5.
- [MINOR] (scope) Section 5.4 claims practical applications in 'Lightweight readability scoring, Text simplification guidance, Curriculum design' but does not demonstrate or evaluate any of these applications. The paper is purely an empirical evaluation of whether uniformity features predict readability, without demonstrating end-to-end utility. Appendix A provides a brief demonstration, but it's not integrated into the main text.
  Action: Either add a demonstration of one practical application in the main text (e.g., show how uniformity features can guide text simplification by identifying sentences with high CV that should be simplified) or tone down the claims about practical applications in Section 5.4. A short demonstration or case study integrated into Section 5.4 would substantially strengthen the paper and justify the applications claimed.
- [MINOR] (evidence) The paper reports positive coefficients for uniformity features, indicating that higher within-sentence variance is associated with higher reading difficulty. This is plausible and supported by bootstrap CIs that exclude zero for most features. However, the interpretation could be strengthened by discussing potential alternative explanations or confounding factors. For example, are uniformity features simply capturing sentence length effects? (Longer sentences may have more variable word properties by chance.)
  Action: Add a brief discussion of potential confounding factors and alternative explanations. For example, analyze whether the uniformity effect holds when controlling for sentence length, or whether certain types of sentences (e.g., lists, definitions) have artificially high CV. This would strengthen the interpretation of the results and address potential reviewer concerns about whether CV is merely a proxy for other factors.
</reviewer_feedback>



<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the field's landscape, prior work, crowded lanes, and the novelty bar — consult it while revising so the updated hypothesis stays genuinely novel and well-positioned.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<task>
IMPORTANT: Your ONLY output is the revised hypothesis text. Do NOT run code, produce artifacts,
fix bugs, or attempt to address the evidence yourself — the next iteration of the invention loop
will generate fresh artifacts based on your revised hypothesis. Reflect and rewrite; nothing else.

Do NOT generate a completely new hypothesis. Take the current hypothesis and REVISE it
to incorporate new evidence. Keep the core idea — refine, narrow, or strengthen it.

1. Does the evidence support the hypothesis? Narrow or broaden scope as needed.
2. Which claims now have strong evidence? Which are still unsupported?
3. Should the hypothesis become more specific based on what we've learned?
4. If reviewer feedback is provided, address the critiques directly.

STABILITY IS OK: If progress is good and evidence supports the current direction, keep the
hypothesis similar or identical. Only make substantive changes when evidence clearly calls for
them — e.g., contradictory results, fundamental reviewer critiques, or findings that refine scope.

You must also classify two kinds of edges in the research trace:

(A) The H↔H edge — how does this revised hypothesis relate to the previous one?
    Set `relation_type` (Moulines's structuralist typology) to one of:
    - "evolution": refining specialised claims, same conceptual frame
    - "embedding": previous hypothesis is now a special case of a broader frame
    - "replacement": rejecting the previous frame entirely (Kuhnian shift)
    Set `relation_rationale` to a brief justification (≤120 chars).

(B) The A↔A edges — for each artifact created THIS iteration, classify each of its
    `in_dependencies` (predecessor → dependent) using MultiCite's citation-function
    typology (Lauscher et al., NAACL 2022) — emit one entry in `artifact_relations`
    per (predecessor, dependent) pair. Predecessors are ALWAYS artifacts from EARLIER
    iterations — artifacts within one iteration run in parallel and cannot depend on
    each other, so never emit a relation between two same-iteration artifacts (it
    will be dropped):
    - "background": predecessor is treated as background context
    - "motivation": predecessor motivated this artifact's research
    - "uses": this artifact uses the predecessor's data, method, or output
    - "extends": this artifact extends the predecessor
    - "similarities": this artifact's results agree with the predecessor's
    - "differences": this artifact's results disagree with the predecessor's
    Each `relation_rationale` must be ≤120 characters.

Output the COMPLETE revised hypothesis (with the H↔H relation fields) AND the full
list of A↔A `artifact_relations` for this iteration's new artifacts.
</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ArtifactRelation": {
      "description": "One typed A\u2194A edge between a dependent artifact and one of its in_dependencies.\n\nMultiCite citation-function typology (Lauscher et al., NAACL 2022),\nreduced to 6 plain-English types.",
      "properties": {
        "from_id": {
          "description": "ID of the predecessor artifact (the one being depended on)",
          "title": "From Id",
          "type": "string"
        },
        "to_id": {
          "description": "ID of the dependent artifact (the new artifact this iteration)",
          "title": "To Id",
          "type": "string"
        },
        "relation_type": {
          "description": "MultiCite citation-function type for the predecessor\u2192dependent edge: 'background' \u2014 predecessor is treated as background context; 'motivation' \u2014 predecessor motivated this artifact's research; 'uses' \u2014 this artifact uses the predecessor's data, method, or output; 'extends' \u2014 this artifact extends the predecessor; 'similarities' \u2014 this artifact's results agree with the predecessor's; 'differences' \u2014 this artifact's results disagree with the predecessor's.",
          "enum": [
            "background",
            "motivation",
            "uses",
            "extends",
            "similarities",
            "differences"
          ],
          "title": "Relation Type",
          "type": "string"
        },
        "relation_rationale": {
          "description": "Brief rationale for this relation type (one short line, max 120 characters).",
          "maxLength": 120,
          "title": "Relation Rationale",
          "type": "string"
        }
      },
      "required": [
        "from_id",
        "to_id",
        "relation_type",
        "relation_rationale"
      ],
      "title": "ArtifactRelation",
      "type": "object"
    }
  },
  "description": "Revised hypothesis after reviewing iteration results.\n\nOutput matches the hypothesis dict structure so it can replace the\noriginal hypothesis in subsequent iterations.",
  "properties": {
    "title": {
      "description": "Revised hypothesis title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); may be unchanged if still accurate.",
      "title": "Title",
      "type": "string"
    },
    "hypothesis": {
      "description": "Revised hypothesis statement \u2014 what we now believe based on evidence",
      "title": "Hypothesis",
      "type": "string"
    },
    "relation_rationale": {
      "description": "Brief rationale for the H\u2194H revision type (one short line, max 120 characters).",
      "maxLength": 120,
      "title": "Relation Rationale",
      "type": "string"
    },
    "confidence_delta": {
      "description": "How confidence changed: 'increased', 'decreased', or 'unchanged'",
      "title": "Confidence Delta",
      "type": "string"
    },
    "key_changes": {
      "description": "Bullet list of specific changes made to the hypothesis",
      "items": {
        "type": "string"
      },
      "title": "Key Changes",
      "type": "array"
    },
    "relation_type": {
      "description": "Moulines's structuralist typology of this hypothesis revision: 'evolution' \u2014 refining specialised claims while keeping the same conceptual frame; 'embedding' \u2014 the previous hypothesis is now a special case of a broader frame; 'replacement' \u2014 rejecting the previous frame entirely (incommensurable, Kuhnian revolution).",
      "enum": [
        "evolution",
        "embedding",
        "replacement"
      ],
      "title": "Relation Type",
      "type": "string"
    },
    "artifact_relations": {
      "description": "Typed A\u2194A edges for this iteration's new artifacts. Emit one entry per (predecessor \u2192 dependent) edge for every in_dependency on each artifact produced this iteration.",
      "items": {
        "$ref": "#/$defs/ArtifactRelation"
      },
      "title": "Artifact Relations",
      "type": "array"
    }
  },
  "required": [
    "title",
    "hypothesis",
    "relation_rationale",
    "confidence_delta",
    "key_changes",
    "relation_type"
  ],
  "title": "RevisedHypothesis",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-21 18:28:24 UTC

```
A lightweight sentence-level readability scoring model for English text using classic surface linguistic features, evaluated on a small public dataset.
```
