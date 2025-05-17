# coding: utf-8

from fastapi.testclient import TestClient


from datetime import datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.line_item_list import LineItemList  # noqa: F401
from openapi_server.models.line_item_show import LineItemShow  # noqa: F401
from openapi_server.models.line_item_update_request import LineItemUpdateRequest  # noqa: F401


def test_line_item_destroy(client: TestClient):
    """Test case for line_item_destroy

    Delete a single LineItem
    """

    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/line_items/{id}.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_line_item_index(client: TestClient):
    """Test case for line_item_index

    Return the data for all LineItems
    """
    params = [("activity_id", 56),     ("bill_id", 56),     ("created_since", '2013-10-20T19:20:30+01:00'),     ("display", True),     ("exclude_ids", 56),     ("fields", 'fields_example'),     ("group_ordering", 56),     ("ids", 56),     ("kind", 'kind_example'),     ("limit", 56),     ("matter_id", 56),     ("page_token", 'page_token_example'),     ("query", 'query_example'),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/line_items.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_line_item_update(client: TestClient):
    """Test case for line_item_update

    Update a single LineItem
    """
    line_item_update_request = openapi_server.LineItemUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/line_items/{id}.json".format(id=56),
    #    headers=headers,
    #    json=line_item_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

