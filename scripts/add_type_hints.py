"""
Script to scan the codebase and add type hints using MonkeyType.

Usage:
    1. Install MonkeyType: pip install monkeytype
    2. Run your application/tests with MonkeyType tracing enabled:
        $ monkeytype run your_script.py
    3. Apply the collected type hints:
        $ python scripts/add_type_hints.py
"""

import os
import subprocess


def apply_type_hints():
    # Find all Python files in the codebase (excluding venv, .git, etc.)
    for root, dirs, files in os.walk("."):
        # Skip virtual environments and hidden folders
        dirs[:] = [d for d in dirs if not d.startswith(".") and d not in ("venv", "env", "__pycache__")]
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                print(f"Applying type hints to {filepath} ...")
                subprocess.run(["monkeytype", "apply", filepath])

if __name__ == "__main__":
    apply_type_hints()