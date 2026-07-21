# Experiment Results Summary

## Overview
This experiment evaluated the Uniformity Principle hypothesis for readability assessment using two datasets:
- WeeBIT: 3,125 sentences
- CEFR-SP: 10,004 sentences
- Total: 13,129 sentences

## Key Findings

### 1. Bootstrap MSE Test (Experiment 1)
Both datasets show statistically significant MSE reduction when adding uniformity features:

**WeeBIT:**
- MSE reduction: 12.44%
- p-value (one-sided): 0.0 (< 0.001)
- 95% CI for MSE difference: [0.011, 0.019]

**CEFR-SP:**
- MSE reduction: 4.57%
- p-value (one-sided): 0.0 (< 0.001)
- 95% CI for MSE difference: [0.002, 0.004]

### 2. Coefficient Confidence Intervals (Experiment 2)
Bootstrap 95% CIs for Ridge regression coefficients show:

**Significant uniformity features (both datasets):**
- cv_syllables: positive coefficient (lower CV = easier reading)
- cv_frequency: positive coefficient (lower CV = easier reading)

**Significant average features:**
- avg_word_length: negative (longer words = harder)
- avg_syllables: positive
- sentence_length: positive (longer sentences = harder)

### 3. Cross-Validation Results (Experiment 3)
Proper 5-fold CV with train/test separation:

**WeeBIT:**
- R² (avg only): 0.2485
- R² (combined): 0.3759
- R² improvement: 0.1275 (51% relative improvement)

**CEFR-SP:**
- R² (avg only): 0.5445
- R² (combined): 0.5904
- R² improvement: 0.0459 (8.4% relative improvement)

### 4. Effect Size Analysis (Experiment 4)
Cohen's d for practical significance:

- WeeBIT: d = 1.55 (large effect)
- CEFR-SP: d = 2.40 (large effect)

### 5. Ablation Study (Experiment 5)
Add-one-in analysis confirms each uniformity feature contributes:

**WeeBIT R² improvements over baseline:**
- + cv_word_length: ΔR² ≈ +0.02
- + cv_syllables: ΔR² ≈ +0.08
- + cv_frequency: ΔR² ≈ +0.05

## Conclusions

1. **Statistical Significance**: Uniformity features significantly reduce MSE (p < 0.001)
2. **Practical Significance**: Large effect sizes (Cohen's d > 1.5)
3. **Novelty**: All existing readability formulas use only average features; adding variance/uniformity measures improves prediction
4. **Feature Importance**: cv_syllables is the most important uniformity feature

## Files Generated

- `method_out.json`: Complete results (15KB)
- `mini_method_out.json`: Mini version for testing (7.3KB)
- `preview_method_out.json`: Preview version (7.3KB)
- `method.py`: Complete experiment implementation
- `run_full.log`: Full run log

## Validation

- All 5 experiments completed for both datasets
- No NaN or Inf values in output
- Sample sizes correct (WeeBIT=3,125, CEFR-SP=10,004)
- Bootstrap CI does not include 0 for key features
- R² improvement positive in all conditions
