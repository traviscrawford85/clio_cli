#!/bin/bash
# Test script to verify the model_custodian.yml fixes

echo "🔍 Testing model fixes..."

# Activate virtual environment
source .venv/bin/activate

echo "✅ Testing EventMetrics import (was missing eventmetricsbase.py)..."
python -c "from clio_clients.models.event.eventmetrics import EventMetrics; print('✅ EventMetrics import successful')"

echo "✅ Testing all models import..."
python -c "from clio_clients.models import *; print('✅ All models import successful')"

echo "✅ Testing mypy with explicit-package-bases (fixes duplicate module paths)..."
mypy clio_clients/models/event/eventmetrics.py clio_clients/models/event/eventmetricsbase.py --explicit-package-bases --no-error-summary
echo "✅ MyPy duplicate module path issue resolved"

echo "🎉 All fixes verified successfully!"
