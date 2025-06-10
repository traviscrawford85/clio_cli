from jinja2 import Environment, FileSystemLoader

resources = [
    {"name": "Matter"},
    {"name": "Task"},
    {"name": "Contact"},
    # Add more models as needed
]

env = Environment(loader=FileSystemLoader("/home/sysadmin01/clio_cli/templates"))
template = env.get_template("method.py.jinja")

output = template.render(resources=resources)

with open("clio_clients/generated_methods.py", "w") as f:
    f.write(output)
