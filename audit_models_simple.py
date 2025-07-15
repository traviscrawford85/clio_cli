#!/usr/bin/env python3
"""
Simple audit script for Clio models to find missing imports.

This script analyzes the existing model files and identifies missing imports
based on MyPy errors and class references.
"""

import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple

def run_mypy_and_extract_errors() -> List[Tuple[str, str, str]]:
    """Run MyPy and extract 'not defined' errors."""
    print("🔍 Running MyPy to identify missing imports...")
    
    try:
        # Run mypy and capture output
        result = subprocess.run([
            'mypy', 
            'clio_clients/models', 
            '--explicit-package-bases',
            '--no-error-summary'
        ], capture_output=True, text=True, cwd='.')
        
        errors = []
        for line in result.stdout.split('\n'):
            if 'not defined' in line:
                # Parse mypy error line
                # Format: file:line: error: Name "ClassName" is not defined  [name-defined]
                match = re.match(r'([^:]+):(\d+): error: Name "([^"]+)" is not defined', line)
                if match:
                    file_path, line_num, class_name = match.groups()
                    errors.append((file_path, line_num, class_name))
        
        print(f"📊 Found {len(errors)} 'not defined' errors")
        return errors
        
    except Exception as e:
        print(f"❌ Error running MyPy: {e}")
        return []

def find_class_definition_file(class_name: str, models_dir: str = 'clio_clients/models') -> str:
    """Find which file defines a class."""
    
    # Common patterns for finding class definitions
    patterns_to_try = [
        f"{class_name.lower()}.py",
        f"{class_name.lower()}base.py", 
        f"{class_name.lower()}show.py",
        f"{class_name.lower()}list.py",
    ]
    
    # Also try subdirectories
    models_path = Path(models_dir)
    
    for pattern in patterns_to_try:
        # Check in root models directory
        file_path = models_path / pattern
        if file_path.exists():
            # Verify the class is actually defined in this file
            if class_defined_in_file(str(file_path), class_name):
                return str(file_path)
        
        # Check in subdirectories
        for subdir in models_path.iterdir():
            if subdir.is_dir() and subdir.name != '__pycache__':
                sub_file_path = subdir / pattern
                if sub_file_path.exists():
                    if class_defined_in_file(str(sub_file_path), class_name):
                        return str(sub_file_path)
    
    return None

def class_defined_in_file(file_path: str, class_name: str) -> bool:
    """Check if a class is defined in a file."""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Look for class definition
        pattern = rf'class\s+{class_name}\s*[\(:]'
        return bool(re.search(pattern, content))
    except:
        return False

def get_import_statement(class_name: str, definition_file: str) -> str:
    """Generate the import statement for a class."""
    
    # Convert file path to module path
    # e.g., clio_clients/models/activitybase.py -> clio_clients.models.activitybase
    module_path = definition_file.replace('/', '.').replace('.py', '')
    
    return f"from {module_path} import {class_name}"

def get_current_imports(file_path: str) -> Set[str]:
    """Get all current import statements from a file."""
    imports = set()
    try:
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith('from ') and ' import ' in line:
                    imports.add(line)
    except:
        pass
    return imports

def add_import_to_file(file_path: str, import_statement: str) -> bool:
    """Add an import statement to a file."""
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
        
        # Find where to insert the import (after existing imports)
        insert_index = 0
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith('from ') or stripped.startswith('import '):
                insert_index = i + 1
            elif stripped and not stripped.startswith('#'):
                break
        
        # Insert the new import
        lines.insert(insert_index, import_statement + '\n')
        
        # Write back to file
        with open(file_path, 'w') as f:
            f.writelines(lines)
        
        return True
    except Exception as e:
        print(f"❌ Error adding import to {file_path}: {e}")
        return False

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--fix":
        print("🔧 FIX MODE ENABLED")
        fix_mode = True
    else:
        print("🔍 AUDIT MODE (use --fix to apply fixes)")
        fix_mode = False
    
    # Get MyPy errors
    errors = run_mypy_and_extract_errors()
    
    if not errors:
        print("✅ No 'not defined' errors found!")
        return
    
    fixes_applied = 0
    fixes_failed = 0
    
    print("\n📋 ANALYSIS RESULTS:")
    print("=" * 60)
    
    # Group errors by file
    errors_by_file = {}
    for file_path, line_num, class_name in errors:
        if file_path not in errors_by_file:
            errors_by_file[file_path] = []
        errors_by_file[file_path].append((line_num, class_name))
    
    for file_path, file_errors in errors_by_file.items():
        print(f"\n📁 {file_path}")
        
        current_imports = get_current_imports(file_path)
        
        for line_num, class_name in file_errors:
            print(f"  Line {line_num}: Missing '{class_name}'")
            
            # Find where the class is defined
            definition_file = find_class_definition_file(class_name)
            
            if definition_file:
                import_statement = get_import_statement(class_name, definition_file)
                print(f"    📍 Found in: {definition_file}")
                print(f"    🔗 Import: {import_statement}")
                
                if fix_mode:
                    if import_statement not in current_imports:
                        if add_import_to_file(file_path, import_statement):
                            print(f"    ✅ Added import")
                            fixes_applied += 1
                        else:
                            print(f"    ❌ Failed to add import")
                            fixes_failed += 1
                    else:
                        print(f"    ⚠️  Import already exists")
                        
            else:
                print(f"    ❌ Class definition not found")
                fixes_failed += 1
    
    print(f"\n🎉 SUMMARY:")
    print(f"   📊 Total errors: {len(errors)}")
    
    if fix_mode:
        print(f"   ✅ Fixes applied: {fixes_applied}")
        print(f"   ❌ Fixes failed: {fixes_failed}")
        
        if fixes_applied > 0:
            print(f"\n🔄 Re-running MyPy to verify fixes...")
            remaining_errors = run_mypy_and_extract_errors()
            print(f"   📉 Remaining errors: {len(remaining_errors)}")

if __name__ == "__main__":
    main()
