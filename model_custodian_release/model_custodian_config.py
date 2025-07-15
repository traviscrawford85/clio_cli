#!/usr/bin/env python3
"""
Portable Model Custodian Configuration

This file contains all project-specific settings for the Model Custodian system.
Modify these values to adapt the system to your project.
"""

import os
from pathlib import Path
from typing import Dict, List, Optional

class ModelCustodianConfig:
    """Configuration class for Model Custodian system."""
    
    def __init__(self, project_root: Optional[str] = None):
        self.project_root = Path(project_root or os.getcwd())
        
    # ============================================================================
    # PROJECT-SPECIFIC SETTINGS (MODIFY THESE FOR YOUR PROJECT)
    # ============================================================================
    
    @property
    def models_directory(self) -> str:
        """Directory containing your Pydantic models."""
        return "clio_clients/models"  # CHANGE THIS: e.g., "myapp/models"
    
    @property
    def openapi_schema_path(self) -> str:
        """Path to your OpenAPI schema file."""
        return "openapi_sdk.yaml"  # CHANGE THIS: e.g., "docs/openapi.yaml"
    
    @property
    def project_module_name(self) -> str:
        """Your project's main module name for imports."""
        return "clio_clients"  # CHANGE THIS: e.g., "myapp"
    
    @property
    def python_version(self) -> str:
        """Python version for CI/CD."""
        return "3.10"  # CHANGE THIS: e.g., "3.11"
    
    @property
    def additional_dependencies(self) -> List[str]:
        """Additional packages needed for your project."""
        return [
            "pydantic>=2.0.0",
            "pyyaml>=6.0",
            "mypy>=1.0.0", 
            "openapi-schemas-pydantic>=3.0.0"
        ]
    
    # ============================================================================
    # DERIVED SETTINGS (USUALLY DON'T NEED TO CHANGE)
    # ============================================================================
    
    @property
    def models_path(self) -> Path:
        """Full path to models directory."""
        return self.project_root / self.models_directory
    
    @property
    def schema_path(self) -> Path:
        """Full path to OpenAPI schema."""
        return self.project_root / self.openapi_schema_path
    
    @property
    def import_base_pattern(self) -> str:
        """Base pattern for import statements."""
        return f"from {self.project_module_name}.models"
    
    @property
    def import_regex_pattern(self) -> str:
        """Regex pattern for detecting imports."""
        module_escaped = self.project_module_name.replace("_", r"\_")
        return rf"from {module_escaped}\.models\.(\w+) import"
    
    def get_model_import(self, model_name: str, submodule: str = None) -> str:
        """Generate import statement for a model."""
        if submodule:
            return f"from {self.project_module_name}.models.{submodule} import {model_name}"
        else:
            return f"from {self.project_module_name}.models.{model_name.lower()} import {model_name}"
    
    def validate_config(self) -> Dict[str, bool]:
        """Validate that all required files and directories exist."""
        validation = {}
        
        validation["models_directory_exists"] = self.models_path.exists()
        validation["schema_file_exists"] = self.schema_path.exists()
        validation["models_directory_is_package"] = (self.models_path / "__init__.py").exists()
        
        return validation
    
    def print_config_summary(self):
        """Print current configuration for verification."""
        print("🔧 Model Custodian Configuration")
        print("=" * 50)
        print(f"📁 Project Root: {self.project_root}")
        print(f"📁 Models Directory: {self.models_directory}")
        print(f"📄 OpenAPI Schema: {self.openapi_schema_path}")
        print(f"🐍 Project Module: {self.project_module_name}")
        print(f"🐍 Python Version: {self.python_version}")
        print(f"📦 Dependencies: {len(self.additional_dependencies)} packages")
        
        validation = self.validate_config()
        print(f"\n✅ Validation Results:")
        for check, passed in validation.items():
            status = "✅" if passed else "❌"
            print(f"  {status} {check.replace('_', ' ').title()}")
        
        if not all(validation.values()):
            print(f"\n⚠️  Some validation checks failed. Please verify your configuration.")

# ============================================================================
# PRESET CONFIGURATIONS FOR COMMON FRAMEWORKS
# ============================================================================

class DjangoConfig(ModelCustodianConfig):
    """Preset for Django projects."""
    
    @property
    def models_directory(self) -> str:
        return "myapp/models"  # Update 'myapp' to your Django app name
    
    @property
    def openapi_schema_path(self) -> str:
        return "schema/openapi.yaml"
    
    @property
    def project_module_name(self) -> str:
        return "myapp"  # Update to your Django app name

class FastAPIConfig(ModelCustodianConfig):
    """Preset for FastAPI projects."""
    
    @property
    def models_directory(self) -> str:
        return "app/models"
    
    @property
    def openapi_schema_path(self) -> str:
        return "docs/openapi.json"  # FastAPI auto-generates
    
    @property
    def project_module_name(self) -> str:
        return "app"

class FlaskConfig(ModelCustodianConfig):
    """Preset for Flask projects."""
    
    @property
    def models_directory(self) -> str:
        return "myflaskapp/models"
    
    @property
    def openapi_schema_path(self) -> str:
        return "api/openapi.yaml"
    
    @property
    def project_module_name(self) -> str:
        return "myflaskapp"

# ============================================================================
# CONFIGURATION FACTORY
# ============================================================================

def get_config(framework: str = "generic", project_root: str = None) -> ModelCustodianConfig:
    """Get configuration for a specific framework."""
    configs = {
        "django": DjangoConfig,
        "fastapi": FastAPIConfig,
        "flask": FlaskConfig,
        "generic": ModelCustodianConfig
    }
    
    config_class = configs.get(framework, ModelCustodianConfig)
    return config_class(project_root)

# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    # Test the configuration
    config = ModelCustodianConfig()
    config.print_config_summary()
    
    print("\n" + "=" * 50)
    print("🚀 Framework Presets Available:")
    for framework in ["django", "fastapi", "flask"]:
        print(f"  📋 {framework}: get_config('{framework}')")
