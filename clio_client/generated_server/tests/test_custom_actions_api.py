# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.custom_action_create_request import CustomActionCreateRequest  # noqa: F401
from openapi_server.models.custom_action_list import CustomActionList  # noqa: F401
from openapi_server.models.custom_action_show import CustomActionShow  # noqa: F401
from openapi_server.models.custom_action_update_request import CustomActionUpdateRequest  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401


def test_custom_action_create(client: TestClient):
    """Test case for custom_action_create

    Create a new CustomAction
    """
    custom_action_create_request = openapi_server.CustomActionCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/custom_actions.json",
    #    headers=headers,
    #    json=custom_action_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_custom_action_destroy(client: TestClient):
    """Test case for custom_action_destroy

    Delete a single CustomAction
    """

    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/custom_actions/{id}.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_custom_action_index(client: TestClient):
    """Test case for custom_action_index

    Return the data for all CustomActions
    """
    params = [("created_since", '2013-10-20T19:20:30+01:00'),     ("fields", 'fields_example'),     ("ids", 56),     ("limit", 56),     ("page_token", 'page_token_example'),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/custom_actions.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_custom_action_show(client: TestClient):
    """Test case for custom_action_show

    Return the data for a single CustomAction
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
    #    "/custom_actions/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_custom_action_update(client: TestClient):
    """Test case for custom_action_update

    Update a single CustomAction
    """
    custom_action_update_request = openapi_server.CustomActionUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/custom_actions/{id}.json".format(id=56),
    #    headers=headers,
    #    json=custom_action_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

