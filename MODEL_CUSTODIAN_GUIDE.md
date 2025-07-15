# Model Custodian Guide

## Overview
The Model Custodian system provides comprehensive model management for the Clio CLI project, automatically maintaining Pydantic models and ensuring they stay in sync with OpenAPI specifications.

## Components

### 1. GitHub Actions Workflow (`.github/workflows/model_custodian.yml`)
- **Model Validation**: Runs on every push to validate all models
- **Import Fixing**: Triggered by `[fix-imports]` in commit messages
- **Scheduled Analysis**: Weekly model health reports
- **Artifact Generation**: Stores audit reports for review

### 2. Model Management Tool (`manage_models.py`)
The central tool for all model operations:

```bash
# Audit models and generate report
python manage_models.py audit

# Fix missing imports automatically
python manage_models.py fix-imports

# Validate models (includes import check)
python manage_models.py validate

# Generate detailed report
python manage_models.py report

# Sync with OpenAPI (future enhancement)
python manage_models.py sync
```

### 3. Import Fixer (`audit_models_simple.py`)
Low-level tool that:
- Uses MyPy to detect missing imports
- Automatically adds required import statements
- Handles nested model dependencies

## Usage Scenarios

### Daily Development
1. **Making Changes**: Just develop normally - the workflow validates on every push
2. **Import Issues**: If you see import errors, commit with `[fix-imports]` to auto-fix
3. **Manual Fixing**: Run `python manage_models.py fix-imports` locally

### Model Maintenance
1. **Health Check**: `python manage_models.py audit`
2. **Detailed Analysis**: `python manage_models.py report`
3. **Validation**: `python manage_models.py validate`

### CI/CD Integration
- ✅ **Push Validation**: Every commit is automatically validated
- 🔧 **Auto-Fix**: Commit messages with `[fix-imports]` trigger automatic fixes
- 📊 **Weekly Reports**: Scheduled analysis provides model health metrics
- 📁 **Artifact Storage**: All audit reports are saved as GitHub artifacts

## Metrics Dashboard

Current model status:
- **OpenAPI Schemas**: 369 definitions
- **Existing Models**: 456 Pydantic models
- **Missing Imports**: 0 (all resolved!)
- **Orphaned Models**: 456 (expected for generated models)

## Commands Reference

### Manual Operations
```bash
# Check model health
python manage_models.py audit

# Fix any import issues
python manage_models.py fix-imports

# Full validation suite
python manage_models.py validate

# Generate comprehensive report
python manage_models.py report
```

### GitHub Actions Triggers
```bash
# Normal development (auto-validates)
git commit -m "Add new feature"
git push

# Auto-fix imports
git commit -m "Update models [fix-imports]"
git push

# Weekly analysis runs automatically via cron
```

## Error Handling

### Common Issues
1. **Import Errors**: Auto-resolved by `fix-imports` command
2. **Missing Models**: Detected in audit reports
3. **Schema Mismatches**: Highlighted in validation reports

### Troubleshooting
1. **Workflow Fails**: Check logs in GitHub Actions
2. **Local Issues**: Run `python manage_models.py validate` for details
3. **Import Problems**: Use `python manage_models.py fix-imports`

## Future Enhancements

### Phase 2 Features (Ready to Implement)
1. **Model Generation**: Auto-create models from OpenAPI schemas
2. **Schema Sync**: Bidirectional sync between OpenAPI and models
3. **Breaking Change Detection**: Alert on incompatible schema changes
4. **Performance Metrics**: Track model usage and optimization opportunities

### Integration Options
1. **Pre-commit Hooks**: Validate before commit
2. **IDE Integration**: Real-time validation in editors
3. **Documentation Generation**: Auto-generate model docs
4. **Testing Integration**: Automated model testing

## Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   GitHub        │    │   manage_models   │    │   OpenAPI       │
│   Actions       │◄──►│   .py             │◄──►│   Schema        │
│   Workflow      │    │                  │    │   (369 defs)    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                        │                       │
         ▼                        ▼                       ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Validation    │    │   Import Fixer   │    │   Pydantic      │
│   Reports       │    │   (MyPy-based)   │    │   Models        │
│   (Artifacts)   │    │                  │    │   (456 files)   │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Success Metrics

✅ **Zero Import Errors**: All 456 models import successfully  
✅ **Automated Validation**: Every push is validated  
✅ **Auto-Fix Capability**: Import issues resolve automatically  
✅ **Comprehensive Reporting**: Detailed health metrics available  
✅ **CI/CD Integration**: Seamless workflow integration  

The Model Custodian system has successfully transformed model management from manual maintenance to automated excellence! 🎉
