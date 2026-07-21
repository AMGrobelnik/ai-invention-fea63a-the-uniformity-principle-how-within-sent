# Readability Datasets for Sentence-Level Readability Assessment

## Overview
This directory contains three standardized readability datasets acquired for evaluating the uniformity hypothesis in sentence-level readability assessment.

## Datasets Acquired (Final Selection)

### 1. CLEAR Corpus (CommonLit Ease of Readability) - PRIMARY
- **Source**: HuggingFace (`casey-martin/CommonLit-Ease-of-Readability`)
- **Size**: 3,543 reading passage excerpts
- **Readability Metrics**: Multiple (Flesch-Kincaid Grade Level, Flesch Reading Ease, ARI, SMOG, Dale-Chall, CAREC, CML2RI)
- **Score Range**: Normalized to 0-1 (0=easiest, 1=hardest)
- **Primary Metric Used**: Flesch-Kincaid Grade Level
- **Text Type**: Excerpts (average 173 words)
- **License**: Unknown (from HuggingFace)
- **Citation**: Crossley, S., et al. (2023). The CommonLit Ease of Readability (CLEAR) Corpus. Springer.

### 2. Agentlans Readability Dataset (Sampled)
- **Source**: HuggingFace (`agentlans/readability`)
- **Size**: 2,000 sampled paragraphs (from 104,761 total)
- **Grade Levels**: Continuous scores from multiple sources
- **Sources**: arxiv (35%), tinystories (24%), fineweb-edu (23%), wikipedia-en (19%)
- **Score Range**: Normalized to 0-1 (0=easiest, 1=hardest)
- **Text Type**: Paragraphs (average 150 words)
- **License**: CC0 1.0
- **Citation**: agentlans (2024). Readability dataset from HuggingFace.

### Note on OneStopEnglish Corpus
OneStopEnglish was acquired but NOT included in final selection due to:
- Longer texts (not ideal for sentence-level evaluation)
- Same content repeated at 3 reading levels (potential data leakage)
- Smaller size (567 examples vs. 3,543 and 2,000 in selected datasets)

The OneStopEnglish data is still available in `datasets/` folder if needed.

## Schema Compliance
All datasets conform to `exp_sel_data_out.json` schema with:
- `input`: text (sentence/excerpt/text)
- `output`: normalized readability score as string (0.0=easiest, 1.0=hardest)
- `metadata_fold`: set to "test"
- `metadata_source`: dataset source identifier
- Additional metadata fields with `metadata_` prefix

## Files per Dataset
- `full_<dataset>.json`: Complete dataset (all examples)
- `mini_<dataset>.json`: 50-example subset for development
- `preview_<dataset>.json`: 3-example preview with truncated text
- `dataset_info_<dataset>.json`: Metadata and statistics

## Comparison to WeeBIT and CEFR-SP
| Dataset | N Examples | Mean Score | Score Range | Avg Text Length |
|----------|-------------|------------|-------------|------------------|
| WeeBIT (from prior experiments) | ~2,000 | ~0.5 | 0-1 | ~20 words (sentences) |
| CEFR-SP (from prior experiments) | ~1,500 | ~0.5 | 0-1 | ~15 words (sentences) |
| **CLEAR Corpus** | 3,543 | 0.50 | 0.0-1.0 | ~173 words (excerpts) |
| **OneStopEnglish** | 567 | 0.50 | 0.0-1.0 | ~200 words (texts) |
| **Agentlans Readability** | 2,000 | 0.42 | 0.004-0.832 | ~150 words (paragraphs) |

## Usage Examples

### Loading CLEAR Corpus
```python
import json
with open('full_CLEAR_corpus.json', 'r') as f:
    data = json.load(f)
examples = data['datasets'][0]['examples']
print(f"Loaded {len(examples)} examples")
print(f"Sample input: {examples[0]['input'][:100]}...")
print(f"Sample output (score): {examples[0]['output']}")
```

### Loading OneStopEnglish
```python
import json
with open('full_OneStopEnglish.json', 'r') as f:
    data = json.load(f)
examples = data['datasets'][0]['examples']
print(f"Loaded {len(examples)} examples")
print(f"Sample metadata_source: {examples[0]['metadata_source']}")
print(f"Sample metadata_original_label: {examples[0]['metadata_original_label']}")
```

## Known Issues and Limitations
1. **CLEAR Corpus**: Texts are excerpts, not sentences. For sentence-level evaluation, consider splitting excerpts into sentences using NLTK.
2. **OneStopEnglish**: Texts are longer than typical sentences. Same content appears at 3 reading levels (data leakage if not careful).
3. **Agentlans Readability**: Only 2,000 of 104,761 examples used. Grade scores are computed metrics, not human annotations.

## Next Steps
1. Use these datasets to evaluate sentence-level readability models
2. Compare performance across datasets to test uniformity hypothesis
3. Consider acquiring WSJ dataset (Liu & Lee 2023) for additional evaluation
4. If sentence-level data needed, split CLEAR excerpts using NLTK sentence tokenizer

## WSJ Dataset Status
The WSJ dataset (Liu & Lee 2023, 1,200 WSJ sentences with 20 annotator ratings) was not acquired due to:
- Dataset requires form submission at http://www.italianlp.it/corpus-of-sentences-rated-with-human-complexity-judgments/download-english-sentences
- Alternative GitHub repositories checked but direct download not available
- Three alternative datasets successfully acquired as fallback

If WSJ dataset is required, submit the form with research affiliation and wait for download link.
