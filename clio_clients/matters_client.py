# Copilot: This module defines the MattersClient class for interacting with Clio's Matters API.
# filepath: /home/sysadmin01/clio_slack_agent/clio_clients/matters_client.py
from .base import BaseClioClient
from typing import List, Optional
from clio_clients.models.matter import Matter


class ClioMattersClient(BaseClioClient):
    """
    Async client for Clio Matters API.
    """

    async def list_matters(
        self,
        limit: Optional[int] = None,
        fields: Optional[str] = None,
    ) -> List[Matter]:
        params = {}
        if limit:
            params["limit"] = limit
        params["fields"] = fields or "id,name,display_number,created_at,updated_at"
        print(f"[ClioMattersClient] list_matters params: {params}")
        resp = await self.get("/matters", params=params)
        resp.raise_for_status()
        data = resp.json().get("data", [])
        return [Matter.model_validate(item) for item in data]

    async def get_matter(self, id: int) -> Matter:
        print(f"[ClioMattersClient] get_matter id: {id}")
        resp = await self.get(f"/matters/{id}")
        resp.raise_for_status()
        return Matter.parse_obj(resp.json().get("data"))
