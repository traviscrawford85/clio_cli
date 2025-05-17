# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.practice_area_create_request import PracticeAreaCreateRequest  # noqa: F401
from openapi_server.models.practice_area_list import PracticeAreaList  # noqa: F401
from openapi_server.models.practice_area_show import PracticeAreaShow  # noqa: F401
from openapi_server.models.practice_area_update_request import PracticeAreaUpdateRequest  # noqa: F401


def test_practice_area_create(client: TestClient):
    """Test case for practice_area_create

    Create a new PracticeArea
    """
    practice_area_create_request = openapi_server.PracticeAreaCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/practice_areas.json",
    #    headers=headers,
    #    json=practice_area_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_practice_area_destroy(client: TestClient):
    """Test case for practice_area_destroy

    Delete a single PracticeArea
    """

    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/practice_areas/{id}.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_practice_area_index(client: TestClient):
    """Test case for practice_area_index

    Return the data for all PracticeAreas
    """
    params = [("code", 'code_example'),     ("created_since", '2013-10-20T19:20:30+01:00'),     ("fields", 'fields_example'),     ("ids", 56),     ("limit", 56),     ("matter_id", 56),     ("name", 'name_example'),     ("order", 'order_example'),     ("page_token", 'page_token_example'),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/practice_areas.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_practice_area_show(client: TestClient):
    """Test case for practice_area_show

    Return the data for a single PracticeArea
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
    #    "/practice_areas/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_practice_area_update(client: TestClient):
    """Test case for practice_area_update

    Update a single PracticeArea
    """
    practice_area_update_request = openapi_server.PracticeAreaUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/practice_areas/{id}.json".format(id=56),
    #    headers=headers,
    #    json=practice_area_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

