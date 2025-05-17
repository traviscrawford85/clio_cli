# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.activity_description_create_request import ActivityDescriptionCreateRequest  # noqa: F401
from openapi_server.models.activity_description_list import ActivityDescriptionList  # noqa: F401
from openapi_server.models.activity_description_show import ActivityDescriptionShow  # noqa: F401
from openapi_server.models.activity_description_update_request import ActivityDescriptionUpdateRequest  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401


def test_activity_description_create(client: TestClient):
    """Test case for activity_description_create

    Create a new ActivityDescription
    """
    activity_description_create_request = openapi_server.ActivityDescriptionCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/activity_descriptions.json",
    #    headers=headers,
    #    json=activity_description_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_activity_description_destroy(client: TestClient):
    """Test case for activity_description_destroy

    Delete a single ActivityDescription
    """

    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/activity_descriptions/{id}.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_activity_description_index(client: TestClient):
    """Test case for activity_description_index

    Return the data for all ActivityDescriptions
    """
    params = [("created_since", '2013-10-20T19:20:30+01:00'),     ("fields", 'fields_example'),     ("flat_rate", True),     ("ids", 56),     ("limit", 56),     ("page_token", 'page_token_example'),     ("rate_for_matter_id", 56),     ("rate_for_user_id", 56),     ("type", 'type_example'),     ("updated_since", '2013-10-20T19:20:30+01:00'),     ("user_id", 56)]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/activity_descriptions.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_activity_description_show(client: TestClient):
    """Test case for activity_description_show

    Return the data for a single ActivityDescription
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
    #    "/activity_descriptions/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_activity_description_update(client: TestClient):
    """Test case for activity_description_update

    Update a single ActivityDescription
    """
    activity_description_update_request = openapi_server.ActivityDescriptionUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/activity_descriptions/{id}.json".format(id=56),
    #    headers=headers,
    #    json=activity_description_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

