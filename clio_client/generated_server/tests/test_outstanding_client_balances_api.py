# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date  # noqa: F401
from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.outstanding_client_balance_list import OutstandingClientBalanceList  # noqa: F401


def test_outstanding_client_balance_index(client: TestClient):
    """Test case for outstanding_client_balance_index

    Return the data for all OutstandingClientBalances
    """
    params = [("contact_id", 56),     ("fields", 'fields_example'),     ("last_paid_end_date", '2013-10-20'),     ("last_paid_start_date", '2013-10-20'),     ("limit", 56),     ("newest_bill_due_end_date", '2013-10-20'),     ("newest_bill_due_start_date", '2013-10-20'),     ("originating_attorney_id", 56),     ("page_token", 'page_token_example'),     ("responsible_attorney_id", 56)]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/outstanding_client_balances.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

