# views/matters_view.py

from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.widget import Widget
from textual.widgets import Static

from clio_client.clio_api_client import ClioApiClient


class MattersView(Widget):
    def __init__(self, client: ClioApiClient):
        super().__init__()
        self.client = client
        self.matters = []

    async def on_mount(self):
        self.matters = await self.client.get_matters()
        self.refresh()

    def compose(self) -> ComposeResult:
        yield VerticalScroll(
            *[
                Static(f"📁 {getattr(m, 'number', '')} — {getattr(m, 'description', 'No description')}")
                for m in self.matters
            ]
        )
