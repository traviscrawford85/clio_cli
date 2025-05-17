# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.matter_create_request import MatterCreateRequest  # noqa: F401
from openapi_server.models.matter_list import MatterList  # noqa: F401
from openapi_server.models.matter_show import MatterShow  # noqa: F401
from openapi_server.models.matter_update_request import MatterUpdateRequest  # noqa: F401


def test_matter_create(client: TestClient):
    """Test case for matter_create

    Create a new Matter
    """
    matter_create_request = openapi_server.MatterCreateRequest()
    params = [("custom_field_ids", 56),     ("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/matters.json",
    #    headers=headers,
    #    json=matter_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_matter_destroy(client: TestClient):
    """Test case for matter_destroy

    Delete a single Matter
    """

    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/matters/{id}.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_matter_index(client: TestClient):
    """Test case for matter_index

    Return the data for all Matters
    """
    params = [("billable", True),     ("client_id", 56),     ("close_date", 'close_date_example'),     ("created_since", '2013-10-20T19:20:30+01:00'),     ("custom_field_ids", 56),     ("custom_field_values", 'custom_field_values_example'),     ("fields", 'fields_example'),     ("grant_id", 56),     ("group_id", 56),     ("ids", 56),     ("limit", 56),     ("notification_event_subscriber_user_id", 56),     ("open_date", 'open_date_example'),     ("order", 'order_example'),     ("originating_attorney_id", 56),     ("page_token", 'page_token_example'),     ("pending_date", 'pending_date_example'),     ("practice_area_id", 56),     ("query", 'query_example'),     ("responsible_attorney_id", 56),     ("responsible_staff_id", 56),     ("status", 'status_example'),     ("subscriber_user_id", 56),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/matters.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_matter_show(client: TestClient):
    """Test case for matter_show

    Return the data for a single Matter
    """
    params = [("custom_field_ids", 56),     ("fields", 'fields_example')]
    headers = {
        "if_modified_since": '2013-10-20',
        "if_none_match": 'if_none_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/matters/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_matter_update(client: TestClient):
    """Test case for matter_update

    Update a single Matter
    """
    matter_update_request = openapi_server.MatterUpdateRequest()
    params = [("custom_field_ids", 56),     ("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/matters/{id}.json".format(id=56),
    #    headers=headers,
    #    json=matter_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

