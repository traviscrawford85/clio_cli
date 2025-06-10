# scripts/bootstrap_token_store.py

import json
import os
from datetime import datetime, timedelta, timezone

import httpx
from dotenv import load_dotenv

load_dotenv()

TOKEN_URL = os.getenv("CLIO_TOKEN_URL")
REFRESH_TOKEN = os.getenv("CLIO_REFRESH_TOKEN")
CLIENT_ID = os.getenv("CLIO_CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIO_CLIENT_SECRET")
TOKEN_STORE_PATH = os.getenv("CLIO_TOKEN_STORE_PATH", "clio_token_store.json")

if not all([TOKEN_URL, REFRESH_TOKEN, CLIENT_ID, CLIENT_SECRET]):
    raise OSError("One or more required .env values are missing.")

response = httpx.post(
    TOKEN_URL,
    data={
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    },
    headers={"Accept": "application/json"}
)
response.raise_for_status()

token_data = response.json()
token_data["refresh_token"] = token_data.get("refresh_token", REFRESH_TOKEN)  # <- keep if not returned
token_data["expires_at"] = (datetime.utcnow() + timedelta(seconds=token_data["expires_in"])).isoformat()

with open(TOKEN_STORE_PATH, "w") as f:
    json.dump(token_data, f, indent=2)

print(f"✅ Token saved to {TOKEN_STORE_PATH}")

with open("clio_token_store.json") as f:
    data = json.load(f)

if isinstance(data["expires_at"], int):
    data["expires_at"] = datetime.fromtimestamp(data["expires_at"], tz=timezone.utc).isoformat()
    with open("clio_token_store.json", "w") as f:
        json.dump(data, f, indent=2)
