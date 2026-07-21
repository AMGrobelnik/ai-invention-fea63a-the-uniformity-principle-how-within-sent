#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "datasets",
#     "loguru",
# ]
# ///

"""Standardize readability datasets to exp_sel_data_out.json schema."""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")


@logger.catch(reraise=True)
def load_dataset(file_path: str) -> list:
    """Load dataset from JSON file."""
    with open(file_path) as f:
        data = json.load(f)

    # Handle different formats:
    # - List directly: return as-is
    # - Dict with "examples" key: return examples
    # - Dict with "dataset_name" and "examples": return examples
    if isinstance(data, list):
        return data
    elif isinstance(data, dict):
        if "examples" in data:
            return data["examples"]
        else:
            # Assume it's a single example or unknown format
            return [data]

    return []


@logger.catch(reraise=True)
def standardize_to_schema(datasets: list) -> dict:
    """Convert datasets to exp_sel_data_out.json schema.

    For readability assessment:
    - input: sentence text
    - output: readability score (as string)
    - metadata_readability_score: numeric score (for downstream use)
    - metadata_source: dataset source
    """
    result = {"datasets": []}

    for dataset_info in datasets:
        dataset_name = dataset_info["name"]
        examples = dataset_info["examples"]

        standardized_examples = []
        for i, example in enumerate(examples):
            # Extract text and readability score
            text = example.get("text", "")
            readability_score = example.get("readability_score", 0.0)

            # Convert to schema format
            standardized_example = {
                "input": text,
                "output": str(readability_score),  # Must be string per schema
                "metadata_readability_score": readability_score,  # Numeric for downstream
                "metadata_source": dataset_name,
                "metadata_row_index": i,
            }

            # Add any additional metadata from source
            if "source_metadata" in example:
                for key, value in example["source_metadata"].items():
                    if key not in ["source"]:  # Already captured
                        standardized_example[f"metadata_{key}"] = value

            standardized_examples.append(standardized_example)

        result["datasets"].append({
            "dataset": dataset_name,
            "examples": standardized_examples
        })

        logger.info(f"Standardized {dataset_name}: {len(standardized_examples)} examples")

    return result


@logger.catch(reraise=True)
def main():
    # Define datasets to process
    datasets_to_process = [
        {
            "name": "WeeBIT",
            "file": "temp/datasets/full_weebit.json"
        },
        {
            "name": "CEFR-SP",
            "file": "temp/datasets/full_cefr_sp.json"
        }
    ]

    # Load all datasets
    all_datasets = []
    for ds_info in datasets_to_process:
        logger.info(f"Loading {ds_info['name']} from {ds_info['file']}")
        examples = load_dataset(ds_info["file"])
        all_datasets.append({
            "name": ds_info["name"],
            "examples": examples
        })

    # Standardize to schema
    logger.info("Standardizing datasets to exp_sel_data_out.json schema...")
    standardized_data = standardize_to_schema(all_datasets)

    # Add metadata
    standardized_data["metadata"] = {
        "description": "Sentence-level readability datasets for readability assessment",
        "task_type": "regression",
        "num_datasets": len(standardized_data["datasets"]),
        "total_examples": sum(len(d["examples"]) for d in standardized_data["datasets"])
    }

    # Save to full_data_out.json
    output_path = Path("full_data_out.json")
    output_path.write_text(json.dumps(standardized_data, indent=2))
    logger.info(f"Saved standardized datasets to {output_path}")
    logger.info(f"Total datasets: {len(standardized_data['datasets'])}")
    logger.info(f"Total examples: {standardized_data['metadata']['total_examples']}")

    # Print sample from each dataset
    for dataset in standardized_data["datasets"]:
        logger.info(f"\nSample from {dataset['dataset']}:")
        sample = dataset["examples"][0]
        logger.info(f"  input: {sample['input'][:100]}...")
        logger.info(f"  output: {sample['output']}")
        logger.info(f"  metadata: { {k: v for k, v in sample.items() if k.startswith('metadata')} }")


if __name__ == "__main__":
    main()
