# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.reminder_create_request import ReminderCreateRequest  # noqa: F401
from openapi_server.models.reminder_list import ReminderList  # noqa: F401
from openapi_server.models.reminder_show import ReminderShow  # noqa: F401
from openapi_server.models.reminder_update_request import ReminderUpdateRequest  # noqa: F401


def test_reminder_create(client: TestClient):
    """Test case for reminder_create

    Create a new Reminder
    """
    reminder_create_request = openapi_server.ReminderCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/reminders.json",
    #    headers=headers,
    #    json=reminder_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_reminder_destroy(client: TestClient):
    """Test case for reminder_destroy

    Delete a single Reminder
    """

    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/reminders/{id}.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_reminder_index(client: TestClient):
    """Test case for reminder_index

    Return the data for all Reminders
    """
    params = [("created_since", '2013-10-20T19:20:30+01:00'),     ("fields", 'fields_example'),     ("ids", 56),     ("limit", 56),     ("notification_method_id", 56),     ("order", 'order_example'),     ("page_token", 'page_token_example'),     ("state", 'state_example'),     ("subject_id", 56),     ("subject_type", 'subject_type_example'),     ("updated_since", '2013-10-20T19:20:30+01:00'),     ("user_id", 56)]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/reminders.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_reminder_show(client: TestClient):
    """Test case for reminder_show

    Return the data for a single Reminder
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
    #    "/reminders/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_reminder_update(client: TestClient):
    """Test case for reminder_update

    Update a single Reminder
    """
    reminder_update_request = openapi_server.ReminderUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/reminders/{id}.json".format(id=56),
    #    headers=headers,
    #    json=reminder_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

