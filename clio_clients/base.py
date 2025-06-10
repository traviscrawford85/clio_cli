# clio_clients/base.py
import os
from typing import Optional

import httpx


class BaseClioClient:
    """
    Base async Clio API client using httpx.
    All Clio API modules should inherit from this.
    """

    def __init__(self, token: str, base_url: Optional[str] = None):
        self.token = token
        self.base_url = base_url or os.environ.get(
            "CLIO_API_HOST", "https://api.clio.com/v4"
        )
        print(
            f"[BaseClioClient] Using token: {self.token[:12]}... base_url: {self.base_url}"
        )  # Print first 12 chars for safety
        self.client = httpx.AsyncClient(
            base_url=self.base_url,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Accept": "application/json",
            },
            timeout=10.0,
        )

    async def get(self, url: str, **kwargs):
        print(f"[BaseClioClient] GET {url} with token: {self.token[:12]}...")
        return await self.client.get(url, **kwargs)

    async def post(self, url: str, **kwargs):
        print(f"[BaseClioClient] POST {url} with token: {self.token[:12]}...")
        return await self.client.post(url, **kwargs)

    async def close(self):
        await self.client.aclose()


class AuthenticatedClient(BaseClioClient):
    """
    For compatibility with OpenAPI-generated code.
    """

    def __init__(self, base_url: str, token: str):
        super().__init__(token=token, base_url=base_url)
        print(
            f"[AuthenticatedClient] Initialized with token: {self.token[:12]}... base_url: {self.base_url}"
        )  # Print first 12 chars for safety
