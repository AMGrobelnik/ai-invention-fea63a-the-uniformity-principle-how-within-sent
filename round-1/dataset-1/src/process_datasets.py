#!/usr/bin/env python3
"""Process readability datasets into standard format."""

from loguru import logger
from pathlib import Path
import json
import sys
from datasets import load_dataset

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def process_weebit():
    """Process WeeBIT dataset."""
    logger.info("Loading WeeBIT dataset...")
    ds = load_dataset('deru35/only_weebit', split='train')

    results = []
    for i, row in enumerate(ds):
        # Map complexity_age_interval to readability score
        # Interval 1 = easiest (youngest), Interval 5 = hardest (oldest)
        # Convert to a 0-1 scale where 0 = easy, 1 = hard
        readability_score = (row['complexity_age_interval'] - 1) / 4.0

        results.append({
            'sentence_id': f'weebit_{i}',
            'text': row['text'],
            'readability_score': readability_score,
            'source_metadata': {
                'source': 'WeeBIT',
                'complexity_age_interval': row['complexity_age_interval'],
                'original_split': 'train'
            }
        })

    logger.info(f"Processed {len(results)} WeeBIT sentences")
    return results

@logger.catch(reraise=True)
def process_cefr_sp():
    """Process CEFR-SP dataset (all splits)."""
    logger.info("Loading CEFR-SP dataset...")
    ds = load_dataset('edesaras/CEFR-Sentence-Level-Annotations')

    results = []
    global_idx = 0
    for split_name in ds.keys():
        for i, row in enumerate(ds[split_name]):
            # Average the two annotators' CEFR levels
            # CEFR levels: 1=A1, 2=A2, 3=B1, 4=B2, 5=C1, 6=C2
            annotator_1 = row['Annotator I']
            annotator_2 = row['Annotator II']

            # Use average, normalize to 0-1 scale
            avg_level = (annotator_1 + annotator_2) / 2.0
            readability_score = (avg_level - 1) / 5.0  # Normalize to 0-1

            results.append({
                'sentence_id': f'cefr_sp_{global_idx}',
                'text': row['text'],
                'readability_score': readability_score,
                'source_metadata': {
                    'source': 'CEFR-SP',
                    'annotator_1': annotator_1,
                    'annotator_2': annotator_2,
                    'original_split': split_name
                }
            })
            global_idx += 1

    logger.info(f"Processed {len(results)} CEFR-SP sentences (all splits)")
    return results

@logger.catch(reraise=True)
def save_dataset(data, name):
    """Save dataset in full/mini/preview formats."""
    output_dir = Path('temp/datasets')
    output_dir.mkdir(parents=True, exist_ok=True)

    # Full dataset
    full_path = output_dir / f'full_{name}.json'
    full_path.write_text(json.dumps(data, indent=2))
    logger.info(f"Saved full dataset: {full_path} ({len(data)} items)")

    # Mini dataset (100 random items)
    import random
    random.seed(42)
    mini_size = min(100, len(data))
    mini_data = random.sample(data, mini_size)
    mini_path = output_dir / f'mini_{name}.json'
    mini_path.write_text(json.dumps(mini_data, indent=2))
    logger.info(f"Saved mini dataset: {mini_path} ({len(mini_data)} items)")

    # Preview dataset (5 items, truncated)
    preview_size = min(5, len(data))
    preview_data = []
    for item in data[:preview_size]:
        preview_item = item.copy()
        if len(preview_item['text']) > 200:
            preview_item['text'] = preview_item['text'][:200] + '...'
        preview_data.append(preview_item)

    preview_path = output_dir / f'preview_{name}.json'
    preview_path.write_text(json.dumps(preview_data, indent=2))
    logger.info(f"Saved preview dataset: {preview_path} ({len(preview_data)} items)")

@logger.catch(reraise=True)
def main():
    # Process WeeBIT dataset
    logger.info("Processing WeeBIT dataset...")
    weebit_data = process_weebit()
    save_dataset(weebit_data, 'weebit')

    # Process CEFR-SP dataset
    logger.info("Processing CEFR-SP dataset...")
    cefr_data = process_cefr_sp()
    save_dataset(cefr_data, 'cefr_sp')

    # Combine datasets for output
    logger.info("Creating combined output files...")

    # Data output 1: WeeBIT
    data_out_1 = {'dataset_name': 'WeeBIT', 'examples': weebit_data}
    Path('data_out_1.json').write_text(json.dumps(data_out_1, indent=2))
    logger.info(f"Saved data_out_1.json ({len(weebit_data)} examples)")

    # Data output 2: CEFR-SP
    data_out_2 = {'dataset_name': 'CEFR-SP', 'examples': cefr_data}
    Path('data_out_2.json').write_text(json.dumps(data_out_2, indent=2))
    logger.info(f"Saved data_out_2.json ({len(cefr_data)} examples)")

    # Create README
    readme_content = """# Readability Datasets

## Dataset 1: WeeBIT (deru35/only_weebit)

- **Source**: HuggingFace Hub (deru35/only_weebit)
- **Description**: WeeBIT corpus for readability assessment, created by Vajjala and Meurers (2012)
- **Size**: 3,125 sentences
- **Readability Levels**: 5 age intervals (1=easiest, 5=hardest)
- **Format**: sentence_id, text, readability_score (0-1 scale), source_metadata
- **Provenance**: Established benchmark dataset for readability assessment

## Dataset 2: CEFR-SP (edesaras/CEFR-Sentence-Level-Annotations)

- **Source**: HuggingFace Hub (edesaras/CEFR-Sentence-Level-Annotations)
- **Description**: CEFR-Based Sentence Profile corpus with 17k English sentences annotated by English education professionals
- **Size**: 17,000 sentences
- **Readability Levels**: CEFR levels A1-C2 (annotated by 2 professionals)
- **Format**: sentence_id, text, readability_score (0-1 scale), source_metadata
- **Provenance**: Published at EMNLP 2022 (Arase et al., 2022)

## Processing Steps

1. Both datasets were loaded from HuggingFace Hub
2. Readability scores were normalized to 0-1 scale (0=easy, 1=hard)
3. Data was converted to standard JSON schema
4. Full, mini, and preview versions were created

## Files

- `data_out_1.json`: WeeBIT dataset
- `data_out_2.json`: CEFR-SP dataset
- `temp/datasets/full_weebit.json`: Full WeeBIT dataset
- `temp/datasets/mini_weebit.json`: Mini WeeBIT dataset (100 samples)
- `temp/datasets/preview_weebit.json`: Preview WeeBIT dataset (5 samples)
- `temp/datasets/full_cefr_sp.json`: Full CEFR-SP dataset
- `temp/datasets/mini_cefr_sp.json`: Mini CEFR-SP dataset (100 samples)
- `temp/datasets/preview_cefr_sp.json`: Preview CEFR-SP dataset (5 samples)
"""

    Path('README.md').write_text(readme_content)
    logger.info("Saved README.md")

    logger.info("Dataset processing complete!")

if __name__ == "__main__":
    main()
