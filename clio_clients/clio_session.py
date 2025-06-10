import os

import httpx


class ClioSession:
    def __init__(self):
        self.token = os.getenv("CLIO_API_TOKEN")
        if not self.token:
            raise ValueError("Missing CLIO_API_TOKEN in environment")
        self.client = httpx.AsyncClient(
            base_url=os.getenv("CLIO_API_HOST", "https://app.clio.com/api/v4"),
            headers={"Authorization": f"Bearer {self.token}"},
        )
