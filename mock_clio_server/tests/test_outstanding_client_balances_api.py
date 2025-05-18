# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date  # noqa: F401
from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401


def test_outstanding_client_balance_index(client: TestClient):
    """Test case for outstanding_client_balance_index

    Return the data for all OutstandingClientBalances
    """
    params = [("contact_idquery", 56),     ("fieldsquery", 'fieldsquery_example'),     ("last_paid_end_datequery", '2013-10-20'),     ("last_paid_start_datequery", '2013-10-20'),     ("limitquery", 56),     ("newest_bill_due_end_datequery", '2013-10-20'),     ("newest_bill_due_start_datequery", '2013-10-20'),     ("originating_attorney_idquery", 56),     ("page_tokenquery", 'page_tokenquery_example'),     ("responsible_attorney_idquery", 56)]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
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

