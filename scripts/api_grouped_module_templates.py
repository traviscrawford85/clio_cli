import os

from jinja2 import Environment, FileSystemLoader, select_autoescape

# Set up Jinja environment
template_dir = "templates"
os.makedirs(template_dir, exist_ok=True)
env = Environment(loader=FileSystemLoader(template_dir), autoescape=select_autoescape())

# Create the Jinja template for grouped API modules
template_content = """\"\"\"{{ tag_group.name }} API Module\"\"\"

{% for tag in tag_group.tags %}
# Tag: {{ tag }}
{% for op in operations_by_tag.get(tag, []) %}
def {{ op.operation_id|replace('#', '_')|lower }}():
    \"\"\"{{ op.summary }}\"\"\"
    # Endpoint: {{ op.method }} {{ op.path }}
    pass

{% endfor %}
{% endfor %}
"""

template_path = os.path.join(template_dir, "api_module_by_group.py.jinja")
with open(template_path, "w") as f:
    f.write(template_content)

# Render a few tag groups for demonstration
rendered_outputs = {}
template = env.get_template("api_module_by_group.py.jinja")

for tag_group in tag_groups[:3]:  # Limit to first 3 for preview
    module_code = template.render(
        tag_group=tag_group, operations_by_tag=operations_by_tag
    )
    rendered_outputs[tag_group["name"]] = module_code

rendered_outputs
