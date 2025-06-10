# matters_view.py
from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.widget import Widget
from textual.widgets import Static
from clio_clients.models.matter import Matter
from clio_clients.clio_dynamic_client import ClioDynamicClient
import logging

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
        self.refresh()

    def compose(self) -> ComposeResult:
        if not self.matters:
            yield Static("\ud83d\udccd No matters available.")
        else:
            yield VerticalScroll(
                *[
                    Static(
                        f"\ud83d\udcc1 Title: {m.title or 'Untitled'}\n"
                        f"\ud83d\udd22 ID: {m.id or 'N/A'}\n"
                        f"\ud83d\udc82 Status: {m.status or 'N/A'}\n"
                        f"\ud83d\udcc5 Created: {m.created_at or 'N/A'}\n"
                        + "\u2500" * 40
                    )
                    for m in self.matters
                ]
            )
