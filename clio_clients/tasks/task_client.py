import httpx
import os
import logging
from typing import Optional
from pydantic import RootModel

from openapi_schemas_pydantic import construct_open_api_with_schema_class
from clio_clients.models.task import Task
from app.core.token_store import get_clio_token
from dotenv import load_dotenv

# Load environment variables from .env at project root
load_dotenv(
    dotenv_path=os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env"
    )
)

# Configure logging for this client
logger = logging.getLogger("clio_clients.tasks")
if not logger.hasHandlers():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )


class TaskListResponse(RootModel):
    root: list[Task]


class ClioTaskClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def list_tasks(self, **params) -> list[Task]:
        headers = {"Authorization": f"Bearer {get_clio_token()}"}
        logger.info(f"Fetching tasks from {self.base_url}/tasks with params: {params}")
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/tasks", headers=headers, params=params
            )
            logger.info(f"Received response: {response.status_code}")
            response.raise_for_status()
            return TaskListResponse.model_validate(response.json()).root

    async def get_task(self, id: str) -> Task:
        headers = {"Authorization": f"Bearer {get_clio_token()}"}
        url = f"{self.base_url}/tasks/{id}"
        logger.info(f"Fetching task {id} from {url}")
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            logger.info(f"Received response: {response.status_code}")
            response.raise_for_status()
            task = Task.model_validate(response.json())
            task.etag = response.headers.get("etag")
            return task

    async def update_task(
        self, id: str, status: str, etag: Optional[str] = None
    ) -> Task:
        update_request = TaskUpdate(data=TaskUpdateData(status=status))
        headers = {"Authorization": f"Bearer {get_clio_token()}"}
        if etag:
            headers["If-Match"] = etag
        url = f"{self.base_url}/tasks/{id}"
        logger.info(
            f"Updating task {id} at {url} with status '{status}' and etag '{etag}'"
        )
        async with httpx.AsyncClient() as client:
            response = await client.patch(
                url,
                json=update_request.model_dump(exclude_unset=True),
                headers=headers,
            )
            logger.info(f"Received response: {response.status_code}")
            response.raise_for_status()
            return Task.model_validate(response.json())

    @staticmethod
    async def get_clio_headers() -> dict[str, str]:
        access_token = get_clio_token()
        return {"Authorization": f"Bearer {access_token}"}
