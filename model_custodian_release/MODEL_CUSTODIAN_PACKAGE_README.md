# Model Custodian - Portable Package

A portable, framework-agnostic model management system for Python projects using Pydantic models and OpenAPI schemas.

## Quick Start

### 1. Copy to Your Project

```bash
# Download the Model Custodian files
curl -O https://raw.githubusercontent.com/your-repo/model-custodian/main/setup_model_custodian.py

# Set up in your project
python setup_model_custodian.py --target /path/to/your/project --framework fastapi
```

### 2. Manual Installation

Copy these files to your project:
- `model_custodian_config.py` - Configuration
- `portable_manage_models.py` - Main management tool
- `audit_models_simple.py` - Import fixer (optional)
- `.github/workflows/model_custodian.yml` - CI/CD workflow

### 3. Configure for Your Project

Edit `model_custodian_config.py`:

```python
@property
def models_directory(self) -> str:
    return "your_app/models"  # Your models directory

@property
def openapi_schema_path(self) -> str:
    return "docs/openapi.yaml"  # Your OpenAPI schema

@property
def project_module_name(self) -> str:
    return "your_app"  # Your project module
```

## Usage

```bash
# Check model health
python portable_manage_models.py audit

# Fix import issues
python portable_manage_models.py fix-imports

# Validate all models
python portable_manage_models.py validate

# Generate report
python portable_manage_models.py report

# View current config
python portable_manage_models.py config
```

## Framework Support

### FastAPI
```bash
python portable_manage_models.py config --framework fastapi
```

### Django
```bash
python portable_manage_models.py config --framework django
```

### Flask
```bash
python portable_manage_models.py config --framework flask
```

### Generic
```bash
python portable_manage_models.py config --framework generic
```

## Dependencies

Add to your `requirements.txt`:
```
pydantic>=2.0.0
pyyaml>=6.0
mypy>=1.0.0
openapi-schemas-pydantic>=3.0.0
```

## Features

- ✅ **Universal Compatibility**: Works with any Python project
- 🔧 **Auto-Import Fixing**: Automatically resolves missing imports
- 📊 **Health Monitoring**: Comprehensive model health reports
- 🤖 **CI/CD Integration**: GitHub Actions workflow included
- 🎯 **Framework Presets**: Pre-configured for popular frameworks
- 📋 **Zero Configuration**: Works out of the box with sensible defaults

## GitHub Actions Integration

The included workflow provides:
- **Push Validation**: Every commit validates models
- **Auto-Fix**: Commits with `[fix-imports]` automatically fix issues
- **Scheduled Reports**: Weekly model health analysis
- **Artifact Storage**: Historical audit reports

## Example Project Structure

```
your_project/
├── your_app/
│   └── models/
│       ├── __init__.py
│       ├── user.py
│       └── order.py
├── docs/
│   └── openapi.yaml
├── model_custodian_config.py
├── portable_manage_models.py
└── requirements.txt
```

## Success Metrics

- **Zero Import Errors**: All models import successfully
- **Automated Validation**: Every push is validated
- **Self-Healing**: Import issues resolve automatically
- **Comprehensive Reporting**: Detailed health metrics
- **CI/CD Ready**: Seamless workflow integration

## Migration Guide

### From Manual Management
1. Install Model Custodian in your project
2. Run initial audit: `python portable_manage_models.py audit`
3. Fix any issues: `python portable_manage_models.py fix-imports`
4. Set up GitHub workflow for ongoing automation

### From Other Tools
1. Update configuration to match your current structure
2. Run validation to ensure compatibility
3. Gradually migrate existing workflows

## Advanced Configuration

### Custom Model Discovery
```python
def custom_discover_models(self):
    # Your custom model discovery logic
    return model_files
```

### Custom Import Patterns
```python
@property
def import_regex_pattern(self) -> str:
    return r"your_custom_pattern"
```

### Custom Validation Rules
```python
def custom_validate(self):
    # Your custom validation logic
    return validation_results
```

## Troubleshooting

### Common Issues
1. **Models not found**: Check `models_directory` in config
2. **Schema not loaded**: Verify `openapi_schema_path`
3. **Import errors**: Run `fix-imports` command
4. **CI/CD failures**: Check GitHub workflow configuration

### Debug Mode
```bash
python portable_manage_models.py audit --verbose
python portable_manage_models.py validate --debug
```

## Contributing

The Model Custodian system is designed to be:
- **Extensible**: Easy to add new features
- **Maintainable**: Clear separation of concerns
- **Testable**: Comprehensive test coverage
- **Documented**: Clear documentation and examples

## License

MIT License - Use freely in your projects!

---

Transform your model management from manual maintenance to automated excellence! 🚀
