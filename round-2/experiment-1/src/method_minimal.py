#!/usr/bin/env python3
"""
Minimal test script for readability prediction.
Uses simple heuristics instead of NLTK to avoid memory issues.
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


def load_datasets(data_path: str, max_examples: int = None) -> list:
    """Load datasets."""
    with open(data_path, 'r') as f:
        data = json.load(f)
    
    examples = []
    for dataset in data['datasets']:
        dataset_name = dataset['dataset']
        for ex in dataset['examples']:
            if max_examples and len(examples) >= max_examples:
                break
            ex_copy = ex.copy()
            ex_copy['metadata_source'] = dataset_name
            examples.append(ex_copy)
    
    return examples


def extract_simple_features(examples: list) -> tuple:
    """
    Extract simple features without external dependencies.
    Features: avg_word_length, avg_syllables (heuristic), sentence_length,
              cv_word_length, cv_syllables
    """
    features = []
    feature_names = ['avg_word_length', 'avg_syllables', 'sentence_length',
                     'cv_word_length', 'cv_syllables']
    
    for ex in examples:
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
            syllables = max(1, vowels - 1 if vowels > 2 else vowels)  # rough heuristic
            syllable_counts.append(syllables)
        
        # Average features
        avg_word_length = np.mean(word_lengths)
        avg_syllables = np.mean(syllable_counts)
        sentence_length = len(words)
        
        # Uniformity (CV)
        cv_word_length = np.std(word_lengths) / (avg_word_length + 1e-10)
        cv_syllables = np.std(syllable_counts) / (avg_syllables + 1e-10)
        
        features.append([
            avg_word_length, avg_syllables, sentence_length,
            cv_word_length, cv_syllables
        ])
    
    return np.array(features), feature_names


def evaluate_features(X: np.ndarray, y: np.ndarray, feature_names: list, cv: KFold):
    """Evaluate features using Ridge regression."""
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    model = Ridge(alpha=1.0)
    scores = cross_val_score(model, X_scaled, y, cv=cv, scoring='r2')
    
    return {
        'feature_names': feature_names,
        'r2_mean': float(np.mean(scores)),
        'r2_std': float(np.std(scores)),
    }


@logger.catch(reraise=True)
def main():
    """Main function."""
    logger.remove()
    logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
    
    logger.info("Starting minimal readability experiment")
    
    # Load data
    data_path = "full_data_out.json"
    
    # Test with different sizes
    for max_ex in [6, 50, 100, None]:
        logger.info(f"\n{'='*60}")
        if max_ex:
            logger.info(f"Testing with {max_ex} examples")
        else:
            logger.info("Testing with ALL examples")
        logger.info(f"{'='*60}")
        
        examples = load_datasets(data_path, max_examples=max_ex)
        logger.info(f"Loaded {len(examples)} examples")
        
        # Extract features
        X, feature_names = extract_simple_features(examples)
        logger.info(f"Feature matrix shape: {X.shape}")
        
        # Get targets
        y = np.array([float(ex['output']) for ex in examples])
        
        # Evaluate
        cv = KFold(n_splits=5, shuffle=True, random_state=42)
        results = evaluate_features(X, y, feature_names, cv)
        
        logger.info(f"R² = {results['r2_mean']:.4f} ± {results['r2_std']:.4f}")
        
        # Save predictions
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        model = Ridge(alpha=1.0)
        model.fit(X_scaled, y)
        predictions = model.predict(X_scaled)
        
        # Add predictions to examples
        for i, ex in enumerate(examples):
            ex['predict_readability'] = str(predictions[i])
        
        # Save output
        output = {
            'metadata': {
                'experiment': 'uniformity_principle_minimal',
                'num_examples': len(examples),
                'feature_names': feature_names,
                'r2_mean': results['r2_mean'],
                'r2_std': results['r2_std'],
            },
            'datasets': [{'dataset': 'combined', 'examples': examples}]
        }
        
        output_path = Path(f"method_out_{max_ex or 'full'}.json")
        output_path.write_text(json.dumps(output, indent=2))
        logger.info(f"Saved results to {output_path}")
        
        # Clean up
        del X, y, examples, output
        import gc
        gc.collect()
    
    logger.info("\nCompleted all tests!")


if __name__ == "__main__":
    main()
