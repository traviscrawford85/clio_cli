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
            from clio_clients.models.contactbase import ContactBase
            response = await self.client.list_contacts()
            # response is already a list
            self.contacts = [ContactBase.model_validate(c) for c in response]
            logger.debug("Fetched %d contacts", len(self.contacts))
        except Exception as e:
            logger.exception("Error fetching contacts")
            self.contacts = []
            await self.mount(Static(f"\u26a0\ufe0f Error fetching contacts: {e}"))
            return
        await self.update_view()


    async def update_view(self):
        await self.remove_children()
        if not self.contacts:
            await self.mount(Static("\ud83d\udcb7 No contacts available."))
        else:
            await self.mount(
                VerticalScroll(
                    *[
                        Static(
                            f"\ud83d\udc64 {(c.first_name or '')} {(c.last_name or '')}{c.name if not (c.first_name or c.last_name) else ''} — ID: {c.id or 'N/A'}"
                        )
                        for c in self.contacts
                    ]
                )
            )
