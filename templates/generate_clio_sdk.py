import argparse
import json
import re
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader


def load_openapi(path: str):
    with open(path, "r") as f:
        if path.endswith(".yaml") or path.endswith(".yml"):
            return yaml.safe_load(f)
        return json.load(f)


def pascalcase(value):
    return "".join(word.capitalize() for word in str(value).replace("_", " ").split())


def snakecase(value):
    return re.sub(r"[^0-9a-zA-Z_]", "_", str(value)).lower()


def map_type(schema):
    if not schema:
        return "Any"
    if "$ref" in schema:
        return schema["$ref"].split("/")[-1]
    t = schema.get("type")
    if t == "array":
        items = schema.get("items")
        item_type = map_type(items) if items else "Any"
        return f"list[{item_type}]"
    return {
        "string": "str",
        "integer": "int",
        "boolean": "bool",
        "number": "float",
        "object": "dict",
    }.get(t, "Any")


def infer_parameters(params):
    result = []
    for param in params:
        name = param["name"]
        required = param.get("required", False)
        param_type = map_type(param.get("schema", {}))
        if not required:
            param_type = f"Optional[{param_type}]"
        result.append(
            {
                "name": name,
                "type": param_type,
                "required": required,
            }
        )
    return result


def infer_request_model(request_body):
    if not request_body:
        return None
    content = request_body.get("content", {})
    if "application/json" in content:
        schema = content["application/json"].get("schema", {})
        return map_type(schema)
    return None


def infer_response_model(responses):
    if "200" in responses and "content" in responses["200"]:
        content = responses["200"]["content"]
        if "application/json" in content:
            schema = content["application/json"].get("schema", {})
            return map_type(schema)
    return "Any"


def generate_sdk(
    openapi,
    template_path,
    output_dir,
    async_mode,
    sdk_name,
    include_services,
    tag_groups_file,
    grouped=False,
    include_interfaces=False,
    oauth=False,
):
    # Adjust output path if sdk_name is specified
    if sdk_name:
        output_dir = str(Path(output_dir) / sdk_name)
        Path(output_dir).mkdir(parents=True, exist_ok=True)

    env = Environment(loader=FileSystemLoader(template_path))
    env.filters["pascalcase"] = pascalcase
    env.filters["snakecase"] = snakecase
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Handle new flags (placeholders for now)
    if grouped:
        # TODO: Implement grouped logic
        pass
    if include_interfaces:
        # TODO: Implement interface generation logic
        pass
    if oauth:
        # TODO: Implement OAuth support logic
        pass

    alias_map = {}
    if tag_groups_file and Path(tag_groups_file).exists():
        with open(tag_groups_file) as f:
            groupings_data = yaml.safe_load(f)
            # Support both dict and list YAML structures
            if isinstance(groupings_data, dict):
                for group, details in groupings_data.items():
                    tags = details.get("tags", []) if isinstance(details, dict) else []
                    for tag in tags:
                        alias_map[tag] = group
            elif isinstance(groupings_data, list):
                for group in groupings_data:
                    group_name = group.get("name")
                    tags = group.get("tags", [])
                    for tag in tags:
                        alias_map[tag] = group_name

    tag_to_operations = {}
    for path, methods in openapi.get("paths", {}).items():
        for method, operation in methods.items():
            tags = operation.get("tags", ["default"])
            for tag in tags:
                alias = alias_map.get(tag, tag)
                tag_to_operations.setdefault(alias, []).append(
                    {
                        "method": method.upper(),
                        "path": path,
                        "operation_id": operation.get(
                            "operationId", "unnamed_operation"
                        ),
                        "summary": operation.get("summary", ""),
                        "parameters": operation.get("parameters", []),
                        "request_body": operation.get("requestBody", {}),
                        "responses": operation.get("responses", {}),
                    }
                )

    for tag, operations in tag_to_operations.items():
        tag_snake = tag.lower().replace(" ", "_")
        api_template = env.get_template("api_class.py.jinja")
        api_output = api_template.render(
            classname=tag,
            description=f"{tag} operations",
            endpoints=operations,
            async_mode=async_mode,
        )
        with open(Path(output_dir) / f"{tag_snake}_api.py", "w") as f:
            f.write(api_output)

        transformer_template = env.get_template("transformers/transformers.py.jinja")
        transformer_output = transformer_template.render(tag=tag, models=[])
        with open(Path(output_dir) / f"{tag_snake}_transformers.py", "w") as f:
            f.write(transformer_output)

    sdk_template = env.get_template("clio_sdk.py.jinja")
    sdk_output = sdk_template.render(tags=tag_to_operations.keys(), sdk_name=sdk_name)
    with open(Path(output_dir) / f"{sdk_name}.py", "w") as f:
        f.write(sdk_output)

    doc_template = env.get_template("doc.md.jinja")
    docs_dir = Path(output_dir) / "docs"
    docs_dir.mkdir(exist_ok=True)
    for tag, ops in tag_to_operations.items():
        doc_output = doc_template.render(tag=tag, operations=ops)
        with open(docs_dir / f"{tag.lower().replace(' ', '_')}.md", "w") as f:
            f.write(doc_output)

    if include_services:
        service_impl_template = env.get_template("services/service_impl.py.jinja")
        service_interface_template = env.get_template(
            "services/service_interface.py.jinja"
        )
        for tag, ops in tag_to_operations.items():
            class_name = f"{tag.title().replace(' ', '')}"
            tag_snake = tag.lower().replace(" ", "_")
            impl_output = service_impl_template.render(
                classname=class_name, operations=ops, tag_snake=tag_snake
            )
            (Path(output_dir) / "services" / f"{tag_snake}_service_impl.py").write_text(
                impl_output
            )
            service_output = service_interface_template.render(
                classname=class_name, operations=ops
            )
            (Path(output_dir) / "interfaces" / f"i_{tag_snake}_service.py").write_text(
                service_output
            )

    x_tag_template = env.get_template("x_tag_groups.yaml.jinja")
    x_tag_output = x_tag_template.render(tags=tag_to_operations.keys())
    with open(Path(output_dir) / "x_tag_groups.yaml", "w") as f:
        f.write(x_tag_output)

    derived_groupings_template = env.get_template("derived_api_groupings.yaml.jinja")
    groupings = {"General": list(tag_to_operations.keys())}
    groupings_output = derived_groupings_template.render(groupings=groupings)
    with open(Path(output_dir) / "derived_api_groupings.yaml", "w") as f:
        f.write(groupings_output)

    derived_template = env.get_template("derived_api_calls.yaml.jinja")
    derived_yaml = derived_template.render(tag_to_operations=tag_to_operations)
    with open(Path(output_dir) / "derived_api_calls.yaml", "w") as f:
        f.write(derived_yaml)

    # Generate FastAPI route modules
    route_template = env.get_template("route_module.py.jinja")
    routes_dir = Path(output_dir) / "routes"
    routes_dir.mkdir(exist_ok=True)
    for tag, ops in tag_to_operations.items():
        tag_snake = tag.lower().replace(" ", "_")
        route_output = route_template.render(tag_snake=tag_snake, operations=ops)
        with open(routes_dir / f"{tag_snake}.py", "w") as f:
            f.write(route_output)

    # Generate main.py for FastAPI
    main_template = env.get_template("main_template.py.jinja")
    main_output = main_template.render(tags=tag_to_operations.keys(), sdk_name=sdk_name)
    with open(Path(output_dir).parent / "main.py", "w") as f:
        f.write(main_output)

    for tag, operations in tag_to_operations.items():
        for op in operations:
            op["parameters"] = infer_parameters(op.get("parameters", []))
            op["request_model"] = infer_request_model(op.get("request_body", {}))
            op["response_model"] = infer_response_model(op.get("responses", {}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--openapi", required=True, help="Path to openapi.json or openapi.yaml"
    )
    parser.add_argument("--templates", required=True, help="Path to Jinja templates")
    parser.add_argument(
        "--target-dir", required=True, help="Output directory for generated SDK"
    )
    parser.add_argument(
        "--async", dest="async_mode", action="store_true", help="Generate async SDK"
    )
    parser.add_argument("--sdk-name", default="clio_sdk", help="Root SDK module name")
    parser.add_argument(
        "--include-services",
        action="store_true",
        help="Include service interfaces and implementations",
    )
    parser.add_argument(
        "--tag-groups",
        default=None,
        help="YAML file with x-tagGroups/derived API groupings",
    )
    parser.add_argument(
        "--grouped", action="store_true", help="Group endpoints in SDK output"
    )
    parser.add_argument(
        "--include-interfaces",
        action="store_true",
        help="Include interface files in SDK output",
    )
    parser.add_argument(
        "--oauth", action="store_true", help="Enable OAuth support in SDK output"
    )
    parser.add_argument(
        "--target-dir", required=True, help="Output directory for generated SDK"
    )
    args = parser.parse_args()

    openapi = load_openapi(args.openapi)
    generate_sdk(
        openapi,
        args.templates,
        args.target_dir,  # <-- change this
        async_mode=args.async_mode,
        sdk_name=args.sdk_name,
        include_services=args.include_services,
        tag_groups_file=args.tag_groups,
        grouped=args.grouped,
        include_interfaces=args.include_interfaces,
        oauth=args.oauth,
    )
