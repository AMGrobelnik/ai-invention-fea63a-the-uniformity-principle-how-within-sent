#!/usr/bin/env python3
"""Statistical evaluation of uniformity features for readability.

This experiment evaluates the Uniformity Principle hypothesis using WeeBIT
(3,125 sentences) and CEFR-SP (10,004 sentences) datasets. Five statistical tests are conducted:

1. PAIRED BOOTSTRAP TEST: Test MSE reduction with 10,000 bootstrap samples
2. COEFFICIENT CI: Bootstrap 95% confidence intervals for Ridge regression coefficients
3. PROPER CV: 5-fold cross-validation with train/test separation
4. EFFECT SIZE: R² improvement with 95% CI, Cohen's d for practical significance
5. ABLATION: Add-one-in and remove-one-out uniformity feature analysis
"""

from loguru import logger
from pathlib import Path
import json
import sys
import os
import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import pronouncing
import re
import nltk
from collections import Counter
import gc
import resource
import psutil

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")


def get_hardware_limits():
    """Detect container RAM and CPU limits."""
    def _detect_cpus():
        try:
            parts = Path("/sys/fs/cgroup/cpu.max").read_text().split()
            if parts[0] != "max":
                return max(1, int(parts[0]) // int(parts[1]))
        except (FileNotFoundError, ValueError):
            pass
        try:
            q = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_quota_us").read_text())
            p = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_period_us").read_text())
            if q > 0:
                return max(1, q // p)
        except (FileNotFoundError, ValueError):
            pass
        try:
            return len(os.sched_getaffinity(0))
        except (AttributeError, OSError):
            pass
        return os.cpu_count() or 1

    def _container_ram_gb():
        for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
            try:
                v = Path(p).read_text().strip()
                if v != "max" and int(v) < 1_000_000_000_000:
                    return int(v) / 1e9
            except (FileNotFoundError, ValueError):
                pass
        return None

    num_cpus = _detect_cpus()
    total_ram_gb = _container_ram_gb() or psutil.virtual_memory().total / 1e9
    available_ram_gb = min(psutil.virtual_memory().available / 1e9, total_ram_gb)

    # Set memory limit to 80% of available
    ram_budget = available_ram_gb * 0.8 * 1e9
    resource.setrlimit(resource.RLIMIT_AS, (int(ram_budget * 3), int(ram_budget * 3)))

    logger.info(f"Hardware: {num_cpus} CPUs, {total_ram_gb:.1f}GB total RAM, {available_ram_gb:.1f}GB available")
    return num_cpus, total_ram_gb, available_ram_gb


def count_syllables(word):
    """Count syllables using CMUdict with heuristic fallback."""
    word = word.lower().strip()
    if not word:
        return 1

    # Try CMUdict first
    phones = pronouncing.phones_for_word(word)
    if phones:
        # Count vowel sounds (digits indicate stress)
        return len([p for p in phones[0].split() if any(c.isdigit() for c in p)])

    # Heuristic fallback: count vowel groups
    word = word.lower()
    vowels = 'aeiouy'
    count = 0
    prev_was_vowel = False

    for i, char in enumerate(word):
        is_vowel = char in vowels
        # 'y' at end of word is usually a vowel
        if char == 'y' and i == len(word) - 1 and len(word) > 1:
            is_vowel = True
        if is_vowel and not prev_was_vowel:
            count += 1
        prev_was_vowel = is_vowel

    # Silent 'e' adjustment
    if word.endswith('e') and count > 1:
        count -= 1

    return max(1, count)


def get_word_frequency(word, freq_dict):
    """Get log-transformed word frequency."""
    return freq_dict.get(word.lower(), 0)


def build_frequency_dict():
    """Build frequency dictionary from NLTK Gutenberg corpus."""
    logger.info("Building word frequency dictionary from NLTK Gutenberg corpus")
    try:
        from nltk.corpus import gutenberg
        words = gutenberg.words()
        freq = Counter(w.lower() for w in words)
        total = sum(freq.values())
        # Normalize as log(1+count)/total_words
        freq_dict = {w: np.log1p(c) / total for w, c in freq.items()}
        logger.info(f"Built frequency dict with {len(freq_dict)} words")
        return freq_dict
    except Exception as e:
        logger.warning(f"Failed to build frequency dict: {e}")
        return {}


def compute_features(sentences, freq_dict):
    """Compute all features for a list of sentences."""
    logger.info(f"Computing features for {len(sentences)} sentences")

    features_list = []
    for i, sent in enumerate(sentences):
        if i % 1000 == 0:
            logger.info(f"Processing sentence {i}/{len(sentences)}")

        # Tokenize words
        words = nltk.word_tokenize(sent)
        words = [w.lower() for w in words if w.isalpha()]

        if not words:
            features_list.append({
                'avg_word_length': 0,
                'avg_syllables': 0,
                'avg_frequency': 0,
                'cv_word_length': 0,
                'cv_syllables': 0,
                'cv_frequency': 0,
                'sentence_length': 0
            })
            continue

        # Compute word-level features
        word_lengths = [len(w) for w in words]
        syllables = [count_syllables(w) for w in words]
        frequencies = [get_word_frequency(w, freq_dict) for w in words]

        # Average features
        avg_word_length = np.mean(word_lengths)
        avg_syllables = np.mean(syllables)
        avg_frequency = np.mean(frequencies) if frequencies else 0

        # Uniformity features (coefficient of variation)
        cv_word_length = np.std(word_lengths) / (avg_word_length + 1e-10)
        cv_syllables = np.std(syllables) / (avg_syllables + 1e-10)
        cv_frequency = np.std(frequencies) / (avg_frequency + 1e-10) if avg_frequency > 0 else 0

        # Sentence length
        sentence_length = len(words)

        features_list.append({
            'avg_word_length': avg_word_length,
            'avg_syllables': avg_syllables,
            'avg_frequency': avg_frequency,
            'cv_word_length': cv_word_length,
            'cv_syllables': cv_syllables,
            'cv_frequency': cv_frequency,
            'sentence_length': sentence_length
        })

    return pd.DataFrame(features_list)


def load_datasets(data_path):
    """Load datasets from JSON file."""
    logger.info(f"Loading data from {data_path}")
    with open(data_path, 'r') as f:
        data = json.load(f)

    sentences, scores, sources = [], [], []
    for dataset in data['datasets']:
        for ex in dataset['examples']:
            sentences.append(ex['input'])
            scores.append(float(ex['output']))
            sources.append(dataset['dataset'])

    logger.info(f"Loaded {len(sentences)} sentences from {len(data['datasets'])} datasets")
    return sentences, np.array(scores), np.array(sources)


def paired_bootstrap_mse_test(X, y, n_bootstrap=10000):
    """Paired bootstrap test for MSE reduction with uniformity features."""
    logger.info(f"Running paired bootstrap MSE test with {n_bootstrap} samples")

    np.random.seed(42)
    n = len(y)

    avg_feats = ['avg_word_length', 'avg_syllables', 'avg_frequency', 'sentence_length']
    unif_feats = ['cv_word_length', 'cv_syllables', 'cv_frequency']
    combined = avg_feats + unif_feats

    mse_diffs = []

    # Adjust minimum OOB size based on dataset size
    min_oob = min(10, max(2, n // 3))

    for b in range(n_bootstrap):
        if b % 1000 == 0:
            logger.info(f"Bootstrap sample {b}/{n_bootstrap}")

        idx = np.random.choice(n, n, replace=True)
        oob = np.setdiff1d(np.arange(n), idx)
        if len(oob) < min_oob:
            # If not enough OOB samples, use a different approach
            # Use 80/20 split for small datasets
            all_idx = np.arange(n)
            np.random.shuffle(all_idx)
            split = int(0.8 * n)
            idx = all_idx[:split]
            oob = all_idx[split:]

        if len(oob) < 2:
            continue

        # Average features only model
        sa = StandardScaler().fit(X.loc[idx, avg_feats])
        X_train_A = sa.transform(X.loc[idx, avg_feats])
        X_test_A = sa.transform(X.loc[oob, avg_feats])
        mA = Ridge(1.0, random_state=42).fit(X_train_A, y[idx])
        mse_A = mean_squared_error(y[oob], mA.predict(X_test_A))

        # Combined model
        sb = StandardScaler().fit(X.loc[idx, combined])
        X_train_B = sb.transform(X.loc[idx, combined])
        X_test_B = sb.transform(X.loc[oob, combined])
        mB = Ridge(1.0, random_state=42).fit(X_train_B, y[idx])
        mse_B = mean_squared_error(y[oob], mB.predict(X_test_B))

        mse_diffs.append(mse_A - mse_B)

    if len(mse_diffs) == 0:
        logger.warning("No valid bootstrap samples collected")
        return {
            'p_value_one_sided': np.nan,
            'p_value_two_sided': np.nan,
            'ci_95': (np.nan, np.nan),
            'mse_reduction_mean': np.nan,
            'mse_reduction_pct': np.nan,
            'n_bootstrap': 0
        }

    mse_diffs = np.array(mse_diffs)

    # Baseline MSE for percentage calculation
    baseline_mse = np.mean((y - np.mean(y))**2)

    # Two-sided p-value: proportion of bootstrap samples with |diff| >= |observed|
    # Use the mean difference as "observed" for two-sided test
    observed_diff = np.mean(mse_diffs)
    p_two_sided = float(np.mean(np.abs(mse_diffs) >= np.abs(observed_diff)))

    return {
        'p_value_one_sided': float(np.mean(mse_diffs <= 0)),
        'p_value_two_sided': p_two_sided,
        'ci_95': (float(np.percentile(mse_diffs, 2.5)), float(np.percentile(mse_diffs, 97.5))),
        'mse_reduction_mean': float(np.mean(mse_diffs)),
        'mse_reduction_pct': float((np.mean(mse_diffs) / baseline_mse) * 100) if baseline_mse > 0 else 0,
        'n_bootstrap': len(mse_diffs)
    }


def bootstrap_coef_ci(X, y, n_bootstrap=10000):
    """Bootstrap 95% confidence intervals for Ridge regression coefficients."""
    logger.info(f"Computing bootstrap coefficient CI with {n_bootstrap} samples")

    np.random.seed(42)
    n, p = len(y), X.shape[1]
    coefs = np.zeros((n_bootstrap, p))

    for b in range(n_bootstrap):
        if b % 1000 == 0:
            logger.info(f"Bootstrap sample {b}/{n_bootstrap}")

        idx = np.random.choice(n, n, replace=True)
        scaler = StandardScaler()
        Xs = scaler.fit_transform(X.iloc[idx])
        model = Ridge(1.0, random_state=42).fit(Xs, y[idx])
        coefs[b] = model.coef_

    results = []
    for i, f in enumerate(X.columns):
        c = coefs[:, i]
        ci_low = float(np.percentile(c, 2.5))
        ci_high = float(np.percentile(c, 97.5))
        mean_coef = float(np.mean(c))

        results.append({
            'feature': f,
            'mean_coef': mean_coef,
            'ci_95_lower': ci_low,
            'ci_95_upper': ci_high,
            'significant': (ci_low > 0) if mean_coef > 0 else (ci_high < 0),
            'coef_range': (float(np.min(c)), float(np.max(c)))
        })

    return pd.DataFrame(results)


def cv_evaluate(X, y, n_splits=5):
    """5-fold cross-validation with proper train/test separation."""
    # Adjust n_splits for small datasets
    n_samples = len(X)
    actual_splits = min(n_splits, n_samples - 1)
    if actual_splits < 2:
        logger.warning(f"Dataset too small for CV (n={n_samples}), using single train/test split")
        # Use a simple train/test split
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        scaler = StandardScaler().fit(X_train)
        model = Ridge(1.0, random_state=42).fit(scaler.transform(X_train), y_train)
        y_pred = model.predict(scaler.transform(X_test))
        r2 = r2_score(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        return {
            'test_r2_mean': float(r2),
            'test_r2_sd': 0.0,
            'test_r2_values': [float(r2)],
            'test_mse_mean': float(mse),
            'test_mse_sd': 0.0,
            'test_mse_values': [float(mse)]
        }

    logger.info(f"Running {actual_splits}-fold cross-validation (adjusted from {n_splits} for n={n_samples})")

    kf = KFold(actual_splits, shuffle=True, random_state=42)
    r2_folds, mse_folds = [], []

    for fold, (train_idx, test_idx) in enumerate(kf.split(X)):
        logger.info(f"Fold {fold + 1}/{actual_splits}")

        scaler = StandardScaler().fit(X.iloc[train_idx])
        model = Ridge(1.0, random_state=42).fit(scaler.transform(X.iloc[train_idx]), y[train_idx])
        y_pred = model.predict(scaler.transform(X.iloc[test_idx]))

        r2_folds.append(r2_score(y[test_idx], y_pred))
        mse_folds.append(mean_squared_error(y[test_idx], y_pred))

    return {
        'test_r2_mean': float(np.mean(r2_folds)),
        'test_r2_sd': float(np.std(r2_folds)),
        'test_r2_values': [float(r) for r in r2_folds],
        'test_mse_mean': float(np.mean(mse_folds)),
        'test_mse_sd': float(np.std(mse_folds)),
        'test_mse_values': [float(m) for m in mse_folds]
    }


def effect_size_analysis(X_avg, X_combined, y, n_bootstrap=10000):
    """Compute effect size analysis with proper bootstrap CI."""
    logger.info("Computing effect size analysis")

    # Bootstrap CI for R² difference
    np.random.seed(42)
    n = len(y)
    r2_diffs = []

    logger.info(f"Bootstrapping R² difference with {n_bootstrap} samples")

    # Adjust min OOB for small datasets
    min_oob = min(10, max(2, n // 3))

    for b in range(n_bootstrap):
        if b % 2000 == 0:
            logger.info(f"Effect size bootstrap {b}/{n_bootstrap}")

        idx = np.random.choice(n, n, replace=True)
        oob = np.setdiff1d(np.arange(n), idx)
        if len(oob) < min_oob:
            all_idx = np.arange(n)
            np.random.shuffle(all_idx)
            split = int(0.8 * n)
            idx = all_idx[:split]
            oob = all_idx[split:]

        if len(oob) < 2:
            continue

        # Compute R² for both models on OOB
        try:
            scaler_avg = StandardScaler().fit(X_avg.iloc[idx])
            model_avg = Ridge(1.0, random_state=42).fit(scaler_avg.transform(X_avg.iloc[idx]), y[idx])
            pred_avg = model_avg.predict(scaler_avg.transform(X_avg.iloc[oob]))
            mse_avg = mean_squared_error(y[oob], pred_avg)
            r2_avg_b = 1 - mse_avg / (np.var(y[oob]) + 1e-10)

            scaler_comb = StandardScaler().fit(X_combined.iloc[idx])
            model_comb = Ridge(1.0, random_state=42).fit(scaler_comb.transform(X_combined.iloc[idx]), y[idx])
            pred_comb = model_comb.predict(scaler_comb.transform(X_combined.iloc[oob]))
            mse_comb = mean_squared_error(y[oob], pred_comb)
            r2_comb_b = 1 - mse_comb / (np.var(y[oob]) + 1e-10)

            r2_diffs.append(r2_comb_b - r2_avg_b)
        except Exception as e:
            logger.debug(f"Bootstrap sample {b} failed: {e}")
            continue

    # Compute point estimates using CV
    cv_avg = cv_evaluate(X_avg, y)
    cv_combined = cv_evaluate(X_combined, y)

    r2_avg = cv_avg['test_r2_mean']
    r2_combined = cv_combined['test_r2_mean']
    r2_diff = r2_combined - r2_avg

    r2_diffs = np.array(r2_diffs) if len(r2_diffs) > 0 else np.array([np.nan])

    # Convert R² to correlation
    r_avg = np.sqrt(max(0, r2_avg))
    r_combined_corr = np.sqrt(max(0, r2_combined))

    # Cohen's d approximation from correlation: d = 2r / sqrt(1 - r^2)
    if 0 < r_combined_corr < 1:
        cohens_d = 2 * r_combined_corr / np.sqrt(1 - r_combined_corr**2)
    else:
        cohens_d = 0

    # Interpretation
    if abs(cohens_d) < 0.2:
        interpretation = "negligible"
    elif abs(cohens_d) < 0.5:
        interpretation = "small"
    elif abs(cohens_d) < 0.8:
        interpretation = "medium"
    else:
        interpretation = "large"

    return {
        'r2_avg': float(r2_avg),
        'r2_combined': float(r2_combined),
        'r2_difference': float(r2_diff),
        'r2_difference_ci_95': (float(np.nanpercentile(r2_diffs, 2.5)), float(np.nanpercentile(r2_diffs, 97.5))) if not np.all(np.isnan(r2_diffs)) else (np.nan, np.nan),
        'correlation_avg': float(r_avg),
        'correlation_combined': float(r_combined_corr),
        'cohens_d': float(cohens_d),
        'effect_interpretation': interpretation
    }


def ablation_study(X, y):
    """Add-one-in and remove-one-out uniformity feature analysis."""
    logger.info("Running ablation study")

    avg_feats = ['avg_word_length', 'avg_syllables', 'avg_frequency', 'sentence_length']
    unif_feats = ['cv_word_length', 'cv_syllables', 'cv_frequency']

    results = []

    # Baseline: average features only
    baseline_r2 = cv_evaluate(X[avg_feats], y)['test_r2_mean']
    results.append({
        'condition': 'baseline_avg_only',
        'features': avg_feats.copy(),
        'test_r2': baseline_r2
    })

    # Add-one-in: average + one uniformity feature at a time
    for uf in unif_feats:
        feats = avg_feats + [uf]
        r2 = cv_evaluate(X[feats], y)['test_r2_mean']
        results.append({
            'condition': f'add_{uf}',
            'features': feats.copy(),
            'test_r2': r2,
            'r2_improvement': r2 - baseline_r2
        })

    # Combined model
    combined_feats = avg_feats + unif_feats
    combined_r2 = cv_evaluate(X[combined_feats], y)['test_r2_mean']
    results.append({
        'condition': 'combined_all',
        'features': combined_feats.copy(),
        'test_r2': combined_r2,
        'r2_improvement': combined_r2 - baseline_r2
    })

    # Remove-one-out: combined minus one uniformity feature at a time
    for uf in unif_feats:
        feats = [f for f in combined_feats if f != uf]
        r2 = cv_evaluate(X[feats], y)['test_r2_mean']
        results.append({
            'condition': f'remove_{uf}',
            'features': feats.copy(),
            'test_r2': r2,
            'r2_change': r2 - combined_r2
        })

    return results


@logger.catch(reraise=True)
def run_experiment(data_path, output_path, n_bootstrap=10000, n_splits=5, sample_size=None):
    """Run all experiments and save results."""
    logger.info(f"Starting experiment with data from {data_path}")

    # Get hardware limits
    num_cpus, total_ram, available_ram = get_hardware_limits()

    # Create logs directory
    Path("logs").mkdir(exist_ok=True)

    # Load data
    sentences, y, sources = load_datasets(data_path)

    # Subsample if requested
    if sample_size and sample_size < len(sentences):
        logger.info(f"Subsampling to {sample_size} examples")
        np.random.seed(42)
        idx = np.random.choice(len(sentences), sample_size, replace=False)
        sentences = [sentences[i] for i in idx]
        y = y[idx]
        sources = sources[idx]

    # Build frequency dictionary
    freq_dict = build_frequency_dict()

    # Compute features
    X = compute_features(sentences, freq_dict)
    logger.info(f"Computed features shape: {X.shape}")
    logger.info(f"Feature columns: {list(X.columns)}")

    # Check for NaN values
    if X.isna().any().any():
        logger.warning("NaN values found in features, filling with 0")
        X = X.fillna(0)

    # Split by dataset for separate analysis
    results = {
        'metadata': {
            'experiment_info': {
                'n_sentences_total': len(sentences),
                'n_bootstrap': n_bootstrap,
                'n_cv_splits': n_splits,
                'hardware': {
                    'num_cpus': num_cpus,
                    'total_ram_gb': total_ram,
                    'available_ram_gb': available_ram
                }
            },
            'experiments': {}
        },
        'datasets': []
    }

    for dataset_name in ['WeeBIT', 'CEFR-SP']:
        logger.info(f"\n{'='*60}")
        logger.info(f"Processing dataset: {dataset_name}")
        logger.info(f"{'='*60}")

        idx = sources == dataset_name
        X_ds = X[idx].reset_index(drop=True)
        y_ds = y[idx]

        logger.info(f"Dataset size: {len(X_ds)} sentences")

        ds_results = {}

        # Experiment 1: Paired Bootstrap MSE Test
        logger.info("Experiment 1: Paired Bootstrap MSE Test")
        ds_results['bootstrap_mse_test'] = paired_bootstrap_mse_test(X_ds, y_ds, n_bootstrap)

        # Experiment 2: Coefficient CI
        logger.info("Experiment 2: Bootstrap Coefficient CI")
        combined_feats = ['avg_word_length', 'avg_syllables', 'avg_frequency', 'sentence_length',
                         'cv_word_length', 'cv_syllables', 'cv_frequency']
        coef_df = bootstrap_coef_ci(X_ds[combined_feats], y_ds, n_bootstrap)
        ds_results['coefficient_ci'] = coef_df.to_dict('records')

        # Experiment 3: Cross-Validation
        logger.info("Experiment 3: Cross-Validation")
        ds_results['cv_avg_only'] = cv_evaluate(X_ds[['avg_word_length', 'avg_syllables', 'avg_frequency', 'sentence_length']], y_ds, n_splits)
        ds_results['cv_combined'] = cv_evaluate(X_ds[combined_feats], y_ds, n_splits)

        # Experiment 4: Effect Size Analysis
        logger.info("Experiment 4: Effect Size Analysis")
        avg_feats = ['avg_word_length', 'avg_syllables', 'avg_frequency', 'sentence_length']
        combined_feats = avg_feats + ['cv_word_length', 'cv_syllables', 'cv_frequency']
        ds_results['effect_size'] = effect_size_analysis(
            X_ds[avg_feats],
            X_ds[combined_feats],
            y_ds,
            n_bootstrap
        )

        # Experiment 5: Ablation Study
        logger.info("Experiment 5: Ablation Study")
        ds_results['ablation'] = ablation_study(X_ds, y_ds)

        # Add to datasets array in correct schema format
        # Get the actual sentence indices for this dataset
        dataset_indices = np.where(idx)[0]

        # Create examples with input (sentence), output (readability score), and predictions
        examples = []
        for i, original_idx in enumerate(dataset_indices):
            examples.append({
                'input': sentences[original_idx],
                'output': str(y_ds[i]),
                'metadata_index': int(original_idx),
                'predict_r2_avg': str(ds_results.get('cv_avg_only', {}).get('test_r2_mean', '')),
                'predict_r2_combined': str(ds_results.get('cv_combined', {}).get('test_r2_mean', ''))
            })

        # Add dataset to results with only allowed fields (dataset and examples)
        results['datasets'].append({
            'dataset': dataset_name,
            'examples': examples
        })

        # Store experiment results in metadata at top level
        if 'experiments' not in results['metadata']:
            results['metadata']['experiments'] = {}
        results['metadata']['experiments'][dataset_name] = ds_results

        # Clean up
        del X_ds, y_ds
        gc.collect()

    # Save results
    logger.info(f"\nSaving results to {output_path}")
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)

    logger.info("Experiment completed successfully!")
    return results


@logger.catch(reraise=True)
def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Uniformity features readability experiment")
    parser.add_argument('--data', type=str, default='full_data_out.json',
                        help='Path to input data JSON file')
    parser.add_argument('--output', type=str, default='method_out.json',
                        help='Path to output JSON file')
    parser.add_argument('--n-bootstrap', type=int, default=10000,
                        help='Number of bootstrap samples')
    parser.add_argument('--n-splits', type=int, default=5,
                        help='Number of CV splits')
    parser.add_argument('--sample-size', type=int, default=None,
                        help='Subsample size (for testing)')

    args = parser.parse_args()

    run_experiment(
        data_path=args.data,
        output_path=args.output,
        n_bootstrap=args.n_bootstrap,
        n_splits=args.n_splits,
        sample_size=args.sample_size
    )


if __name__ == "__main__":
    main()
