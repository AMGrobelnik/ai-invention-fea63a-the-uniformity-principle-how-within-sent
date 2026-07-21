# review_paper — test_idea

> Phase: `invention_loop` · round 2 · `review_paper`
> Run: `run_nOuUUSNqdMp4` — The Uniformity Principle: How Within-Sentence Consistency Predicts Readability
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `review_paper` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-21 18:24:16 UTC

````
<role>
You are a very experienced and critical conference reviewer specialized in the domain of the work under review.
You have reviewed for top-tier venues in the relevant field. Your reviews are known for
being thorough, fair, and grounded in the actual state of the field.
</role>

<paper>
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
</paper>

<supplementary_materials>
The authors' code, data, and experimental artifacts. You may read these to verify
claims made in the paper — check if the code matches the described methodology,
if the results are reproducible, and if the data supports the conclusions.

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
</supplementary_materials>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for judging whether the paper's contribution is genuinely novel versus already-done or a known dead end in this field.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<previous_review>
Your review from the previous iteration. Check which critiques have been addressed
in the revised paper. Do NOT re-raise critiques that have been adequately fixed.
Only re-raise if the fix is insufficient.

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
</previous_review>

<task>
Review this paper as you would for a top-tier venue submission.

STEP 1 — READ THE PAPER: Read it carefully. Note claims, methodology, and results.

STEP 2 — CHECK THE CODE: Read the supplementary materials to verify the paper's claims.
Do the experiments match what's described? Are there discrepancies between code and paper?

STEP 3 — SEARCH THE LITERATURE: Ground your review in evidence.
- Search for the closest existing work — is this genuinely novel or incremental?
- Check if the proposed methodology has known failure modes
- What level of contribution gets accepted at top venues in this area?

STEP 4 — WRITE YOUR REVIEW:
For each critique:
1. Categorize: methodology, evidence, novelty, clarity, scope, or rigor
2. Rate severity: major (would cause rejection) or minor (polish)
3. Describe the issue clearly
4. Suggest a concrete action to address it

Focus on the most impactful issues. Provide your review via structured output.
</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/review_paper/review_paper/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "Critique": {
      "description": "A single actionable critique from the reviewer.",
      "properties": {
        "category": {
          "description": "Category: 'methodology', 'evidence', 'novelty', 'clarity', 'scope', or 'rigor'",
          "title": "Category",
          "type": "string"
        },
        "severity": {
          "description": "Severity: 'major' or 'minor'",
          "title": "Severity",
          "type": "string"
        },
        "description": {
          "description": "Clear description of the issue",
          "title": "Description",
          "type": "string"
        },
        "suggested_action": {
          "description": "Concrete suggestion for how to address this critique",
          "title": "Suggested Action",
          "type": "string"
        }
      },
      "required": [
        "category",
        "severity",
        "description",
        "suggested_action"
      ],
      "title": "Critique",
      "type": "object"
    },
    "DimensionScore": {
      "description": "Score for a single review dimension with improvement suggestions.",
      "properties": {
        "dimension": {
          "description": "Dimension name: 'soundness', 'presentation', or 'contribution'",
          "title": "Dimension",
          "type": "string"
        },
        "score": {
          "description": "Score from 1 (poor) to 4 (excellent)",
          "title": "Score",
          "type": "integer"
        },
        "justification": {
          "description": "Brief justification for this score",
          "title": "Justification",
          "type": "string"
        },
        "improvements": {
          "description": "Specific improvements to raise the score (what + how + why)",
          "items": {
            "type": "string"
          },
          "title": "Improvements",
          "type": "array"
        }
      },
      "required": [
        "dimension",
        "score",
        "justification"
      ],
      "title": "DimensionScore",
      "type": "object"
    }
  },
  "description": "Adversarial review of the paper draft.\n\nID format: review_it{iteration}__{model}",
  "properties": {
    "overall_assessment": {
      "description": "Overall assessment of the paper's quality and readiness",
      "title": "Overall Assessment",
      "type": "string"
    },
    "strengths": {
      "description": "Key strengths of the paper",
      "items": {
        "type": "string"
      },
      "title": "Strengths",
      "type": "array"
    },
    "dimension_scores": {
      "description": "Scores (1-4) for: soundness, presentation, contribution",
      "items": {
        "$ref": "#/$defs/DimensionScore"
      },
      "title": "Dimension Scores",
      "type": "array"
    },
    "critiques": {
      "description": "Actionable critiques \u2014 specific issues with concrete suggestions",
      "items": {
        "$ref": "#/$defs/Critique"
      },
      "title": "Critiques",
      "type": "array"
    },
    "score": {
      "description": "Overall quality score from 1 (very strong reject) to 10 (award quality)",
      "title": "Score",
      "type": "integer"
    },
    "confidence": {
      "default": 3,
      "description": "Confidence in assessment from 1 (educated guess) to 5 (absolutely certain)",
      "title": "Confidence",
      "type": "integer"
    }
  },
  "required": [
    "overall_assessment",
    "strengths",
    "critiques",
    "score"
  ],
  "title": "ReviewerFeedback",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/review_paper/review_paper/.sdk_openhands_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-21 18:24:16 UTC

```
A lightweight sentence-level readability scoring model for English text using classic surface linguistic features, evaluated on a small public dataset.
```

### [3] SKILL-INPUT — aii-web-research-tools · 2026-07-21 18:24:40 UTC

The agent loaded the **aii-web-research-tools** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-web-research-tools
description: "Comprehensive web research toolkit — use whenever a task needs MORE than a handful of WebSearch/WebFetch calls (multi-source literature reviews, deep verification across many pages, paper/PDF mining, cross-referencing claims, building bibliographies). Not for single quick lookups — use raw WebSearch/WebFetch for those. Adds aii_web_tools__fetch_grep for exact regex extraction over HTML or PDFs (arXiv, journals) with context windows, beyond what WebFetch's lossy summary returns. Trigger: any extensive/comprehensive/deep research task, literature review, multi-source investigation, verify many citations, arxiv, paper, PDF, exact quote, methodology, table value, regex."
---

## Available Web Tools

Three levels of web tools:

1. **WebSearch** — broad discovery. Returns titles, URLs, snippets. Cheapest. Use first to scan the landscape.
2. **WebFetch** — read a specific page. LLM summarizes it. HTML only. May miss specific details.
3. **aii_web_tools__fetch_grep** — exact text extraction from HTML or PDF. Regex matching with context windows.
   Use for precise details, methodology, or when WebFetch missed something.
   Key params: pattern (required), max_matches (default 20), context_chars (default 200 per side).

**Workflow:** WebSearch → WebFetch for gist → aii_web_tools__fetch_grep for exact details or PDFs.

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-web-research-tools"
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [4] SKILL-INPUT — aii-web-tools · 2026-07-21 18:25:06 UTC

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
