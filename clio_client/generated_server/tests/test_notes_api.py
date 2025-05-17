# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.note_create_request import NoteCreateRequest  # noqa: F401
from openapi_server.models.note_list import NoteList  # noqa: F401
from openapi_server.models.note_show import NoteShow  # noqa: F401
from openapi_server.models.note_update_request import NoteUpdateRequest  # noqa: F401


def test_note_create(client: TestClient):
    """Test case for note_create

    Create a new Note
    """
    note_create_request = openapi_server.NoteCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/notes.json",
    #    headers=headers,
    #    json=note_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_note_destroy(client: TestClient):
    """Test case for note_destroy

    Delete a single Note
    """

    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/notes/{id}.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_note_index(client: TestClient):
    """Test case for note_index

    Return the data for all Notes
    """
    params = [("contact_id", 56),     ("created_since", '2013-10-20T19:20:30+01:00'),     ("fields", 'fields_example'),     ("has_time_entries", True),     ("ids", 56),     ("limit", 56),     ("matter_id", 56),     ("order", 'order_example'),     ("page_token", 'page_token_example'),     ("query", 'query_example'),     ("type", 'type_example'),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/notes.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_note_show(client: TestClient):
    """Test case for note_show

    Return the data for a single Note
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
    #    "/notes/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_note_update(client: TestClient):
    """Test case for note_update

    Update a single Note
    """
    note_update_request = openapi_server.NoteUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/notes/{id}.json".format(id=56),
    #    headers=headers,
    #    json=note_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

