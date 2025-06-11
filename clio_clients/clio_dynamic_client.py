import logging
import re
from typing import Any, Dict, List, Optional

import httpx
import yaml
from clio_clients.models.contact import Contact
from clio_clients.models.contactbase import ContactBase
from clio_clients.models.matter import Matter
from clio_clients.models.task import Task
from database.token_storage import load_token_data
from openapi_schemas_pydantic import construct_open_api_with_schema_class
from openapi_schemas_pydantic.v3_1_0 import OpenAPI

logger = logging.getLogger(__name__)


class ClioDynamicClient:
    def __init__(
        self,
        spec_path: str,
        clio_user_id: str = "default",
        base_url: str = "https://app.clio.com/api/v4",
    ):
        logger.debug("Loading OpenAPI spec from %s", spec_path)
        with open(spec_path) as f:
            raw_spec = yaml.safe_load(f)
            parsed_spec = OpenAPI.model_validate(raw_spec)
            self.spec = construct_open_api_with_schema_class(parsed_spec)

        self.base_url = base_url.rstrip("/")
        token_data = load_token_data(clio_user_id)
        self.headers = {
            "Authorization": f"Bearer {token_data['access_token']}",
            "Accept": "application/json",
        }
        self.http_client = httpx.AsyncClient(
            base_url=self.base_url, headers=self.headers
        )
        logger.debug("Initialized HTTP client with base_url=%s", self.base_url)

    def find_operation(self, operation_id: str):
        for path, path_item in self.spec.paths.items():
            for method in ["get", "post", "put", "delete", "patch"]:
                op = getattr(path_item, method, None)
                if op and op.operationId == operation_id:
                    logger.debug("Found operation %s for path %s", operation_id, path)
                    return method.upper(), path, op
        raise ValueError(f"Operation ID {operation_id} not found")

    def substitute_path_params(self, path: str, params: Dict[str, Any]) -> str:
        path_params = re.findall(r"{(.*?)}", path)
        for param in path_params:
            if param not in params:
                raise ValueError(f"Missing path parameter: {param}")
            path = path.replace(f"{{{param}}}", str(params[param]))
        return path

    async def call(
        self,
        operation_id: str,
        *,
        path_params: Optional[Dict[str, Any]] = None,
        query_params: Optional[Dict[str, Any]] = None,
        body: Optional[Dict] = None,
    ):
        logger.debug("Calling operation_id=%s", operation_id)
        method, path, op = self.find_operation(operation_id)
        path_params = path_params or {}
        query_params = query_params or {}

        full_path = self.substitute_path_params(path, path_params)

        response = await self.http_client.request(
            method=method,
            url=full_path,
            params=query_params,
            json=body if method in ["POST", "PUT", "PATCH"] else None,
        )

        logger.debug("Response status code: %s", response.status_code)
        response.raise_for_status()

        if op.responses and "200" in op.responses and op.responses["200"].content:
            schema = op.responses["200"].content.get("application/json")
            if schema and schema.schema:
                parsed = schema.schema.model_validate(response.json()).model_dump()
                logger.debug("Parsed response for %s", operation_id)
                return parsed

        return response.json()

    async def list_matters(self, limit=5) -> List[Matter]:
        logger.debug("Fetching matters")
        raw = await self.call("Matter#index", query_params={"limit": limit})
        logger.debug("Raw matters response: %s", raw)
        return [Matter.model_validate(m) for m in raw["data"]]

    async def list_tasks(self, limit=5) -> List[Task]:
        logger.debug("Fetching tasks")
        raw = await self.call("Task#index", query_params={"limit": limit})
        logger.debug("Raw tasks response: %s", raw)
        return [Task.model_validate(t) for t in raw["data"]]

    async def list_contacts(self, limit=5, fields: str = None) -> list:
        logger.debug("Fetching contacts")
        params = {"limit": limit}
        if fields:
            params["fields"] = fields
        raw = await self.call("Contact#index", query_params=params)
        logger.debug("Raw contacts response: %s", raw)
        return [ContactBase.model_validate(c) for c in raw["data"]]
