# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.bank_account_create_request import BankAccountCreateRequest  # noqa: F401
from openapi_server.models.bank_account_list import BankAccountList  # noqa: F401
from openapi_server.models.bank_account_show import BankAccountShow  # noqa: F401
from openapi_server.models.bank_account_update_request import BankAccountUpdateRequest  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401


def test_bank_account_create(client: TestClient):
    """Test case for bank_account_create

    Create a new BankAccount
    """
    bank_account_create_request = openapi_server.BankAccountCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/bank_accounts.json",
    #    headers=headers,
    #    json=bank_account_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_bank_account_destroy(client: TestClient):
    """Test case for bank_account_destroy

    Delete a single BankAccount
    """

    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/bank_accounts/{id}.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_bank_account_index(client: TestClient):
    """Test case for bank_account_index

    Return the data for all BankAccounts
    """
    params = [("created_since", '2013-10-20T19:20:30+01:00'),     ("fields", 'fields_example'),     ("ids", 56),     ("limit", 56),     ("order", 'order_example'),     ("page_token", 'page_token_example'),     ("show_empty_accounts", True),     ("type", 'type_example'),     ("updated_since", '2013-10-20T19:20:30+01:00'),     ("user_id", 56)]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/bank_accounts.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_bank_account_show(client: TestClient):
    """Test case for bank_account_show

    Return the data for a single BankAccount
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
    #    "/bank_accounts/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_bank_account_update(client: TestClient):
    """Test case for bank_account_update

    Update a single BankAccount
    """
    bank_account_update_request = openapi_server.BankAccountUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/bank_accounts/{id}.json".format(id=56),
    #    headers=headers,
    #    json=bank_account_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

