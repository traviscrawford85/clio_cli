"""
Enhanced script to apply type hints using MonkeyType.

Usage:
    1. Run your code with MonkeyType tracing enabled:
        $ monkeytype run your_script.py
    2. Apply collected type hints to all traced modules:
        $ python scripts/add_type_hints.py

Options:
    --dry-run       Show what would be done, but don’t apply changes.
    --verbose       Print detailed output.
"""

import logging
import subprocess
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DRY_RUN = "--dry-run" in sys.argv
VERBOSE = "--verbose" in sys.argv


def run_command(command: list[str], check: bool = True) -> subprocess.CompletedProcess:
    if VERBOSE or DRY_RUN:
        print(" ".join(command))
    if not DRY_RUN:
        return subprocess.run(command, check=check)


def apply_type_hints():
    try:
        # List all modules MonkeyType has data for
        result = subprocess.run(
            ["monkeytype", "list-modules"],
            check=True,
            capture_output=True,
            text=True,
        )
        modules = result.stdout.strip().splitlines()
        if not modules:
            logger.warning("No modules found in MonkeyType DB.")
            return

        for module in modules:
            logger.info(f"Applying type hints to {module}")
            run_command(["monkeytype", "apply", module])
    except subprocess.CalledProcessError as e:
        logger.error(f"Error while applying type hints: {e}")


if __name__ == "__main__":
    apply_type_hints()
