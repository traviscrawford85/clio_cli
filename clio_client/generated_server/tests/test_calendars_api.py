# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.calendar_create_request import CalendarCreateRequest  # noqa: F401
from openapi_server.models.calendar_list import CalendarList  # noqa: F401
from openapi_server.models.calendar_show import CalendarShow  # noqa: F401
from openapi_server.models.calendar_update_request import CalendarUpdateRequest  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401


def test_calendar_create(client: TestClient):
    """Test case for calendar_create

    Create a new Calendar
    """
    calendar_create_request = openapi_server.CalendarCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/calendars.json",
    #    headers=headers,
    #    json=calendar_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_calendar_destroy(client: TestClient):
    """Test case for calendar_destroy

    Delete a single Calendar
    """

    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/calendars/{id}.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_calendar_index(client: TestClient):
    """Test case for calendar_index

    Return the data for all Calendars
    """
    params = [("created_since", '2013-10-20T19:20:30+01:00'),     ("fields", 'fields_example'),     ("filter_inactive_users", True),     ("ids", 56),     ("limit", 56),     ("order", 'order_example'),     ("owner", True),     ("page_token", 'page_token_example'),     ("source", 'source_example'),     ("type", 'type_example'),     ("updated_since", '2013-10-20T19:20:30+01:00'),     ("visible", True),     ("writeable", True)]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/calendars.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_calendar_show(client: TestClient):
    """Test case for calendar_show

    Return the data for a single Calendar
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
    #    "/calendars/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_calendar_update(client: TestClient):
    """Test case for calendar_update

    Update a single Calendar
    """
    calendar_update_request = openapi_server.CalendarUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/calendars/{id}.json".format(id=56),
    #    headers=headers,
    #    json=calendar_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

