#!/usr/bin/env python3
"""Combine acquired readability datasets into exp_sel_data_out.json format."""

import json
from pathlib import Path
from loguru import logger
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    # Load all three datasets
    datasets_dir = Path("datasets")
    
    # Dataset files
    clear_file = datasets_dir / "full_CLEAR_corpus.json"
    ose_file = datasets_dir / "full_OneStopEnglish.json"
    agentlans_file = datasets_dir / "full_agentlans_readability.json"
    
    output_file = Path("full_data_out.json")
    
    logger.info("Loading datasets...")
    
    # Load and combine datasets
    combined = {"datasets": []}
    
    # Load CLEAR corpus
    if clear_file.exists():
        with open(clear_file, 'r') as f:
            clear_data = json.load(f)
        combined["datasets"].append(clear_data["datasets"][0])
        logger.info(f"Loaded CLEAR corpus: {len(clear_data['datasets'][0]['examples'])} examples")
    
    # Load OneStopEnglish
    if ose_file.exists():
        with open(ose_file, 'r') as f:
            ose_data = json.load(f)
        combined["datasets"].append(ose_data["datasets"][0])
        logger.info(f"Loaded OneStopEnglish: {len(ose_data['datasets'][0]['examples'])} examples")
    
    # Load agentlans readability
    if agentlans_file.exists():
        with open(agentlans_file, 'r') as f:
            agentlans_data = json.load(f)
        combined["datasets"].append(agentlans_data["datasets"][0])
        logger.info(f"Loaded agentlans readability: {len(agentlans_data['datasets'][0]['examples'])} examples")
    
    # Save combined output
    with open(output_file, 'w') as f:
        json.dump(combined, f, indent=2)
    
    total_examples = sum(len(d["examples"]) for d in combined["datasets"])
    logger.info(f"Saved {output_file}: {len(combined['datasets'])} datasets, {total_examples} total examples")

if __name__ == "__main__":
    main()
