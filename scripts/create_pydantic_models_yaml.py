from pathlib import Path
import yaml
from pydantic import BaseModel
from typing import Any, Dict, List, Optional, Union
from jinja2 import Environment, FileSystemLoader
import re

# Load the OpenAPI spec
openapi_path = Path("openapi_sdk.yaml")
openapi_data = yaml.safe_load(openapi_path.read_text())

# Extract components/schemas
schemas: Dict[str, Any] = openapi_data.get("components", {}).get("schemas", {})


# Prepare model field parsing
def get_python_type(schema: Dict[str, Any]) -> str:
    if "$ref" in schema:
        return schema["$ref"].split("/")[-1]
    typ = schema.get("type", "Any")
    if typ == "string":
        fmt = schema.get("format")
        if fmt == "date-time":
            return "datetime"
        elif fmt == "date":
            return "date"
        return "str"
    elif typ == "integer":
        return "int"
    elif typ == "number":
        return "float"
    elif typ == "boolean":
        return "bool"
    elif typ == "array":
        items = schema.get("items", {})
        return f"List[{get_python_type(items)}]"
    elif typ == "object":
        return "dict"
    return "Any"


# Jinja2 environment setup
env = Environment(loader=FileSystemLoader("."), trim_blocks=True, lstrip_blocks=True)
template_str = """
from pydantic import BaseModel
from typing import Optional, Any, List
from datetime import datetime, date

{% for model in models %}
class {{ model.name }}(BaseModel):
{% if model.fields|length == 0 %}
    pass
{% else %}
{% for field in model.fields %}
    {{ field.name }}: {{ field.type }}{% if not field.required %} = None{% endif %}
{% endfor %}
{% endif %}

{% endfor %}
"""
template = env.from_string(template_str)

# Extract models
models = []
for name, schema in schemas.items():
    required_fields = schema.get("required", [])
    properties = schema.get("properties", {})
    fields = []
    for prop_name, prop_schema in properties.items():
        fields.append(
            {
                "name": prop_name,
                "type": get_python_type(prop_schema),
                "required": prop_name in required_fields,
            }
        )
    models.append({"name": name, "fields": fields})

# Render the models
rendered_code = template.render(models=models)

output_path = Path("clio_clients/models/generated_models.py")
output_path.write_text(rendered_code)
print(f"✅ Models written to {output_path}")
