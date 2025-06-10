import logging
from textual.app import App
from textual.widget import Widget
from textual.widgets import Header, Footer, Static
from views.tasks_view import TasksView
from views.matters_view import MattersView
from views.contacts_view import ContactsView

logger = logging.getLogger(__name__)


class DashboardApp(App):
    CSS = ""  # Add any styling if needed

    def __init__(self, client):
        super().__init__()
        self.client = client
        self.current_view = "matters"

    async def on_mount(self):
        logger.debug("Dashboard mounted, switching to matters view")
        await self.switch_view("matters")

    async def switch_view(self, view: str):
        logger.debug("Switching view to %s", view)
        container = self.query_one("#main", expect_type=Widget)
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
            await container.mount(Static(f"⚠️ Failed to load {view}: {e}"))

    def compose(self):
        yield Header()
        yield Static(id="main")
        yield Footer()

    def on_key(self, event):
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
