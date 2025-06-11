# matters_view.py
import logging

from clio_clients.clio_dynamic_client import ClioDynamicClient
from clio_clients.models.matter import Matter
from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.widget import Widget
from textual.widgets import Static

logger = logging.getLogger(__name__)


class MattersView(Widget):
    def __init__(self, client: ClioDynamicClient):
        super().__init__()
        self.client = client
        self.matters: list[Matter] = []

    async def on_mount(self):
        logger.debug("MattersView mounted")
        try:
            self.matters = await self.client.list_matters()
            logger.debug("Fetched %d matters", len(self.matters))
        except Exception as e:
            logger.exception("Error fetching matters")
            self.matters = []
            await self.mount(Static(f"\u26a0\ufe0f Error fetching matters: {e}"))
            return  # Don't continue if error
        await self.update_view()

    async def update_view(self):
        await self.remove_children()
        if not self.matters:
            await self.mount(Static("\ud83d\udccd No matters available."))
        else:
            await self.mount(
                VerticalScroll(
                    *[
                        Static(
                            f"\ud83d\udcc1 Matter: {m.display_number or 'Untitled'}\n"
                            f"\ud83d\udd22 ID: {m.id or 'N/A'}\n"
                            f"\ud83d\udc82 Status: {getattr(m, 'status', 'N/A')}\n"
                            f"\ud83d\udcc5 Created: {getattr(m, 'created_at', 'N/A')}\n"
                            + "\u2500" * 40
                        )
                        for m in self.matters
                    ]
                )
            )
