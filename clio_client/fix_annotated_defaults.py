import os
import re

# Set the directory where your generated files are located
API_DIR = "generated_server/openapi_server/apis"

# Regex to find Annotated lines with Query(None, description=...)
pattern = re.compile(r"Annotated\[(.+?),\s*Query\(\s*None\s*,(.*?)\)")

def patch_file(filepath):
    with open(filepath, "r") as f:
        content = f.read()

    # Replace pattern with corrected form
    new_content = pattern.sub(r"Annotated[\1, Query(\2)] = None", content)

    if content != new_content:
        with open(filepath, "w") as f:
            f.write(new_content)
        print(f"✅ Patched: {filepath}")

def patch_all_files():
    for root, _, files in os.walk(API_DIR):
        for file in files:
            if file.endswith(".py"):
                patch_file(os.path.join(root, file))

if __name__ == "__main__":
    patch_all_files()
