# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401
from clio_mock.models.my_event_update_request import MyEventUpdateRequest  # noqa: F401


def test_my_event_destroy(client: TestClient):
    """Test case for my_event_destroy

    Clear (delete) a single in-app notification event
    """

    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/internal_notifications/my_events/{id}.json".format(idpath=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_my_event_index(client: TestClient):
    """Test case for my_event_index

    Return the data for all of my in-app notification events
    """
    params = [("fieldsquery", 'fieldsquery_example'),     ("limitquery", 56),     ("page_tokenquery", 'page_tokenquery_example')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
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
    my_event_update_request = clio_mock.MyEventUpdateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_matc_hheader": 'if_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/internal_notifications/my_events/{id}.json".format(idpath=56),
    #    headers=headers,
    #    json=my_event_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

