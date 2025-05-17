# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.custom_field_set_create_request import CustomFieldSetCreateRequest  # noqa: F401
from openapi_server.models.custom_field_set_list import CustomFieldSetList  # noqa: F401
from openapi_server.models.custom_field_set_show import CustomFieldSetShow  # noqa: F401
from openapi_server.models.custom_field_set_update_request import CustomFieldSetUpdateRequest  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401


def test_custom_field_set_create(client: TestClient):
    """Test case for custom_field_set_create

    Create a new CustomFieldSet
    """
    custom_field_set_create_request = openapi_server.CustomFieldSetCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/custom_field_sets.json",
    #    headers=headers,
    #    json=custom_field_set_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_custom_field_set_destroy(client: TestClient):
    """Test case for custom_field_set_destroy

    Delete a single CustomFieldSet
    """

    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/custom_field_sets/{id}.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_custom_field_set_index(client: TestClient):
    """Test case for custom_field_set_index

    Return the data for all CustomFieldSets
    """
    params = [("created_since", '2013-10-20T19:20:30+01:00'),     ("displayed", True),     ("fields", 'fields_example'),     ("ids", 56),     ("limit", 56),     ("order", 'order_example'),     ("page_token", 'page_token_example'),     ("parent_type", 'parent_type_example'),     ("query", 'query_example'),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/custom_field_sets.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_custom_field_set_show(client: TestClient):
    """Test case for custom_field_set_show

    Return the data for a single CustomFieldSet
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
    #    "/custom_field_sets/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_custom_field_set_update(client: TestClient):
    """Test case for custom_field_set_update

    Update a single CustomFieldSet
    """
    custom_field_set_update_request = openapi_server.CustomFieldSetUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/custom_field_sets/{id}.json".format(id=56),
    #    headers=headers,
    #    json=custom_field_set_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

