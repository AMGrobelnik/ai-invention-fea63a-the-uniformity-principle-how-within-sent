# gen_art_dataset_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_art`
> Run: `run_nOuUUSNqdMp4` — The Uniformity Principle: How Within-Sentence Consistency Predicts Readability
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_dataset_1` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-07-21 15:44:20 UTC

```
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_1_idx1
type: dataset
title: Acquire WSJ or CLEAR readability dataset
summary: >-
  Find, download, and standardize an additional sentence-level readability dataset (WSJ from Liu & Lee 2023 or CLEAR corpus)
  to evaluate the uniformity hypothesis beyond WeeBIT and CEFR-SP. Output as standardized JSON with full/mini/preview splits.
runpod_compute_profile: gpu
ideal_dataset_criteria: >-
  Target: English sentence-level readability dataset with 1,000+ sentences and numerical readability scores. Ideally acquire
  TWO datasets (target_num_datasets=2). Primary targets: (1) WSJ dataset (Liu & Lee 2023) - 1,200 WSJ sentences with 20 annotator
  ratings each, available from authors or HuggingFace; (2) CLEAR corpus - ~5,000 excerpts grades 3-12 with multiple readability
  metrics (MIT license), available from CommonLit or HuggingFace. Must be openly available, machine-readable (CSV/JSON/TSV),
  and have associated readability scores (annotator ratings or computed metrics). Output must conform to exp_sel_data_out.json
  schema with 'input' (sentence text) and 'output' (normalized 0-1 readability score) fields. If only excerpts (not sentences)
  available, use as-is or split into sentences with NLTK.
dataset_search_plan: "IMPORTANT: Acquire at least TWO distinct datasets for robust evaluation. Execute searches in parallel\
  \ where possible.\n\nPHASE 1: Search for and acquire WSJ dataset (Liu & Lee 2023) [PRIORITY 1]\n==========================================================================\n\
  SEARCH STEPS (execute in parallel where possible):\n1. HuggingFace search: Use aii-hf-datasets skill\n   - Command: python\
  \ aii_hf_search_datasets.py --query 'WSJ readability' --limit 10\n   - Command: python aii_hf_search_datasets.py --query\
  \ 'Liu Lee readability' --limit 10\n   - Command: python aii_hf_search_datasets.py --query 'readability annotator ratings'\
  \ --limit 10\n2. Web search for paper and dataset:\n   - Search: 'Liu Lee 2023 Assessing Reliability Automatic Readability\
  \ Assessment Metrics BEA'\n   - Search: 'WSJ 1200 sentences readability dataset'\n   - Check ACL Anthology or arXiv for\
  \ paper appendix with dataset link\n3. Check open data repositories:\n   - Figshare.com search: 'WSJ readability dataset'\n\
  \   - Zenodo.org search: 'readability assessment WSJ'\n   - OSF.io search: 'readability dataset'\n4. If not found openly,\
  \ draft author contact:\n   - Likely authors: Chao Liu, Weiwei Lee (check paper for affiliations)\n   - Email template:\
  \ request dataset access for research, mention reproducibility\n\nACQUISITION (if found):\n- If on HuggingFace: Use aii-hf-datasets\
  \ download script with dataset ID\n- If CSV/JSON URL: Use requests.get() or wget to download\n- If requires request: Send\
  \ email, wait up to 2 days (proceed with other datasets in parallel)\n\nSUCCESS CRITERIA: WSJ dataset downloaded with columns:\
  \ sentence_id, sentence_text, readability_score (mean of 20 annotators)\nFALLBACK: If not acquired within 2 hours, proceed\
  \ to Phase 2 but continue monitoring for author response\n\nPHASE 2: Acquire CLEAR corpus (CommonLit) [PRIORITY 2]\n=============================================================\n\
  SEARCH STEPS:\n1. HuggingFace search:\n   - Command: python aii_hf_search_datasets.py --query 'commonlit' --limit 10\n \
  \  - Command: python aii_hf_search_datasets.py --query 'CLEAR corpus' --limit 10\n2. Web search:\n   - Search: 'CommonLit\
  \ CLEAR corpus download'\n   - Search: 'CLEAR readability corpus MIT license'\n3. Check CommonLit website:\n   - URL: https://www.commonlit.org/en/research/corpus\
  \ (or similar)\n   - Look for 'Download' or 'Request Access' button\n4. Check HuggingFace directly:\n   - Try dataset IDs:\
  \ 'common_lit', 'commonlit', 'clear_corpus'\n\nACQUISITION:\n- If on HuggingFace: Preview first (python aii_hf_preview_datasets.py\
  \ commonlit/dataset_id), then download\n- If on CommonLit website: Register account, download CSV/JSON (may need agreement\
  \ to terms)\n- Expected format: CSV with columns like 'text', 'grade_level', 'fk_grade_level', 'lexile_level'\n\nHANDLING\
  \ EXCERPTS (not sentences):\nOption A (PREFERRED): Use excerpts as-is. Readability formulas work on text excerpts, not just\
  \ sentences.\nOption B (IF SENTENCES REQUIRED): Split excerpts into sentences:\n   from nltk.tokenize import sent_tokenize\n\
  \   nltk.download('punkt')\n   sentences = sent_tokenize(excerpt)\n   Create one row per sentence, assign excerpt's readability\
  \ score to each sentence\n\nSUCCESS CRITERIA: CLEAR corpus downloaded with text excerpts and at least one readability score\
  \ column\nFALLBACK: If unavailable, proceed to Phase 3\n\nPHASE 3: Alternative dataset acquisition [PRIORITY 3 - if Phases\
  \ 1-2 incomplete]\n==================================================================================\nSearch for additional\
  \ readability datasets to reach target_num_datasets=2:\n\n1. WeeBIT additional data:\n   - Check if WeeBIT has additional\
  \ sentences beyond what's already used\n   - Dataset may have multiple sources (Wikipedia, Simple Wikipedia, etc.)\n\n2.\
  \ CEFR-SP additional data:\n   - Check for additional CEFR-SP splits or versions\n   - Dataset may have sentence-level annotations\
  \ not yet extracted\n\n3. HuggingFace broader search:\n   - Command: python aii_hf_search_datasets.py --query 'readability'\
  \ --limit 30\n   - Preview promising datasets (eii_hf_preview_datasets.py <dataset_id>)\n   - Look for: sentence text +\
  \ readability score/grade level\n\n4. OneStopEnglish corpus:\n   - Search GitHub: 'OneStopEnglish corpus'\n   - Check NLP4CALL\
  \ repository (nlp4call.github.io)\n   - Dataset: Texts at 3 levels (elementary, intermediate, advanced)\n   - Need to split\
  \ into sentences and assign scores: elementary=0.3, intermediate=0.6, advanced=0.9\n\n5. Standard Readability Dataset (Vajjala\
  \ & Meurers 2012):\n   - Search: 'Standard Readability Dataset Vajjala Meurers'\n   - Check ACL Anthology or authors' websites\n\
  \n6. Newsela corpus (requires registration):\n   - Website: newsela.com\n   - Has articles at 5 grade levels\n   - Need\
  \ Newsela API access or special agreement (check if available to researchers)\n\nSUCCESS CRITERIA: At least 2 datasets total\
  \ acquired (including WSJ and/or CLEAR)\n\nPHASE 4: Standardize datasets to exp_sel_data_out.json schema\n==============================================================\n\
  Execute separately for each acquired dataset.\n\nSTEP 1: Load and inspect raw data\n   import pandas as pd\n   df = pd.read_csv('dataset.csv')\
  \  # or pd.read_json(), depending on format\n   print(df.columns)\n   print(df.head())\n   print(df.info())\n\nSTEP 2: Map\
  \ to schema\n   Schema required fields:\n   - 'input': string (sentence or excerpt text)\n   - 'output': float (normalized\
  \ readability score, 0.0=easiest, 1.0=hardest)\n   Optional fields:\n   - 'metadata_fold': string (default='test' for new\
  \ evaluation datasets)\n   - 'sentence_id': string or int (original ID if available)\n\n   Mapping examples:\n   - WSJ:\
  \ input ← 'sentence_text', output ← 'mean_readability_score'\n   - CLEAR: input ← 'text', output ← normalize('grade_level'\
  \ or 'fk_grade_level')\n\nSTEP 3: Normalize readability scores to 0-1\n   Formula: normalized = (raw_score - min_score)\
  \ / (max_score - min_score)\n   \n   SPECIAL CASES:\n   - If lower raw scores = easier (e.g., Flesch-Kincaid grade level):\
  \ invert so 0.0=easiest\n     normalized = 1.0 - ((raw_score - min_score) / (max_score - min_score))\n   - If all scores\
  \ identical (can't normalize): use raw scores, document in README\n   - If multiple readability metrics: create SEPARATE\
  \ output files for each metric\n\nSTEP 4: Create output files\n   a. full_dataset.json: ALL rows, full text, properly formatted\n\
  \      - Use df.to_json('full_dataset.json', orient='records', lines=True)\n      - Validate with aii-json skill\n\n   b.\
  \ mini_dataset.json: 50 randomly sampled rows\n      - df_sample = df.sample(n=50, random_state=42)\n      - Save to mini_dataset.json\n\
  \n   c. preview_dataset.json: 3 rows, text truncated to 100 chars\n      - df_preview = df.head(3).copy()\n      - df_preview['input']\
  \ = df_preview['input'].str[:100] + '...'\n      - Save to preview_dataset.json\n\nSTEP 5: Validate schema\n   - Use aii-json\
  \ skill: validate full_dataset.json against exp_sel_data_out.json schema\n   - Fix any validation errors before proceeding\n\
  \nPHASE 5: Document dataset statistics\n====================================\nExecute for each standardized dataset.\n\n\
  1. Compute basic statistics:\n   - n_sentences: len(df)\n   - mean_score, std_score, min_score, max_score\n   - Score histogram:\
  \ pd.cut(df['output'], bins=10).value_counts()\n   - Sentence length distribution: df['input'].str.split().str.len().describe()\n\
  \n2. Create comparison table (vs. WeeBIT and CEFR-SP):\n   | Dataset | N Sentences | Mean Score | Score Range | Avg Sentence\
  \ Length |\n   |----------|-------------|------------|-------------|---------------------|\n   | WeeBIT   | [from prior\
  \ experiments] | [value] | [range] | [value] |\n   | CEFR-SP  | [from prior experiments] | [value] | [range] | [value] |\n\
  \   | NEW DS   | [computed] | [computed] | [computed] | [computed] |\n\n3. Check data quality:\n   - Duplicates: df.duplicated('input').sum()\n\
  \   - Outliers: rows where score > mean + 3*std or score < mean - 3*std\n   - Very short sentences: df[df['input'].str.split().str.len()\
  \ < 3]\n\n4. Save dataset_info.json:\n   {\n     \"dataset_name\": \"WSJ_Liu_Lee_2023\",\n     \"source_url\": \"https://huggingface.co/datasets/...\"\
  ,\n     \"license\": \"MIT\",\n     \"n_sentences\": 1200,\n     \"score_distribution\": {\"mean\": 0.5, \"std\": 0.2, ...},\n\
  \     \"preprocessing\": \"None / Sentence splitting with NLTK\",\n     \"schema_version\": \"exp_sel_data_out.json v1.0\"\
  \n   }\n\n5. Create README.md with:\n   - Dataset description and source\n   - Loading instructions (pandas code)\n   -\
  \ Comparison to WeeBIT/CEFR-SP\n   - Known issues or limitations\n   - Citation information\n\nTIME ALLOCATION:\n-----------------\n\
  - Phase 1 (WSJ search): 2 hours (including author contact)\n- Phase 2 (CLEAR acquisition): 1.5 hours\n- Phase 3 (Alternatives):\
  \ 1.5 hours (if 1-2 fail or to acquire 2nd dataset)\n- Phase 4 (Standardization): 2 hours (for 2 datasets)\n- Phase 5 (Documentation):\
  \ 1 hour\n- BUFFER: 1 hour for unexpected issues\nTOTAL: 6 hours (with 1 hour buffer within the 6h limit)\n\nTECHNICAL IMPLEMENTATION\
  \ NOTES FOR EXECUTOR:\n=============================================\n1. Using aii-hf-datasets skill:\n   - Search: python\
  \ aii_hf_search_datasets.py --query 'X' --limit 10\n   - Preview: python aii_hf_preview_datasets.py <dataset_id> --num-rows\
  \ 5\n   - Download: python aii_hf_download_datasets.py <dataset_id> --split train\n\n2. Direct download (if not on HuggingFace):\n\
  \   import requests\n   url = 'https://example.com/dataset.csv'\n   response = requests.get(url, stream=True)\n   with open('dataset.csv',\
  \ 'wb') as f:\n       for chunk in response.iter_content(chunk_size=8192):\n           f.write(chunk)\n\n3. Schema validation:\n\
  \   - Use aii-json skill to validate output\n   - If aii-json not available: manually check JSON structure matches schema\n\
  \n4. Handling missing values:\n   - Drop rows where 'input' is NaN or empty string\n   - Drop rows where 'output' is NaN\
  \ (unless dataset is for unsupervised evaluation)\n\n5. Output file organization:\n   Save all output files in: /workspace/datasets/<dataset_name>/\n\
  \   Files: full_dataset.json, mini_dataset.json, preview_dataset.json, dataset_info.json, README.md\n\nERROR HANDLING AND\
  \ FALLBACK STRATEGIES:\n========================================\n1. Dataset not found:\n   - Log search query and result\n\
  \   - Try next candidate in the priority list\n   - Continue until target_num_datasets (2) acquired\n\n2. Download fails\
  \ (connection error, 404):\n   - Retry 3 times with 5-second delays\n   - Try mirror URL if available\n   - Skip to next\
  \ candidate\n\n3. Schema validation fails:\n   - Print exact validation errors\n   - Check field names, data types, required\
  \ fields\n   - Fix and re-validate\n\n4. Score normalization fails (constant scores or NaN):\n   - Use raw scores without\
  \ normalization\n   - Document in README.md\n   - Add warning that scores are not normalized\n\n5. CLEAR excerpts too long\
  \ (>500 words):\n   - Option A: Truncate to 200 words (preserve readability)\n   - Option B: Split into sentences (more\
  \ work but better for sentence-level evaluation)\n   - Decision: Use Option A (truncate) for speed, unless explicitly instructed\
  \ otherwise\n\n6. WeeBIT/CEFR-SP already used in experiments:\n   - DO NOT include WeeBIT or CEFR-SP as \"new\" datasets\n\
  \   - These are already available; find genuinely new datasets\n   - Check if WeeBIT/CEFR-SP have additional splits not\
  \ yet used (acceptable to use)\n\nDELIVERABLES CHECKLIST:\n========================\nFor each acquired dataset (target:\
  \ 2 datasets), ensure:\n[ ] full_<dataset_name>.json - Complete standardized dataset\n[ ] mini_<dataset_name>.json - 50-row\
  \ subset for development\n[ ] preview_<dataset_name>.json - 3-row preview with truncated text\n[ ] dataset_info.json - Metadata\
  \ and statistics\n[ ] README.md - Documentation and usage examples\n[ ] Comparison table (new dataset vs. WeeBIT vs. CEFR-SP)\n\
  \nEXECUTION ORDER:\n=================\n1. Start Phase 1 (WSJ search) and Phase 2 (CLEAR search) IN PARALLEL\n2. If Phase\
  \ 1 succeeds: download and standardize WSJ dataset\n3. If Phase 2 succeeds: download and standardize CLEAR dataset\n4. If\
  \ only 1 dataset acquired: start Phase 3 to acquire 2nd dataset\n5. Standardize all acquired datasets (Phase 4)\n6. Document\
  \ statistics (Phase 5)\n7. Verify all deliverables present"
target_num_datasets: 2
</artifact_plan>



<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Web search (Serper), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-image-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
</skills>
</available_resources>

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for dataset selection, evaluation metrics, agent orchestration patterns.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing.
TODO 2. Read skill files for your data sources (see <available_data_sources>) and domain handbook if applicable (see <available_domain_handbooks>). Based on plan and context, decide which source(s) to use. Include everything specified in the artifact plan, but you may also collect additional relevant data beyond what's listed. Run 16 diverse searches across chosen source(s) — BROAD, GENERAL terms, not very specific. Parallelize where supported.
TODO 3. Identify the 8 most promising datasets. IMPORTANT: Only consider datasets under 300MB. Preview/inspect sample rows for each candidate. Parallelize previews.
TODO 4. Research each candidate BEFORE choosing which to download. For each, search the web (aii-web-tools skill): dataset name, papers citing it, original source/task, popularity. Red flags: no search results, no papers, anonymized features (F1, F2...), <100 downloads, no documentation. Green flags: papers using it, clear documentation, meaningful features, established benchmark. Also consider: will features/structure allow meaningful evaluation of the planned method?
TODO 5. Decide which to KEEP vs DISCARD. Look for: clear structure, relevant fields, quality examples matching requirements, confirmed provenance. Determine which 4 datasets have the most suitable data. Download and save to `temp/datasets/`. Parallelize downloads.
</todos>
```

### [2] HUMAN-USER prompt · 2026-07-21 15:44:20 UTC

```
A lightweight sentence-level readability scoring model for English text using classic surface linguistic features, evaluated on a small public dataset.
```

### [3] SKILL-INPUT — aii-python · 2026-07-21 15:44:36 UTC

The agent loaded the **aii-python** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-python
description: Python coding standards for experiment and evaluation scripts. Covers environment setup, logging, error handling, and code structure.
---

## Environment Setup

- Python 3.12+
- **NEVER use `pip` or `.venv/bin/pip`** — they are not installed. Use `uv` for ALL package operations:
  ```bash
  uv venv .venv --python=3.12
  source .venv/bin/activate  # or: .venv/bin/python script.py
  uv pip install pandas loguru  # NOT: pip install
  ```
- Create `.toml` file with dependencies, create uv `.venv` and activate it
- NO inline dependencies (no `# /// script` headers)

## Logging

Use `loguru` for all logging. Add a file sink alongside stdout.

```python
from loguru import logger
import sys

logger.remove()  # Remove default handler
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")
```

Rules:
- Log every major step (data loading, processing start/end, results)
- If applicable, log every LLM API call input and output
- Truncate long outputs in logs (add truncation logic for potentially large strings)
- Use `logger.error()` in except blocks (traceback auto-captured)

## Error Handling

- Wrap major operations in try/except blocks
- Use `@logger.catch(reraise=True)` decorator on main functions — without `reraise=True`, the script exits 0 even on uncaught exceptions, hiding failures from downstream consumers
- Use explicit exception types, not bare `except:`
- Never silently swallow exceptions — always log them

```python
@logger.catch(reraise=True)
def main():
    try:
        data = load_data(path)
    except FileNotFoundError:
        logger.error("Data file not found")
        raise
    except json.JSONDecodeError:
        logger.error("Invalid JSON in data file")
        raise
```

## Code Structure

- Use `pathlib.Path` for file operations: `Path("data/input.json").read_text()` not `open(...).read()`
- Use type hints for function signatures
- Use keyword arguments for functions with more than 4 parameters
- No hardcoded paths — derive from script location or accept as arguments

## Script Pattern

Standard pattern for experiment/evaluation scripts:

```python
#!/usr/bin/env python3
"""Brief description of what this script does."""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    # Load data
    data_path = Path("full_data_out.json")
    logger.info(f"Loading data from {data_path}")
    data = json.loads(data_path.read_text())
    logger.info(f"Loaded {len(data['examples'])} examples")

    # Process
    results = []
    for i, example in enumerate(data["examples"]):
        try:
            result = process(example)
            results.append(result)
        except Exception:
            logger.error(f"Failed on example {i}")
            continue

    # Save output
    output = {"examples": results}
    Path("method_out.json").write_text(json.dumps(output, indent=2))
    logger.info(f"Saved {len(results)} results")

if __name__ == "__main__":
    main()
```
````

### [4] SKILL-INPUT — aii-hf-datasets · 2026-07-21 15:44:36 UTC

The agent loaded the **aii-hf-datasets** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-hf-datasets
description: Searches, previews, and downloads datasets from HuggingFace Hub. Use when user needs machine learning datasets, training data, HuggingFace datasets, dataset discovery, or .parquet/.json exports.
---

## Contents

- Workflow (3-phase dataset discovery)
- Scripts (Search, Preview, Download)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Workflow: 3-Phase Dataset Discovery

### Phase 1: Search for Datasets
Find datasets with metadata (configs, splits, features, sizes)
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_search_datasets.py --query "sentiment analysis" --limit 5
```

### Phase 2: Preview Dataset (if promising)
Inspect metadata AND sample rows in one call
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_preview_datasets.py openai/gsm8k
```

### Phase 3: Download Dataset (if suitable)
Download after reviewing the preview
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_download_datasets.py openai/gsm8k --config main --split train
```

---

## Scripts

### Search HuggingFace Datasets (aii_hf_search_datasets.py)

Search and discover datasets on HuggingFace Hub.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_search_datasets.py --query "text classification" --limit 5
```

**Parallel execution (multiple queries):**

IMPORTANT: Use full python path with GNU parallel (venv activate does NOT work in parallel subshells):
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_search_datasets.py" && \
parallel -j 10 -k --group --will-cite '$PY $S --query {} --limit 3' ::: 'sentiment' 'classification' 'translation'
```

**Example output:**
```
Found 5 dataset(s) for query='text classification'

============================================================
Dataset 1: stanfordnlp/imdb
Downloads: 2,500,000 | Likes: 1,234
Description: Large Movie Review Dataset for binary sentiment classification...
Tags: text-classification, en, sentiment-analysis
```

**Result fields per dataset:**

Each entry in ``results`` carries:

- ``id`` / ``downloads`` / ``likes`` / ``tags`` / ``description`` — standard
  HF metadata
- ``has_loader_script`` (bool) — repo ships a top-level ``<repo>.py`` loader.
  ``datasets>=3`` won't run these directly; the dataset is reachable only
  via the Datasets Server's pre-converted parquet shards. Treat as a yellow
  flag.
- ``loadable`` (bool) — **prefer datasets where this is ``True``.** Means
  the dataset is reachable via *some* path: either native parquet (no
  script) or HF auto-converted the script's output to parquet. When
  ``False``, the script needs deps HF can't install (e.g. ``conllu``,
  custom audio decoders) and ``aii_hf_datasets__download_datasets`` will
  fail — pick a different candidate.

**Parameters:**

`--query` (optional)
- Search query string
- Example: `--query "sentiment analysis"`

`--limit` (optional)
- Maximum number of results (default: 5)

`--tags` (optional)
- Filter by tags (comma-separated)
- Format: `category:value`
- Examples: `language:en`, `task_categories:text-classification`

`--sort` (optional)
- Sort by field: `downloads`, `likes` (default: downloads)

**Tips:**
- Search displays full dataset metadata
- Use tags to filter: `--tags "language:en,task_categories:translation"`

---

### Preview HuggingFace Dataset (aii_hf_preview_datasets.py)

Inspect a specific dataset - shows metadata AND sample rows.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_preview_datasets.py openai/gsm8k --num-rows 5
```

**Parallel execution (multiple datasets):**

IMPORTANT: Use full python path with GNU parallel:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_preview_datasets.py" && \
parallel -j 10 -k --group --will-cite '$PY $S {} --num-rows 3' ::: 'openai/gsm8k' 'imdb' 'squad'
```

**Example output:**
```
============================================================
Dataset: openai/gsm8k
============================================================
Downloads: 425,109 | Likes: 1,102

Description: GSM8K (Grade School Math 8K) is a dataset of 8.5K high quality
linguistically diverse grade school math word problems...

Configs: main, socratic

--- Sample Rows (train) ---
Columns: question, answer

Row 1:
  question: Natalia sold clips to 48 of her friends in April...
  answer: Natalia sold 48/2 = <<48/2=24>>24 clips in May...
```

**Parameters:**

`dataset_id` (required, positional)
- HuggingFace dataset ID
- Examples: `openai/gsm8k`, `glue`, `imdb`

`--config` (optional)
- Dataset configuration/subset name
- Auto-detects first config if not specified

`--split` (optional)
- Split to preview (default: `train`)

`--num-rows` (optional)
- Number of sample rows (default: 5, max: 20)

**Tips:**
- Use after search to verify data structure
- Streaming mode - doesn't download full dataset

---

### Download HuggingFace Dataset (aii_hf_download_datasets.py)

Download datasets and save to files.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_download_datasets.py openai/gsm8k --config main --split train
```

**Parallel execution (multiple datasets):**

IMPORTANT: Use full python path with GNU parallel. Use `eval {}` pattern when datasets need different flags (e.g. `--config`):
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_download_datasets.py" && \
parallel -j 10 -k --group --will-cite 'eval {}' ::: '$PY $S openai/gsm8k --config main --split train' '$PY $S imdb --split train' '$PY $S squad --split train'
```

**Example output:**
```
Downloaded: openai/gsm8k

  train:
    Rows: 7,473
    Preview: temp/datasets/preview_openai_gsm8k_main_train.json
    Mini: temp/datasets/mini_openai_gsm8k_main_train.json
    Full: temp/datasets/full_openai_gsm8k_main_train.json
```

**Parameters:**

`dataset_id` (required, positional)
- HuggingFace dataset ID
- Examples: `openai/gsm8k`, `imdb`

`--config` (optional)
- Dataset configuration/subset name
- Use preview to see available configs

`--split` (optional)
- Specific split to load (e.g., `train`, `test`)
- If not specified, loads all splits

`--output-dir` (optional)
- Output directory (default: `temp/datasets/`)

**Output files (auto-saved):**
1. **Preview**: `preview_{dataset}_{split}.json` - 3 truncated rows - **READ THIS** for quick inspection
2. **Mini**: `mini_{dataset}_{split}.json` - 3 full rows - for development/testing
3. **Full**: `full_{dataset}_{split}.json` - All rows - **DO NOT READ directly** - use as input path for code

**Tips:**
- Only read preview file directly with Read tool
- Mini and full are input paths for processing code

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [5] SKILL-INPUT — aii-json · 2026-07-21 15:44:36 UTC

The agent loaded the **aii-json** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-json
description: JSON validation and formatting toolkit. Validate JSON files against schemas for experiment pipelines, and generate full/mini/preview versions of JSON datasets. Use for validating pipeline outputs, checking schema compliance, or creating size-optimized JSON variants.
---

## Contents

- Validating JSON (schema validation against experiment schemas)
- Formatting JSON (generate full/mini/preview versions)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Validating JSON

Validate JSON files against predefined schemas for experiment-based hypothesis selection, data collection, solution generation, and evaluation.

### Quick Start

1. Read the schema spec you need to adhere to (e.g., `schemas/exp_eval_sol_out.json`)
2. Create your output file following that schema structure
3. Validate:

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /path/to/eval_out.json
```

### Script: aii_json_validate_schema.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /tmp/eval_out.json
```

**Parallel execution (multiple validations):**

IMPORTANT: When validating multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_validate_schema.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --format {1} --file {2}' ::: 'exp_sel_data_out' 'exp_gen_sol_out' 'exp_eval_sol_out' :::+ '/tmp/full_data_out.json' '/tmp/method_out.json' '/tmp/eval_out.json'
```

**Example output (success):**
```
Validating: aii_json_validate_schema.py
Format: exp_eval_sol_out

✓ Validation PASSED
```

**Example output (failure):**
```
Validating: aii_json_validate_schema.py
Format: exp_sel_data_out

✗ Validation FAILED

Errors:
  Path: datasets → 0 → examples → 0
  Error: 'output' is a required property
  Validator: required
```

**Parameters:**

`--format` (required)
- Format type to validate against
- Determines which schema to use

`--file` (required)
- Path to JSON file to validate
- Must be valid JSON
- **Always pass an absolute path.** Relative paths resolve from the
  ability server's CWD (typically ``/ai-inventor/aii_server``), not from
  your agent workspace, so ``data_out/x.json`` will silently look in the
  wrong directory and fail with "Could not load JSON file". The validate
  endpoint also accepts a ``workspace_dir`` arg if you need to keep a
  relative path — pass your workspace path there.

**Tips:**
- Fix errors in your JSON and rerun validation until it passes

### Schema Files

Schemas are stored in `.claude/skills/aii-json/schemas/`:

**Hypothesis Selection & Evaluation:**
- `sel_hypo_out.json` - Hypothesis Selection output (all hypotheses with selected flags)
- `feasibility_eval_all.json` - All hypotheses with feasibility scores
- `feasibility_eval_top.json` - Top 5 most feasible hypotheses
- `novelty_research_one.json` - Single hypothesis novelty research arguments with citations
- `novelty_eval_all.json` - All hypotheses with novelty scores
- `novelty_eval_top.json` - Single best selected hypothesis

**Experiment Pipeline:**
- `exp_sel_data_out.json` - Experiment Data Selection format
- `exp_gen_sol_out.json` - Experiment Solution Generation format
- `exp_eval_sol_out.json` - Experiment Solution Evaluation format

---

## Formatting JSON

Generate three size-optimized versions of a JSON file for efficient development and preview:
- **full**: Identical to original (all data)
- **mini**: First 3 items only (for quick testing)
- **preview**: Mini + all strings truncated to 200 chars (for quick inspection)

### Quick Start

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

### Script: aii_json_format_mini_preview.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

**Parallel execution (multiple files):**

IMPORTANT: When formatting multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_format_mini_preview.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --input {}' ::: 'full_data_out.json' 'method_out.json' 'eval_out.json'
```

**Example output:**
```
Generated 3 versions:
  Full (50 items): /path/to/full_method_out.json
  Mini (3 items): /path/to/mini_method_out.json
  Preview (3 items, truncated): /path/to/preview_method_out.json
```

**Parameters:**

`--input` (required)
- Path to input JSON file
- Must have a top-level array
- Example: `method_out.json`, `full_data_out.json`

`--output-dir` (optional)
- Output directory for generated files
- Default: same directory as input file
- Files are prefixed with `full_`, `mini_`, `preview_`

**Output Files:**

All three files use the same base name with different prefixes:
- `full_{basename}.json` - Complete dataset (identical to original)
- `mini_{basename}.json` - First 3 array items only
- `preview_{basename}.json` - First 3 items with strings truncated to 200 chars

**Tips:**
- Input JSON must have a top-level array structure
- String truncation is recursive (applies to nested objects and arrays)
- Use preview files for quick inspection without reading large datasets
- Use mini files for developing/testing code before running on full dataset

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [6] SKILL-INPUT — aii-web-tools · 2026-07-21 15:44:38 UTC

The agent loaded the **aii-web-tools** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-web-tools
description: "Web research toolkit: web search (Serper/Google), web page fetch as markdown (HTML and PDF), and regex grep over full page/PDF text. Use whenever a task needs to search the web, read a page, mine a paper/PDF, verify citations, or extract exact quotes, numbers, or methodology from a URL."
---

## Web tools

You have three web capabilities: **search**, **fetch**, and **grep** (exact
regex extraction over a full page or PDF).

**Pick where they come from, in this order:**

1. **If you have built-in `WebSearch` / `WebFetch` tools, PREFER those over the
   scripts below.** They may be **deferred tools** (listed by name but with
   schemas not yet loaded) — if so, call `ToolSearch("select:WebSearch,WebFetch")`
   ONCE to load them, then use them normally. Do not skip them just because they
   need that one extra load step; they are the preferred path. Pair them with the
   `aii_web_tools__fetch_grep` script below when you need exact text / numbers /
   methodology that a summary would miss, or when reading a PDF.
2. **Only if you have NO built-in `WebSearch` / `WebFetch`** (e.g. the OpenHands
   backend), use the scripts in this skill (below). They are our own
   implementations — Serper.dev for search, html2text + PyMuPDF for fetch, and
   regex grep over the full document text. They work without any built-in web
   tools.

Workflow either way: **search** (discover) → **fetch** (read for the gist) →
**grep** (pull exact details / read PDFs).

---

## Running the scripts

Run every script with the skill's pre-provisioned interpreter (it already has
`requests`, `html2text`, `pymupdf`, `python-dotenv`). Set `PY` once:

```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

### 1. Search the web (Serper.dev / Google)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation LLM" --max-results 10
```

Returns ranked title / URL / snippet lines. Use it first to scan the
landscape; snippets are for discovery only — fetch a page before judging it.

### 2. Fetch a page as markdown (HTML or PDF)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/abs/2303.11366" --max-chars 10000
```

`--max-chars` caps output (default 10000); `--char-offset N` pages further in.
Handles PDFs transparently via PyMuPDF.

### 3. Grep a page or PDF (exact regex extraction)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/pdf/2303.11366" --pattern "verbal reinforcement" --max-matches 20 --context-chars 200
```

Returns only the matching sections with surrounding context — the right tool
for exact numbers, table values, methodology, or long PDFs where a summary
would lose the detail. `-i` for case-insensitive.

**Parallelize** independent searches/fetches in one turn; only sequence a
fetch after the search that produced its URL.

---

## Notes

- The scripts call our ability server. If a script prints
  `Ability service not available`, the server is down — say so rather than
  silently improvising a different search method.
- Do **not** hand-roll your own `requests`/scraping for search when these
  tools are available: Serper returns clean Google results and the fetch/grep
  scripts already handle HTML, PDFs, and encoding.
````

### [7] SYSTEM-USER prompt · 2026-07-21 15:56:47 UTC

```
YOUR PREVIOUS SESSION WAS INTERRUPTED: A single operation exceeded the 720s message timeout. Each individual operation must complete within 720s. Do NOT mock, skip, or compromise your execution — still do the real work. Try to make operations run faster if possible. If a command genuinely takes longer than 720s, split it into sequential parts that each complete within the time limit.

CONTINUE FOLLOWING THESE INSTRUCTIONS:

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_1_idx1
type: dataset
title: Acquire WSJ or CLEAR readability dataset
summary: >-
  Find, download, and standardize an additional sentence-level readability dataset (WSJ from Liu & Lee 2023 or CLEAR corpus)
  to evaluate the uniformity hypothesis beyond WeeBIT and CEFR-SP. Output as standardized JSON with full/mini/preview splits.
runpod_compute_profile: gpu
ideal_dataset_criteria: >-
  Target: English sentence-level readability dataset with 1,000+ sentences and numerical readability scores. Ideally acquire
  TWO datasets (target_num_datasets=2). Primary targets: (1) WSJ dataset (Liu & Lee 2023) - 1,200 WSJ sentences with 20 annotator
  ratings each, available from authors or HuggingFace; (2) CLEAR corpus - ~5,000 excerpts grades 3-12 with multiple readability
  metrics (MIT license), available from CommonLit or HuggingFace. Must be openly available, machine-readable (CSV/JSON/TSV),
  and have associated readability scores (annotator ratings or computed metrics). Output must conform to exp_sel_data_out.json
  schema with 'input' (sentence text) and 'output' (normalized 0-1 readability score) fields. If only excerpts (not sentences)
  available, use as-is or split into sentences with NLTK.
dataset_search_plan: "IMPORTANT: Acquire at least TWO distinct datasets for robust evaluation. Execute searches in parallel\
  \ where possible.\n\nPHASE 1: Search for and acquire WSJ dataset (Liu & Lee 2023) [PRIORITY 1]\n==========================================================================\n\
  SEARCH STEPS (execute in parallel where possible):\n1. HuggingFace search: Use aii-hf-datasets skill\n   - Command: python\
  \ aii_hf_search_datasets.py --query 'WSJ readability' --limit 10\n   - Command: python aii_hf_search_datasets.py --query\
  \ 'Liu Lee readability' --limit 10\n   - Command: python aii_hf_search_datasets.py --query 'readability annotator ratings'\
  \ --limit 10\n2. Web search for paper and dataset:\n   - Search: 'Liu Lee 2023 Assessing Reliability Automatic Readability\
  \ Assessment Metrics BEA'\n   - Search: 'WSJ 1200 sentences readability dataset'\n   - Check ACL Anthology or arXiv for\
  \ paper appendix with dataset link\n3. Check open data repositories:\n   - Figshare.com search: 'WSJ readability dataset'\n\
  \   - Zenodo.org search: 'readability assessment WSJ'\n   - OSF.io search: 'readability dataset'\n4. If not found openly,\
  \ draft author contact:\n   - Likely authors: Chao Liu, Weiwei Lee (check paper for affiliations)\n   - Email template:\
  \ request dataset access for research, mention reproducibility\n\nACQUISITION (if found):\n- If on HuggingFace: Use aii-hf-datasets\
  \ download script with dataset ID\n- If CSV/JSON URL: Use requests.get() or wget to download\n- If requires request: Send\
  \ email, wait up to 2 days (proceed with other datasets in parallel)\n\nSUCCESS CRITERIA: WSJ dataset downloaded with columns:\
  \ sentence_id, sentence_text, readability_score (mean of 20 annotators)\nFALLBACK: If not acquired within 2 hours, proceed\
  \ to Phase 2 but continue monitoring for author response\n\nPHASE 2: Acquire CLEAR corpus (CommonLit) [PRIORITY 2]\n=============================================================\n\
  SEARCH STEPS:\n1. HuggingFace search:\n   - Command: python aii_hf_search_datasets.py --query 'commonlit' --limit 10\n \
  \  - Command: python aii_hf_search_datasets.py --query 'CLEAR corpus' --limit 10\n2. Web search:\n   - Search: 'CommonLit\
  \ CLEAR corpus download'\n   - Search: 'CLEAR readability corpus MIT license'\n3. Check CommonLit website:\n   - URL: https://www.commonlit.org/en/research/corpus\
  \ (or similar)\n   - Look for 'Download' or 'Request Access' button\n4. Check HuggingFace directly:\n   - Try dataset IDs:\
  \ 'common_lit', 'commonlit', 'clear_corpus'\n\nACQUISITION:\n- If on HuggingFace: Preview first (python aii_hf_preview_datasets.py\
  \ commonlit/dataset_id), then download\n- If on CommonLit website: Register account, download CSV/JSON (may need agreement\
  \ to terms)\n- Expected format: CSV with columns like 'text', 'grade_level', 'fk_grade_level', 'lexile_level'\n\nHANDLING\
  \ EXCERPTS (not sentences):\nOption A (PREFERRED): Use excerpts as-is. Readability formulas work on text excerpts, not just\
  \ sentences.\nOption B (IF SENTENCES REQUIRED): Split excerpts into sentences:\n   from nltk.tokenize import sent_tokenize\n\
  \   nltk.download('punkt')\n   sentences = sent_tokenize(excerpt)\n   Create one row per sentence, assign excerpt's readability\
  \ score to each sentence\n\nSUCCESS CRITERIA: CLEAR corpus downloaded with text excerpts and at least one readability score\
  \ column\nFALLBACK: If unavailable, proceed to Phase 3\n\nPHASE 3: Alternative dataset acquisition [PRIORITY 3 - if Phases\
  \ 1-2 incomplete]\n==================================================================================\nSearch for additional\
  \ readability datasets to reach target_num_datasets=2:\n\n1. WeeBIT additional data:\n   - Check if WeeBIT has additional\
  \ sentences beyond what's already used\n   - Dataset may have multiple sources (Wikipedia, Simple Wikipedia, etc.)\n\n2.\
  \ CEFR-SP additional data:\n   - Check for additional CEFR-SP splits or versions\n   - Dataset may have sentence-level annotations\
  \ not yet extracted\n\n3. HuggingFace broader search:\n   - Command: python aii_hf_search_datasets.py --query 'readability'\
  \ --limit 30\n   - Preview promising datasets (eii_hf_preview_datasets.py <dataset_id>)\n   - Look for: sentence text +\
  \ readability score/grade level\n\n4. OneStopEnglish corpus:\n   - Search GitHub: 'OneStopEnglish corpus'\n   - Check NLP4CALL\
  \ repository (nlp4call.github.io)\n   - Dataset: Texts at 3 levels (elementary, intermediate, advanced)\n   - Need to split\
  \ into sentences and assign scores: elementary=0.3, intermediate=0.6, advanced=0.9\n\n5. Standard Readability Dataset (Vajjala\
  \ & Meurers 2012):\n   - Search: 'Standard Readability Dataset Vajjala Meurers'\n   - Check ACL Anthology or authors' websites\n\
  \n6. Newsela corpus (requires registration):\n   - Website: newsela.com\n   - Has articles at 5 grade levels\n   - Need\
  \ Newsela API access or special agreement (check if available to researchers)\n\nSUCCESS CRITERIA: At least 2 datasets total\
  \ acquired (including WSJ and/or CLEAR)\n\nPHASE 4: Standardize datasets to exp_sel_data_out.json schema\n==============================================================\n\
  Execute separately for each acquired dataset.\n\nSTEP 1: Load and inspect raw data\n   import pandas as pd\n   df = pd.read_csv('dataset.csv')\
  \  # or pd.read_json(), depending on format\n   print(df.columns)\n   print(df.head())\n   print(df.info())\n\nSTEP 2: Map\
  \ to schema\n   Schema required fields:\n   - 'input': string (sentence or excerpt text)\n   - 'output': float (normalized\
  \ readability score, 0.0=easiest, 1.0=hardest)\n   Optional fields:\n   - 'metadata_fold': string (default='test' for new\
  \ evaluation datasets)\n   - 'sentence_id': string or int (original ID if available)\n\n   Mapping examples:\n   - WSJ:\
  \ input ← 'sentence_text', output ← 'mean_readability_score'\n   - CLEAR: input ← 'text', output ← normalize('grade_level'\
  \ or 'fk_grade_level')\n\nSTEP 3: Normalize readability scores to 0-1\n   Formula: normalized = (raw_score - min_score)\
  \ / (max_score - min_score)\n   \n   SPECIAL CASES:\n   - If lower raw scores = easier (e.g., Flesch-Kincaid grade level):\
  \ invert so 0.0=easiest\n     normalized = 1.0 - ((raw_score - min_score) / (max_score - min_score))\n   - If all scores\
  \ identical (can't normalize): use raw scores, document in README\n   - If multiple readability metrics: create SEPARATE\
  \ output files for each metric\n\nSTEP 4: Create output files\n   a. full_dataset.json: ALL rows, full text, properly formatted\n\
  \      - Use df.to_json('full_dataset.json', orient='records', lines=True)\n      - Validate with aii-json skill\n\n   b.\
  \ mini_dataset.json: 50 randomly sampled rows\n      - df_sample = df.sample(n=50, random_state=42)\n      - Save to mini_dataset.json\n\
  \n   c. preview_dataset.json: 3 rows, text truncated to 100 chars\n      - df_preview = df.head(3).copy()\n      - df_preview['input']\
  \ = df_preview['input'].str[:100] + '...'\n      - Save to preview_dataset.json\n\nSTEP 5: Validate schema\n   - Use aii-json\
  \ skill: validate full_dataset.json against exp_sel_data_out.json schema\n   - Fix any validation errors before proceeding\n\
  \nPHASE 5: Document dataset statistics\n====================================\nExecute for each standardized dataset.\n\n\
  1. Compute basic statistics:\n   - n_sentences: len(df)\n   - mean_score, std_score, min_score, max_score\n   - Score histogram:\
  \ pd.cut(df['output'], bins=10).value_counts()\n   - Sentence length distribution: df['input'].str.split().str.len().describe()\n\
  \n2. Create comparison table (vs. WeeBIT and CEFR-SP):\n   | Dataset | N Sentences | Mean Score | Score Range | Avg Sentence\
  \ Length |\n   |----------|-------------|------------|-------------|---------------------|\n   | WeeBIT   | [from prior\
  \ experiments] | [value] | [range] | [value] |\n   | CEFR-SP  | [from prior experiments] | [value] | [range] | [value] |\n\
  \   | NEW DS   | [computed] | [computed] | [computed] | [computed] |\n\n3. Check data quality:\n   - Duplicates: df.duplicated('input').sum()\n\
  \   - Outliers: rows where score > mean + 3*std or score < mean - 3*std\n   - Very short sentences: df[df['input'].str.split().str.len()\
  \ < 3]\n\n4. Save dataset_info.json:\n   {\n     \"dataset_name\": \"WSJ_Liu_Lee_2023\",\n     \"source_url\": \"https://huggingface.co/datasets/...\"\
  ,\n     \"license\": \"MIT\",\n     \"n_sentences\": 1200,\n     \"score_distribution\": {\"mean\": 0.5, \"std\": 0.2, ...},\n\
  \     \"preprocessing\": \"None / Sentence splitting with NLTK\",\n     \"schema_version\": \"exp_sel_data_out.json v1.0\"\
  \n   }\n\n5. Create README.md with:\n   - Dataset description and source\n   - Loading instructions (pandas code)\n   -\
  \ Comparison to WeeBIT/CEFR-SP\n   - Known issues or limitations\n   - Citation information\n\nTIME ALLOCATION:\n-----------------\n\
  - Phase 1 (WSJ search): 2 hours (including author contact)\n- Phase 2 (CLEAR acquisition): 1.5 hours\n- Phase 3 (Alternatives):\
  \ 1.5 hours (if 1-2 fail or to acquire 2nd dataset)\n- Phase 4 (Standardization): 2 hours (for 2 datasets)\n- Phase 5 (Documentation):\
  \ 1 hour\n- BUFFER: 1 hour for unexpected issues\nTOTAL: 6 hours (with 1 hour buffer within the 6h limit)\n\nTECHNICAL IMPLEMENTATION\
  \ NOTES FOR EXECUTOR:\n=============================================\n1. Using aii-hf-datasets skill:\n   - Search: python\
  \ aii_hf_search_datasets.py --query 'X' --limit 10\n   - Preview: python aii_hf_preview_datasets.py <dataset_id> --num-rows\
  \ 5\n   - Download: python aii_hf_download_datasets.py <dataset_id> --split train\n\n2. Direct download (if not on HuggingFace):\n\
  \   import requests\n   url = 'https://example.com/dataset.csv'\n   response = requests.get(url, stream=True)\n   with open('dataset.csv',\
  \ 'wb') as f:\n       for chunk in response.iter_content(chunk_size=8192):\n           f.write(chunk)\n\n3. Schema validation:\n\
  \   - Use aii-json skill to validate output\n   - If aii-json not available: manually check JSON structure matches schema\n\
  \n4. Handling missing values:\n   - Drop rows where 'input' is NaN or empty string\n   - Drop rows where 'output' is NaN\
  \ (unless dataset is for unsupervised evaluation)\n\n5. Output file organization:\n   Save all output files in: /workspace/datasets/<dataset_name>/\n\
  \   Files: full_dataset.json, mini_dataset.json, preview_dataset.json, dataset_info.json, README.md\n\nERROR HANDLING AND\
  \ FALLBACK STRATEGIES:\n========================================\n1. Dataset not found:\n   - Log search query and result\n\
  \   - Try next candidate in the priority list\n   - Continue until target_num_datasets (2) acquired\n\n2. Download fails\
  \ (connection error, 404):\n   - Retry 3 times with 5-second delays\n   - Try mirror URL if available\n   - Skip to next\
  \ candidate\n\n3. Schema validation fails:\n   - Print exact validation errors\n   - Check field names, data types, required\
  \ fields\n   - Fix and re-validate\n\n4. Score normalization fails (constant scores or NaN):\n   - Use raw scores without\
  \ normalization\n   - Document in README.md\n   - Add warning that scores are not normalized\n\n5. CLEAR excerpts too long\
  \ (>500 words):\n   - Option A: Truncate to 200 words (preserve readability)\n   - Option B: Split into sentences (more\
  \ work but better for sentence-level evaluation)\n   - Decision: Use Option A (truncate) for speed, unless explicitly instructed\
  \ otherwise\n\n6. WeeBIT/CEFR-SP already used in experiments:\n   - DO NOT include WeeBIT or CEFR-SP as \"new\" datasets\n\
  \   - These are already available; find genuinely new datasets\n   - Check if WeeBIT/CEFR-SP have additional splits not\
  \ yet used (acceptable to use)\n\nDELIVERABLES CHECKLIST:\n========================\nFor each acquired dataset (target:\
  \ 2 datasets), ensure:\n[ ] full_<dataset_name>.json - Complete standardized dataset\n[ ] mini_<dataset_name>.json - 50-row\
  \ subset for development\n[ ] preview_<dataset_name>.json - 3-row preview with truncated text\n[ ] dataset_info.json - Metadata\
  \ and statistics\n[ ] README.md - Documentation and usage examples\n[ ] Comparison table (new dataset vs. WeeBIT vs. CEFR-SP)\n\
  \nEXECUTION ORDER:\n=================\n1. Start Phase 1 (WSJ search) and Phase 2 (CLEAR search) IN PARALLEL\n2. If Phase\
  \ 1 succeeds: download and standardize WSJ dataset\n3. If Phase 2 succeeds: download and standardize CLEAR dataset\n4. If\
  \ only 1 dataset acquired: start Phase 3 to acquire 2nd dataset\n5. Standardize all acquired datasets (Phase 4)\n6. Document\
  \ statistics (Phase 5)\n7. Verify all deliverables present"
target_num_datasets: 2
</artifact_plan>



<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Web search (Serper), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-image-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
</skills>
</available_resources>

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for dataset selection, evaluation metrics, agent orchestration patterns.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing.
TODO 2. Read skill files for your data sources (see <available_data_sources>) and domain handbook if applicable (see <available_domain_handbooks>). Based on plan and context, decide which source(s) to use. Include everything specified in the artifact plan, but you may also collect additional relevant data beyond what's listed. Run 16 diverse searches across chosen source(s) — BROAD, GENERAL terms, not very specific. Parallelize where supported.
TODO 3. Identify the 8 most promising datasets. IMPORTANT: Only consider datasets under 300MB. Preview/inspect sample rows for each candidate. Parallelize previews.
TODO 4. Research each candidate BEFORE choosing which to download. For each, search the web (aii-web-tools skill): dataset name, papers citing it, original source/task, popularity. Red flags: no search results, no papers, anonymized features (F1, F2...), <100 downloads, no documentation. Green flags: papers using it, clear documentation, meaningful features, established benchmark. Also consider: will features/structure allow meaningful evaluation of the planned method?
TODO 5. Decide which to KEEP vs DISCARD. Look for: clear structure, relevant fields, quality examples matching requirements, confirmed provenance. Determine which 4 datasets have the most suitable data. Download and save to `temp/datasets/`. Parallelize downloads.
</todos>

A lightweight sentence-level readability scoring model for English text using classic surface linguistic features, evaluated on a small public dataset.
```

### [8] SYSTEM-USER prompt · 2026-07-21 16:04:10 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_1_idx1
type: dataset
title: Acquire WSJ or CLEAR readability dataset
summary: >-
  Find, download, and standardize an additional sentence-level readability dataset (WSJ from Liu & Lee 2023 or CLEAR corpus)
  to evaluate the uniformity hypothesis beyond WeeBIT and CEFR-SP. Output as standardized JSON with full/mini/preview splits.
runpod_compute_profile: gpu
ideal_dataset_criteria: >-
  Target: English sentence-level readability dataset with 1,000+ sentences and numerical readability scores. Ideally acquire
  TWO datasets (target_num_datasets=2). Primary targets: (1) WSJ dataset (Liu & Lee 2023) - 1,200 WSJ sentences with 20 annotator
  ratings each, available from authors or HuggingFace; (2) CLEAR corpus - ~5,000 excerpts grades 3-12 with multiple readability
  metrics (MIT license), available from CommonLit or HuggingFace. Must be openly available, machine-readable (CSV/JSON/TSV),
  and have associated readability scores (annotator ratings or computed metrics). Output must conform to exp_sel_data_out.json
  schema with 'input' (sentence text) and 'output' (normalized 0-1 readability score) fields. If only excerpts (not sentences)
  available, use as-is or split into sentences with NLTK.
dataset_search_plan: "IMPORTANT: Acquire at least TWO distinct datasets for robust evaluation. Execute searches in parallel\
  \ where possible.\n\nPHASE 1: Search for and acquire WSJ dataset (Liu & Lee 2023) [PRIORITY 1]\n==========================================================================\n\
  SEARCH STEPS (execute in parallel where possible):\n1. HuggingFace search: Use aii-hf-datasets skill\n   - Command: python\
  \ aii_hf_search_datasets.py --query 'WSJ readability' --limit 10\n   - Command: python aii_hf_search_datasets.py --query\
  \ 'Liu Lee readability' --limit 10\n   - Command: python aii_hf_search_datasets.py --query 'readability annotator ratings'\
  \ --limit 10\n2. Web search for paper and dataset:\n   - Search: 'Liu Lee 2023 Assessing Reliability Automatic Readability\
  \ Assessment Metrics BEA'\n   - Search: 'WSJ 1200 sentences readability dataset'\n   - Check ACL Anthology or arXiv for\
  \ paper appendix with dataset link\n3. Check open data repositories:\n   - Figshare.com search: 'WSJ readability dataset'\n\
  \   - Zenodo.org search: 'readability assessment WSJ'\n   - OSF.io search: 'readability dataset'\n4. If not found openly,\
  \ draft author contact:\n   - Likely authors: Chao Liu, Weiwei Lee (check paper for affiliations)\n   - Email template:\
  \ request dataset access for research, mention reproducibility\n\nACQUISITION (if found):\n- If on HuggingFace: Use aii-hf-datasets\
  \ download script with dataset ID\n- If CSV/JSON URL: Use requests.get() or wget to download\n- If requires request: Send\
  \ email, wait up to 2 days (proceed with other datasets in parallel)\n\nSUCCESS CRITERIA: WSJ dataset downloaded with columns:\
  \ sentence_id, sentence_text, readability_score (mean of 20 annotators)\nFALLBACK: If not acquired within 2 hours, proceed\
  \ to Phase 2 but continue monitoring for author response\n\nPHASE 2: Acquire CLEAR corpus (CommonLit) [PRIORITY 2]\n=============================================================\n\
  SEARCH STEPS:\n1. HuggingFace search:\n   - Command: python aii_hf_search_datasets.py --query 'commonlit' --limit 10\n \
  \  - Command: python aii_hf_search_datasets.py --query 'CLEAR corpus' --limit 10\n2. Web search:\n   - Search: 'CommonLit\
  \ CLEAR corpus download'\n   - Search: 'CLEAR readability corpus MIT license'\n3. Check CommonLit website:\n   - URL: https://www.commonlit.org/en/research/corpus\
  \ (or similar)\n   - Look for 'Download' or 'Request Access' button\n4. Check HuggingFace directly:\n   - Try dataset IDs:\
  \ 'common_lit', 'commonlit', 'clear_corpus'\n\nACQUISITION:\n- If on HuggingFace: Preview first (python aii_hf_preview_datasets.py\
  \ commonlit/dataset_id), then download\n- If on CommonLit website: Register account, download CSV/JSON (may need agreement\
  \ to terms)\n- Expected format: CSV with columns like 'text', 'grade_level', 'fk_grade_level', 'lexile_level'\n\nHANDLING\
  \ EXCERPTS (not sentences):\nOption A (PREFERRED): Use excerpts as-is. Readability formulas work on text excerpts, not just\
  \ sentences.\nOption B (IF SENTENCES REQUIRED): Split excerpts into sentences:\n   from nltk.tokenize import sent_tokenize\n\
  \   nltk.download('punkt')\n   sentences = sent_tokenize(excerpt)\n   Create one row per sentence, assign excerpt's readability\
  \ score to each sentence\n\nSUCCESS CRITERIA: CLEAR corpus downloaded with text excerpts and at least one readability score\
  \ column\nFALLBACK: If unavailable, proceed to Phase 3\n\nPHASE 3: Alternative dataset acquisition [PRIORITY 3 - if Phases\
  \ 1-2 incomplete]\n==================================================================================\nSearch for additional\
  \ readability datasets to reach target_num_datasets=2:\n\n1. WeeBIT additional data:\n   - Check if WeeBIT has additional\
  \ sentences beyond what's already used\n   - Dataset may have multiple sources (Wikipedia, Simple Wikipedia, etc.)\n\n2.\
  \ CEFR-SP additional data:\n   - Check for additional CEFR-SP splits or versions\n   - Dataset may have sentence-level annotations\
  \ not yet extracted\n\n3. HuggingFace broader search:\n   - Command: python aii_hf_search_datasets.py --query 'readability'\
  \ --limit 30\n   - Preview promising datasets (eii_hf_preview_datasets.py <dataset_id>)\n   - Look for: sentence text +\
  \ readability score/grade level\n\n4. OneStopEnglish corpus:\n   - Search GitHub: 'OneStopEnglish corpus'\n   - Check NLP4CALL\
  \ repository (nlp4call.github.io)\n   - Dataset: Texts at 3 levels (elementary, intermediate, advanced)\n   - Need to split\
  \ into sentences and assign scores: elementary=0.3, intermediate=0.6, advanced=0.9\n\n5. Standard Readability Dataset (Vajjala\
  \ & Meurers 2012):\n   - Search: 'Standard Readability Dataset Vajjala Meurers'\n   - Check ACL Anthology or authors' websites\n\
  \n6. Newsela corpus (requires registration):\n   - Website: newsela.com\n   - Has articles at 5 grade levels\n   - Need\
  \ Newsela API access or special agreement (check if available to researchers)\n\nSUCCESS CRITERIA: At least 2 datasets total\
  \ acquired (including WSJ and/or CLEAR)\n\nPHASE 4: Standardize datasets to exp_sel_data_out.json schema\n==============================================================\n\
  Execute separately for each acquired dataset.\n\nSTEP 1: Load and inspect raw data\n   import pandas as pd\n   df = pd.read_csv('dataset.csv')\
  \  # or pd.read_json(), depending on format\n   print(df.columns)\n   print(df.head())\n   print(df.info())\n\nSTEP 2: Map\
  \ to schema\n   Schema required fields:\n   - 'input': string (sentence or excerpt text)\n   - 'output': float (normalized\
  \ readability score, 0.0=easiest, 1.0=hardest)\n   Optional fields:\n   - 'metadata_fold': string (default='test' for new\
  \ evaluation datasets)\n   - 'sentence_id': string or int (original ID if available)\n\n   Mapping examples:\n   - WSJ:\
  \ input ← 'sentence_text', output ← 'mean_readability_score'\n   - CLEAR: input ← 'text', output ← normalize('grade_level'\
  \ or 'fk_grade_level')\n\nSTEP 3: Normalize readability scores to 0-1\n   Formula: normalized = (raw_score - min_score)\
  \ / (max_score - min_score)\n   \n   SPECIAL CASES:\n   - If lower raw scores = easier (e.g., Flesch-Kincaid grade level):\
  \ invert so 0.0=easiest\n     normalized = 1.0 - ((raw_score - min_score) / (max_score - min_score))\n   - If all scores\
  \ identical (can't normalize): use raw scores, document in README\n   - If multiple readability metrics: create SEPARATE\
  \ output files for each metric\n\nSTEP 4: Create output files\n   a. full_dataset.json: ALL rows, full text, properly formatted\n\
  \      - Use df.to_json('full_dataset.json', orient='records', lines=True)\n      - Validate with aii-json skill\n\n   b.\
  \ mini_dataset.json: 50 randomly sampled rows\n      - df_sample = df.sample(n=50, random_state=42)\n      - Save to mini_dataset.json\n\
  \n   c. preview_dataset.json: 3 rows, text truncated to 100 chars\n      - df_preview = df.head(3).copy()\n      - df_preview['input']\
  \ = df_preview['input'].str[:100] + '...'\n      - Save to preview_dataset.json\n\nSTEP 5: Validate schema\n   - Use aii-json\
  \ skill: validate full_dataset.json against exp_sel_data_out.json schema\n   - Fix any validation errors before proceeding\n\
  \nPHASE 5: Document dataset statistics\n====================================\nExecute for each standardized dataset.\n\n\
  1. Compute basic statistics:\n   - n_sentences: len(df)\n   - mean_score, std_score, min_score, max_score\n   - Score histogram:\
  \ pd.cut(df['output'], bins=10).value_counts()\n   - Sentence length distribution: df['input'].str.split().str.len().describe()\n\
  \n2. Create comparison table (vs. WeeBIT and CEFR-SP):\n   | Dataset | N Sentences | Mean Score | Score Range | Avg Sentence\
  \ Length |\n   |----------|-------------|------------|-------------|---------------------|\n   | WeeBIT   | [from prior\
  \ experiments] | [value] | [range] | [value] |\n   | CEFR-SP  | [from prior experiments] | [value] | [range] | [value] |\n\
  \   | NEW DS   | [computed] | [computed] | [computed] | [computed] |\n\n3. Check data quality:\n   - Duplicates: df.duplicated('input').sum()\n\
  \   - Outliers: rows where score > mean + 3*std or score < mean - 3*std\n   - Very short sentences: df[df['input'].str.split().str.len()\
  \ < 3]\n\n4. Save dataset_info.json:\n   {\n     \"dataset_name\": \"WSJ_Liu_Lee_2023\",\n     \"source_url\": \"https://huggingface.co/datasets/...\"\
  ,\n     \"license\": \"MIT\",\n     \"n_sentences\": 1200,\n     \"score_distribution\": {\"mean\": 0.5, \"std\": 0.2, ...},\n\
  \     \"preprocessing\": \"None / Sentence splitting with NLTK\",\n     \"schema_version\": \"exp_sel_data_out.json v1.0\"\
  \n   }\n\n5. Create README.md with:\n   - Dataset description and source\n   - Loading instructions (pandas code)\n   -\
  \ Comparison to WeeBIT/CEFR-SP\n   - Known issues or limitations\n   - Citation information\n\nTIME ALLOCATION:\n-----------------\n\
  - Phase 1 (WSJ search): 2 hours (including author contact)\n- Phase 2 (CLEAR acquisition): 1.5 hours\n- Phase 3 (Alternatives):\
  \ 1.5 hours (if 1-2 fail or to acquire 2nd dataset)\n- Phase 4 (Standardization): 2 hours (for 2 datasets)\n- Phase 5 (Documentation):\
  \ 1 hour\n- BUFFER: 1 hour for unexpected issues\nTOTAL: 6 hours (with 1 hour buffer within the 6h limit)\n\nTECHNICAL IMPLEMENTATION\
  \ NOTES FOR EXECUTOR:\n=============================================\n1. Using aii-hf-datasets skill:\n   - Search: python\
  \ aii_hf_search_datasets.py --query 'X' --limit 10\n   - Preview: python aii_hf_preview_datasets.py <dataset_id> --num-rows\
  \ 5\n   - Download: python aii_hf_download_datasets.py <dataset_id> --split train\n\n2. Direct download (if not on HuggingFace):\n\
  \   import requests\n   url = 'https://example.com/dataset.csv'\n   response = requests.get(url, stream=True)\n   with open('dataset.csv',\
  \ 'wb') as f:\n       for chunk in response.iter_content(chunk_size=8192):\n           f.write(chunk)\n\n3. Schema validation:\n\
  \   - Use aii-json skill to validate output\n   - If aii-json not available: manually check JSON structure matches schema\n\
  \n4. Handling missing values:\n   - Drop rows where 'input' is NaN or empty string\n   - Drop rows where 'output' is NaN\
  \ (unless dataset is for unsupervised evaluation)\n\n5. Output file organization:\n   Save all output files in: /workspace/datasets/<dataset_name>/\n\
  \   Files: full_dataset.json, mini_dataset.json, preview_dataset.json, dataset_info.json, README.md\n\nERROR HANDLING AND\
  \ FALLBACK STRATEGIES:\n========================================\n1. Dataset not found:\n   - Log search query and result\n\
  \   - Try next candidate in the priority list\n   - Continue until target_num_datasets (2) acquired\n\n2. Download fails\
  \ (connection error, 404):\n   - Retry 3 times with 5-second delays\n   - Try mirror URL if available\n   - Skip to next\
  \ candidate\n\n3. Schema validation fails:\n   - Print exact validation errors\n   - Check field names, data types, required\
  \ fields\n   - Fix and re-validate\n\n4. Score normalization fails (constant scores or NaN):\n   - Use raw scores without\
  \ normalization\n   - Document in README.md\n   - Add warning that scores are not normalized\n\n5. CLEAR excerpts too long\
  \ (>500 words):\n   - Option A: Truncate to 200 words (preserve readability)\n   - Option B: Split into sentences (more\
  \ work but better for sentence-level evaluation)\n   - Decision: Use Option A (truncate) for speed, unless explicitly instructed\
  \ otherwise\n\n6. WeeBIT/CEFR-SP already used in experiments:\n   - DO NOT include WeeBIT or CEFR-SP as \"new\" datasets\n\
  \   - These are already available; find genuinely new datasets\n   - Check if WeeBIT/CEFR-SP have additional splits not\
  \ yet used (acceptable to use)\n\nDELIVERABLES CHECKLIST:\n========================\nFor each acquired dataset (target:\
  \ 2 datasets), ensure:\n[ ] full_<dataset_name>.json - Complete standardized dataset\n[ ] mini_<dataset_name>.json - 50-row\
  \ subset for development\n[ ] preview_<dataset_name>.json - 3-row preview with truncated text\n[ ] dataset_info.json - Metadata\
  \ and statistics\n[ ] README.md - Documentation and usage examples\n[ ] Comparison table (new dataset vs. WeeBIT vs. CEFR-SP)\n\
  \nEXECUTION ORDER:\n=================\n1. Start Phase 1 (WSJ search) and Phase 2 (CLEAR search) IN PARALLEL\n2. If Phase\
  \ 1 succeeds: download and standardize WSJ dataset\n3. If Phase 2 succeeds: download and standardize CLEAR dataset\n4. If\
  \ only 1 dataset acquired: start Phase 3 to acquire 2nd dataset\n5. Standardize all acquired datasets (Phase 4)\n6. Document\
  \ statistics (Phase 5)\n7. Verify all deliverables present"
target_num_datasets: 2
</artifact_plan>



<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Web search (Serper), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-image-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
</skills>
</available_resources>

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for dataset selection, evaluation metrics, agent orchestration patterns.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. For the top 4 datasets, create data.py (uv inline script) that: loads from temp/datasets/, standardizes to exp_sel_data_out.json schema (aii-json skill), extracts all examples per dataset, handles domain requirements, saves to full_data_out.json.

Each data ROW must be a separate example — do NOT create one example per dataset or per fold. Each data point (row, sample, instance) = one example. 500 rows → 500 examples. The output is GROUPED BY DATASET:
```json
{
  "datasets": [
    {
      "dataset": "iris",
      "examples": [
        {"input": "...", "output": "...", "metadata_fold": 2, "metadata_feature_names": [...]},
        ...
      ]
    },
    {
      "dataset": "adult_census",
      "examples": [...]
    }
  ]
}
```
Per-example required fields:
- `input`: input features/text (tabular: JSON string of feature values)
- `output`: target/label (as string)
Per-example optional metadata via `metadata_<name>` fields (flat, not nested object):
- `metadata_fold`: fold assignment (int), `metadata_feature_names`: feature name list, `metadata_task_type`: "classification"/"regression", `metadata_n_classes`: number of classes, `metadata_row_index`: original row index, etc.
Do NOT use `split`, `dataset`, or `context` as per-example fields. Dataset name goes at the group level, metadata goes in `metadata_*` fields.
TODO 2. Run 'uv run data.py' and fix errors. Validate full_data_out.json against exp_sel_data_out.json schema (aii-json skill) — fix errors. Generate preview, mini, full versions with aii-json skill's format script.
TODO 3. Read preview to inspect examples. Choose THE BEST 2 DATASETS based on domain requirements and artifact objective. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
````

### [9] SYSTEM-USER prompt · 2026-07-21 16:12:36 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_dataset_1_idx1
type: dataset
title: Acquire WSJ or CLEAR readability dataset
summary: >-
  Find, download, and standardize an additional sentence-level readability dataset (WSJ from Liu & Lee 2023 or CLEAR corpus)
  to evaluate the uniformity hypothesis beyond WeeBIT and CEFR-SP. Output as standardized JSON with full/mini/preview splits.
runpod_compute_profile: gpu
ideal_dataset_criteria: >-
  Target: English sentence-level readability dataset with 1,000+ sentences and numerical readability scores. Ideally acquire
  TWO datasets (target_num_datasets=2). Primary targets: (1) WSJ dataset (Liu & Lee 2023) - 1,200 WSJ sentences with 20 annotator
  ratings each, available from authors or HuggingFace; (2) CLEAR corpus - ~5,000 excerpts grades 3-12 with multiple readability
  metrics (MIT license), available from CommonLit or HuggingFace. Must be openly available, machine-readable (CSV/JSON/TSV),
  and have associated readability scores (annotator ratings or computed metrics). Output must conform to exp_sel_data_out.json
  schema with 'input' (sentence text) and 'output' (normalized 0-1 readability score) fields. If only excerpts (not sentences)
  available, use as-is or split into sentences with NLTK.
dataset_search_plan: "IMPORTANT: Acquire at least TWO distinct datasets for robust evaluation. Execute searches in parallel\
  \ where possible.\n\nPHASE 1: Search for and acquire WSJ dataset (Liu & Lee 2023) [PRIORITY 1]\n==========================================================================\n\
  SEARCH STEPS (execute in parallel where possible):\n1. HuggingFace search: Use aii-hf-datasets skill\n   - Command: python\
  \ aii_hf_search_datasets.py --query 'WSJ readability' --limit 10\n   - Command: python aii_hf_search_datasets.py --query\
  \ 'Liu Lee readability' --limit 10\n   - Command: python aii_hf_search_datasets.py --query 'readability annotator ratings'\
  \ --limit 10\n2. Web search for paper and dataset:\n   - Search: 'Liu Lee 2023 Assessing Reliability Automatic Readability\
  \ Assessment Metrics BEA'\n   - Search: 'WSJ 1200 sentences readability dataset'\n   - Check ACL Anthology or arXiv for\
  \ paper appendix with dataset link\n3. Check open data repositories:\n   - Figshare.com search: 'WSJ readability dataset'\n\
  \   - Zenodo.org search: 'readability assessment WSJ'\n   - OSF.io search: 'readability dataset'\n4. If not found openly,\
  \ draft author contact:\n   - Likely authors: Chao Liu, Weiwei Lee (check paper for affiliations)\n   - Email template:\
  \ request dataset access for research, mention reproducibility\n\nACQUISITION (if found):\n- If on HuggingFace: Use aii-hf-datasets\
  \ download script with dataset ID\n- If CSV/JSON URL: Use requests.get() or wget to download\n- If requires request: Send\
  \ email, wait up to 2 days (proceed with other datasets in parallel)\n\nSUCCESS CRITERIA: WSJ dataset downloaded with columns:\
  \ sentence_id, sentence_text, readability_score (mean of 20 annotators)\nFALLBACK: If not acquired within 2 hours, proceed\
  \ to Phase 2 but continue monitoring for author response\n\nPHASE 2: Acquire CLEAR corpus (CommonLit) [PRIORITY 2]\n=============================================================\n\
  SEARCH STEPS:\n1. HuggingFace search:\n   - Command: python aii_hf_search_datasets.py --query 'commonlit' --limit 10\n \
  \  - Command: python aii_hf_search_datasets.py --query 'CLEAR corpus' --limit 10\n2. Web search:\n   - Search: 'CommonLit\
  \ CLEAR corpus download'\n   - Search: 'CLEAR readability corpus MIT license'\n3. Check CommonLit website:\n   - URL: https://www.commonlit.org/en/research/corpus\
  \ (or similar)\n   - Look for 'Download' or 'Request Access' button\n4. Check HuggingFace directly:\n   - Try dataset IDs:\
  \ 'common_lit', 'commonlit', 'clear_corpus'\n\nACQUISITION:\n- If on HuggingFace: Preview first (python aii_hf_preview_datasets.py\
  \ commonlit/dataset_id), then download\n- If on CommonLit website: Register account, download CSV/JSON (may need agreement\
  \ to terms)\n- Expected format: CSV with columns like 'text', 'grade_level', 'fk_grade_level', 'lexile_level'\n\nHANDLING\
  \ EXCERPTS (not sentences):\nOption A (PREFERRED): Use excerpts as-is. Readability formulas work on text excerpts, not just\
  \ sentences.\nOption B (IF SENTENCES REQUIRED): Split excerpts into sentences:\n   from nltk.tokenize import sent_tokenize\n\
  \   nltk.download('punkt')\n   sentences = sent_tokenize(excerpt)\n   Create one row per sentence, assign excerpt's readability\
  \ score to each sentence\n\nSUCCESS CRITERIA: CLEAR corpus downloaded with text excerpts and at least one readability score\
  \ column\nFALLBACK: If unavailable, proceed to Phase 3\n\nPHASE 3: Alternative dataset acquisition [PRIORITY 3 - if Phases\
  \ 1-2 incomplete]\n==================================================================================\nSearch for additional\
  \ readability datasets to reach target_num_datasets=2:\n\n1. WeeBIT additional data:\n   - Check if WeeBIT has additional\
  \ sentences beyond what's already used\n   - Dataset may have multiple sources (Wikipedia, Simple Wikipedia, etc.)\n\n2.\
  \ CEFR-SP additional data:\n   - Check for additional CEFR-SP splits or versions\n   - Dataset may have sentence-level annotations\
  \ not yet extracted\n\n3. HuggingFace broader search:\n   - Command: python aii_hf_search_datasets.py --query 'readability'\
  \ --limit 30\n   - Preview promising datasets (eii_hf_preview_datasets.py <dataset_id>)\n   - Look for: sentence text +\
  \ readability score/grade level\n\n4. OneStopEnglish corpus:\n   - Search GitHub: 'OneStopEnglish corpus'\n   - Check NLP4CALL\
  \ repository (nlp4call.github.io)\n   - Dataset: Texts at 3 levels (elementary, intermediate, advanced)\n   - Need to split\
  \ into sentences and assign scores: elementary=0.3, intermediate=0.6, advanced=0.9\n\n5. Standard Readability Dataset (Vajjala\
  \ & Meurers 2012):\n   - Search: 'Standard Readability Dataset Vajjala Meurers'\n   - Check ACL Anthology or authors' websites\n\
  \n6. Newsela corpus (requires registration):\n   - Website: newsela.com\n   - Has articles at 5 grade levels\n   - Need\
  \ Newsela API access or special agreement (check if available to researchers)\n\nSUCCESS CRITERIA: At least 2 datasets total\
  \ acquired (including WSJ and/or CLEAR)\n\nPHASE 4: Standardize datasets to exp_sel_data_out.json schema\n==============================================================\n\
  Execute separately for each acquired dataset.\n\nSTEP 1: Load and inspect raw data\n   import pandas as pd\n   df = pd.read_csv('dataset.csv')\
  \  # or pd.read_json(), depending on format\n   print(df.columns)\n   print(df.head())\n   print(df.info())\n\nSTEP 2: Map\
  \ to schema\n   Schema required fields:\n   - 'input': string (sentence or excerpt text)\n   - 'output': float (normalized\
  \ readability score, 0.0=easiest, 1.0=hardest)\n   Optional fields:\n   - 'metadata_fold': string (default='test' for new\
  \ evaluation datasets)\n   - 'sentence_id': string or int (original ID if available)\n\n   Mapping examples:\n   - WSJ:\
  \ input ← 'sentence_text', output ← 'mean_readability_score'\n   - CLEAR: input ← 'text', output ← normalize('grade_level'\
  \ or 'fk_grade_level')\n\nSTEP 3: Normalize readability scores to 0-1\n   Formula: normalized = (raw_score - min_score)\
  \ / (max_score - min_score)\n   \n   SPECIAL CASES:\n   - If lower raw scores = easier (e.g., Flesch-Kincaid grade level):\
  \ invert so 0.0=easiest\n     normalized = 1.0 - ((raw_score - min_score) / (max_score - min_score))\n   - If all scores\
  \ identical (can't normalize): use raw scores, document in README\n   - If multiple readability metrics: create SEPARATE\
  \ output files for each metric\n\nSTEP 4: Create output files\n   a. full_dataset.json: ALL rows, full text, properly formatted\n\
  \      - Use df.to_json('full_dataset.json', orient='records', lines=True)\n      - Validate with aii-json skill\n\n   b.\
  \ mini_dataset.json: 50 randomly sampled rows\n      - df_sample = df.sample(n=50, random_state=42)\n      - Save to mini_dataset.json\n\
  \n   c. preview_dataset.json: 3 rows, text truncated to 100 chars\n      - df_preview = df.head(3).copy()\n      - df_preview['input']\
  \ = df_preview['input'].str[:100] + '...'\n      - Save to preview_dataset.json\n\nSTEP 5: Validate schema\n   - Use aii-json\
  \ skill: validate full_dataset.json against exp_sel_data_out.json schema\n   - Fix any validation errors before proceeding\n\
  \nPHASE 5: Document dataset statistics\n====================================\nExecute for each standardized dataset.\n\n\
  1. Compute basic statistics:\n   - n_sentences: len(df)\n   - mean_score, std_score, min_score, max_score\n   - Score histogram:\
  \ pd.cut(df['output'], bins=10).value_counts()\n   - Sentence length distribution: df['input'].str.split().str.len().describe()\n\
  \n2. Create comparison table (vs. WeeBIT and CEFR-SP):\n   | Dataset | N Sentences | Mean Score | Score Range | Avg Sentence\
  \ Length |\n   |----------|-------------|------------|-------------|---------------------|\n   | WeeBIT   | [from prior\
  \ experiments] | [value] | [range] | [value] |\n   | CEFR-SP  | [from prior experiments] | [value] | [range] | [value] |\n\
  \   | NEW DS   | [computed] | [computed] | [computed] | [computed] |\n\n3. Check data quality:\n   - Duplicates: df.duplicated('input').sum()\n\
  \   - Outliers: rows where score > mean + 3*std or score < mean - 3*std\n   - Very short sentences: df[df['input'].str.split().str.len()\
  \ < 3]\n\n4. Save dataset_info.json:\n   {\n     \"dataset_name\": \"WSJ_Liu_Lee_2023\",\n     \"source_url\": \"https://huggingface.co/datasets/...\"\
  ,\n     \"license\": \"MIT\",\n     \"n_sentences\": 1200,\n     \"score_distribution\": {\"mean\": 0.5, \"std\": 0.2, ...},\n\
  \     \"preprocessing\": \"None / Sentence splitting with NLTK\",\n     \"schema_version\": \"exp_sel_data_out.json v1.0\"\
  \n   }\n\n5. Create README.md with:\n   - Dataset description and source\n   - Loading instructions (pandas code)\n   -\
  \ Comparison to WeeBIT/CEFR-SP\n   - Known issues or limitations\n   - Citation information\n\nTIME ALLOCATION:\n-----------------\n\
  - Phase 1 (WSJ search): 2 hours (including author contact)\n- Phase 2 (CLEAR acquisition): 1.5 hours\n- Phase 3 (Alternatives):\
  \ 1.5 hours (if 1-2 fail or to acquire 2nd dataset)\n- Phase 4 (Standardization): 2 hours (for 2 datasets)\n- Phase 5 (Documentation):\
  \ 1 hour\n- BUFFER: 1 hour for unexpected issues\nTOTAL: 6 hours (with 1 hour buffer within the 6h limit)\n\nTECHNICAL IMPLEMENTATION\
  \ NOTES FOR EXECUTOR:\n=============================================\n1. Using aii-hf-datasets skill:\n   - Search: python\
  \ aii_hf_search_datasets.py --query 'X' --limit 10\n   - Preview: python aii_hf_preview_datasets.py <dataset_id> --num-rows\
  \ 5\n   - Download: python aii_hf_download_datasets.py <dataset_id> --split train\n\n2. Direct download (if not on HuggingFace):\n\
  \   import requests\n   url = 'https://example.com/dataset.csv'\n   response = requests.get(url, stream=True)\n   with open('dataset.csv',\
  \ 'wb') as f:\n       for chunk in response.iter_content(chunk_size=8192):\n           f.write(chunk)\n\n3. Schema validation:\n\
  \   - Use aii-json skill to validate output\n   - If aii-json not available: manually check JSON structure matches schema\n\
  \n4. Handling missing values:\n   - Drop rows where 'input' is NaN or empty string\n   - Drop rows where 'output' is NaN\
  \ (unless dataset is for unsupervised evaluation)\n\n5. Output file organization:\n   Save all output files in: /workspace/datasets/<dataset_name>/\n\
  \   Files: full_dataset.json, mini_dataset.json, preview_dataset.json, dataset_info.json, README.md\n\nERROR HANDLING AND\
  \ FALLBACK STRATEGIES:\n========================================\n1. Dataset not found:\n   - Log search query and result\n\
  \   - Try next candidate in the priority list\n   - Continue until target_num_datasets (2) acquired\n\n2. Download fails\
  \ (connection error, 404):\n   - Retry 3 times with 5-second delays\n   - Try mirror URL if available\n   - Skip to next\
  \ candidate\n\n3. Schema validation fails:\n   - Print exact validation errors\n   - Check field names, data types, required\
  \ fields\n   - Fix and re-validate\n\n4. Score normalization fails (constant scores or NaN):\n   - Use raw scores without\
  \ normalization\n   - Document in README.md\n   - Add warning that scores are not normalized\n\n5. CLEAR excerpts too long\
  \ (>500 words):\n   - Option A: Truncate to 200 words (preserve readability)\n   - Option B: Split into sentences (more\
  \ work but better for sentence-level evaluation)\n   - Decision: Use Option A (truncate) for speed, unless explicitly instructed\
  \ otherwise\n\n6. WeeBIT/CEFR-SP already used in experiments:\n   - DO NOT include WeeBIT or CEFR-SP as \"new\" datasets\n\
  \   - These are already available; find genuinely new datasets\n   - Check if WeeBIT/CEFR-SP have additional splits not\
  \ yet used (acceptable to use)\n\nDELIVERABLES CHECKLIST:\n========================\nFor each acquired dataset (target:\
  \ 2 datasets), ensure:\n[ ] full_<dataset_name>.json - Complete standardized dataset\n[ ] mini_<dataset_name>.json - 50-row\
  \ subset for development\n[ ] preview_<dataset_name>.json - 3-row preview with truncated text\n[ ] dataset_info.json - Metadata\
  \ and statistics\n[ ] README.md - Documentation and usage examples\n[ ] Comparison table (new dataset vs. WeeBIT vs. CEFR-SP)\n\
  \nEXECUTION ORDER:\n=================\n1. Start Phase 1 (WSJ search) and Phase 2 (CLEAR search) IN PARALLEL\n2. If Phase\
  \ 1 succeeds: download and standardize WSJ dataset\n3. If Phase 2 succeeds: download and standardize CLEAR dataset\n4. If\
  \ only 1 dataset acquired: start Phase 3 to acquire 2nd dataset\n5. Standardize all acquired datasets (Phase 4)\n6. Document\
  \ statistics (Phase 5)\n7. Verify all deliverables present"
target_num_datasets: 2
</artifact_plan>



<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Web search (Serper), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-image-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
</skills>
</available_resources>

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for dataset selection, evaluation metrics, agent orchestration patterns.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Update data.py to only include the chosen 2 datasets and generate full_data_out.json. Re-run to generate full_data_out.json. Validate output format with aii-json skill and fix any errors. Generate full, mini, and preview versions with aii-json skill's format script using `--input full_data_out.json` (creates full_full_data_out.json, mini_full_data_out.json, preview_full_data_out.json — rename to full_data_out.json, mini_data_out.json, preview_data_out.json).
TODO 2. Verify full_data_out.json, preview_data_out.json, and mini_data_out.json exist in your workspace (see <workspace>) and contain correct data.
TODO 3. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to full_data_out.json.
TODO 4. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "DatasetExpectedFiles": {
      "description": "All expected output files from dataset artifact.",
      "properties": {
        "script": {
          "description": "Path to data.py script. Example: 'data.py'",
          "title": "Script",
          "type": "string"
        },
        "datasets": {
          "description": "Dataset file groups \u2014 one per dataset, each with full/mini/preview variants",
          "items": {
            "$ref": "#/$defs/DatasetFileSet"
          },
          "title": "Datasets",
          "type": "array"
        }
      },
      "required": [
        "script",
        "datasets"
      ],
      "title": "DatasetExpectedFiles",
      "type": "object"
    },
    "DatasetFileSet": {
      "description": "One dataset's three required output variants.",
      "properties": {
        "full": {
          "description": "Full dataset JSON file(s). Single file or split files. Example: ['full_data_out.json'] or ['full_data_out/full_data_out_1.json', 'full_data_out/full_data_out_2.json']",
          "items": {
            "type": "string"
          },
          "title": "Full",
          "type": "array"
        },
        "mini": {
          "description": "Mini dataset JSON file path (3 examples). Example: 'mini_data_out.json'",
          "title": "Mini",
          "type": "string"
        },
        "preview": {
          "description": "Preview dataset JSON file path (10 examples). Example: 'preview_data_out.json'",
          "title": "Preview",
          "type": "string"
        }
      },
      "required": [
        "full",
        "mini",
        "preview"
      ],
      "title": "DatasetFileSet",
      "type": "object"
    }
  },
  "description": "Dataset artifact \u2014 structured output + file metadata.\n\nFinds, evaluates, and prepares datasets for research experiments.\nProduces data.py and full_data_out.json files.",
  "properties": {
    "title": {
      "default": "",
      "description": "Artifact title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); describe the content, not a status.",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "layman_summary": {
      "default": "",
      "description": "One-sentence plain-language summary of what this artifact does, accessible to non-experts. Used only in the per-artifact README, not in downstream prompts.",
      "maxLength": 250,
      "minLength": 80,
      "title": "Layman Summary",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Summary for downstream artifacts: what this artifact provides",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/DatasetExpectedFiles",
      "description": "All output files you created. Must include data.py script plus dataset file groups (full/mini/preview variants)."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files"
  ],
  "title": "DatasetArtifact",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `/ai-inventor/aii_data/runs/run_nOuUUSNqdMp4/3_invention_loop/iter_2/gen_art/gen_art_dataset_1/.sdk_openhands_agent_struct_out.json`.
````
