"""
Derive API Calls from OpenAPI Spec

This script analyzes an OpenAPI specification to extract and classify API operations
based on their structure and metadata. The goal is to generate a structured summary
of the API, including inferred CRUD operation types, request/response characteristics,
and key metadata.
"""

import re
import sys
from pathlib import Path

import yaml


def load_spec(spec_path):
    with open(spec_path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def resolve_ref(ref, root):
    """Resolve a local $ref in the OpenAPI spec."""
    if not ref.startswith("#/"):
        return None
    parts = ref.lstrip("#/").split("/")
    val = root
    for part in parts:
        val = val.get(part)
        if val is None:
            return None
    return val


def collect_parameters(operation, path_item, root):
    """Collect parameters from both path and operation, resolving $refs."""
    params = []
    seen = set()
    for param_list in [
        path_item.get("parameters", []),
        operation.get("parameters", []),
    ]:
        for param in param_list:
            if "$ref" in param:
                resolved = resolve_ref(param["$ref"], root)
                if resolved:
                    key = (resolved.get("name"), resolved.get("in"))
                    if key not in seen:
                        params.append(resolved)
                        seen.add(key)
            else:
                key = (param.get("name"), param.get("in"))
                if key not in seen:
                    params.append(param)
                    seen.add(key)
    return params


def get_request_body_schema_name(request_body, root):
    """Extract the schema name from a requestBody (if any)."""
    if "$ref" in request_body:
        resolved = resolve_ref(request_body["$ref"], root)
        if not resolved:
            return None
        request_body = resolved
    content = request_body.get("content", {})
    for media_type, media_obj in content.items():
        schema = media_obj.get("schema", {})
        if "$ref" in schema:
            ref = schema["$ref"]
            # Extract the schema name from the ref
            match = re.match(r"#/components/schemas/([^/]+)", ref)
            if match:
                return match.group(1)
        elif "title" in schema:
            return schema["title"]
    return None


def infer_crud_type(path, method):
    """Infer CRUD type based on path and method."""
    if method == "post":
        if "{" not in path:
            return "Create"
    if method == "get":
        if "{" in path:
            return "Retrieve"
        else:
            return "List"
    if method in ("patch", "put"):
        return "Update"
    if method == "delete":
        return "Delete"
    return "Other"


def main():
    spec_path = Path("openapi_sdk.yaml")
    if not spec_path.exists():
        print("❌ Spec file not found:", spec_path)
        sys.exit(1)
    spec = load_spec(spec_path)
    root = spec

    results = []
    for path, path_item in spec.get("paths", {}).items():
        for method in path_item:
            if method not in {"get", "post", "put", "patch", "delete"}:
                continue
            operation = path_item[method]
            op_id = operation.get("operationId")
            summary = operation.get("summary", "")
            description = operation.get("description", "")
            tags = operation.get("tags", [])
            crud_type = infer_crud_type(path, method)
            # Parameters
            params = collect_parameters(operation, path_item, root)
            query_params = [p["name"] for p in params if p.get("in") == "query"]
            # Request body
            req_body_schema = None
            if "requestBody" in operation:
                req_body_schema = get_request_body_schema_name(
                    operation["requestBody"], root
                )
            # Response codes
            response_codes = list(operation.get("responses", {}).keys())

            results.append(
                {
                    "path": path,
                    "method": method.upper(),
                    "crud_type": crud_type,
                    "operation_id": op_id,
                    "summary": summary,
                    "description": description,
                    "tags": tags,
                    "request_body_schema": req_body_schema,
                    "query_parameters": query_params,
                    "response_codes": response_codes,
                }
            )

    # Output as YAML for review
    print(yaml.safe_dump(results, sort_keys=False, allow_unicode=True))
    # Optionally, write to a file
    output_path = Path("api_calls_summary.yaml")
    with output_path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(results, f, sort_keys=False, allow_unicode=True)
    print(f"✅ Summary written to {output_path}")


if __name__ == "__main__":
    main()
