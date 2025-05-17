# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.activity_rate_create_request import ActivityRateCreateRequest  # noqa: F401
from openapi_server.models.activity_rate_list import ActivityRateList  # noqa: F401
from openapi_server.models.activity_rate_show import ActivityRateShow  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401


def test_activity_rate_create(client: TestClient):
    """Test case for activity_rate_create

    Create a new ActivityRate
    """
    activity_rate_create_request = openapi_server.ActivityRateCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/activity_rates.json",
    #    headers=headers,
    #    json=activity_rate_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_activity_rate_destroy(client: TestClient):
    """Test case for activity_rate_destroy

    Delete a single ActivityRate
    """

    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/activity_rates/{id}.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_activity_rate_index(client: TestClient):
    """Test case for activity_rate_index

    Return the data for all ActivityRates
    """
    params = [("co_counsel_contact_id", 56),     ("contact_id", 56),     ("created_since", '2013-10-20T19:20:30+01:00'),     ("fields", 'fields_example'),     ("ids", 56),     ("limit", 56),     ("page_token", 'page_token_example'),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/activity_rates.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_activity_rate_show(client: TestClient):
    """Test case for activity_rate_show

    Return the data for a single ActivityRate
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
    #    "/activity_rates/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_activity_rate_update(client: TestClient):
    """Test case for activity_rate_update

    Update a single ActivityRate
    """
    activity_rate_create_request = openapi_server.ActivityRateCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/activity_rates/{id}.json".format(id=56),
    #    headers=headers,
    #    json=activity_rate_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

