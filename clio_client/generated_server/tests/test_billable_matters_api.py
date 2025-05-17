# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date  # noqa: F401
from pydantic import Field, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.billable_matter_list import BillableMatterList  # noqa: F401
from openapi_server.models.billable_matter_show import BillableMatterShow  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401


def test_billable_matter_ids(client: TestClient):
    """Test case for billable_matter_ids

    Returns the unique identifiers of all BillableMatter
    """
    params = [("client_id", 56),     ("custom_field_values", 'custom_field_values_example'),     ("end_date", '2013-10-20'),     ("fields", 'fields_example'),     ("limit", 56),     ("matter_id", 56),     ("originating_attorney_id", 56),     ("page_token", 'page_token_example'),     ("query", 'query_example'),     ("responsible_attorney_id", 56),     ("start_date", '2013-10-20')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/billable_matters/ids.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_billable_matter_index(client: TestClient):
    """Test case for billable_matter_index

    Return the data for all BillableMatters
    """
    params = [("client_id", 56),     ("custom_field_values", 'custom_field_values_example'),     ("end_date", '2013-10-20'),     ("fields", 'fields_example'),     ("limit", 56),     ("matter_id", 56),     ("originating_attorney_id", 56),     ("page_token", 'page_token_example'),     ("query", 'query_example'),     ("responsible_attorney_id", 56),     ("start_date", '2013-10-20')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/billable_matters.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

