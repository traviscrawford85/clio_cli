# contacts_view.py
import logging

from clio_clients.clio_dynamic_client import ClioDynamicClient
from clio_clients.models.contact import Contact
from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.widget import Widget
from textual.widgets import Static

logger = logging.getLogger(__name__)


class ContactsView(Widget):
    def __init__(self, client: ClioDynamicClient):
        super().__init__()
        self.client = client
        self.contacts: list[Contact] = []

    async def on_mount(self):
        logger.debug("ContactsView mounted")
        try:
            self.contacts = await self.client.list_contacts()
            logger.debug("Fetched %d contacts", len(self.contacts))
        except Exception as e:
            logger.exception("Error fetching contacts")
            self.contacts = []
            await self.mount(Static(f"\u26a0\ufe0f Error fetching contacts: {e}"))
        self.refresh()

    def compose(self) -> ComposeResult:
        if not self.contacts:
            yield Static("\ud83d\udcb7 No contacts available.")
        else:
            yield VerticalScroll(
                *[
                    Static(
                        f"\ud83d\udc64 {c.first_name or ''} {c.last_name or ''} — ID: {c.id or 'N/A'}"
                    )
                    for c in self.contacts
                ]
            )
