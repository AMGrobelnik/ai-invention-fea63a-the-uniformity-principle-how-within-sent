# Experiment Summary

## Task
Test the Uniformity Principle for readability prediction by comparing average-only vs uniformity (CV) features.

## Implementation (method.py)

### Features Extracted
1. **Average features** (traditional readability features):
   - avg_word_length
   - avg_syllables (vowel-count heuristic)
   - avg_word_freq (based on common word list)
   - sentence_length

2. **Uniformity features** (coefficient of variation within sentence):
   - cv_word_length
   - cv_syllables
   - cv_word_freq

### Methods Compared
- average_only: Ridge regression on average features
- uniformity_only: Ridge regression on uniformity features
- combined: Ridge regression on all features

### Statistical Analysis
- 5-fold cross-validation for R² evaluation
- Bootstrap confidence intervals (2000 samples) for comparing average vs combined

## Results

### R² (5-fold CV, mean ± std)
- average_only: R² = 0.1914 ± 0.0154
- uniformity_only: R² = 0.1656 ± 0.0113
- combined: R² = 0.2365 ± 0.0156

### Bootstrap CI (average vs combined)
- Mean difference: 0.047
- 95% CI: [0.042, 0.053]
- p-value < 0.001
- Result: Combined significantly outperforms average-only (p < 0.001)

## Conclusions
1. The Uniformity Principle provides additional predictive power beyond average features
2. Combined model (average + uniformity) achieves best performance
3. Bootstrap CI confirms statistical significance of improvement

## Output Files
- method_out.json: Main results in exp_gen_sol_out schema format
- logs/run.log: Detailed execution log

## Schema Validation
Output validates against exp_gen_sol_out.json schema.

## Dataset
- WeeBIT: 3,125 sentences
- CEFR-SP: 10,004 sentences
- Total: 13,129 sentences
