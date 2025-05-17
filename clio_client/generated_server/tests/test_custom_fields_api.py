# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.custom_field_create_request import CustomFieldCreateRequest  # noqa: F401
from openapi_server.models.custom_field_list import CustomFieldList  # noqa: F401
from openapi_server.models.custom_field_show import CustomFieldShow  # noqa: F401
from openapi_server.models.custom_field_update_request import CustomFieldUpdateRequest  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401


def test_custom_field_create(client: TestClient):
    """Test case for custom_field_create

    Create a new CustomField
    """
    custom_field_create_request = openapi_server.CustomFieldCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/custom_fields.json",
    #    headers=headers,
    #    json=custom_field_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_custom_field_destroy(client: TestClient):
    """Test case for custom_field_destroy

    Delete a single CustomField
    """

    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/custom_fields/{id}.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_custom_field_index(client: TestClient):
    """Test case for custom_field_index

    Return the data for all CustomFields
    """
    params = [("created_since", '2013-10-20T19:20:30+01:00'),     ("deleted", True),     ("field_type", 'field_type_example'),     ("fields", 'fields_example'),     ("ids", 56),     ("limit", 56),     ("order", 'order_example'),     ("page_token", 'page_token_example'),     ("parent_type", 'parent_type_example'),     ("query", 'query_example'),     ("updated_since", '2013-10-20T19:20:30+01:00'),     ("visible_and_required", True)]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/custom_fields.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_custom_field_show(client: TestClient):
    """Test case for custom_field_show

    Return the data for a single CustomField
    """
    params = [("fields", 'fields_example')]
    headers = {
        "if_modified_since": '2013-10-20',
        "if_none_match": 'if_none_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/custom_fields/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_custom_field_update(client: TestClient):
    """Test case for custom_field_update

    Update a single CustomField
    """
    custom_field_update_request = openapi_server.CustomFieldUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/custom_fields/{id}.json".format(id=56),
    #    headers=headers,
    #    json=custom_field_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

