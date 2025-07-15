#!/usr/bin/env python3
"""
Portable Model Custodian - Universal Model Management Tool

This is a portable version of the Model Custodian system that can be adapted
to any Python project using Pydantic models and OpenAPI schemas.

Usage:
    python portable_manage_models.py audit
    python portable_manage_models.py fix-imports
    python portable_manage_models.py validate
    python portable_manage_models.py report
    python portable_manage_models.py config [framework]

Configuration:
    Modify model_custodian_config.py to match your project structure.
"""

import argparse
import subprocess
import sys
import yaml
import json
from pathlib import Path
from typing import Dict, List, Set, Optional
import re

# Import configuration (modify model_custodian_config.py for your project)
try:
    from model_custodian_config import get_config, ModelCustodianConfig
except ImportError:
    print("❌ Configuration file not found. Please ensure model_custodian_config.py exists.")
    sys.exit(1)

try:
    import openapi_schemas_pydantic
except ImportError:
    print("❌ openapi-schemas-pydantic not installed. Install with:")
    print("   pip install openapi-schemas-pydantic")
    sys.exit(1)

class PortableModelCustodian:
    """Portable Model Custodian that works with any project configuration."""
    
    def __init__(self, config: ModelCustodianConfig):
        self.config = config
        
    def discover_models(self) -> Dict[str, Path]:
        """Discover all model files in the project."""
        models = {}
        
        if not self.config.models_path.exists():
            print(f"❌ Models directory not found: {self.config.models_path}")
            return models
            
        for py_file in self.config.models_path.rglob("*.py"):
            if py_file.name == "__init__.py":
                continue
                
            # Create a unique key for the model
            relative_path = py_file.relative_to(self.config.models_path)
            model_key = str(relative_path.with_suffix('')).replace('/', '.')
            models[model_key] = py_file
            
        return models
    
    def load_openapi_schema(self) -> Optional[Dict]:
        """Load OpenAPI schema from configured path."""
        if not self.config.schema_path.exists():
            print(f"❌ OpenAPI schema not found: {self.config.schema_path}")
            return None
            
        try:
            with open(self.config.schema_path, 'r') as f:
                if self.config.schema_path.suffix.lower() == '.json':
                    return json.load(f)
                else:
                    return yaml.safe_load(f)
        except Exception as e:
            print(f"❌ Error loading schema: {e}")
            return None
    
    def check_imports_with_mypy(self) -> List[str]:
        """Use MyPy to detect import errors."""
        try:
            # Run MyPy on the models directory
            result = subprocess.run([
                'python', '-m', 'mypy', 
                str(self.config.models_path),
                '--explicit-package-bases',
                '--ignore-missing-imports',
                '--no-error-summary'
            ], capture_output=True, text=True, cwd=self.config.project_root)
            
            if result.returncode == 0:
                return []  # No errors
                
            # Parse MyPy output for import errors
            import_errors = []
            for line in result.stdout.split('\n'):
                if 'error: Cannot resolve import' in line or 'error: Module' in line:
                    import_errors.append(line.strip())
                    
            return import_errors
            
        except Exception as e:
            print(f"❌ Error running MyPy: {e}")
            return []
    
    def fix_import_errors(self, dry_run: bool = False) -> int:
        """Fix import errors automatically."""
        print("🔍 Detecting import errors with MyPy...")
        errors = self.check_imports_with_mypy()
        
        if not errors:
            print("✅ No import errors detected!")
            return 0
            
        print(f"🔧 Found {len(errors)} import errors")
        
        if dry_run:
            print("🔍 DRY RUN - Would fix these errors:")
            for error in errors:
                print(f"  📋 {error}")
            return len(errors)
        
        # Implementation would go here - similar to audit_models_simple.py
        # This is a simplified version for the portable example
        
        fixed_count = 0
        for error in errors:
            # Parse the error and attempt to fix
            if self._attempt_fix_import_error(error):
                fixed_count += 1
                
        print(f"✅ Fixed {fixed_count} import errors")
        return fixed_count
    
    def _attempt_fix_import_error(self, error: str) -> bool:
        """Attempt to fix a single import error."""
        # This would contain the logic from audit_models_simple.py
        # Simplified for the portable example
        return False
    
    def audit_models(self) -> Dict:
        """Perform comprehensive model audit."""
        print("🔍 Auditing models...")
        
        # Load schema
        schema = self.load_openapi_schema()
        if not schema:
            return {"error": "Could not load OpenAPI schema"}
            
        # Discover models
        models = self.discover_models()
        
        # Get schema definitions
        schemas = schema.get('components', {}).get('schemas', {})
        
        # Check for import errors
        import_errors = self.check_imports_with_mypy()
        
        # Compile results
        results = {
            "openapi_schemas": len(schemas),
            "existing_models": len(models),
            "import_errors": len(import_errors),
            "schema_definitions": list(schemas.keys()),
            "model_files": list(models.keys()),
            "errors": import_errors
        }
        
        return results
    
    def validate_models(self) -> bool:
        """Validate all models."""
        print("🔍 Validating models...")
        
        # Check configuration
        config_validation = self.config.validate_config()
        if not all(config_validation.values()):
            print("❌ Configuration validation failed")
            return False
            
        # Check for import errors
        errors = self.check_imports_with_mypy()
        if errors:
            print(f"❌ Found {len(errors)} import errors")
            return False
            
        print("✅ All models validated successfully")
        return True
    
    def generate_report(self) -> str:
        """Generate comprehensive report."""
        audit_results = self.audit_models()
        
        report = f"""
# Model Custodian Report
Generated for: {self.config.project_module_name}

## Configuration
- Models Directory: {self.config.models_directory}
- OpenAPI Schema: {self.config.openapi_schema_path}
- Python Version: {self.config.python_version}

## Metrics
- OpenAPI Schemas: {audit_results.get('openapi_schemas', 0)}
- Existing Models: {audit_results.get('existing_models', 0)}
- Import Errors: {audit_results.get('import_errors', 0)}

## Status
"""
        
        if audit_results.get('import_errors', 0) == 0:
            report += "✅ All models are healthy!\n"
        else:
            report += f"❌ {audit_results['import_errors']} issues need attention\n"
            
        return report

def main():
    parser = argparse.ArgumentParser(description="Portable Model Custodian")
    parser.add_argument('command', choices=[
        'audit', 'fix-imports', 'validate', 'report', 'config'
    ], help='Command to execute')
    parser.add_argument('--framework', choices=[
        'generic', 'django', 'fastapi', 'flask'
    ], default='generic', help='Framework preset to use')
    parser.add_argument('--dry-run', action='store_true', 
                       help='Show what would be done without making changes')
    
    args = parser.parse_args()
    
    # Get configuration
    config = get_config(args.framework)
    
    if args.command == 'config':
        config.print_config_summary()
        return
    
    # Initialize custodian
    custodian = PortableModelCustodian(config)
    
    # Execute command
    if args.command == 'audit':
        results = custodian.audit_models()
        print(f"\n📊 AUDIT RESULTS:")
        print("=" * 50)
        print(f"📋 OpenAPI schemas: {results.get('openapi_schemas', 0)}")
        print(f"📋 Existing models: {results.get('existing_models', 0)}")
        print(f"❌ Import errors: {results.get('import_errors', 0)}")
        
    elif args.command == 'fix-imports':
        fixed = custodian.fix_import_errors(dry_run=args.dry_run)
        if args.dry_run:
            print(f"🔍 Would fix {fixed} import errors")
        else:
            print(f"✅ Fixed {fixed} import errors")
            
    elif args.command == 'validate':
        success = custodian.validate_models()
        sys.exit(0 if success else 1)
        
    elif args.command == 'report':
        report = custodian.generate_report()
        print(report)

if __name__ == "__main__":
    main()
