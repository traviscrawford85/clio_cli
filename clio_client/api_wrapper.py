from typing import Any

from clio_client.clio_generated_client.api.matters.matterindex import MatterIndexParams
from clio_client.clio_generated_client.models import Activity, Contact, Matter, Task
from clio_client.clio_sdk import ApiClient
from clio_client.clio_sdk.api.activities_api import ActivityIndexParams
from clio_client.clio_sdk.api.contacts_api import ContactIndexParams
from clio_client.clio_sdk.api.tasks_api import TaskIndexParams
from clio_client.clio_sdk.exceptions import UnauthorizedException


class ClioApiWrapper:
    def __init__(self, client: ApiClient):
        self.client = client

    def list_matters(self, **kwargs: Any) -> list[Matter]:
        try:
            params = MatterIndexParams(**kwargs)
            api = self.client.matters_api
            response = api.matter_index(params=params)
            return response.data or []
        except UnauthorizedException as exc:
            raise RuntimeError("Unauthorized access to matters endpoint") from exc

    def list_contacts(self, **kwargs: Any) -> list[Contact]:
        try:
            params = ContactIndexParams(**kwargs)
            api = self.client.contacts_api
            response = api.contact_index(params=params)
            return response.data or []
        except UnauthorizedException as exc:
            raise RuntimeError("Unauthorized access to contacts endpoint") from exc

    def list_activities(self, **kwargs: Any) -> list[Activity]:
        try:
            params = ActivityIndexParams(**kwargs)
            api = self.client.activities_api
            response = api.activity_index(params=params)
            return response.data or []
        except UnauthorizedException as exc:
            raise RuntimeError("Unauthorized access to activities endpoint") from exc

    def list_tasks(self, **kwargs: Any) -> list[Task]:
        try:
            params = TaskIndexParams(**kwargs)
            api = self.client.tasks_api
            response = api.task_index(params=params)
            return response.data or []
        except UnauthorizedException as exc:
            raise RuntimeError("Unauthorized access to tasks endpoint") from exc
