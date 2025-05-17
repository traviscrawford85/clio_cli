import httpx
from typing import List, Optional
# Define placeholder model classes if not available elsewhere
from typing import Any

class Matter:
    @classmethod
    def model_validate(cls, data: Any):
        return cls(**data)

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class Contact:
    @classmethod
    def model_validate(cls, data: Any):
        return cls(**data)

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class Task:
    @classmethod
    def model_validate(cls, data: Any):
        return cls(**data)

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class ClioApiClient:
    def __init__(self, token: str, base_url: str = "https://app.clio.com/api/v4"):
        self.token = token
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json"
        }
        self.client = httpx.AsyncClient(base_url=self.base_url, headers=self.headers)

    async def get_matters(self) -> List[Matter]:
        resp = await self.client.get("/matters")
        resp.raise_for_status()
        return [Matter.model_validate(item) for item in resp.json().get("data", [])]

    async def get_contacts(self) -> List[Contact]:
        resp = await self.client.get("/contacts")
        resp.raise_for_status()
        return [Contact.model_validate(item) for item in resp.json().get("data", [])]

    async def get_tasks(self) -> List[Task]:
        resp = await self.client.get("/tasks")
        resp.raise_for_status()
        return [Task.model_validate(item) for item in resp.json().get("data", [])]

    async def close(self):
        await self.client.aclose()


# Example usage for testing
if __name__ == "__main__":
    import asyncio

    async def main():
        token = "your-access-token-here"  # replace with a real token
        client = ClioApiClient(token)

        matters = await client.get_matters()
        for m in matters:
            print(f"Matter: {m}")

        contacts = await client.get_contacts()
        for c in contacts:
            print(f"Contact: {c}")

        tasks = await client.get_tasks()
        for t in tasks:
            print(f"Task: {t}")

        await client.close()

    asyncio.run(main())
