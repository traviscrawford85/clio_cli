# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.calendar_visibility_list import CalendarVisibilityList  # noqa: F401
from openapi_server.models.calendar_visibility_show import CalendarVisibilityShow  # noqa: F401
from openapi_server.models.calendar_visibility_update_request import CalendarVisibilityUpdateRequest  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401


def test_calendar_visibility_index(client: TestClient):
    """Test case for calendar_visibility_index

    Return the data for all CalendarVisibilities
    """
    params = [("created_since", '2013-10-20T19:20:30+01:00'),     ("fields", 'fields_example'),     ("ids", 56),     ("limit", 56),     ("page_token", 'page_token_example'),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/task_calendars.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_calendar_visibility_show(client: TestClient):
    """Test case for calendar_visibility_show

    Return the data for a single CalendarVisibility
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
    #    "/task_calendars/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_calendar_visibility_update(client: TestClient):
    """Test case for calendar_visibility_update

    Update a single CalendarVisibility
    """
    calendar_visibility_update_request = openapi_server.CalendarVisibilityUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/task_calendars/{id}.json".format(id=56),
    #    headers=headers,
    #    json=calendar_visibility_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

