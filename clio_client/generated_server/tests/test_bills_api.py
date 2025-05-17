# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.bill_list import BillList  # noqa: F401
from openapi_server.models.bill_show import BillShow  # noqa: F401
from openapi_server.models.bill_update_request import BillUpdateRequest  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401


def test_bill_destroy(client: TestClient):
    """Test case for bill_destroy

    Delete or void a Bill
    """

    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/bills/{id}.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_bill_index(client: TestClient):
    """Test case for bill_index

    Return the data for all Bills
    """
    params = [("client_id", 56),     ("created_since", '2013-10-20T19:20:30+01:00'),     ("currency_id", 56),     ("custom_field_values", 'custom_field_values_example'),     ("due_after", '2013-10-20'),     ("due_at", '2013-10-20'),     ("due_before", '2013-10-20'),     ("fields", 'fields_example'),     ("ids", 56),     ("issued_after", '2013-10-20'),     ("issued_before", '2013-10-20'),     ("last_sent_end_date", '2013-10-20'),     ("last_sent_start_date", '2013-10-20'),     ("limit", 56),     ("matter_id", 56),     ("order", 'order_example'),     ("originating_attorney_id", 56),     ("overdue_only", True),     ("page_token", 'page_token_example'),     ("query", 56),     ("responsible_attorney_id", 56),     ("state", 'state_example'),     ("status", 'status_example'),     ("type", 'type_example'),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/bills.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_bill_preview(client: TestClient):
    """Test case for bill_preview

    Returns the pre-rendered html for the Bill
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/bills/{id}/preview.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_bill_show(client: TestClient):
    """Test case for bill_show

    Return the data for a single Bill
    """
    params = [("fields", 'fields_example'),     ("navigation_next", 56),     ("navigation_previous", 56)]
    headers = {
        "if_modified_since": '2013-10-20',
        "if_none_match": 'if_none_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/bills/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_bill_update(client: TestClient):
    """Test case for bill_update

    Update a single Bill
    """
    bill_update_request = openapi_server.BillUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/bills/{id}.json".format(id=56),
    #    headers=headers,
    #    json=bill_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

