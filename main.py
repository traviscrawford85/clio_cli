# main.py or clio_dashboard_app/__main__.py

import os

from dotenv import load_dotenv
from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.widgets import Footer, Header, Static

# Update the import below to match the actual class or function name in clio_api_client.py
# For example, if the class is named ClioClient, use:
# from .clio_client.clio_api_client import ClioClient
from clio_client.clio_api_client import \
    ClioApiClient  # <-- Ensure this class exists in clio_api_client.py
from views.contacts_view import ContactsView
from views.matters_view import MattersView
from views.tasks_view import TasksView

load_dotenv()  # Load .env file for token, base_url

def get_clio_client() -> ClioApiClient:
    token = os.getenv("CLIO_API_TOKEN")
    base_url = os.getenv("CLIO_API_BASE_URL", "http://localhost:8000")
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
    container = self.query_one("#main", expect_type=Widget)
    try:
        self.current_view = view
        container.remove_children()
        if view == "matters":
            await container.mount(MattersView(self.client))
        elif view == "contacts":
            await container.mount(ContactsView(self.client))
        elif view == "tasks":
            await container.mount(TasksView(self.client))
    except Exception as e:
        await container.mount(Static(f"Failed to load {view} view: {e}"))


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
