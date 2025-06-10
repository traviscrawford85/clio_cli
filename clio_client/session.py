# clio_client/session.py
import json
import os
from datetime import datetime, timedelta

import requests
from clio_client.clio_sdk import ApiClient, Configuration


class ClioSession:
    def __init__(self):
        self.token_path = "clio_client/clio_token_store.json"
        self.token_data = self.load_token()
        self.api_client = self.create_api_client()

    def load_token(self) -> dict:
        with open(self.token_path) as f:
            return json.load(f)

    def save_token(self, tokens: dict):
        with open(self.token_path, "w") as f:
            json.dump(tokens, f, indent=2)

    def token_expired(self) -> bool:
        return datetime.utcnow() >= datetime.fromisoformat(self.token_data["expires_at"])

    def refresh_token(self):
        payload = {
            "grant_type": "refresh_token",
            "client_id": os.getenv("CLIO_CLIENT_ID"),
            "client_secret": os.getenv("CLIO_CLIENT_SECRET"),
            "refresh_token": self.token_data["refresh_token"],
        }
        resp = requests.post(os.getenv("CLIO_TOKEN_URL"), data=payload)
        resp.raise_for_status()
        new_tokens = resp.json()
        new_tokens["expires_at"] = (datetime.utcnow() + timedelta(seconds=new_tokens["expires_in"])).isoformat()
        self.token_data = new_tokens
        self.save_token(new_tokens)

    def ensure_valid_token(self):
        if self.token_expired():
            self.refresh_token()

    def create_api_client(self) -> ApiClient:
        self.ensure_valid_token()
        config = Configuration()
        config.host = os.getenv("CLIO_API_HOST")
        config.access_token = self.token_data["access_token"]
        client = ApiClient(configuration=config)
        client.default_headers["Authorization"] = f"Bearer {config.access_token}"
        return client



    def ensure_valid_token(self):
        if self.token_expired():
            print("[ClioSession.ensure_valid_token] 🔁 Access token expired. Refreshing...")
            new_token_data = refresh_token(self.token_data)
            # Always update the refresh token if present
            if "refresh_token" in new_token_data:
                self.token_data["refresh_token"] = new_token_data["refresh_token"]
            self.token_data.update(new_token_data)
            self.save_token(self.token_data)
            self.api_client = self.create_api_client(self.token_data)
            self.matters_api = MattersApi(self.api_client)
            self.contacts_api = ContactsApi(self.api_client)
            self.tasks_api = TasksApi(self.api_client)
            print("[ClioSession.ensure_valid_token] Token refreshed and APIs re-initialized.")
        else:
            print("[ClioSession.ensure_valid_token] Token is still valid.")
