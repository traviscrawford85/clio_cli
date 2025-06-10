from clio_clients.clio_session import ClioSession  # Adjust the import path as needed


class ClioApiClient:
    def __init__(self, session: ClioSession):
        self.client = session.client

    async def list_tasks(self, limit=5):
        resp = await self.client.get("/tasks", params={"limit": limit})
        resp.raise_for_status()
        return resp.json().get("data", [])
