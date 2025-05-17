import json

def check_duplicate_parameters(spec_file):
    with open(spec_file, 'r') as f:
        spec = json.load(f)
    
    for path, path_item in spec.get("paths", {}).items():
        for method, operation in path_item.items():
            if method not in ["get", "post", "put", "patch", "delete"]:
                continue
            params = operation.get("parameters", [])
            seen = set()
            duplicates = []
            for param in params:
                key = (param.get("name"), param.get("in"))
                if key in seen:
                    duplicates.append(key)
                else:
                    seen.add(key)
            if duplicates:
                print(f"❗ Duplicates in {method.upper()} {path}: {duplicates}")
    print("✅ Duplicate check complete.")

# Usage
check_duplicate_parameters('merged_openapi.json')
