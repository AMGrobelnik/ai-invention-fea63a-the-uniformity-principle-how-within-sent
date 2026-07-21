#!/usr/bin/env python3
"""Quick test script to debug method.py issues."""

import sys
sys.path.insert(0, '/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_experiment_1')

from pathlib import Path
import json
import numpy as np

# Test 1: Load mini dataset
print("Test 1: Loading mini dataset...")
with open("mini_data_out.json", 'r') as f:
    data = json.load(f)
    
examples = []
for dataset in data['datasets']:
    dataset_name = dataset['dataset']
    for ex in dataset['examples']:
        ex_copy = ex.copy()
        ex_copy['metadata_source'] = dataset_name
        examples.append(ex_copy)
        
print(f"Loaded {len(examples)} examples")

# Test 2: Test feature extraction with a simple implementation
print("\nTest 2: Testing feature extraction...")

def simple_features(text):
    """Extract simple features from text."""
    words = text.split()
    if not words:
        return [0, 0, 0, 0, 0, 0, 0]
    
    # Average features
    avg_word_length = np.mean([len(w) for w in words])
    avg_syllables = np.mean([max(1, len(w) // 3) for w in words])  # rough estimate
    avg_word_freq = 0  # placeholder
    sentence_length = len(words)
    
    # Uniformity features (CV)
    word_lengths = [len(w) for w in words]
    syllable_counts = [max(1, len(w) // 3) for w in words]
    
    cv_word_length = np.std(word_lengths) / (avg_word_length + 1e-10)
    cv_syllables = np.std(syllable_counts) / (avg_syllables + 1e-10)
    cv_word_freq = 0  # placeholder
    
    return [avg_word_length, avg_syllables, avg_word_freq, sentence_length,
            cv_word_length, cv_syllables, cv_word_freq]

# Extract features for all examples
X = []
for ex in examples:
    features = simple_features(ex['input'])
    X.append(features)
    
X = np.array(X)
print(f"Feature matrix shape: {X.shape}")
print(f"Feature sample: {X[0]}")

# Test 3: Test model training
print("\nTest 3: Testing model training...")
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score, KFold
from sklearn.preprocessing import StandardScaler

y = np.array([float(ex['output']) for ex in examples])
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = Ridge(alpha=1.0)
cv = KFold(n_splits=2, shuffle=True, random_state=42)
scores = cross_val_score(model, X_scaled, y, cv=cv, scoring='r2')
print(f"R² scores: {scores}")
print(f"Mean R²: {np.mean(scores):.4f}")

print("\nAll tests passed!")
