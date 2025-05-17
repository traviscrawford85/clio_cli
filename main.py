# main.py or clio_dashboard_app/__main__.py

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.widget import Widget
from dotenv import load_dotenv
import os
from clio_client.clio_api_client import ClioApiClient
from views.matters_view import MattersView
from views.contacts_view import ContactsView
from views.tasks_view import TasksView

load_dotenv()  # Load .env file for token, base_url

def get_clio_client() -> ClioApiClient:
    token = os.getenv("CLIO_API_TOKEN")
    base_url = os.getenv("CLIO_API_BASE_URL", "https://app.clio.com/api/v4")
    if not token:
        raise EnvironmentError("CLIO_API_TOKEN is missing.")
    return ClioApiClient(token=token, base_url=base_url)


class DashboardApp(App):
    def __init__(self, client: ClioApiClient):
        super().__init__()
        self.client = client
        self.current_view = "matters"

    async def on_mount(self):
        await self.switch_view("matters")

    async def switch_view(self, view: str):
        self.current_view = view
        container = self.query_one("#main", expect_type=Widget)
        container.remove_children()
        if view == "matters":
            container.mount(MattersView(self.client))
        elif view == "contacts":
            container.mount(ContactsView(self.client))
        elif view == "tasks":
            container.mount(TasksView(self.client))

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static(id="main")
        yield Footer()

    def on_key(self, event):
        if event.key == "1":
            self.call_later(lambda: self.switch_view("matters"))
        elif event.key == "2":
            self.call_later(lambda: self.switch_view("contacts"))
        elif event.key == "3":
            self.call_later(lambda: self.switch_view("tasks"))
        elif event.key == "q":
            self.exit()


def run_dashboard():
    try:
        client = get_clio_client()
        DashboardApp(client).run()
    except Exception as e:
        print(f"❌ Failed to start app: {e}")


if __name__ == "__main__":
    run_dashboard()
