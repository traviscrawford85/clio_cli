import http.server
import json
import os
import socketserver
import webbrowser
from datetime import datetime, timedelta
from urllib.parse import parse_qs, urlparse

import httpx
from dotenv import load_dotenv
import logging
from database.token_storage import save_token_data

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] %(levelname)-8s %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

load_dotenv()

PORT = int(os.getenv("PORT", 8000))
CLIENT_ID = os.getenv("CLIO_CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIO_CLIENT_SECRET")
REDIRECT_URI = os.getenv(
    "CLIO_REDIRECT_URI", f"http://localhost:{PORT}/oauth/clio/callback"
)
TOKEN_URL = os.getenv("CLIO_TOKEN_URL", "https://app.clio.com/oauth/token")
TOKEN_STORE_PATH = os.path.join(
    os.path.dirname(__file__), "clio_client", "clio_token_store.json"
)


class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


class OAuthHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        logger.debug(f"Received GET request: {self.path}")
        # Only handle the correct callback path
        if not self.path.startswith("/oauth/clio/callback"):
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")
            return

        query = parse_qs(urlparse(self.path).query)
        code = query.get("code", [None])[0]

        if not code:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(
                b"Missing code in callback. Please ensure you are using the correct redirect URI."
            )
            logger.error("Missing code in callback.")
            return

        logger.info("Received OAuth code, exchanging for tokens...")
        try:
            resp = httpx.post(
                TOKEN_URL,
                data={
                    "grant_type": "authorization_code",
                    "client_id": CLIENT_ID,
                    "client_secret": CLIENT_SECRET,
                    "redirect_uri": REDIRECT_URI,
                    "code": code,
                },
                headers={"Accept": "application/json"},
            )
            resp.raise_for_status()
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"Token exchange failed: {e}".encode())
            logger.error(f"Token exchange failed: {e}")
            return

        tokens = resp.json()
        tokens["expires_at"] = (
            datetime.utcnow() + timedelta(seconds=tokens["expires_in"])
        ).timestamp()  # store as timestamp for DB

        # Save to DB instead of file
        save_token_data("default", {  # Use a real user_id if available
            "access_token": tokens["access_token"],
            "refresh_token": tokens["refresh_token"],
            "expires_at": tokens["expires_at"],
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        })

        self.send_response(200)
        self.end_headers()
        self.wfile.write(
            "✅ Clio Authorization Complete! You can close this tab.".encode("utf-8")
        )
        logger.info("Access and refresh tokens saved to database")


def run_oauth_flow():
    auth_url = (
        f"https://app.clio.com/oauth/authorize"
        f"?response_type=code"
        f"&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        f"&scope=all"
    )
    print("\U0001f310 Opening browser for Clio OAuth...")
    logger.info(f"Opening browser to: {auth_url}")
    webbrowser.open(auth_url)

    with ReusableTCPServer(("", PORT), OAuthHandler) as httpd:
        print(f"\u23f3 Waiting for OAuth callback on port {PORT}...")
        logger.info(f"Waiting for OAuth callback on port {PORT}...")
        httpd.handle_request()


if __name__ == "__main__":
    run_oauth_flow()
