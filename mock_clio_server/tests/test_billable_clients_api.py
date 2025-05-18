# coding: utf-8

from fastapi.testclient import TestClient


from datetime import datetime  # noqa: F401
from pydantic import Field, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401


def test_billable_client_index(client: TestClient):
    """Test case for billable_client_index

    Return the data for all BillableClients
    """
    params = [("client_idquery", 56),     ("custom_field_valuesquery", 'custom_field_valuesquery_example'),     ("end_datequery", '2013-10-20T19:20:30+01:00'),     ("fieldsquery", 'fieldsquery_example'),     ("limitquery", 56),     ("matter_idquery", 56),     ("originating_attorney_idquery", 56),     ("page_tokenquery", 'page_tokenquery_example'),     ("queryquery", 'queryquery_example'),     ("responsible_attorney_idquery", 56),     ("start_datequery", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/billable_clients.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

