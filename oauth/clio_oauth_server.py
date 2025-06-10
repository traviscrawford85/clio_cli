import os
import time

import requests
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

from oauth.token_store import save_token_data

app = FastAPI()

@app.get("/")
async def clio_home():
    redirect_uri = os.getenv('CLIO_REDIRECT_URI')
    auth_url = (
        f"https://app.clio.com/oauth/authorize?"
        f"client_id={os.getenv('CLIO_CLIENT_ID')}&"
        f"redirect_uri={redirect_uri}&"
        f"response_type=code&"
        f"scope=all"
    )
    return RedirectResponse(url=auth_url)

@app.get("/api/oauth/callback")
async def clio_callback(request: Request):
    code = request.query_params.get("code")
    user_id = request.query_params.get("state", "default")

    CLIO_CLIENT_ID = os.getenv('CLIO_CLIENT_ID')
    CLIO_CLIENT_SECRET = os.getenv('CLIO_CLIENT_SECRET')
    CLIO_REDIRECT_URI = os.getenv('CLIO_REDIRECT_URI')

    payload = {
        "grant_type": "authorization_code",
        "client_id": CLIO_CLIENT_ID,
        "client_secret": CLIO_CLIENT_SECRET,
        "redirect_uri": CLIO_REDIRECT_URI,
        "code": code,
    }

    token_response = requests.post("https://app.clio.com/oauth/token", data=payload)
    tokens = token_response.json()
    tokens["expires_at"] = int(time.time()) + tokens.get("expires_in", 3600)
    tokens["client_id"] = CLIO_CLIENT_ID
    tokens["client_secret"] = CLIO_CLIENT_SECRET

    save_token_data(user_id, tokens)
    return {"message": f"✅ Clio Authorization Complete for user {user_id}!"}
