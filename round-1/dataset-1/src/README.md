# Readability Datasets

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
