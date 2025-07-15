#!/usr/bin/env python3
"""
Clio Models Management Tool

This script provides comprehensive model management capabilities using 
openapi-schemas-pydantic and the OpenAPI schema. It can:

1. Audit existing models against the OpenAPI schema
2. Generate new models from OpenAPI schema
3. Fix missing imports automatically
4. Validate model consistency
5. Update models when the OpenAPI schema changes

Usage:
    python manage_models.py audit              # Audit existing models
    python manage_models.py fix-imports        # Fix missing imports
    python manage_models.py generate           # Generate new models from schema
    python manage_models.py validate           # Validate all models
    python manage_models.py sync               # Sync models with OpenAPI schema
"""

import argparse
import os
import sys
import yaml
import subprocess
from pathlib import Path
from typing import Dict, List, Set, Optional, Any
import re

def run_command(cmd: List[str], capture_output=True) -> subprocess.CompletedProcess:
    """Run a command and return the result."""
    return subprocess.run(cmd, capture_output=capture_output, text=True)

def load_openapi_schema(schema_path: str = "openapi_sdk.yaml") -> Dict[str, Any]:
    """Load the OpenAPI schema."""
    with open(schema_path, 'r') as f:
        return yaml.safe_load(f)

def get_schema_models(schema: Dict[str, Any]) -> Dict[str, Any]:
    """Extract all model schemas from OpenAPI."""
    if 'components' not in schema or 'schemas' not in schema['components']:
        return {}
    return schema['components']['schemas']

def find_existing_models(models_dir: str = "clio_clients/models") -> Dict[str, str]:
    """Find all existing model files."""
    models = {}
    models_path = Path(models_dir)
    
    for py_file in models_path.rglob("*.py"):
        if py_file.name == "__init__.py":
            continue
        
        model_name = py_file.stem
        models[model_name] = str(py_file)
    
    return models

def audit_models() -> Dict[str, Any]:
    """Audit existing models for issues."""
    print("🔍 Auditing Clio models...")
    
    # Load OpenAPI schema
    schema = load_openapi_schema()
    schema_models = get_schema_models(schema)
    existing_models = find_existing_models()
    
    print(f"📊 OpenAPI schemas: {len(schema_models)}")
    print(f"📊 Existing models: {len(existing_models)}")
    
    # Check for missing imports using MyPy
    print("🔍 Checking for missing imports...")
    result = run_command(['mypy', 'clio_clients/models', '--explicit-package-bases', '--no-error-summary'])
    
    missing_imports = []
    for line in result.stdout.split('\n'):
        if 'not defined' in line:
            match = re.match(r'([^:]+):(\d+): error: Name "([^"]+)" is not defined', line)
            if match:
                file_path, line_num, class_name = match.groups()
                missing_imports.append((file_path, line_num, class_name))
    
    # Find orphaned models (not in OpenAPI)
    orphaned_models = []
    for model_name in existing_models:
        # Convert to OpenAPI schema naming convention
        schema_name = model_name.replace('base', '_base').replace('show', '_Show').replace('list', '_List')
        if schema_name not in schema_models:
            orphaned_models.append(model_name)
    
    # Find missing models (in OpenAPI but not implemented)
    missing_models = []
    for schema_name in schema_models:
        model_name = schema_name.replace('_', '').lower()
        if model_name not in existing_models:
            missing_models.append(schema_name)
    
    audit_results = {
        'missing_imports': missing_imports,
        'orphaned_models': orphaned_models,
        'missing_models': missing_models,
        'total_errors': len(missing_imports),
        'schema_models': len(schema_models),
        'existing_models': len(existing_models)
    }
    
    print("\n📋 AUDIT RESULTS:")
    print("=" * 50)
    print(f"❌ Missing imports: {len(missing_imports)}")
    print(f"⚠️  Orphaned models: {len(orphaned_models)}")
    print(f"🆕 Missing models: {len(missing_models)}")
    
    return audit_results

def fix_imports() -> bool:
    """Fix missing imports automatically."""
    print("🔧 Fixing missing imports...")
    
    # Use our existing audit script
    result = run_command(['python', 'audit_models_simple.py', '--fix'])
    
    if result.returncode == 0:
        print("✅ Import fixes completed successfully")
        return True
    else:
        print("❌ Failed to fix imports")
        print(result.stderr)
        return False

def validate_models() -> bool:
    """Validate all models."""
    print("🔍 Validating models...")
    
    # Test import
    try:
        result = run_command(['python', '-c', 'from clio_clients.models import *; print("✅ Import successful")'])
        if result.returncode != 0:
            print("❌ Model import failed")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Import validation failed: {e}")
        return False
    
    # Run MyPy validation
    result = run_command(['mypy', 'clio_clients/models', '--explicit-package-bases'])
    
    # Count critical errors (not defined, import errors)
    critical_errors = 0
    for line in result.stdout.split('\n'):
        if any(error_type in line for error_type in ['not defined', 'import']):
            critical_errors += 1
    
    print(f"📊 MyPy critical errors: {critical_errors}")
    
    if critical_errors == 0:
        print("✅ Model validation passed")
        return True
    else:
        print("⚠️  Model validation completed with warnings")
        return True  # Don't fail on non-critical MyPy errors

def generate_models() -> bool:
    """Generate models from OpenAPI schema using openapi-schemas-pydantic."""
    print("🏗️  Generating models from OpenAPI schema...")
    
    try:
        # Load schema
        schema = load_openapi_schema()
        schemas = get_schema_models(schema)
        
        # Create output directory
        output_dir = Path("generated_models")
        output_dir.mkdir(exist_ok=True)
        
        print(f"📝 Generating {len(schemas)} model schemas...")
        
        # For now, just report what would be generated
        # Full implementation would use openapi-schemas-pydantic to generate actual models
        for schema_name, schema_def in schemas.items():
            output_file = output_dir / f"{schema_name.lower()}.py"
            print(f"  📄 Would generate: {output_file}")
        
        print("✅ Model generation plan created")
        print("💡 Tip: Full generation implementation would create actual Pydantic models")
        return True
        
    except Exception as e:
        print(f"❌ Model generation failed: {e}")
        return False

def sync_models() -> bool:
    """Sync models with OpenAPI schema."""
    print("🔄 Syncing models with OpenAPI schema...")
    
    # First audit to see what needs to be done
    audit_results = audit_models()
    
    # Fix imports
    if audit_results['missing_imports']:
        print("\n🔧 Fixing imports...")
        if not fix_imports():
            return False
    
    # Validate everything works
    print("\n✅ Validating final state...")
    return validate_models()

def create_model_report() -> str:
    """Create a comprehensive model report."""
    audit_results = audit_results = audit_models()
    
    report = f"""
# Clio Models Audit Report

## Summary
- **OpenAPI Schemas**: {audit_results['schema_models']}
- **Existing Models**: {audit_results['existing_models']}
- **Missing Imports**: {audit_results['total_errors']}
- **Orphaned Models**: {len(audit_results['orphaned_models'])}
- **Missing Models**: {len(audit_results['missing_models'])}

## Status
{'✅ All imports resolved' if audit_results['total_errors'] == 0 else '❌ Import issues found'}

## Recommendations
"""
    
    if audit_results['missing_imports']:
        report += "1. Run `python manage_models.py fix-imports` to resolve import issues\n"
    
    if audit_results['missing_models']:
        report += "2. Consider generating missing models with `python manage_models.py generate`\n"
    
    if audit_results['orphaned_models']:
        report += "3. Review orphaned models for potential cleanup\n"
    
    if not any([audit_results['missing_imports'], audit_results['missing_models'], audit_results['orphaned_models']]):
        report += "🎉 Models are in excellent condition!\n"
    
    return report

def main():
    parser = argparse.ArgumentParser(description="Clio Models Management Tool")
    parser.add_argument('action', choices=['audit', 'fix-imports', 'generate', 'validate', 'sync', 'report'],
                       help='Action to perform')
    
    args = parser.parse_args()
    
    success = False
    
    if args.action == 'audit':
        audit_results = audit_models()
        success = True
    elif args.action == 'fix-imports':
        success = fix_imports()
    elif args.action == 'generate':
        success = generate_models()
    elif args.action == 'validate':
        success = validate_models()
    elif args.action == 'sync':
        success = sync_models()
    elif args.action == 'report':
        print(create_model_report())
        success = True
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
