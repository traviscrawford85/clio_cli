import logging

from textual.app import App
from textual.containers import Container
from textual.widget import Widget
from textual.widgets import Footer, Header, Static
from utils.clean_strings import safe_unicode  # Add this import
from views.contacts_view import ContactsView
from views.matters_view import MattersView
from views.tasks_view import TasksView

logger = logging.getLogger(__name__)


class DashboardApp(App[Widget]):
    CSS_PATH = None  # or point to your .tcss file
    BINDINGS = [
        ("1", "switch('matters')", "Matters"),
        ("2", "switch('contacts')", "Contacts"),
        ("3", "switch('tasks')", "Tasks"),
        ("q", "quit", "Quit"),
    ]

    def __init__(self, client):
        super().__init__()
        self.client = client

    def compose(self):
        yield Header()
        yield Container(id="main")
        yield Footer()

    async def on_mount(self):
        logger.debug("Dashboard mounted, switching to matters view")
        await self.switch_view("matters")

    async def switch_view(self, view: str):
        logger.debug("Switching view to %s", view)
        container = self.query_one("#main", expect_type=Container)
        await container.remove_children()
        try:
            if view == "matters":
                await container.mount(MattersView(self.client))
            elif view == "contacts":
                await container.mount(ContactsView(self.client))
            elif view == "tasks":
                await container.mount(TasksView(self.client))
            else:
                await container.mount(Static(f"Unknown view '{view}'"))
        except Exception as e:
            logger.exception("Error mounting view '%s'", view)
            # Sanitize the error message before displaying
            await container.mount(Static(safe_unicode(f"⚠️ Failed to load {view}: {e}")))

    from textual.events import Key

    def on_key(self, event: Key):
        key = event.key
        logger.debug("Key pressed: %s", key)
        if key == "1":
            self.run_worker(self.switch_view("matters"))
        elif key == "2":
            self.run_worker(self.switch_view("contacts"))
        elif key == "3":
            self.run_worker(self.switch_view("tasks"))
        elif key in ("q", "ctrl+q"):
            logger.debug("Quit key pressed, exiting")
            self.exit()
