# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.group_create_request import GroupCreateRequest  # noqa: F401
from openapi_server.models.group_list import GroupList  # noqa: F401
from openapi_server.models.group_show import GroupShow  # noqa: F401


def test_group_create(client: TestClient):
    """Test case for group_create

    Create a new Group
    """
    group_create_request = openapi_server.GroupCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/groups.json",
    #    headers=headers,
    #    json=group_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_group_destroy(client: TestClient):
    """Test case for group_destroy

    Delete a single Group
    """

    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/groups/{id}.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_group_index(client: TestClient):
    """Test case for group_index

    Return the data for all Groups
    """
    params = [("archived", True),     ("created_since", '2013-10-20T19:20:30+01:00'),     ("fields", 'fields_example'),     ("ids", 56),     ("limit", 56),     ("name", 'name_example'),     ("order", 'order_example'),     ("page_token", 'page_token_example'),     ("query", 'query_example'),     ("type", 'type_example'),     ("updated_since", '2013-10-20T19:20:30+01:00'),     ("user_id", 56)]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/groups.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_group_show(client: TestClient):
    """Test case for group_show

    Return the data for a single Group
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
    #    "/groups/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_group_update(client: TestClient):
    """Test case for group_update

    Update a single Group
    """
    group_create_request = openapi_server.GroupCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/groups/{id}.json".format(id=56),
    #    headers=headers,
    #    json=group_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

