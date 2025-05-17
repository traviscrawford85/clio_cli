# coding: utf-8

from fastapi.testclient import TestClient


from datetime import datetime  # noqa: F401
from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.grant_funding_source_create_request import GrantFundingSourceCreateRequest  # noqa: F401
from openapi_server.models.grant_funding_source_list import GrantFundingSourceList  # noqa: F401
from openapi_server.models.grant_funding_source_show import GrantFundingSourceShow  # noqa: F401


def test_grant_funding_source_create(client: TestClient):
    """Test case for grant_funding_source_create

    Create a new grant funding source
    """
    grant_funding_source_create_request = openapi_server.GrantFundingSourceCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/grant_funding_sources.json",
    #    headers=headers,
    #    json=grant_funding_source_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_grant_funding_source_destroy(client: TestClient):
    """Test case for grant_funding_source_destroy

    Delete a single grant funding source
    """
    grant_funding_source_create_request = openapi_server.GrantFundingSourceCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/grant_funding_sources/{id}.json".format(id=56),
    #    headers=headers,
    #    json=grant_funding_source_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_grant_funding_source_index(client: TestClient):
    """Test case for grant_funding_source_index

    Return the data for all grant funding sources
    """
    params = [("created_since", '2013-10-20T19:20:30+01:00'),     ("fields", 'fields_example'),     ("ids", 56),     ("limit", 56),     ("name", 'name_example'),     ("page_token", 'page_token_example'),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/grant_funding_sources.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_grant_funding_source_update(client: TestClient):
    """Test case for grant_funding_source_update

    Update a single grant funding source
    """
    grant_funding_source_create_request = openapi_server.GrantFundingSourceCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/grant_funding_sources/{id}.json".format(id=56),
    #    headers=headers,
    #    json=grant_funding_source_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

