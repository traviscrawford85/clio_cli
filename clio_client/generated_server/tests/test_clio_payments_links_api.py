# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.clio_payments_link_create_request import ClioPaymentsLinkCreateRequest  # noqa: F401
from openapi_server.models.clio_payments_link_list import ClioPaymentsLinkList  # noqa: F401
from openapi_server.models.clio_payments_link_show import ClioPaymentsLinkShow  # noqa: F401
from openapi_server.models.clio_payments_link_update_request import ClioPaymentsLinkUpdateRequest  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401


def test_clio_payments_link_create(client: TestClient):
    """Test case for clio_payments_link_create

    Create a new ClioPaymentsLink
    """
    clio_payments_link_create_request = openapi_server.ClioPaymentsLinkCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/clio_payments/links.json",
    #    headers=headers,
    #    json=clio_payments_link_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_clio_payments_link_index(client: TestClient):
    """Test case for clio_payments_link_index

    Return the data for all ClioPaymentsLinks
    """
    params = [("active", True),     ("created_since", '2013-10-20T19:20:30+01:00'),     ("fields", 'fields_example'),     ("ids", 56),     ("limit", 56),     ("page_token", 'page_token_example'),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/clio_payments/links.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_clio_payments_link_show(client: TestClient):
    """Test case for clio_payments_link_show

    Return the data for a single ClioPaymentsLink
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
    #    "/clio_payments/links/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_clio_payments_link_update(client: TestClient):
    """Test case for clio_payments_link_update

    Update a single ClioPaymentsLink
    """
    clio_payments_link_update_request = openapi_server.ClioPaymentsLinkUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/clio_payments/links/{id}.json".format(id=56),
    #    headers=headers,
    #    json=clio_payments_link_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

