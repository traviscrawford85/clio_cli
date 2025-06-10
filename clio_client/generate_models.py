from datamodel_code_generator import InputFileType, generate
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OPENAPI_FILE = BASE_DIR / "../openapi.yaml"
OUTPUT_DIR = BASE_DIR / "clio_client" / "models"

# Ensure output directory exists
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

generate(
    input=str(OPENAPI_FILE),
    input_file_type=InputFileType.OpenAPI,
    output=str(OUTPUT_DIR),
    target_python_version="3.10",
    disable_timestamp=True,
    field_constraints=True,
    use_standard_collections=True,
    use_default_union=True,
    use_title_as_name=True,
)

print(f"✅ Models generated at: {OUTPUT_DIR}")
