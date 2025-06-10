import os
import re

# Ensure this script always operates on the correct models folder
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "clio_clients", "models"))


def fix_imports_in_file(filepath: str):
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    original_content = content

    # Fix pydantic imports
    content = re.sub(
        r"from clio_clients\.models\.pydantic import (BaseModel|Field)",
        r"from pydantic import \1",
        content,
    )
    # Fix typing imports
    content = re.sub(
        r"from clio_clients\.models\.typing import (.+)",
        r"from typing import \1",
        content,
    )
    # Remove __future__ import if not needed
    content = re.sub(
        r"from clio_clients\.models\.__future__ import annotations\n", "", content
    )
    # Fix relative imports: from .foo import Bar -> from clio_clients.models.foo import Bar
    content = re.sub(
        r"from\s+\.(\w+)\s+import\s+([A-Za-z0-9_, ]+)",
        r"from clio_clients.models.\1 import \2",
        content,
    )
    # Fix relative imports for subfolders: from ..enum.foo import Bar -> from clio_clients.models.enum.foo import Bar
    content = re.sub(
        r"from\s+\.\.(\w+)\.(\w+)\s+import\s+([A-Za-z0-9_, ]+)",
        r"from clio_clients.models.\1.\2 import \3",
        content,
    )

    if content != original_content:
        print(f"🛠️  Fixed imports in {os.path.relpath(filepath, MODELS_DIR)}")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    folders_created = set()
    for root, dirs, files in os.walk(MODELS_DIR):
        for file in files:
            if file.endswith(".py"):
                fix_imports_in_file(os.path.join(root, file))
        # Print folders created (excluding the root models folder)
        for d in dirs:
            if d.startswith('.') or d == '__pycache__':
                continue
            folder_path = os.path.join(root, d)
            if folder_path not in folders_created:
                print(
                    f"📁 Found/created folder: {os.path.relpath(folder_path, MODELS_DIR)}"
                )
                folders_created.add(folder_path)


if __name__ == "__main__":
    print(f"🔎 Scanning for model files in: {MODELS_DIR}")
    main()
