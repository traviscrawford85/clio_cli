# views/contacts_view.py
from textual.widgets import Static
from textual.containers import VerticalScroll
from textual.app import ComposeResult
from textual.widget import Widget
from clio_client.clio_api_client import ClioApiClient

class ContactsView(Widget):
    def __init__(self, client: ClioApiClient):
        super().__init__()
        self.client = client
        self.contacts = []

    async def on_mount(self):
        self.contacts = await self.client.get_contacts()
        self.refresh()

    def compose(self) -> ComposeResult:
        yield VerticalScroll(
            *[Static(f"👤 {getattr(c, 'first_name', '')} {getattr(c, 'last_name', '')}") for c in self.contacts]
        )
