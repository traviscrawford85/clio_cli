import time
from contextlib import contextmanager

import requests
from .db import SessionLocal  # relative import
from .clio_token import ClioToken  # relative import


@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def refresh_access_token(token_data: dict) -> dict:
    response = requests.post(
        "https://app.clio.com/oauth/token",
        data={
            "grant_type": "refresh_token",
            "refresh_token": token_data["refresh_token"],
            "client_id": token_data["client_id"],
            "client_secret": token_data["client_secret"],
        },
    )
    response.raise_for_status()
    new_data = response.json()

    return {
        "access_token": new_data["access_token"],
        "refresh_token": new_data.get("refresh_token", token_data["refresh_token"]),
        "expires_at": time.time() + new_data["expires_in"],
        "client_id": token_data["client_id"],
        "client_secret": token_data["client_secret"],
    }


def load_token_data(clio_user_id: str) -> dict:
    with get_db() as db:
        token = db.query(ClioToken).filter_by(clio_user_id=clio_user_id).first()
        if not token:
            raise FileNotFoundError(f"No token for user: {clio_user_id}")

        if time.time() >= token.expires_at:
            updated = refresh_access_token({
                "refresh_token": token.refresh_token,
                "client_id": token.client_id,
                "client_secret": token.client_secret,
            })
            save_token_data(clio_user_id, updated)
            return updated

        return {
            "access_token": token.access_token,
            "refresh_token": token.refresh_token,
            "expires_at": token.expires_at,
            "client_id": token.client_id,
            "client_secret": token.client_secret,
        }


def save_token_data(clio_user_id: str, data: dict):
    with get_db() as db:
        token = db.query(ClioToken).filter_by(clio_user_id=clio_user_id).first()
        if token:
            token.access_token = data["access_token"]
            token.refresh_token = data["refresh_token"]
            token.expires_at = data["expires_at"]
            token.client_id = data["client_id"]
            token.client_secret = data["client_secret"]
        else:
            token = ClioToken(
                clio_user_id=clio_user_id,
                access_token=data["access_token"],
                refresh_token=data["refresh_token"],
                expires_at=data["expires_at"],
                client_id=data["client_id"],
                client_secret=data["client_secret"],
            )
            db.add(token)
        db.commit()
