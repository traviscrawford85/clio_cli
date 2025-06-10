import logging
import os

from app import DashboardApp
from clio_clients.clio_dynamic_client import ClioDynamicClient
from database.db import initialize_database
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] %(levelname)-8s %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("clio_dashboard")


def run_dashboard():
    logger.debug("Starting dashboard...")
    load_dotenv()
    initialize_database()
    spec_path = os.path.join(os.path.dirname(__file__), "openapi_sdk.yaml")
    client = ClioDynamicClient(spec_path=spec_path, clio_user_id="default")
    DashboardApp(client).run()
    logger.debug("Dashboard exited")


if __name__ == "__main__":
    run_dashboard()
