from textual.app import App, ComposeResult
from textual.containers import Container, VerticalScroll
from textual.widgets import Header, Footer, Static
import os
import sys


sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from dotenv import load_dotenv
from typing import List

from clio_client import clio_api_client
from clio_client.openapi_client.models import Matter
from clio_client.openapi_client.api import MattersApi

# Load environment variables from .env file
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

def get_clio_client() -> clio_api_client.ClioApiClient:
    """Instantiate and return a Clio API client using environment variables."""
    token = os.getenv("CLIO_API_TOKEN")
    base_url = os.getenv("CLIO_API_BASE_URL")
    if not token:
        raise EnvironmentError("CLIO_API_TOKEN not set in environment or .env file.")
    if not base_url:
        raise EnvironmentError("CLIO_API_BASE_URL not set in environment or .env file.")
    return clio_api_client.ClioApiClient(
        token=token,
        base_url=base_url
    )

try:
    clio = get_clio_client()
    matters_api = MattersApi(clio)
except Exception as e:
    clio = None
    matters_api = None
    print(f"Failed to initialize Clio client: {e}")

class MatterItem(Static):
    """Widget to display a single Matter."""
    def __init__(self, matter: Matter):
        label = f"{matter.display_number} — {matter.description or 'No description'}"
        super().__init__(f"📁 [b cyan]{label}[/]")

class ClioMatterDashboard(App):
    """Textual app dashboard for displaying Clio Matters."""
    CSS_PATH = None

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Container(
            VerticalScroll(
                *[MatterItem(m) for m in self.get_matters()]
            )
        )
        yield Footer()

    def get_matters(self) -> List[Matter]:
        """Fetch matters from Clio API, or return empty list on error."""
        if not matters_api:
            print("Clio client not initialized. Set CLIO_API_TOKEN in your .env file.")
            return []
        try:
            response = matters_api.matter_index()
            return response.data or []
        except Exception as e:
            print(f"Error fetching matters: {e}")
            return []

    def on_key(self, event):
        """Exit the app when 'q' is pressed."""
        if event.key == "q":
            self.exit()

if __name__ == "__main__":
    ClioMatterDashboard().run()
