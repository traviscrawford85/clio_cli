import logging

from clio_clients.clio_dynamic_client import ClioDynamicClient
from clio_clients.models.task import Task
from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.widget import Widget
from textual.widgets import Static

logger = logging.getLogger(__name__)


class TasksView(Widget):
    def __init__(self, client: ClioDynamicClient):
        super().__init__()
        self.client = client
        self.tasks: list[Task] = []

    async def on_mount(self):
        logger.debug("TasksView mounted")
        try:
            self.tasks = await self.client.list_tasks()
            logger.debug("Received %d tasks", len(self.tasks))
        except Exception as e:
            logger.exception("Error fetching tasks")
            self.tasks = []
            await self.mount(Static(f"\u26a0\ufe0f Error fetching tasks: {e}"))
            return
        await self.update_view()

    async def update_view(self):
        await self.remove_children()
        if not self.tasks:
            await self.mount(Static("\ud83d\udcb7 No tasks available."))
        else:
            await self.mount(
                VerticalScroll(
                    *[
                        Static(
                            f"\ud83d\udc64 {t.name or t.description or 'Untitled Task'}\nStatus: {t.status or 'unknown'} | ID: {t.id}"
                        )
                        for t in self.tasks
                    ]
                )
            )
