import logging
from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.widget import Widget
from textual.widgets import Static
from clio_clients.models.task import Task
from clio_clients.clio_dynamic_client import ClioDynamicClient

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
            await self.mount(Static(f"⚠️ Error fetching tasks:\n{e}"))
        self.refresh()

    def compose(self) -> ComposeResult:
        if not self.tasks:
            yield Static("📭 No tasks available.")
        else:
            yield VerticalScroll(
                *[
                    Static(
                        f"📋 {t.name or t.description or 'Untitled Task'}\n"
                        f"Status: {t.status or 'unknown'} | ID: {t.id}"
                    )
                    for t in self.tasks
                ]
            )
