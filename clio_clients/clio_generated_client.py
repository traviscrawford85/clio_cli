import os
import httpx
from typing import List, Optional
from pydantic import BaseModel


# --- Pydantic Models ---

class Task(BaseModel):
    id: int
    name: Optional[str]
    description: Optional[str]
    status: Optional[str]


class Matter(BaseModel):
    id: int
    title: Optional[str]
    status: Optional[str]
    created_at: Optional[str]


class Contact(BaseModel):
    id: int
    first_name: Optional[str]
    last_name: Optional[str]


class ListResponse(BaseModel):
    data: List


# --- API Client ---

class ClioApiClient:
    def __init__(self):
        token = os.getenv("CLIO_API_TOKEN")
        base_url = os.getenv("CLIO_API_HOST", "https://api.clio.com/v4")
        if not token:
            raise ValueError("CLIO_API_TOKEN is required")
        self.client = httpx.AsyncClient(
            base_url=base_url,
            headers={"Authorization": f"Bearer {token}"},
        )

    async def get_tasks(self, limit: int = 5) -> List[Task]:
        resp = await self.client.get("/tasks", params={"limit": limit})
        resp.raise_for_status()
        data = resp.json().get("data", [])
        return [Task(**t) for t in data]

    async def get_matters(self, limit: int = 5) -> ListResponse:
        resp = await self.client.get("/matters", params={"limit": limit})
        resp.raise_for_status()
        data = resp.json().get("data", [])
        return ListResponse(data=[Matter(**m) for m in data])

    async def get_contacts(self, limit: int = 5) -> List[Contact]:
        resp = await self.client.get("/contacts", params={"limit": limit})
        resp.raise_for_status()
        data = resp.json().get("data", [])
        return [Contact(**c) for c in data]
