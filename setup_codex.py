import os

from dotenv import load_dotenv

# Load .env.codex instead of .env
load_dotenv(dotenv_path=".env.codex")

# Optionally print or verify loaded values
print("Codex environment loaded")
