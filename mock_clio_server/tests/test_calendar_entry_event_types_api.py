# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.activity_show import ActivityShow  # noqa: F401
from clio_mock.models.calendar_entry_event_type_create_request import CalendarEntryEventTypeCreateRequest  # noqa: F401
from clio_mock.models.calendar_entry_event_type_update_request import CalendarEntryEventTypeUpdateRequest  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401


def test_calendar_entry_event_type_create(client: TestClient):
    """Test case for calendar_entry_event_type_create

    Create a new calendar entry event type
    """
    calendar_entry_event_type_create_request = clio_mock.CalendarEntryEventTypeCreateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
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
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/calendar_entry_event_types/{id}.json".format(idpath=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_calendar_entry_event_type_index(client: TestClient):
    """Test case for calendar_entry_event_type_index

    Return the data for all calendar entry event types
    """
    params = [("created_sincequery", '2013-10-20T19:20:30+01:00'),     ("fieldsquery", 'fieldsquery_example'),     ("idsquery", 56),     ("limitquery", 56),     ("page_tokenquery", 'page_tokenquery_example'),     ("updated_sincequery", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
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
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_modified_sinc_eheader": '2013-10-20',
        "if_none_matc_hheader": 'if_none_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/calendar_entry_event_types/{id}.json".format(idpath=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_calendar_entry_event_type_update(client: TestClient):
    """Test case for calendar_entry_event_type_update

    Update a single calendar entry event type
    """
    calendar_entry_event_type_update_request = clio_mock.CalendarEntryEventTypeUpdateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_matc_hheader": 'if_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/calendar_entry_event_types/{id}.json".format(idpath=56),
    #    headers=headers,
    #    json=calendar_entry_event_type_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

