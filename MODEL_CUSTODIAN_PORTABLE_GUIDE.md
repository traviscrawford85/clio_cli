# Making Model Custodian Portable for Other Projects

## Overview
The Model Custodian system can be easily adapted for any Python project that uses:
- Pydantic models
- OpenAPI schemas
- Type checking with MyPy
- GitHub Actions CI/CD

## Core Components to Port

### 1. Essential Files
```
manage_models.py          # Main management tool
audit_models_simple.py    # Import fixer
.github/workflows/model_custodian.yml  # CI/CD workflow
```

### 2. Configuration Files
```
requirements.txt          # Add model management dependencies
pyproject.toml           # Update for your project structure
```

## Adaptation Steps

### Step 1: Update File Paths
In `manage_models.py`, change these paths to match your project:

```python
# FROM (Clio-specific):
MODELS_DIR = "clio_clients/models"
OPENAPI_SCHEMA = "openapi_sdk.yaml"

# TO (Generic):
MODELS_DIR = "your_project/models"  # Your models directory
OPENAPI_SCHEMA = "openapi.yaml"     # Your OpenAPI schema file
```

### Step 2: Update Import Patterns
In `audit_models_simple.py`, modify the import pattern:

```python
# FROM (Clio-specific):
import_pattern = r"from clio_clients\.models\.(\w+) import"

# TO (Generic):
import_pattern = r"from your_project\.models\.(\w+) import"
```

### Step 3: Configure GitHub Workflow
Update `.github/workflows/model_custodian.yml`:

```yaml
# Update Python version if needed
python-version: "3.10"  # or your version

# Update requirements installation
pip install -r requirements.txt
pip install your-project-specific-deps

# Update model validation command
python manage_models.py validate
```

## Project Structure Requirements

Your project should have this structure:
```
your_project/
├── models/
│   ├── __init__.py
│   ├── user/
│   │   ├── __init__.py
│   │   └── user.py
│   └── order/
│       ├── __init__.py
│       └── order.py
├── openapi.yaml           # Your OpenAPI schema
├── manage_models.py       # Ported management tool
├── audit_models_simple.py # Ported import fixer
└── requirements.txt
```

## Dependencies to Add

Add these to your `requirements.txt`:
```
pydantic>=2.0.0
pyyaml>=6.0
mypy>=1.0.0
openapi-schemas-pydantic>=3.0.0
```

## Configuration Examples

### For Django Projects
```python
# In manage_models.py
MODELS_DIR = "myapp/models"
OPENAPI_SCHEMA = "schema/openapi.yaml"

# Import pattern in audit_models_simple.py
import_pattern = r"from myapp\.models\.(\w+) import"
```

### For FastAPI Projects
```python
# In manage_models.py
MODELS_DIR = "app/models"
OPENAPI_SCHEMA = "docs/openapi.json"  # FastAPI auto-generates this

# Import pattern
import_pattern = r"from app\.models\.(\w+) import"
```

### For Flask Projects
```python
# In manage_models.py
MODELS_DIR = "myflaskapp/models"
OPENAPI_SCHEMA = "api/openapi.yaml"

# Import pattern
import_pattern = r"from myflaskapp\.models\.(\w+) import"
```

## Usage Commands (Same Across Projects)

```bash
# Health check
python manage_models.py audit

# Fix imports
python manage_models.py fix-imports

# Full validation
python manage_models.py validate

# Generate report
python manage_models.py report
```

## GitHub Integration

The workflow triggers work the same way:
1. **Auto-validation**: Every push
2. **Auto-fix**: Commit with `[fix-imports]`
3. **Scheduled analysis**: Weekly reports

## Benefits for Other Projects

### 1. Immediate Value
- ✅ Catch import errors before they reach production
- ✅ Automated model validation in CI/CD
- ✅ Self-healing import management

### 2. Long-term Benefits
- 📊 Model health tracking over time
- 🔄 OpenAPI schema synchronization
- 📁 Historical audit reports
- 🤖 Automated model generation

### 3. Team Benefits
- 👥 Consistent model management across team
- 📈 Reduced manual maintenance overhead
- 🛡️ Proactive issue detection
- 📋 Clear model health metrics

## Customization Points

### Model Discovery
Customize how models are found:
```python
def find_models(base_dir):
    # Custom logic for your project structure
    return model_files
```

### Import Pattern Matching
Adjust for your import style:
```python
# For absolute imports
pattern = r"from myproject\.models\.(\w+) import (\w+)"

# For relative imports
pattern = r"from \.(\w+) import (\w+)"
```

### Schema Location
Support different schema formats:
```python
# JSON schemas
schema = json.load(open("schema.json"))

# Multiple schema files
schemas = glob.glob("schemas/*.yaml")
```

## Migration Checklist

- [ ] Copy core files (`manage_models.py`, `audit_models_simple.py`)
- [ ] Update file paths and import patterns
- [ ] Configure GitHub workflow
- [ ] Add dependencies to requirements.txt
- [ ] Test with `python manage_models.py audit`
- [ ] Verify GitHub Actions workflow
- [ ] Document project-specific usage

## Example: Porting to "ECommerce API"

```bash
# 1. Copy files
cp manage_models.py ../ecommerce-api/
cp audit_models_simple.py ../ecommerce-api/
cp .github/workflows/model_custodian.yml ../ecommerce-api/.github/workflows/

# 2. Update paths in manage_models.py
sed -i 's/clio_clients/ecommerce_api/g' ../ecommerce-api/manage_models.py
sed -i 's/openapi_sdk.yaml/api_schema.yaml/g' ../ecommerce-api/manage_models.py

# 3. Update import patterns
sed -i 's/clio_clients/ecommerce_api/g' ../ecommerce-api/audit_models_simple.py

# 4. Test
cd ../ecommerce-api
python manage_models.py audit
```

## Success Stories

Projects that could benefit:
- **API Backends**: FastAPI, Django REST, Flask-RESTX
- **Microservices**: Each service with its own models
- **Data Processing**: Pydantic models for data validation
- **ML Pipelines**: Model schemas for feature validation

The Model Custodian system transforms model management from a manual chore into automated excellence, regardless of the project! 🚀
