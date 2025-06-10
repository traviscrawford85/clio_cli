import yaml
from openapi_schemas_pydantic import OpenAPI

# Load your spec
with open("openapi_sdk.yaml") as f:
    spec_dict = yaml.safe_load(f)

# Validate using Pydantic models
spec = OpenAPI(**spec_dict)

# Now you can access spec.paths, spec.components, etc.
print(spec.paths)
