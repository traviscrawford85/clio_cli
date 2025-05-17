import os
import re

API_FOLDER = "./openapi_server/apis"

def get_new_name(filename, param):
    """Generate a new param name like document_id or client_id"""
    base = filename.replace("_api.py", "")
    return f"{base}_{param}"

def fix_file(filepath):
    with open(filepath, "r") as f:
        content = f.read()

    # Find all function definitions
    func_pattern = re.compile(r"async def (\w+)\(.*?\):", re.DOTALL)
    functions = func_pattern.findall(content)

    # Find all parameter blocks
    param_block_pattern = re.compile(r"async def (\w+)\((.*?)\):", re.DOTALL)
    param_blocks = param_block_pattern.findall(content)

    modified = False

    for func_name, param_block in param_blocks:
        # Find param names
        params = re.findall(r"(\w+): Annotated", param_block)
        duplicates = [p for p in set(params) if params.count(p) > 1]

        for dup in duplicates:
            new_name = get_new_name(os.path.basename(filepath), dup)
            print(f"Fixing duplicate '{dup}' → '{new_name}' in {func_name} of {filepath}")
            # Replace param names
            param_block = re.sub(
                fr"\b{dup}\b", new_name, param_block, count=1
            )  # rename first occurrence only

            # Update function body call
            call_pattern = re.compile(rf"{func_name}\((.*?)\)")
            call_block = call_pattern.search(content)
            if call_block:
                updated_call = call_block.group(1).replace(dup, new_name, 1)
                content = content.replace(call_block.group(1), updated_call)

        # Replace updated param block in content
        content = re.sub(
            rf"(async def {func_name}\()(.*?)(\):)",
            rf"\1{param_block}\3",
            content,
            flags=re.DOTALL,
        )
        modified = True

    if modified:
        with open(filepath, "w") as f:
            f.write(content)

def main():
    for root, _, files in os.walk(API_FOLDER):
        for file in files:
            if file.endswith("_api.py"):
                fix_file(os.path.join(root, file))
                print("✅ Duplicate parameter cleanup complete.")


if __name__ == "__main__":
    main()
