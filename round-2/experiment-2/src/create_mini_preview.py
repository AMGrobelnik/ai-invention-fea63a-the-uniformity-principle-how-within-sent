#!/usr/bin/env python3
"""Generate mini and preview versions of method_out.json."""

import json
from pathlib import Path

def create_mini_preview(input_path, output_dir=None):
    """Create mini and preview versions of the results."""
    input_path = Path(input_path)
    if output_dir is None:
        output_dir = input_path.parent
    
    with open(input_path, 'r') as f:
        data = json.load(f)
    
    # Create mini version (keep structure but reduce data)
    mini_data = {
        'experiment_info': data.get('experiment_info', {}),
        'datasets': {}
    }
    
    # For mini, keep only first dataset or sample results
    if 'datasets' in data:
        # Just keep WeeBIT for mini
        if 'WeeBIT' in data['datasets']:
            mini_data['datasets']['WeeBIT'] = data['datasets']['WeeBIT']
    
    mini_path = output_dir / f"mini_{input_path.name}"
    with open(mini_path, 'w') as f:
        json.dump(mini_data, f, indent=2)
    print(f"Created mini version: {mini_path}")
    
    # Create preview version (truncate long strings)
    preview_data = json.loads(json.dumps(mini_data))
    
    def truncate_strings(obj, max_len=200):
        if isinstance(obj, str):
            return obj[:max_len] + "..." if len(obj) > max_len else obj
        elif isinstance(obj, dict):
            return {k: truncate_strings(v, max_len) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [truncate_strings(item, max_len) for item in obj]
        else:
            return obj
    
    preview_data = truncate_strings(preview_data)
    
    preview_path = output_dir / f"preview_{input_path.name}"
    with open(preview_path, 'w') as f:
        json.dump(preview_data, f, indent=2)
    print(f"Created preview version: {preview_path}")

if __name__ == "__main__":
    import sys
    input_file = sys.argv[1] if len(sys.argv) > 1 else "method_out.json"
    create_mini_preview(input_file)
