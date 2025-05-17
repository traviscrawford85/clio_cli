# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.user_list import UserList  # noqa: F401
from openapi_server.models.user_show import UserShow  # noqa: F401


def test_user_index(client: TestClient):
    """Test case for user_index

    Return the data for all Users
    """
    params = [("created_since", '2013-10-20T19:20:30+01:00'),     ("enabled", True),     ("fields", 'fields_example'),     ("ids", 56),     ("include_co_counsel", True),     ("limit", 56),     ("name", 'name_example'),     ("order", 'order_example'),     ("page_token", 'page_token_example'),     ("pending_setup", True),     ("role", 'role_example'),     ("subscription_type", 'subscription_type_example'),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/users.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_show(client: TestClient):
    """Test case for user_show

    Return the data for a single User
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
    #    "/users/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_who_am_i(client: TestClient):
    """Test case for user_who_am_i

    Return the data for the current User
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
    #    "/users/who_am_i.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

