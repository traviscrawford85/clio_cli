import re
from pathlib import Path

INPUT_FILE = Path("clio_clients/generated_models_fixed.py")
OUTPUT_DIR = Path("clio_clients/models")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

code = INPUT_FILE.read_text()

import_block = code.split("class ", 1)[0]
matches = re.finditer(r"(class\s+(\w+)\((.*?)\):\n((?: {4}.*\n)+))", code)

written = []

for match in matches:
    class_block = match.group(0)
    class_name = match.group(2)
    base_classes = [b.strip() for b in match.group(3).split(",")]

    filename = OUTPUT_DIR / f"{class_name.lower()}.py"

    # Prepare import statements for base classes that are not built-in or from pydantic/typing
    needed_imports = []
    for base in base_classes:
        if base in ("BaseModel", "Enum", "IntEnum", "str", "int", "float", "object"):
            continue
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
