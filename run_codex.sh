#!/bin/bash
echo "🔧 Installing dependencies..."
pip install -r requirements.txt

echo "⚙️  Setting up environment for Codex..."
python setup_codex.py

echo "🚀 Ready to run Codex workflows!"
