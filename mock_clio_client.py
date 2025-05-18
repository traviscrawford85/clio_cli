import os
from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.widgets import Footer, Header, Static, Tabs, Input
from textual.containers import VerticalScroll, Horizontal
from textual.events import Key
from textual.binding import Binding
from textual.reactive import reactive
from dotenv import load_dotenv

# Simulated mock client (replace with real ClioApiClient when needed)
class MockClioClient:
    async def get_matters(self):
        return [
            {"number": "PI-001", "description": "Auto Accident - Rear-End Collision"},
            {"number": "PI-002", "description": "Premises Liability - Slip and Fall"},
            {"number": "PI-003", "description": "Medical Malpractice - Surgical Error"},
            {"number": "PI-004", "description": "General Negligence - Dog Bite"},
            {"number": "PI-005", "description": "School Injury - Playground Accident"},
        ]

    async def get_contacts(self):
        return [
            {"name": "Alice Example", "email": "alice@example.com"},
            {"name": "Bob Client", "email": "bob@injurylaw.com"},
        ]

    async def get_tasks(self):
        return [
            {"title": "Schedule IME for PI-001", "due_date": "2025-06-01"},
            {"title": "Send demand letter for PI-002", "due_date": "2025-06-03"},
        ]


class MattersView(Widget):
    filter_text = reactive("")

    def __init__(self, client):
        super().__init__()
        self.client = client
        self.data = []

    async def on_mount(self):
        self.data = await self.client.get_matters()
        await self.refresh_view()
        await self.mount(Input(placeholder="Filter matters...", id="filter"))

    async def refresh_view(self):
        await self.query("VerticalScroll").remove()
        filtered = [m for m in self.data if self.filter_text.lower() in m['description'].lower()]
        await self.mount(VerticalScroll(
            *[Static(f"📁 {m['number']}: {m['description']}") for m in filtered]
        ))
        await self.mount(Static(f"Total: {len(filtered)}", id="summary"))

    async def on_input_changed(self, message: Input.Changed) -> None:
        self.filter_text = message.value
        await self.refresh_view()


class ContactsView(Widget):
    def __init__(self, client):
        super().__init__()
        self.client = client

    async def on_mount(self):
        data = await self.client.get_contacts()
        await self.mount(VerticalScroll(
            *[Static(f"👤 {c['name']} <{c['email']}>") for c in data]
        ))
        await self.mount(Static(f"Total: {len(data)}", id="summary"))


class TasksView(Widget):
    def __init__(self, client):
        super().__init__()
        self.client = client

    async def on_mount(self):
        data = await self.client.get_tasks()
        await self.mount(VerticalScroll(
            *[Static(f"✅ {t['title']} (Due: {t['due_date']})") for t in data]
        ))
        await self.mount(Static(f"Total: {len(data)}", id="summary"))


class DashboardApp(App):
    CSS_PATH = "textual.css"
    BINDINGS = [
        Binding("1", "switch('Matters')", "Matters"),
        Binding("2", "switch('Contacts')", "Contacts"),
        Binding("3", "switch('Tasks')", "Tasks"),
        Binding("r", "refresh", "Refresh"),
        Binding("q", "quit", "Quit"),
        Binding("ctrl+q", "quit", "Quit"),
    ]

    def __init__(self, client):
        super().__init__()
        self.client = client
        self.current_view = "Matters"

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Tabs("Matters", "Contacts", "Tasks", id="main-tabs")
        yield Static("Loading...", id="main")
        yield Static("Press 1-Matters, 2-Contacts, 3-Tasks, R-Refresh, Q-Quit", id="help")
        yield Footer()

    async def on_mount(self) -> None:
        await self.switch_view("Matters")

    async def switch_view(self, tab: str) -> None:
        container = self.query_one("#main", expect_type=Widget)
        container.remove_children()
        self.current_view = tab
        if tab == "Matters":
            await container.mount(MattersView(self.client))
        elif tab == "Contacts":
            await container.mount(ContactsView(self.client))
        elif tab == "Tasks":
            await container.mount(TasksView(self.client))

    def on_tabs_tab_activated(self, event: Tabs.TabActivated) -> None:
        self.call_later(lambda: self.switch_view(str(event.tab.label)))

    def action_switch(self, view: str) -> None:
        self.call_later(lambda: self.switch_view(view))

    def action_refresh(self) -> None:
        self.call_later(lambda: self.switch_view(self.current_view))


def run_dashboard():
    load_dotenv()
    client = MockClioClient()  # swap with get_clio_client() if needed
    DashboardApp(client).run()


if __name__ == "__main__":
    run_dashboard()
