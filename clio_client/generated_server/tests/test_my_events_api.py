# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.my_event_list import MyEventList  # noqa: F401
from openapi_server.models.my_event_show import MyEventShow  # noqa: F401
from openapi_server.models.my_event_update_request import MyEventUpdateRequest  # noqa: F401


def test_my_event_destroy(client: TestClient):
    """Test case for my_event_destroy

    Clear (delete) a single in-app notification event
    """

    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/internal_notifications/my_events/{id}.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_my_event_index(client: TestClient):
    """Test case for my_event_index

    Return the data for all of my in-app notification events
    """
    params = [("fields", 'fields_example'),     ("limit", 56),     ("page_token", 'page_token_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/internal_notifications/my_events.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_my_event_update(client: TestClient):
    """Test case for my_event_update

    Mark a single in-app notification event as read/unread
    """
    my_event_update_request = openapi_server.MyEventUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/internal_notifications/my_events/{id}.json".format(id=56),
    #    headers=headers,
    #    json=my_event_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

