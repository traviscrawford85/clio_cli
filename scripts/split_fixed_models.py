import re
import sys
from pathlib import Path

# Enum-like prefixes to organize into subfolders
ENUM_PREFIXES = [
    "enum",
    "color",
    "status",
    "type",
    "source",
    "priority",
    "event",
    "format",
    "hierarchy",
    "kind",
    "lientype",
    "lightcolor",
    "name",
    "model",
    "parenttype",
    "permission",
    "secondarytaxrule",
    "statue",
    "decimal",
]


def get_enum_subfolder(class_name: str) -> str | None:
    for prefix in ENUM_PREFIXES:
        if class_name.lower().startswith(prefix):
            return prefix
    return None


INPUT_FILE = Path("models.py")
if not INPUT_FILE.exists():
    print(
        f"ERROR: {INPUT_FILE} does not exist. Did datamodel-codegen run successfully?",
        file=sys.stderr,
    )
    sys.exit(1)

code = INPUT_FILE.read_text()

OUTPUT_DIR = Path("clio_clients/models")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

import_block = code.split("class ", 1)[0]
matches = re.finditer(r"(class\s+(\w+)\((.*?)\):\n((?: {4}.*\n)+))", code)

written = []
folders_created = set()

for match in matches:
    class_block = match.group(0)
    class_name = match.group(2)
    base_classes = [b.strip() for b in match.group(3).split(",")]

    subfolder = get_enum_subfolder(class_name)
    if subfolder:
        target_dir = OUTPUT_DIR / subfolder
        if not target_dir.exists():
            target_dir.mkdir(parents=True, exist_ok=True)
            print(f"📁 Created subfolder: {target_dir.relative_to(OUTPUT_DIR)}")
            folders_created.add(str(target_dir.relative_to(OUTPUT_DIR)))
        filename = target_dir / f"{class_name.lower()}.py"
    else:
        filename = OUTPUT_DIR / f"{class_name.lower()}.py"

    # Prepare import statements for base classes that are not built-in or from pydantic/typing
    needed_imports = []
    for base in base_classes:
        if base in ("BaseModel", "Enum", "IntEnum", "str", "int", "float", "object"):
            continue
        # Import from the same directory (since all non-enums are flat)
        needed_imports.append(f"from .{base.lower()} import {base}")

    # Remove duplicate imports
    needed_imports = list(dict.fromkeys(needed_imports))

    # Write the file
    with open(filename, "w") as f:
        f.write(import_block.strip() + "\n")
        if needed_imports:
            f.write("\n" + "\n".join(needed_imports) + "\n")
        f.write("\n" + class_block)
    written.append(str(filename.relative_to(OUTPUT_DIR.parent)))

print(f"✅ Split {len(written)} model classes into files in: {OUTPUT_DIR}")
if folders_created:
    print("Enum subfolders created:")
    for folder in sorted(folders_created):
        print(f"  - {folder}")
