#!/usr/bin/env python3
"""
Audit and regenerate Clio models using openapi-schemas-pydantic.

This script will:
1. Load the OpenAPI schema from openapi_sdk.yaml
2. Generate Pydantic models using openapi-schemas-pydantic
3. Compare with existing models in clio_clients/models/
4. Report differences and missing imports
5. Optionally regenerate models with proper imports
"""

import yaml
import os
import sys
from pathlib import Path
from typing import Dict, List, Set
import re

try:
    import openapi_schemas_pydantic
except ImportError:
    print("ERROR: openapi-schemas-pydantic not installed. Install with: pip install openapi-schemas-pydantic")
    sys.exit(1)

def load_openapi_schema(schema_path: str) -> Dict:
    """Load OpenAPI schema from YAML file."""
    with open(schema_path, 'r') as f:
        return yaml.safe_load(f)

def get_existing_models(models_dir: str) -> Dict[str, str]:
    """Get all existing model files."""
    models = {}
    models_path = Path(models_dir)
    
    for py_file in models_path.rglob("*.py"):
        if py_file.name == "__init__.py":
            continue
        
        relative_path = py_file.relative_to(models_path)
        model_name = py_file.stem
        models[model_name] = str(py_file)
    
    return models

def extract_imports_from_file(file_path: str) -> Set[str]:
    """Extract all imports from a Python file."""
    imports = set()
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            
        # Find all import statements
        import_pattern = r'from\s+(\S+)\s+import\s+(\S+)'
        matches = re.findall(import_pattern, content)
        
        for module, name in matches:
            imports.add(f"{module}.{name}")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    
    return imports

def extract_class_references(file_path: str) -> Set[str]:
    """Extract all class references that might need imports."""
    references = set()
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Look for type annotations and class references
        # This is a simple regex - could be more sophisticated
        patterns = [
            r':\s*([A-Z][a-zA-Z0-9_]*)',  # Type annotations
            r'\$ref:\s*[\'"]#/components/schemas/([A-Z][a-zA-Z0-9_]*)[\'"]',  # OpenAPI refs
            r'([A-Z][a-zA-Z0-9_]*)\s*\(',  # Class instantiation
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, content)
            references.update(matches)
            
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")
    
    return references

def generate_models_from_openapi(schema_path: str, output_dir: str = None):
    """Generate Pydantic models from OpenAPI schema."""
    
    print("🔍 Loading OpenAPI schema...")
    schema = load_openapi_schema(schema_path)
    
    if 'components' not in schema or 'schemas' not in schema['components']:
        print("❌ No schemas found in OpenAPI file")
        return
    
    schemas = schema['components']['schemas']
    print(f"📊 Found {len(schemas)} schemas in OpenAPI file")
    
    print("\n🔍 Analyzing existing models...")
    existing_models = get_existing_models('clio_clients/models')
    print(f"📊 Found {len(existing_models)} existing model files")
    
    # Analyze each existing model
    missing_imports = {}
    unused_models = set(existing_models.keys())
    
    for schema_name, schema_def in schemas.items():
        # Convert OpenAPI schema name to Python class name
        python_name = schema_name.replace('_', '').lower()
        
        if python_name in existing_models:
            unused_models.discard(python_name)
            file_path = existing_models[python_name]
            
            # Extract current imports and references
            current_imports = extract_imports_from_file(file_path)
            class_refs = extract_class_references(file_path)
            
            # Check for missing imports based on schema references
            if isinstance(schema_def, dict):
                missing = find_missing_imports_for_schema(schema_def, current_imports, schemas)
                if missing:
                    missing_imports[python_name] = {
                        'file': file_path,
                        'missing': missing
                    }
    
    # Report findings
    print("\n📋 AUDIT RESULTS:")
    print("=" * 50)
    
    if missing_imports:
        print(f"\n❌ Models with missing imports ({len(missing_imports)}):")
        for model_name, info in missing_imports.items():
            print(f"  📁 {model_name} ({info['file']})")
            for missing in info['missing']:
                print(f"    🔗 Missing: {missing}")
    
    if unused_models:
        print(f"\n⚠️  Models not found in OpenAPI schema ({len(unused_models)}):")
        for model in sorted(unused_models):
            print(f"  📁 {model}")
    
    # Check for schemas without corresponding models
    missing_models = []
    for schema_name in schemas.keys():
        python_name = schema_name.replace('_', '').lower()
        if python_name not in existing_models:
            missing_models.append(schema_name)
    
    if missing_models:
        print(f"\n🆕 OpenAPI schemas without models ({len(missing_models)}):")
        for schema in sorted(missing_models):
            print(f"  📋 {schema}")
    
    return {
        'missing_imports': missing_imports,
        'unused_models': unused_models,
        'missing_models': missing_models,
        'schemas': schemas
    }

def find_missing_imports_for_schema(schema_def: dict, current_imports: Set[str], all_schemas: Dict) -> List[str]:
    """Find missing imports for a schema based on its references."""
    missing = []
    
    def check_ref(obj):
        if isinstance(obj, dict):
            if '$ref' in obj:
                ref_path = obj['$ref']
                if ref_path.startswith('#/components/schemas/'):
                    ref_name = ref_path.split('/')[-1]
                    expected_import = f"clio_clients.models.{ref_name.lower()}.{ref_name}"
                    if expected_import not in current_imports:
                        missing.append(ref_name)
            
            for value in obj.values():
                check_ref(value)
        elif isinstance(obj, list):
            for item in obj:
                check_ref(item)
    
    check_ref(schema_def)
    return missing

def fix_imports_for_model(file_path: str, missing_imports: List[str]) -> str:
    """Generate import statements to fix missing imports."""
    imports_to_add = []
    
    for missing_class in missing_imports:
        # Convert class name to module name (simple heuristic)
        module_name = missing_class.lower().replace('_', '')
        
        # Check if base class exists
        base_file = f"clio_clients/models/{module_name}base.py"
        if os.path.exists(base_file):
            imports_to_add.append(f"from clio_clients.models.{module_name}base import {missing_class}Base")
        
        # Check for regular class file
        class_file = f"clio_clients/models/{module_name}.py"
        if os.path.exists(class_file):
            imports_to_add.append(f"from clio_clients.models.{module_name} import {missing_class}")
    
    return imports_to_add

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--fix":
        print("🔧 FIXING MODE ENABLED")
        fix_mode = True
    else:
        print("🔍 AUDIT MODE (use --fix to apply fixes)")
        fix_mode = False
    
    schema_path = "openapi_sdk.yaml"
    if not os.path.exists(schema_path):
        print(f"❌ OpenAPI schema file not found: {schema_path}")
        return
    
    results = generate_models_from_openapi(schema_path)
    
    if fix_mode and results['missing_imports']:
        print("\n🔧 Applying fixes...")
        
        for model_name, info in results['missing_imports'].items():
            file_path = info['file']
            missing = info['missing']
            
            print(f"  📝 Fixing {model_name}...")
            
            # Generate import statements
            import_statements = fix_imports_for_model(file_path, missing)
            
            if import_statements:
                # Read current file
                with open(file_path, 'r') as f:
                    content = f.read()
                
                # Find where to insert imports (after existing imports)
                lines = content.split('\n')
                insert_index = 0
                
                for i, line in enumerate(lines):
                    if line.strip().startswith('from ') or line.strip().startswith('import '):
                        insert_index = i + 1
                    elif line.strip() and not line.strip().startswith('#'):
                        break
                
                # Insert new imports
                for import_stmt in import_statements:
                    lines.insert(insert_index, import_stmt)
                    insert_index += 1
                
                # Write back to file
                with open(file_path, 'w') as f:
                    f.write('\n'.join(lines))
                
                print(f"    ✅ Added {len(import_statements)} imports")
            else:
                print(f"    ⚠️  Could not determine imports to add")
    
    print("\n🎉 Audit complete!")

if __name__ == "__main__":
    main()
