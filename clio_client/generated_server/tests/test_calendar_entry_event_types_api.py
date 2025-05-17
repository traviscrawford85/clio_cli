# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.calendar_entry_event_type import CalendarEntryEventType  # noqa: F401
from openapi_server.models.calendar_entry_event_type_create_request import CalendarEntryEventTypeCreateRequest  # noqa: F401
from openapi_server.models.calendar_entry_event_type_update_request import CalendarEntryEventTypeUpdateRequest  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401


def test_calendar_entry_event_type_create(client: TestClient):
    """Test case for calendar_entry_event_type_create

    Create a new calendar entry event type
    """
    calendar_entry_event_type_create_request = openapi_server.CalendarEntryEventTypeCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/calendar_entry_event_types.json",
    #    headers=headers,
    #    json=calendar_entry_event_type_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_calendar_entry_event_type_destroy(client: TestClient):
    """Test case for calendar_entry_event_type_destroy

    Delete a single calendar entry event type
    """

    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/calendar_entry_event_types/{id}.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_calendar_entry_event_type_index(client: TestClient):
    """Test case for calendar_entry_event_type_index

    Return the data for all calendar entry event types
    """
    params = [("created_since", '2013-10-20T19:20:30+01:00'),     ("fields", 'fields_example'),     ("ids", 56),     ("limit", 56),     ("page_token", 'page_token_example'),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/calendar_entry_event_types.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_calendar_entry_event_type_show(client: TestClient):
    """Test case for calendar_entry_event_type_show

    Return the data for a single calendar entry event type
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
    #    "/calendar_entry_event_types/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_calendar_entry_event_type_update(client: TestClient):
    """Test case for calendar_entry_event_type_update

    Update a single calendar entry event type
    """
    calendar_entry_event_type_update_request = openapi_server.CalendarEntryEventTypeUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/calendar_entry_event_types/{id}.json".format(id=56),
    #    headers=headers,
    #    json=calendar_entry_event_type_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

