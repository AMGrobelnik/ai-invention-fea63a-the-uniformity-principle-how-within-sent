#!/usr/bin/env python3
"""
Readability prediction experiment testing the Uniformity Principle.
Compares average-only vs uniformity (CV) features for predicting readability.
"""

from loguru import logger
from pathlib import Path
import json
import sys
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import KFold, cross_val_score
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')


@logger.catch(reraise=True)
def main():
    """Run readability prediction experiment."""
    # Setup logging
    logger.remove()
    logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
    Path("logs").mkdir(exist_ok=True)
    logger.add("logs/run.log", rotation="30 MB", level="DEBUG")
    
    logger.info("Starting Uniformity Principle readability experiment")
    
    # Load data
    data_path = Path("full_data_out.json")
    if not data_path.exists():
        logger.error(f"Data file not found: {data_path}")
        return
    
    with open(data_path, 'r') as f:
        data = json.load(f)
    
    # Combine all examples
    all_examples = []
    for dataset in data['datasets']:
        dataset_name = dataset['dataset']
        for ex in dataset['examples']:
            ex_copy = ex.copy()
            ex_copy['metadata_source'] = dataset_name
            all_examples.append(ex_copy)
    
    logger.info(f"Loaded {len(all_examples)} total examples")
    
    # Extract features
    logger.info("Extracting features...")
    X, feature_names = extract_features(all_examples)
    
    # Get targets
    y = np.array([float(ex['output']) for ex in all_examples])
    
    # Define feature sets
    # Features: avg_word_length, avg_syllables, avg_word_freq, sentence_length, 
    #            cv_word_length, cv_syllables, cv_word_freq
    avg_indices = [0, 1, 2, 3]  # avg features only
    uniformity_indices = [4, 5, 6]  # CV features only
    combined_indices = [0, 1, 2, 3, 4, 5, 6]  # all features
    
    # Cross-validation setup
    cv = KFold(n_splits=5, shuffle=True, random_state=42)
    
    # Evaluate each feature set
    results = {}
    
    logger.info("Evaluating average-only features...")
    results['average_only'] = evaluate_feature_set(X, y, feature_names, avg_indices, cv)
    
    logger.info("Evaluating uniformity-only features...")
    results['uniformity_only'] = evaluate_feature_set(X, y, feature_names, uniformity_indices, cv)
    
    logger.info("Evaluating combined features...")
    results['combined'] = evaluate_feature_set(X, y, feature_names, combined_indices, cv)
    
    # Generate predictions for output
    logger.info("Generating predictions...")
    predictions = generate_predictions(X, y, avg_indices, uniformity_indices, combined_indices)
    
    # Bootstrap CI for average vs combined
    logger.info("Computing bootstrap CI...")
    bootstrap_results = compute_bootstrap_ci(y, predictions['average_only'], predictions['combined'],
                                             n_bootstrap=2000)
    
    # Add predictions to examples
    output_examples = []
    for i, ex in enumerate(all_examples):
        ex_with_pred = ex.copy()
        ex_with_pred['predict_average_only'] = str(predictions['average_only'][i])
        ex_with_pred['predict_uniformity_only'] = str(predictions['uniformity_only'][i])
        ex_with_pred['predict_combined'] = str(predictions['combined'][i])
        output_examples.append(ex_with_pred)
    
    # Organize by dataset
    dataset_examples = {}
    for ex in output_examples:
        source = ex.get('metadata_source', 'unknown')
        if source not in dataset_examples:
            dataset_examples[source] = []
        dataset_examples[source].append(ex)
    
    # Create output in exp_gen_sol_out schema
    output = {
        'metadata': {
            'experiment': 'uniformity_principle_readability',
            'num_examples': len(all_examples),
            'feature_names': feature_names,
            'results': results,
            'bootstrap_avg_vs_combined': bootstrap_results,
        },
        'datasets': []
    }
    
    for dataset_name, dataset_exs in dataset_examples.items():
        output['datasets'].append({
            'dataset': dataset_name,
            'examples': dataset_exs
        })
    
    # Save output
    output_path = Path("method_out.json")
    output_path.write_text(json.dumps(output, indent=2))
    logger.info(f"Saved results to {output_path}")
    
    # Log summary
    logger.info("="*60)
    logger.info("RESULTS SUMMARY")
    logger.info("="*60)
    for method, result in results.items():
        logger.info(f"{method}: R2 = {result['r2_mean']:.4f} +/- {result['r2_std']:.4f}")
    logger.info("="*60)


def extract_features(examples: list) -> tuple:
    """
    Extract features from examples.
    
    Features:
    0: avg_word_length
    1: avg_syllables (heuristic)
    2: avg_word_freq (heuristic - based on word length and common words)
    3: sentence_length
    4: cv_word_length (uniformity)
    5: cv_syllables (uniformity)
    6: cv_word_freq (uniformity)
    """
    features = []
    feature_names = ['avg_word_length', 'avg_syllables', 'avg_word_freq', 'sentence_length',
                     'cv_word_length', 'cv_syllables', 'cv_word_freq']
    
    # Common English words (higher frequency)
    common_words = set(['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'i',
                        'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at',
                        'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she',
                        'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what'])
    
    for i, ex in enumerate(examples):
        if i % 5000 == 0 and i > 0:
            logger.info(f"Extracted features for {i}/{len(examples)} examples")
        
        text = ex['input']
        words = text.split()
        
        if not words:
            features.append([0] * len(feature_names))
            continue
        
        # Word lengths
        word_lengths = [len(w) for w in words]
        
        # Syllable heuristic: count vowel groups
        syllable_counts = []
        for w in words:
            w_lower = w.lower()
            vowels = sum(1 for c in w_lower if c in 'aeiouy')
            # Rough heuristic
            syllables = max(1, vowels)
            syllable_counts.append(syllables)
        
        # Word frequency heuristic: common words = higher freq
        word_freqs = []
        for w in words:
            w_lower = w.lower().strip('.,!?;:"\'()[]{}')
            if w_lower in common_words:
                word_freqs.append(3.0)  # high frequency
            elif len(w_lower) <= 4:
                word_freqs.append(2.0)  # medium frequency
            else:
                word_freqs.append(1.0)  # low frequency
        word_freqs_log = [np.log(f + 1) for f in word_freqs]
        
        # Average features
        avg_word_length = np.mean(word_lengths)
        avg_syllables = np.mean(syllable_counts)
        avg_word_freq = np.mean(word_freqs_log)
        sentence_length = len(words)
        
        # Uniformity features (coefficient of variation)
        cv_word_length = np.std(word_lengths) / (avg_word_length + 1e-10)
        cv_syllables = np.std(syllable_counts) / (avg_syllables + 1e-10)
        cv_word_freq = np.std(word_freqs_log) / (avg_word_freq + 1e-10) if word_freqs_log else 0
        
        features.append([
            avg_word_length, avg_syllables, avg_word_freq, sentence_length,
            cv_word_length, cv_syllables, cv_word_freq
        ])
    
    return np.array(features), feature_names


def evaluate_feature_set(X: np.ndarray, y: np.ndarray, feature_names: list,
                        feature_indices: list, cv: KFold) -> dict:
    """Evaluate a feature set using cross-validation."""
    X_subset = X[:, feature_indices]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_subset)
    
    model = Ridge(alpha=1.0)
    scores_r2 = cross_val_score(model, X_scaled, y, cv=cv, scoring='r2')
    
    return {
        'feature_names': [feature_names[i] for i in feature_indices],
        'r2_mean': float(np.mean(scores_r2)),
        'r2_std': float(np.std(scores_r2)),
    }


def generate_predictions(X: np.ndarray, y: np.ndarray,
                        avg_indices: list, uniformity_indices: list, 
                        combined_indices: list) -> dict:
    """Generate predictions using all training data."""
    predictions = {}
    
    # Average-only
    scaler = StandardScaler()
    X_avg = scaler.fit_transform(X[:, avg_indices])
    model = Ridge(alpha=1.0)
    model.fit(X_avg, y)
    predictions['average_only'] = model.predict(X_avg)
    
    # Uniformity-only
    scaler = StandardScaler()
    X_uni = scaler.fit_transform(X[:, uniformity_indices])
    model = Ridge(alpha=1.0)
    model.fit(X_uni, y)
    predictions['uniformity_only'] = model.predict(X_uni)
    
    # Combined
    scaler = StandardScaler()
    X_comb = scaler.fit_transform(X[:, combined_indices])
    model = Ridge(alpha=1.0)
    model.fit(X_comb, y)
    predictions['combined'] = model.predict(X_comb)
    
    return predictions


def compute_bootstrap_ci(y_true: np.ndarray, y_pred1: np.ndarray, y_pred2: np.ndarray,
                         n_bootstrap: int = 2000, confidence: float = 0.95) -> dict:
    """
    Compute bootstrap confidence interval for difference in R2 between two models.
    """
    from sklearn.metrics import r2_score
    
    logger.info(f"Computing bootstrap CI with {n_bootstrap} samples...")
    
    n = len(y_true)
    differences = []
    
    for i in range(n_bootstrap):
        if i % 500 == 0 and i > 0:
            logger.info(f"Bootstrap sample {i}/{n_bootstrap}")
        
        # Sample with replacement
        indices = np.random.choice(n, n, replace=True)
        y_true_b = y_true[indices]
        y_pred1_b = y_pred1[indices]
        y_pred2_b = y_pred2[indices]
        
        # Compute R2 for both
        r2_1 = r2_score(y_true_b, y_pred1_b)
        r2_2 = r2_score(y_true_b, y_pred2_b)
        differences.append(r2_2 - r2_1)
    
    differences = np.array(differences)
    mean_diff = np.mean(differences)
    
    # Confidence interval
    alpha = 1 - confidence
    ci_lower = np.percentile(differences, (alpha/2) * 100)
    ci_upper = np.percentile(differences, (1 - alpha/2) * 100)
    
    # P-value (two-sided test for difference != 0)
    p_value = 2 * min(
        np.mean(differences <= 0),
        np.mean(differences >= 0)
    )
    
    return {
        'mean_diff': float(mean_diff),
        'ci_lower': float(ci_lower),
        'ci_upper': float(ci_upper),
        'p_value': float(p_value),
        'significant': bool(p_value < 0.05)
    }


if __name__ == "__main__":
    main()
