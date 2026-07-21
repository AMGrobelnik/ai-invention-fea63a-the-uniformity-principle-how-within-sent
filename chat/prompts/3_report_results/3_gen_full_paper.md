# gen_full_paper — report_results

> Phase: `gen_paper_repo` · `gen_full_paper`
> Run: `run_nOuUUSNqdMp4` — The Uniformity Principle: How Within-Sentence Consistency Predicts Readability
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_full_paper` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-21 18:56:20 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<task>
Create a publication-ready top-conference LaTeX paper with BibTeX from <paper_text> and <available_figures>, compile to PDF.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<paper_text>
title: 'The Uniformity Principle: How Within-Sentence Consistency Predicts Readability'
abstract: >-
  Classic readability formulas (e.g., Flesch-Kincaid) rely exclusively on average values of surface linguistic features. This
  paper introduces the Uniformity Principle: readability is predicted not only by these averages but also by the uniformity
  (consistent difficulty) of word-level features within a sentence. We evaluate this hypothesis on 13,129 sentences from two
  public benchmarks (WeeBIT and CEFR-SP) using five-fold cross-validation with Ridge regression. Uniformity features (coefficient
  of variation of word length, syllable count, and word frequency) are statistically significant predictors of readability
  scores (p < 0.001), yielding R-squared improvements of +0.127 (95% CI [0.091, 0.153]) on WeeBIT and +0.046 (95% CI [0.037,
  0.053]) on CEFR-SP beyond traditional average features. Bootstrap effect sizes are large (Cohen's d = 1.55 and 2.40). The
  coefficient of variation of syllable counts is the most predictive uniformity feature (coefficient +0.141 on WeeBIT, p <
  0.001). These findings support the Uniformity Principle as a previously unrecognized aspect of readability, providing a
  lightweight and interpretable enhancement to traditional readability assessment.
paper_text: |-
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
  3. **Significant findings**: We show that uniformity features provide statistically significant predictive power beyond traditional features (p < 0.001), with R² improvements of +0.127 (95% CI [0.091, 0.153]) and +0.046 (95% CI [0.037, 0.053]), large effect sizes (Cohen's d = 1.55 and 2.40), and 12.4% and 4.6% MSE reductions \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-fea63a-the-uniformity-principle-how-within-sent/tree/main/round-2/experiment-2}}.
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

  **Out-of-vocabulary handling**: For syllable counting, we use the CMU Pronouncing Dictionary (123,455 words) as the primary source, with a heuristic fallback that counts vowel groups for out-of-vocabulary (OOV) words. Analysis of both datasets shows OOV rates of 8.2% for WeeBIT and 6.7% for CEFR-SP. For word frequency, words not in the Gutenberg corpus (42,339 words) are assigned a default frequency of 0 (log(1+0) = 0), resulting in OOV rates of 31.4% and 28.9% respectively. Using SUBTLEX-US norms [8] (based on 51M subtitle words) would reduce OOV rates to approximately 5% and improve frequency feature quality; we identify this as an important direction for future work \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-fea63a-the-uniformity-principle-how-within-sent/tree/main/round-1/research-1}}.

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

  **Statistical evaluation**: We employ five complementary statistical tests :
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

  **Word frequency norms**: This study uses the NLTK Gutenberg corpus for word frequency, which our earlier research identified as suboptimal compared to SUBTLEX-US norms [8]. SUBTLEX-US is based on 51 million words from film subtitles and better predicts word processing times. Using SUBTLEX-US would likely improve the quality of frequency-based uniformity features and increase R² improvements .

  **Dataset scope**: Evaluation is limited to two sentence-level datasets. WeeBIT has only 5 readability levels and was originally designed for document-level assessment. CEFR-SP sentences are annotated based on document-level CEFR ratings rather than direct sentence-level annotation. A third dataset (CLEAR corpus, 3,543 excerpts with continuous grade-level scores [13]) was acquired but not included in the current experiments due to time constraints \footnote{Code: \url{https://github.com/AMGrobelnik/ai-invention-fea63a-the-uniformity-principle-how-within-sent/tree/main/round-2/dataset-1}}. The generalizability of results to document-level readability and to other languages is not yet established.

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
summary: >-
  This paper introduces the Uniformity Principle: the hypothesis that within-sentence uniformity of word-level linguistic
  features (measured by coefficient of variation of word length, syllables, and word frequency) predicts readability independently
  of traditional average features. Through systematic evaluation on 13,129 sentences from WeeBIT and CEFR-SP datasets with
  rigorous statistical testing (bootstrap confidence intervals, effect sizes, ablation studies), we demonstrate that uniformity
  features provide statistically significant predictive power beyond traditional features (p < 0.001), yielding R² improvements
  of +0.127 and +0.046 with large effect sizes (Cohen's d = 1.55 and 2.40). The coefficient of variation of syllable counts
  is the most robust uniformity predictor. These findings suggest that the Uniformity Principle captures a previously unrecognized
  aspect of readability, providing a lightweight and interpretable enhancement to traditional readability assessment.
</paper_text>

<available_figures>
--- Item 1 ---
id: fig1
title: Uniformity Principle Concept
caption: >-
  Conceptual illustration of the Uniformity Principle. Left: A sentence with uniform word difficulty (low CV) allows consistent
  processing rhythm. Right: A sentence with variable word difficulty (high CV) creates peak cognitive load spikes. The figure
  shows a hypothetical cognitive load trace over time for each case.
image_gen_detailed_description: >-
  Horizontal concept diagram with two rows. Top row: 'Uniform sentence' with 5 small equal-height bars (representing words
  of equal difficulty) labeled 'the cat sat on mat' with a flat line above showing 'steady cognitive load'. Bottom row: 'Variable
  sentence' with 5 bars of varying heights labeled 'The photosynthesis mechanism converts' with a jagged line above showing
  'peak cognitive load spikes'. Use sans-serif font, clean white background, blue for uniform, orange for variable, 21:9 aspect
  ratio.
aspect_ratio: '21:9'
summary: >-
  Conceptual diagram showing how uniform sentences allow steady processing while variable sentences create cognitive load
  spikes
figure_path: figures/fig1_v0.jpg

--- Item 2 ---
id: fig2
title: Dataset Characteristics
caption: >-
  Dataset characteristics. (a) Distribution of readability scores for WeeBIT (5 levels, n=3,125) and CEFR-SP (6 levels mapped
  to continuous, n=10,004). (b) Sentence length distributions. (c) Word length distributions. All figures show the combined
  13,129 sentences used in experiments.
image_gen_detailed_description: >-
  Three-panel figure (3 subplots in a row). Panel A (top left): Histogram of readability scores, WeeBIT shown in blue bars
  (peaks at 0.2, 0.4, 0.6, 0.8 with 5 levels), CEFR-SP in orange bars (smoother distribution from 0.0 to 1.0). Panel B (top
  right): Histogram of sentence lengths in words, x-axis 0-70 words, y-axis count, peak at 15-20 words. Panel C (bottom):
  Histogram of word lengths in characters, x-axis 1-15 characters, peak at 3-5 characters. Use sans-serif font, white background,
  16:9 aspect ratio.
aspect_ratio: '21:9'
summary: >-
  Three-panel figure showing distributions of readability scores, sentence lengths, and word lengths across both datasets
figure_path: figures/fig2_v0.jpg

--- Item 3 ---
id: fig3
title: R² Comparison Across Feature Sets
caption: >-
  Main results. Bar chart showing cross-validated R² for three feature sets (average only, uniformity only, combined) on both
  datasets. Error bars show ±1 SD across 5 folds. Combined significantly outperforms average only on both datasets (p < 0.001,
  bootstrap test). WeeBIT: R² = 0.248 → 0.376 (+0.127). CEFR-SP: R² = 0.544 → 0.590 (+0.046).
image_gen_detailed_description: >-
  Grouped bar chart with two groups (WeeBIT, CEFR-SP). X-axis: 'WeeBIT (n=3,125)' and 'CEFR-SP (n=10,004)'. Y-axis: R² from
  0.0 to 0.7. Three bars per group: 'Average only' (blue, R²=0.248 for WeeBIT, 0.544 for CEFR-SP), 'Uniformity only' (orange,
  R²=0.198 for WeeBIT, 0.487 for CEFR-SP), 'Combined' (green, R²=0.376 for WeeBIT, 0.590 for CEFR-SP). Error bars: WeeBIT
  SD=0.027/0.021/0.035, CEFR-SP SD=0.009/0.011/0.006. Use sans-serif font, white background, 16:9 aspect ratio.
aspect_ratio: '21:9'
summary: >-
  Bar chart comparing R² across average-only, uniformity-only, and combined feature sets on both datasets
figure_path: figures/fig3_v0.jpg

--- Item 4 ---
id: fig4
title: Ablation Study Results
caption: >-
  Ablation study results. Bar chart showing R² improvement from adding each uniformity feature to the average-only baseline.
  WeeBIT: cv_syllables contributes +0.116, cv_frequency +0.025, cv_word_length +0.038. CEFR-SP: cv_frequency contributes +0.032,
  cv_word_length +0.022, cv_syllables +0.014. Error bars show ±1 SD.
image_gen_detailed_description: >-
  Grouped bar chart with two groups (WeeBIT, CEFR-SP). X-axis: 'WeeBIT' and 'CEFR-SP'. Y-axis: R² improvement (ΔR²) from 0.0
  to 0.12. Three bars per group: 'cv_word_length' (blue, +0.038 for WeeBIT, +0.022 for CEFR-SP), 'cv_syllables' (orange, +0.116
  for WeeBIT, +0.014 for CEFR-SP), 'cv_frequency' (green, +0.025 for WeeBIT, +0.032 for CEFR-SP). All values are positive.
  Error bars: WeeBIT SD approximately 0.01 for each, CEFR-SP SD approximately 0.005 for each. Use sans-serif font, white background,
  16:9 aspect ratio.
aspect_ratio: '21:9'
summary: >-
  Bar chart showing R² improvement from adding each uniformity feature to the average-only baseline
figure_path: figures/fig4_v0.jpg

--- Item 5 ---
id: fig5
title: Bootstrap Coefficient Confidence Intervals
caption: >-
  Bootstrap coefficient confidence intervals. Forest plot showing 95% CIs for Ridge regression coefficients on the combined
  model. WeeBIT (top): cv_syllables (β=0.141, CI[0.125,0.157]) and cv_frequency (β=0.104, CI[0.069,0.138]) are significant
  predictors. CEFR-SP (bottom): all three uniformity features are significant. Coefficients > 0 indicate higher CV (less uniformity)
  predicts higher difficulty.
image_gen_detailed_description: >-
  Forest plot (two panels stacked vertically). Top panel: 'WeeBIT coefficients' with 7 horizontal lines representing 95% CIs
  for coefficients: avg_word_length (-0.127, CI[-0.152,-0.102], crosses zero - not significant in direction), avg_syllables
  (0.052, CI[0.029,0.075]), avg_frequency (0.032, CI[-0.005,0.071], crosses zero), sentence_length (0.108, CI[0.099,0.117]),
  cv_word_length (-0.001, CI[-0.018,0.016], crosses zero), cv_syllables (0.141, CI[0.125,0.157], does not cross zero - significant),
  cv_frequency (0.104, CI[0.069,0.138], does not cross zero - significant). Bottom panel: 'CEFR-SP coefficients' with similar
  format: cv_word_length (0.017, CI[0.014,0.021]), cv_syllables (0.018, CI[0.014,0.021]), cv_frequency (0.066, CI[0.060,0.072]),
  all significant. Vertical line at 0. Use sans-serif font, white background, 4:3 aspect ratio.
aspect_ratio: '21:9'
summary: >-
  Forest plot showing bootstrap 95% confidence intervals for Ridge regression coefficients on both datasets
figure_path: figures/fig5_v0.jpg
</available_figures>

<figure_requirements>
CRITICAL: Include ALL figures from <available_figures>. No exceptions.

- Every figure MUST use \includegraphics{figures/filename.jpg}
- Do NOT skip, convert to tables, or describe without inserting
- Each needs: \begin{figure*|figure}[placement], \includegraphics, \caption, \label, \end{...} — pick env + placement by the figure's `aspect_ratio` field (see PLACEMENT below). Constrain every \includegraphics with `width=\linewidth,height=0.4\textheight,keepaspectratio` (single-column) or `width=\textwidth,height=0.45\textheight,keepaspectratio` (figure*). Use exactly these option keys — `max height=` is NOT valid LaTeX
- Use the `caption` field from each figure for \caption{...} — do NOT invent new captions
- Place figures where their [FIGURE:fig_id] markers appear in paper_text
- VERIFICATION: paper.tex MUST have exact same number of \includegraphics as <available_figures>
- Do NOT generate new figure images (no matplotlib, no PIL, no image generation). Use ONLY the pre-generated figures from <available_figures>. They were already created by a previous pipeline step.

PLACEMENT BY ASPECT RATIO (use the `aspect_ratio` field on each figure):
- `21:9` (architecture diagrams / hero figures): \begin{figure*}[!t] (full two-column width, top of page). The hero architecture diagram should appear EARLY in the paper — typically at the top of page 2. Marker placement in paper_text already determines this; preserve it.
- `16:9` (comparisons, multi-panel results): \begin{figure*}[!t] for full-width or \begin{figure}[!htbp] for single-column.
- `4:3` / `1:1` / `3:2` / `3:4` / `9:16`: \begin{figure}[!htbp] (single-column).
</figure_requirements>

<artifact_links>
The paper_text contains \footnote{Code: \url{...}} references linking to artifact source code
on GitHub. Include \usepackage{hyperref} and \usepackage{url}.
Preserve these exactly as-is — do not remove, rewrite, or convert them to plain text.
The URLs will not resolve yet (the repo is deployed after compilation) — do NOT try to verify or fix them.
</artifact_links>

<headings>
NEVER use inline math (``$...$``) inside ``\section{...}`` / ``\subsection{...}`` / ``\subsubsection{...}`` arguments — hyperref's bookmark builder errors out (``Token not allowed in a PDF string``) and the PDF outline breaks. If a section heading needs a math-looking term, use the text equivalent (``d star`` not ``$d^*$``, ``alpha-equivalent`` not ``$\alpha$-equivalent``) or wrap it in ``\texorpdfstring{$math$}{plain}``. Inline math inside body paragraphs is fine.
</headings>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.
TODO 2. Review <paper_text> and <available_figures>. Copy all figure images into ./figures/ in your workspace. Count figures — MUST include every one. Plan placements per section. Build `./references.bib` via aii_semscholar_bib__fetch — collect DOIs/ArXiv IDs from <paper_text> and batch-fetch all BibTeX in one call. Do NOT fabricate entries.
TODO 3. Create `./paper.tex` per aii-paper-to-latex skill's setup, write ALL sections, insert ALL figures from <available_figures>, include `./references.bib` via \bibliography. Compile to PDF per skill's process. Fix errors.
TODO 4. CRITICAL VERIFICATION: Run `grep -c 'includegraphics' paper.tex`, confirm count equals figures in <available_figures>. If not, add missing figures. Verify `./paper.pdf` was created.
TODO 5. VISUAL REVIEW: Write Python script to convert EVERY page of paper.pdf to PNG at 150 DPI (use pdf2image or pymupdf). Then read ALL page screenshots — each page image costs ~1,600 tokens so a 15-page paper is only ~24K tokens. You MUST read every page. The ONLY exception is if all page images would not fit in your remaining context — in that case, read as many as fit and state which pages you are skipping and why. Check every page for layout issues, overlapping figures, cut-off text, bad spacing, formatting problems. Fix issues and recompile.
TODO 6. FINAL READ: Check page count (`pdfinfo paper.pdf` or pymupdf). Read entire paper.pdf — check for missing sections, unclear explanations, inconsistencies, typos. Fix and recompile. The ONLY exception is if all pages would not fit in your remaining context — in that case, read as many pages as fit and state which pages you are skipping and why.
</todos>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FullPaperExpectedFiles": {
      "description": "All expected output files from full paper generation.",
      "properties": {
        "paper_tex_path": {
          "description": "Path to LaTeX source file. Example: 'paper.tex'",
          "title": "Paper Tex Path",
          "type": "string"
        },
        "paper_pdf_path": {
          "description": "Path to compiled PDF. Example: 'paper.pdf'",
          "title": "Paper Pdf Path",
          "type": "string"
        },
        "references_bib_path": {
          "description": "Path to BibTeX bibliography file. Example: 'references.bib'",
          "title": "References Bib Path",
          "type": "string"
        },
        "figure_paths": {
          "description": "Paths to all figure image files. Example: ['figures/fig1_v0.jpg', 'figures/fig2_v0.jpg']",
          "items": {
            "type": "string"
          },
          "title": "Figure Paths",
          "type": "array"
        }
      },
      "required": [
        "paper_tex_path",
        "paper_pdf_path",
        "references_bib_path",
        "figure_paths"
      ],
      "title": "FullPaperExpectedFiles",
      "type": "object"
    }
  },
  "description": "Full paper \u2014 structured output from paper generation.",
  "properties": {
    "title": {
      "description": "Paper title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance. Aim for about 4-8 words (~40 characters).",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "description": "Brief summary of the generated paper: sections written, figures included, compilation status",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/FullPaperExpectedFiles",
      "description": "All output files you created. Must include paper.tex, paper.pdf, references.bib, and paths to all figure files."
    }
  },
  "required": [
    "title",
    "summary",
    "out_expected_files"
  ],
  "title": "FullPaper",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-07-21 18:56:20 UTC

```
A lightweight sentence-level readability scoring model for English text using classic surface linguistic features, evaluated on a small public dataset.
```

### [3] SKILL-INPUT — aii-paper-to-latex · 2026-07-21 18:56:32 UTC

The agent loaded the **aii-paper-to-latex** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-to-latex
description: LaTeX paper assembly and compilation. Covers document setup, figure inclusion from pre-generated JPEGs, compilation process, and output files. Use when assembling a paper from pre-written text and pre-generated figures into a compiled PDF.
---

## LaTeX Paper Assembly

Assembles a research paper from paper text, pre-generated figure JPEGs, and bibliography into a compiled PDF.

### Document Setup

```latex
\documentclass[11pt,letterpaper]{article}
\usepackage{graphicx, geometry, amsmath, hyperref, natbib, booktabs, xcolor, listings}
\geometry{margin=1in}
\hypersetup{colorlinks=true, linkcolor=black, citecolor=black, urlcolor=black}
```

### Figure Inclusion

CRITICAL: Include ALL figures. Every figure MUST appear in the paper.

```latex
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.92\textwidth,keepaspectratio]{figures/filename.jpg}
  \caption{Descriptive caption.}
  \label{fig:label}
\end{figure}
```

Rules:
- ALWAYS use `[!htbp]` float placement (NOT `[t]` or `[h]` alone)
- ALWAYS constrain with `width` and `keepaspectratio` to prevent page takeover
- Every figure needs `\caption`, `\label`, and a `\ref` in the text
- Do NOT convert figures to tables or describe them without inserting the image
- Do NOT skip any figures

### Compilation Process

Run each command separately (do NOT chain with `&&` — pdflatex often exits non-zero on warnings, which would skip bibtex and leave citations as `??`):

```bash
pdflatex -interaction=nonstopmode paper.tex
bibtex paper
pdflatex -interaction=nonstopmode paper.tex
pdflatex -interaction=nonstopmode paper.tex
```

All four commands are required. Skipping bibtex causes `??` in all citations.
Fix any errors between runs. Verify `./paper.pdf` was created.

### Output Files

- `./paper.tex` — LaTeX source
- `./references.bib` — bibliography file
- `./paper.pdf` — compiled PDF
- `./figures/*.jpg` — all figure images (pre-generated, copied into workspace)
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-07-21 18:56:32 UTC

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

### [5] SKILL-INPUT — aii-web-tools · 2026-07-21 18:57:59 UTC

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
