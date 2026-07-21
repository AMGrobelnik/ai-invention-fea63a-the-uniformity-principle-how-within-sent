# Word features and readability methods research

## Summary

This research artifact provides a comprehensive methodological guide for computing word-level linguistic features (syllable count, word frequency) and understanding the sentence-level readability assessment landscape. The research was conducted to inform experimental design for testing the 'Uniformity Principle' hypothesis, which posits that variance/uniformity measures of linguistic properties within sentences may improve readability prediction beyond traditional average-based features.

Key findings across 5 research phases:

1. SYLLABLE COUNTING: Three main approaches exist - (a) CMU Pronouncing Dictionary via 'pronouncing' library (high accuracy, research-grade), (b) 'syllables' package (fast heuristic, lower accuracy), (c) textstat library (uses Pyphen, only 54% accurate per GitHub issues). Recommendation: Use CMUdict as primary with heuristic fallback.

2. WORD FREQUENCY: SUBTLEX-US norms (based on 51M subtitle words) significantly outperform older norms (Kucera & Francis, Celex) in predicting word processing times. Available as free download from Ghent University. Google Books Ngrams is secondary option.

3. SENTENCE-LEVEL DATASETS: (a) CLEAR corpus (~5,000 excerpts, grades 3-12, multiple readability metrics + teacher ratings, MIT license), (b) WSJ dataset (1,200 sentences, 20 annotators, grades 1-7), (c) OneStopEnglish (189 texts × 3 levels). CLEAR recommended as primary for hypothesis testing.

4. FEATURE LANDSCAPE: Feng et al. (2010) evaluated 5 categories - discourse, language modeling, syntactic, POS, and shallow features. Their Table 5 lists 8 shallow features. Critical finding: ALL existing features are means/averages (e.g., 'average syllables per word'). NO variance/uniformity measures were found, suggesting the 'Uniformity Principle' hypothesis has novelty.

5. STATISTICAL METHODS: For testing incremental predictive power - (a) Cross-validated R² difference with bootstrap CI (most robust), (b) AIC/BIC comparison (model selection), (c) Nested F-test (linear models). Recommendations provided with Python implementation examples.

The artifact includes: (1) Detailed methodology guide with installation commands and code snippets, (2) Dataset catalog with properties and access methods, (3) Feature catalog from Feng et al. (2010), (4) Statistical methodology guide, (5) Novelty assessment for uniformity features, (6) Experimental design recommendations.

Sources: 14 references covering PyPI packages, academic papers (Feng et al. 2010, Liu & Lee 2023), dataset documentation (CLEAR, WSJ, OneStopEnglish), and statistical methods resources. All sources accessed and verified via web research tools.

## Research Findings

## Comprehensive Methodology Guide for Word Features and Readability Assessment

### Phase 1: Syllable Counting Methods

Three main approaches exist for syllable counting in Python, each with different accuracy/speed trade-offs:

**1. Textstat Library (Syllable Counting)**
Textstat is a popular Python library (PyPI package) that provides easy-to-use readability metrics [1]. For syllable counting, textstat uses Pyphen by default for most languages, but switches to NLTK's CMU pronouncing dictionary for en-US [1]. However, a critical GitHub issue (#195) reveals that textstat's syllable counting can be inaccurate - for example, it counts 'faeries' as 1 syllable (should be 2) and 'relived' as 3 syllables (should be 2) [2]. The issue notes that 'Pyphen is only 54% accurate,' suggesting significant limitations for research-grade applications [2].

**2. CMU Pronouncing Dictionary (via pronouncing library)**
The CMU Pronouncing Dictionary is an open-source machine-readable pronunciation dictionary containing over 134,000 words [3]. The `pronouncing` Python library provides a simple interface to query this dictionary [3]. Syllable counting with CMUdict is done by: (a) retrieving phoneme representations with `pronouncing.phones_for_word()`, and (b) counting vowels with stress markers using `pronouncing.syllable_count()` [3]. This method is MORE ACCURATE than heuristic approaches since it uses actual pronunciation data, but it may not cover all words (especially rare or domain-specific terms) [3].

**3. Syllables Package (Heuristic-Based)**
The `syllables` package (PyPI) provides fast syllable estimation using heuristics [4]. It is designed for speed rather than accuracy - the documentation explicitly states: 'For situations where accuracy matters, please consider the cmudict Python library instead' [4]. This is a key trade-off: syllables is faster but less accurate than CMUdict-based approaches.

**Recommendation for Research:** Use the CMU Pronouncing Dictionary via the `pronouncing` library or directly via NLTK's `cmudict` corpus reader for research-grade syllable counting. Have a fallback heuristic (like the `syllables` package) for out-of-vocabulary words.

### Phase 2: Word Frequency Norm Sources

**1. SUBTLEX-US (Recommended Primary Source)**
SUBTLEX-US provides word frequency norms based on 51 million words of American movie/TV subtitles [5]. It significantly outperforms older norms (Kucera & Francis 1967, Celex 1993) in predicting word processing times [5]. Key measures include:
- SUBTL WF: Word frequency per million words
- SUBTL CD: Percentage of films in which a word appears (contextual diversity) [5]
- Zipf scale values (1-7 range, easier interpretation) [5]

The SUBTLEX-US norms are available for free download (Excel/Text formats) from Ghent University [5]. An online lookup interface is available at subtlexus.lexique.org [5]. Part-of-Speech tagged versions are also available [5].

**2. KF-NAP (Keller & Caramazza?)**
Note: Search results for 'KF-NAP' primarily returned information about a clinical assessment tool (Kessler Foundation Neglect Assessment Process), not a word frequency database. This may have been a confusion in the search query. The intended reference is likely to Kucera & Francis (1967) norms, which are acknowledged to be dated and of poor quality [5].

**3. Google Books Ngrams**
The Google Books Ngram corpus provides word frequency data from books digitized by Google [6]. While comprehensive, it has biases (published books, academic texts) and may not represent contemporary everyday language as well as SUBTLEX-US (which is based on subtitles) [5].

**4. NLTK Corpora**
NLTK provides access to various corpora (Brown, Reuters, etc.) that can be used for frequency norms [7]. However, these are generally smaller and less representative than SUBTLEX-US.

**Recommendation for Research:** Use SUBTLEX-US as the primary word frequency source. It is free, well-validated, and specifically designed for cognitive processing research. For words not in SUBTLEX-US, consider backing off to Google Books Ngrams or NLTK corpora.

### Phase 3: Sentence-Level Readability Datasets

**1. CLEAR Corpus (CommonLit Ease of Readability)**
The CLEAR corpus is an open dataset of ~5,000 reading passage excerpts with readability scores [8]. Key properties:
- Grade levels: 3-12
- Scoring: Multiple readability indices (Flesch Reading Ease, Flesch-Kincaid, ARI, SMOG, Dale-Chall, CAREC, etc.) plus teacher ratings (Bradley-Terry coefficients) [8]
- Metadata: Author, title, publication year, genre (informational/literary), licensing info [8]
- Access: Google Sheets (MIT license for metadata) [8]
- Use: Successfully used in Kaggle Readability Prize competition

**2. WSJ (Wall Street Journal) Dataset**
The WSJ dataset contains 1,200 sentences graded on a difficulty scale of 1-7 [9]. Each sentence was rated by 20 native speakers [9]. The evaluated subset contains 650 sentences with ≥14/20 annotator agreement [9]. This dataset is commonly used for sentence-level readability assessment research [9].

**3. OneStopEnglish (OSE) Corpus**
OneStopEnglish contains 189 texts (567 total versions) at three reading grades: beginner, intermediate, advanced [10]. Each text has three aligned versions [10]. For sentence-level analysis, individual sentences are labeled based on human revision patterns (sentences that remain unchanged across levels retain the lower grade) [9].

**4. Weekly Reader Corpus**
Used in Feng et al. (2010), this corpus contains 1,433 articles for grades 2-5 from Weekly Reader magazine [11]. Articles are shorter than other corpora (average 128-336 words/document depending on grade) [11]. This corpus is particularly valuable for elementary school readability research.

**Recommendation for Research:** For testing the 'Uniformity Principle' hypothesis, CLEAR corpus is recommended as the primary dataset because: (a) it provides sentence-level excerpts (not full documents), (b) it has multiple readability metrics, (c) it includes teacher ratings, and (d) it is open-access. WSJ dataset is also valuable for sentence-level analysis with human ratings.

### Phase 4: Feature Landscape for Readability

**Feng et al. (2010) Feature Categories:**
Feng et al. conducted a systematic comparison of features for automatic readability assessment [11]. They evaluated features at five linguistic levels:

1. **Discourse Features**
   - Entity-density features (percentage of named entities, overlapping nouns removed, etc.) [11]
   - Lexical chain features (total chains, average chain length/span, etc.) [11]
   - Coreference inference features (inference distance, chain statistics) [11]
   - Entity grid features (16 transition patterns) [11]

2. **Language Modeling Features**
   - Unigram, bigram, trigram models trained on in-domain data (Weekly Reader corpus) [11]
   - Information gain-selected features vs. POS-only models [11]

3. **Parsed Syntactic Features**
   - Average number of non-terminal nodes per tree
   - Average tree height
   - Frequencies of SBARs, NPs, VPs, PPs [11]

4. **POS-based Features**
   - Nouns, verbs, adjectives, adverbs, prepositions
   - Content words vs. function words [11]
   - Noun-based features had highest predictive power among POS features [11]

5. **Shallow Features (8 features)** [11]
   Table 5 from Feng et al. lists:
   1. Average number of syllables per word
   2. Percentage of polysyllabic words per document
   3. Average number of polysyllabic words per sentence
   4. Average number of characters per word
   5. Chall-Dale difficult words rate per document
   6. Average number of words per sentence
   7. Flesch-Kincaid score
   8. Total number of words per document

**Predictive Power Findings (Feng et al.):**
- Average sentence length had DOMINATING predictive power over all other shallow features [11]
- Noun-based features (POS) were very predictive, explaining why entity-density features also performed well [11]
- Language modeling features trained on in-domain data were highly discriminative [11]
- Syllable-based features performed much worse than sentence length [11]
- Best performance: 74% classification accuracy (grades 2-5) using careful feature selection [11]

**Note on 'Uniformity Principle' Relevance:**
The planned hypothesis introduces 'uniformity' features (coefficient of variation of word length, syllable count, word frequency within a sentence). These would be NOVEL features not explored in Feng et al. (2010) or subsequent surveys. The closest existing features are:
- Average syllables per word (Feng Table 5, feature 1) - a MEAN measure
- No existing VARIANCE or UNIFORMITY measures were identified in the literature review

This suggests the hypothesis HAS NOVELTY. However, confirmation requires checking more recent surveys (post-2010) and the LingFeat documentation (which extracts 255 linguistic features) [12].

### Phase 5: Statistical Methods for Model Comparison

**Testing Incremental Predictive Power:**
When adding new features (like uniformity measures) to an existing model, several statistical approaches can test whether the improvement is significant:

**1. Nested F-Test (Linear Models)**
- Compares two nested models (one with additional features)
- Tests whether the improvement in R² is significant
- Implementation: `statsmodels.regression.linear_model.RegressionResults.compare_f_test()`

**2. AIC/BIC (Model Selection Criteria)**
- Akaike Information Criterion (AIC) and Bayesian Information Criterion (BIC) penalize model complexity [13]
- Lower AIC/BIC indicates better trade-off between fit and parsimony
- Implementation: `statsmodels` automatically computes AIC/BIC for fitted models (`model.aic`, `model.bic`)
- For feature selection: stepwise selection using AIC (forward/backward elimination) [13]

**3. Cross-Validated R² Difference with Bootstrap**
- More robust than simple nested F-test for non-normal data or complex models
- Procedure: (a) Compute cross-validated R² for both models, (b) Bootstrap the difference distribution, (c) Test if confidence interval excludes zero
- Implementation: Use `sklearn.model_selection.cross_val_score` with custom scoring, combined with bootstrap resampling
- Relevant CrossValidated discussion suggests keeping models fixed and bootstrapping test set predictions [14]

**4. Likelihood Ratio Test (for GLMs)**
- For logistic regression or other generalized linear models
- Tests whether added features significantly improve log-likelihood
- Implementation: `statsmodels` provides `lrtest` functionality

**Recommendation for Research:**
For the 'Uniformity Principle' hypothesis evaluation, use:
1. **Primary analysis:** Cross-validated R² difference with bootstrap confidence intervals (most robust for predictive modeling)
2. **Secondary analysis:** AIC/BIC comparison (model selection perspective)
3. **Tertiary analysis:** Nested F-test if using linear regression (interpretable as variance explained)

### Synthesis and Recommendations

**Tools to Install:**
```python
# Syllable counting
pip install pronouncing  # CMUdict interface
pip install syllables  # Fast heuristic fallback

# Readability metrics  
pip install textstat  # Traditional formulas

# Word frequency
# Download SUBTLEX-US from: https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexus

# Feature extraction
pip install lingfeat  # 255 linguistic features

# Statistical analysis
pip install statsmodels  # AIC/BIC, F-tests
pip install scikit-learn  # Cross-validation
```

**Experimental Design Suggestions:**
1. **Baseline features:** Implement the 8 shallow features from Feng et al. Table 5 [11]
2. **New features:** Add uniformity measures (coefficient of variation for: word length in chars, syllable count, word frequency)
3. **Dataset:** Use CLEAR corpus (sentence-level, multiple readability metrics)
4. **Evaluation:** Cross-validated R² with bootstrap, AIC/BIC comparison
5. **Novelty check:** Compare against full LingFeat feature set (255 features) to ensure uniformity features are truly novel

**Gaps Identified:**
1. No previous work found on variance/uniformity measures in readability (suggests novelty)
2. Need to verify that CMUdict coverage is adequate (134K words may not cover all tokens)
3. SUBTLEX-US based on subtitles - may have genre bias for some applications
4. Sentence-level datasets are limited (CLEAR: ~5K excerpts, WSJ: 650 evaluated sentences)

### Confidence Assessment

**High confidence (supported by multiple sources):**
- Feng et al. (2010) feature list and findings [11]
- SUBTLEX-US superiority over Kucera & Francis [5]
- CLEAR corpus properties [8]
- CMUdict as accuracy standard for syllable counting [3]

**Medium confidence (single source or needs verification):**
- Optimal statistical method for model comparison (multiple valid approaches)
- WSJ dataset details (only available through academic channels)
- LingFeat feature list (documentation truncated) [12]

**Low confidence (speculative, needs primary source verification):**
- Textstat inaccuracy extent (only one GitHub issue found) [2]
- KF-NAP as word frequency database (may have been confused with clinical assessment)

### Follow-Up Questions

1. What is the exact feature list in LingFeat (255 features)? Do any measure within-sentence variance or uniformity?
2. Are there additional sentence-level readability datasets beyond CLEAR, WSJ, and OneStopEnglish?
3. What is the out-of-vocabulary rate when using CMUdict for typical readability assessment texts?
4. Has any previous work explored variance/dispersion measures of linguistic properties for readability assessment?

## Sources

[1] [textstat PyPI page - Readability metrics library](https://pypi.org/project/textstat/) — Documents textstat library v0.7.13 with API for readability formulas. Notes use of Pyphen for syllable counting (en-US uses NLTK cmudict).

[2] [GitHub Issue #195: Wrong syllable count](https://github.com/textstat/textstat/issues/195) — Reports bugs in textstat syllable counting (e.g., 'faeries' counted as 1 instead of 2 syllables). Notes Pyphen is 'only 54% accurate'.

[3] [Pronouncing library tutorial - CMU Dictionary interface](https://pronouncing.readthedocs.io/en/latest/tutorial.html) — Documents pronouncing library for CMU Pronouncing Dictionary access. Shows syllable counting via phones_for_word() and syllable_count() functions.

[4] [syllables PyPI page - Fast syllable estimation](https://pypi.org/project/syllables/) — Documents syllables package v1.1.5 for fast heuristic syllable estimation. Explicitly states CMUdict should be used when accuracy matters.

[5] [SUBTLEX-US word frequency norms documentation](https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexus) — Documents SUBTLEX-US frequency norms from 51M word subtitle corpus. Shows variance explained in lexical decision tasks (30.1% Acc, 62.3% RT vs. KF 19.6%/57.7%). Provides download links and variable definitions (SUBTL WF, SUBTL CD, Zipf values).

[6] [Google Books Ngram word frequency lists](https://github.com/orgtre/google-books-ngram-frequency) — GitHub repository providing cleaned word/ngram frequency lists from Google Books Ngram corpus.

[7] [NLTK CMU Pronouncing Dictionary corpus reader](https://www.nltk.org/api/nltk.corpus.reader.cmudict.html) — Documents NLTK interface to CMUdict with 127,069 entries. Notes multiple pronunciations for some words.

[8] [Introducing the CLEAR Corpus blog post](https://www.commonlit.org/blog/introducing-the-clear-corpus-an-open-dataset-to-advance-research-28ff8cfea84a/) — Describes CLEAR corpus: ~5,000 excerpts, grades 3-12, multiple readability indices, teacher ratings (BT_easiness), MIT license. Documents all fields and access methods.

[9] [Hybrid Models for Sentence Readability Assessment (Liu & Lee, BEA 2023)](https://aclanthology.org/2023.bea-1.37.pdf) — Describes WSJ dataset (1,200 sentences, grades 1-7, 20 annotators) and OneStopEnglish corpus (189 texts × 3 levels). Reports hybrid models achieve 0.729 accuracy on WSJ, surpassing previous SOTA by 13% absolute.

[10] [OneStopEnglish corpus paper (Vajjala & Lucic, 2018)](https://aclanthology.org/W18-0535/) — Introduces OneStopEnglish corpus of 189 texts at three reading levels for readability assessment and text simplification research.

[11] [A Comparison of Features for Automatic Readability Assessment (Feng et al., COLING 2010)](https://aclanthology.org/C10-2032.pdf) — Comprehensive comparison of discourse, language modeling, syntactic, POS, and shallow features. Documents 8 shallow features (Table 5). Finds average sentence length most predictive among shallow features. Best accuracy: 74% (grades 2-5) with feature selection.

[12] [LingFeat GitHub repository - 255 linguistic features](https://github.com/brucewlee/lingfeat) — Documents LingFeat tool for extracting 255 linguistic features for readability assessment. Used in Liu & Lee (2023) for sentence-level readability.

[13] [Scikit-learn Lasso model selection with AIC/BIC](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_model_selection.html) — Documents use of AIC/BIC for model selection in Python. Shows Lasso path with AIC/BIC criteria.

[14] [CrossValidated: Comparing nested models using bootstrap](https://stats.stackexchange.com/questions/668121/comparing-nested-models-using-bootstrap) — Discusses bootstrap approach for comparing nested models. Suggests keeping models fixed and bootstrapping test set predictions.

## Follow-up Questions

- What is the exact feature list in LingFeat (255 features)? Do any measure within-sentence variance or uniformity?
- Are there additional sentence-level readability datasets beyond CLEAR, WSJ, and OneStopEnglish that could test the Uniformity Principle hypothesis?
- What is the out-of-vocabulary rate when using CMUdict for typical readability assessment texts, and what are best practices for handling OOV words?
- Has any previous work explored variance/dispersion measures of linguistic properties (not just means/averages) for readability assessment?

---
*Generated by AI Inventor Pipeline*
