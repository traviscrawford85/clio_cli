# views/tasks_view.py
from textual.widgets import Static
from textual.containers import VerticalScroll
from textual.app import ComposeResult
from textual.widget import Widget
from clio_client.clio_api_client import ClioApiClient

class TasksView(Widget):
    def __init__(self, client: ClioApiClient):
        super().__init__()
        self.client = client
        self.tasks = []

    async def on_mount(self):
        self.tasks = await self.client.get_tasks()
        self.refresh()

    def compose(self) -> ComposeResult:
        yield VerticalScroll(
            *[Static(f"📋 {getattr(t, 'description', 'No description')}") for t in self.tasks]
        )
