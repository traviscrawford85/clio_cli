# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.calendar_entry_create_request import CalendarEntryCreateRequest  # noqa: F401
from openapi_server.models.calendar_entry_list import CalendarEntryList  # noqa: F401
from openapi_server.models.calendar_entry_show import CalendarEntryShow  # noqa: F401
from openapi_server.models.calendar_entry_update_request import CalendarEntryUpdateRequest  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401


def test_calendar_entry_create(client: TestClient):
    """Test case for calendar_entry_create

    Create a new CalendarEntry
    """
    calendar_entry_create_request = openapi_server.CalendarEntryCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/calendar_entries.json",
    #    headers=headers,
    #    json=calendar_entry_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_calendar_entry_destroy(client: TestClient):
    """Test case for calendar_entry_destroy

    Delete a single CalendarEntry
    """

    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/calendar_entries/{id}.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_calendar_entry_index(client: TestClient):
    """Test case for calendar_entry_index

    Return the data for all CalendarEntries
    """
    params = [("calendar_id", 56),     ("created_since", '2013-10-20T19:20:30+01:00'),     ("expanded", True),     ("external_property_name", 'external_property_name_example'),     ("external_property_value", 'external_property_value_example'),     ("fields", 'fields_example'),     ("var_from", '2013-10-20T19:20:30+01:00'),     ("has_court_rule", True),     ("ids", 56),     ("is_all_day", True),     ("limit", 56),     ("matter_id", 56),     ("owner_entries_across_all_users", True),     ("page_token", 'page_token_example'),     ("query", 'query_example'),     ("source", 'source_example'),     ("to", '2013-10-20T19:20:30+01:00'),     ("updated_since", '2013-10-20T19:20:30+01:00'),     ("visible", True)]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/calendar_entries.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_calendar_entry_show(client: TestClient):
    """Test case for calendar_entry_show

    Return the data for a single CalendarEntry
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
    #    "/calendar_entries/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_calendar_entry_update(client: TestClient):
    """Test case for calendar_entry_update

    Update a single CalendarEntry
    """
    calendar_entry_update_request = openapi_server.CalendarEntryUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/calendar_entries/{id}.json".format(id=56),
    #    headers=headers,
    #    json=calendar_entry_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

