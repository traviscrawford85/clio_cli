# coding: utf-8

from fastapi.testclient import TestClient


from datetime import datetime  # noqa: F401
from pydantic import Field, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.trust_line_item_list import TrustLineItemList  # noqa: F401
from openapi_server.models.trust_line_item_show import TrustLineItemShow  # noqa: F401
from openapi_server.models.trust_line_item_update_request import TrustLineItemUpdateRequest  # noqa: F401


def test_trust_line_item_index(client: TestClient):
    """Test case for trust_line_item_index

    Return the data for all TrustLineItems
    """
    params = [("bill_id", 56),     ("created_since", '2013-10-20T19:20:30+01:00'),     ("fields", 'fields_example'),     ("ids", 56),     ("limit", 56),     ("matter_id", 56),     ("order", 'order_example'),     ("page_token", 'page_token_example'),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/trust_line_items.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_trust_line_item_update(client: TestClient):
    """Test case for trust_line_item_update

    Update a single TrustLineItem
    """
    trust_line_item_update_request = openapi_server.TrustLineItemUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/trust_line_items/{id}.json".format(id=56),
    #    headers=headers,
    #    json=trust_line_item_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

