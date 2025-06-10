import re

input_path = "clio_clients/generated_models.py"
output_path = "clio_clients/generated_models_fixed.py"

with open(input_path) as infile, open(output_path, "w") as outfile:
    for line in infile:
        # Only process lines inside a class (heuristic: lines with '=' and not starting with 'class' or 'def')
        if (
            "=" in line
            and not line.strip().startswith("class")
            and not line.strip().startswith("def")
            and not line.strip().startswith("#")
        ):
            # Split by ';' or by multiple assignments on the same line
            parts = re.split(r"(?<![<>=])\s{2,}", line.strip())
            for part in parts:
                if part:
                    outfile.write("    " + part.strip() + "\n")
        else:
            outfile.write(line)
print(f"Refactored file written to {output_path}")
