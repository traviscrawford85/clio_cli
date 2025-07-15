#!/usr/bin/env python3
"""
Model Custodian Setup Script

This script helps you set up the Model Custodian system in a new project.
It will copy the necessary files and help configure them for your project.

Usage:
    python setup_model_custodian.py --target /path/to/your/project
    python setup_model_custodian.py --target /path/to/your/project --framework fastapi
"""

import argparse
import shutil
import os
from pathlib import Path
import sys

def copy_model_custodian_files(source_dir: Path, target_dir: Path, framework: str = "generic"):
    """Copy Model Custodian files to target project."""
    
    # Files to copy
    files_to_copy = [
        "model_custodian_config.py",
        "portable_manage_models.py", 
        "audit_models_simple.py"  # If it exists
    ]
    
    # Optional files
    optional_files = [
        "MODEL_CUSTODIAN_GUIDE.md",
        "MODEL_CUSTODIAN_PORTABLE_GUIDE.md"
    ]
    
    print(f"📁 Setting up Model Custodian in: {target_dir}")
    
    # Ensure target directory exists
    target_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy core files
    copied_files = []
    for file_name in files_to_copy:
        source_file = source_dir / file_name
        target_file = target_dir / file_name
        
        if source_file.exists():
            shutil.copy2(source_file, target_file)
            copied_files.append(file_name)
            print(f"✅ Copied: {file_name}")
        else:
            print(f"⚠️  File not found: {file_name}")
    
    # Copy optional files
    for file_name in optional_files:
        source_file = source_dir / file_name
        target_file = target_dir / file_name
        
        if source_file.exists():
            shutil.copy2(source_file, target_file)
            print(f"📋 Copied documentation: {file_name}")
    
    # Copy GitHub workflow if .github directory exists or can be created
    github_dir = target_dir / ".github" / "workflows"
    if github_dir.exists() or create_github_workflow(source_dir, target_dir):
        workflow_source = source_dir / ".github" / "workflows" / "model_custodian.yml"
        workflow_target = github_dir / "model_custodian.yml"
        
        if workflow_source.exists():
            github_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(workflow_source, workflow_target)
            print(f"🔄 Copied GitHub workflow: model_custodian.yml")
    
    return copied_files

def create_github_workflow(source_dir: Path, target_dir: Path) -> bool:
    """Ask user if they want to set up GitHub Actions."""
    response = input("🤖 Set up GitHub Actions workflow? (y/n): ").lower().strip()
    return response in ['y', 'yes']

def update_config_for_framework(target_dir: Path, framework: str, project_name: str):
    """Update configuration for specific framework."""
    config_file = target_dir / "model_custodian_config.py"
    
    if not config_file.exists():
        print("❌ Configuration file not found")
        return
    
    # Read current config
    with open(config_file, 'r') as f:
        content = f.read()
    
    # Framework-specific replacements
    replacements = {
        "django": {
            "clio_clients/models": f"{project_name}/models",
            "openapi_sdk.yaml": "schema/openapi.yaml", 
            "clio_clients": project_name
        },
        "fastapi": {
            "clio_clients/models": "app/models",
            "openapi_sdk.yaml": "docs/openapi.json",
            "clio_clients": "app"
        },
        "flask": {
            "clio_clients/models": f"{project_name}/models",
            "openapi_sdk.yaml": "api/openapi.yaml",
            "clio_clients": project_name
        },
        "generic": {
            "clio_clients/models": f"{project_name}/models",
            "openapi_sdk.yaml": "openapi.yaml",
            "clio_clients": project_name
        }
    }
    
    if framework in replacements:
        for old, new in replacements[framework].items():
            content = content.replace(f'"{old}"', f'"{new}"')
        
        # Write updated config
        with open(config_file, 'w') as f:
            f.write(content)
        
        print(f"🔧 Updated configuration for {framework}")
    else:
        print(f"⚠️  Unknown framework: {framework}")

def create_requirements_section(target_dir: Path):
    """Add Model Custodian dependencies to requirements.txt."""
    requirements_file = target_dir / "requirements.txt"
    
    dependencies = [
        "# Model Custodian dependencies",
        "pydantic>=2.0.0",
        "pyyaml>=6.0", 
        "mypy>=1.0.0",
        "openapi-schemas-pydantic>=3.0.0"
    ]
    
    if requirements_file.exists():
        with open(requirements_file, 'r') as f:
            existing = f.read()
        
        # Check if dependencies already exist
        if "openapi-schemas-pydantic" in existing:
            print("📦 Dependencies already present in requirements.txt")
            return
        
        # Append dependencies
        with open(requirements_file, 'a') as f:
            f.write("\n\n" + "\n".join(dependencies))
        print("📦 Added dependencies to existing requirements.txt")
    else:
        # Create new requirements.txt
        with open(requirements_file, 'w') as f:
            f.write("\n".join(dependencies))
        print("📦 Created requirements.txt with dependencies")

def create_example_usage(target_dir: Path, project_name: str, framework: str):
    """Create example usage script."""
    
    example_content = f'''#!/usr/bin/env python3
"""
Example usage of Model Custodian for {project_name}

This script shows how to use the Model Custodian system in your project.
"""

from model_custodian_config import get_config
from portable_manage_models import PortableModelCustodian

def main():
    # Get configuration for {framework}
    config = get_config("{framework}")
    
    # Print current configuration
    config.print_config_summary()
    
    # Initialize custodian
    custodian = PortableModelCustodian(config)
    
    # Run audit
    print("\\n🔍 Running audit...")
    results = custodian.audit_models()
    
    print(f"📊 Results:")
    print(f"  OpenAPI schemas: {{results.get('openapi_schemas', 0)}}")
    print(f"  Existing models: {{results.get('existing_models', 0)}}")
    print(f"  Import errors: {{results.get('import_errors', 0)}}")

if __name__ == "__main__":
    main()
'''
    
    example_file = target_dir / "example_model_custodian.py"
    with open(example_file, 'w') as f:
        f.write(example_content)
    
    print(f"📋 Created example usage: example_model_custodian.py")

def main():
    parser = argparse.ArgumentParser(description="Set up Model Custodian in a new project")
    parser.add_argument('--target', required=True, help='Target project directory')
    parser.add_argument('--framework', choices=['django', 'fastapi', 'flask', 'generic'], 
                       default='generic', help='Framework preset')
    parser.add_argument('--project-name', help='Project name (auto-detected if not provided)')
    
    args = parser.parse_args()
    
    # Paths
    source_dir = Path(__file__).parent
    target_dir = Path(args.target)
    
    # Auto-detect project name
    project_name = args.project_name or target_dir.name
    
    print(f"🚀 Setting up Model Custodian")
    print(f"📁 Source: {source_dir}")
    print(f"📁 Target: {target_dir}")
    print(f"🏗️  Framework: {args.framework}")
    print(f"📋 Project: {project_name}")
    
    if not target_dir.exists():
        print(f"❌ Target directory does not exist: {target_dir}")
        sys.exit(1)
    
    # Copy files
    copied_files = copy_model_custodian_files(source_dir, target_dir, args.framework)
    
    if not copied_files:
        print("❌ No files were copied. Check source directory.")
        sys.exit(1)
    
    # Update configuration
    update_config_for_framework(target_dir, args.framework, project_name)
    
    # Handle dependencies
    create_requirements_section(target_dir)
    
    # Create example
    create_example_usage(target_dir, project_name, args.framework)
    
    print(f"\n✅ Model Custodian setup complete!")
    print(f"\n🚀 Next steps:")
    print(f"1. cd {target_dir}")
    print(f"2. pip install -r requirements.txt")
    print(f"3. python portable_manage_models.py config")
    print(f"4. python portable_manage_models.py audit")
    print(f"5. Review and customize model_custodian_config.py")
    
    if (target_dir / ".github" / "workflows" / "model_custodian.yml").exists():
        print(f"6. Commit and push to activate GitHub Actions")

if __name__ == "__main__":
    main()
