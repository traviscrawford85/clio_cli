import json
import sys
from pathlib import Path

def merge_dicts(base, patch):
    for key, value in patch.items():
        if key in base:
            if isinstance(base[key], dict) and isinstance(value, dict):
                merge_dicts(base[key], value)
            else:
                base[key] = value  # overwrite scalar or array
        else:
            base[key] = value

def main(base_file, patch_file, output_file):
    base_path = Path(base_file)
    patch_path = Path(patch_file)

    if not base_path.exists() or not patch_path.exists():
        print(f"❌ One of the input files does not exist.")
        sys.exit(1)

    with open(base_path, 'r', encoding='utf-8') as f:
        base_data = json.load(f)

    with open(patch_path, 'r', encoding='utf-8') as f:
        patch_data = json.load(f)

    merge_dicts(base_data, patch_data)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(base_data, f, indent=2)

    print(f"✅ Merged spec saved as {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python merge_openapi.py base.json patch.json output.json")
        sys.exit(1)
    
    base_file, patch_file, output_file = sys.argv[1], sys.argv[2], sys.argv[3]
    main(base_file, patch_file, output_file)
