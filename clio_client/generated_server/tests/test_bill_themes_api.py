# coding: utf-8

from fastapi.testclient import TestClient


from datetime import datetime  # noqa: F401
from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.bill_theme_list import BillThemeList  # noqa: F401
from openapi_server.models.bill_theme_show import BillThemeShow  # noqa: F401
from openapi_server.models.bill_theme_update_request import BillThemeUpdateRequest  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401


def test_bill_theme_index(client: TestClient):
    """Test case for bill_theme_index

    Return the data for all BillThemes
    """
    params = [("created_since", '2013-10-20T19:20:30+01:00'),     ("fields", 'fields_example'),     ("ids", 56),     ("limit", 56),     ("page_token", 'page_token_example'),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/bill_themes.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_bill_theme_update(client: TestClient):
    """Test case for bill_theme_update

    Update a single BillTheme
    """
    bill_theme_update_request = openapi_server.BillThemeUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/bill_themes/{id}.json".format(id=56),
    #    headers=headers,
    #    json=bill_theme_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

