# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.activity_create_request import ActivityCreateRequest  # noqa: F401
from openapi_server.models.activity_list import ActivityList  # noqa: F401
from openapi_server.models.activity_show import ActivityShow  # noqa: F401
from openapi_server.models.activity_update_request import ActivityUpdateRequest  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401


def test_activity_create(client: TestClient):
    """Test case for activity_create

    Create a new Activity
    """
    activity_create_request = openapi_server.ActivityCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/activities.json",
    #    headers=headers,
    #    json=activity_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_activity_destroy(client: TestClient):
    """Test case for activity_destroy

    Delete a single Activity
    """

    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/activities/{id}.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_activity_index(client: TestClient):
    """Test case for activity_index

    Return the data for all Activities
    """
    params = [("activity_description_id", 56),     ("calendar_entry_id", 56),     ("communication_id", 56),     ("contact_note_id", 56),     ("created_since", '2013-10-20T19:20:30+01:00'),     ("end_date", '2013-10-20T19:20:30+01:00'),     ("expense_category_id", 56),     ("fields", 'fields_example'),     ("flat_rate", True),     ("grant_id", 56),     ("ids", 56),     ("limit", 56),     ("matter_id", 56),     ("matter_note_id", 56),     ("only_unaccounted_for", True),     ("order", 'order_example'),     ("page_token", 'page_token_example'),     ("query", 'query_example'),     ("start_date", '2013-10-20T19:20:30+01:00'),     ("status", 'status_example'),     ("task_id", 56),     ("type", 'type_example'),     ("updated_since", '2013-10-20T19:20:30+01:00'),     ("user_id", 56)]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/activities.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_activity_show(client: TestClient):
    """Test case for activity_show

    Return the data for a single Activity
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
    #    "/activities/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_activity_update(client: TestClient):
    """Test case for activity_update

    Update a single Activity
    """
    activity_update_request = openapi_server.ActivityUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/activities/{id}.json".format(id=56),
    #    headers=headers,
    #    json=activity_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

