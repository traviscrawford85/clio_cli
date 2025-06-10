# filepath: /home/sysadmin01/clio_slack_agent/clio_clients/tasks.py
from .base import BaseClioClient
from typing import List, Optional
from clio_clients.models.task import Task


class ClioTaskClient(BaseClioClient):
    """
    Async client for Clio Tasks API.
    """

    async def list_tasks(
        self,
        assignee_type: Optional[str] = None,
        limit: Optional[int] = None,
        fields: Optional[str] = None,
    ) -> List[Task]:
        params = {}
        if assignee_type:
            params["assignee_type"] = assignee_type
        if limit:
            params["limit"] = limit
        if fields:
            params["fields"] = fields
        print(f"[ClioTaskClient] list_tasks params: {params}")
        resp = await self.get("/tasks", params=params)
        resp.raise_for_status()
        data = resp.json().get("data", [])
        return [Task.model_validate(item) for item in data]

    async def get_task(self, id: int) -> Task:
        print(f"[ClioTaskClient] get_task id: {id}")
        resp = await self.get(f"/tasks/{id}")
        resp.raise_for_status()
        return Task.parse_obj(resp.json().get("data"))

    async def update_task(self, id: int, payload: dict) -> Task:
        print(f"[ClioTaskClient] update_task id: {id} payload: {payload}")
        resp = await self.client.put(f"/tasks/{id}", json=payload)
        resp.raise_for_status()
        return Task.parse_obj(resp.json().get("data"))
