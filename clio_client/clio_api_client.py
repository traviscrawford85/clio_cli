import logging

from clio_client.api_wrapper import ApiClientWrapper
from clio_client.clio_sdk.api import ContactsApi, MattersApi, TasksApi
from clio_client.clio_sdk.exceptions import ApiException
from clio_client.clio_sdk.models import Contact, Matter, Task
from clio_client.session import ClioSession

logger = logging.getLogger(__name__)

class ClioApiClient:
    def __init__(self, session: ClioSession):
        logger.debug("[ClioApiClient.__init__] Initializing ClioApiClient with session.")
        self.session = session
        self.api_wrapper = ApiClientWrapper(session)
        self.contacts_api = ContactsApi(session.api_client)
        self.matters_api = MattersApi(session.api_client)
        self.tasks_api = TasksApi(session.api_client)

    async def get_contacts(self) -> list[Contact]:
        try:
            logger.debug("[ClioApiClient.get_contacts] Fetching contacts.")
            response = self.api_wrapper.call(self.contacts_api.contact_index)
            return response.data or []
        except ApiException as e:
            logger.error(f"Failed to fetch contacts: {e}")
            return []

    async def get_matters(self) -> list[Matter]:
        try:
            logger.debug("[ClioApiClient.get_matters] Fetching matters.")
            response = self.api_wrapper.call(self.matters_api.matter_index)
            return response.data or []
        except ApiException as e:
            logger.error(f"Failed to fetch matters: {e}")
            return []

    async def get_tasks(self) -> list[Task]:
        try:
            logger.debug("[ClioApiClient.get_tasks] Fetching tasks.")
            response = self.api_wrapper.call(self.tasks_api.task_index)
            return response.data or []
        except ApiException as e:
            logger.error(f"Failed to fetch tasks: {e}")
            return []
