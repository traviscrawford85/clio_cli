#!/bin/bash
set -e

# Activate virtual environment or set up env
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run Python setup script
python setup_codex.py
