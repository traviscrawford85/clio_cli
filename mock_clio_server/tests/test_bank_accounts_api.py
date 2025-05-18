# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.activity_show import ActivityShow  # noqa: F401
from clio_mock.models.bank_account_create_request import BankAccountCreateRequest  # noqa: F401
from clio_mock.models.bank_account_update_request import BankAccountUpdateRequest  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401


def test_bank_account_create(client: TestClient):
    """Test case for bank_account_create

    Create a new BankAccount
    """
    bank_account_create_request = clio_mock.BankAccountCreateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
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
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/bank_accounts/{id}.json".format(idpath=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_bank_account_index(client: TestClient):
    """Test case for bank_account_index

    Return the data for all BankAccounts
    """
    params = [("created_sincequery", '2013-10-20T19:20:30+01:00'),     ("fieldsquery", 'fieldsquery_example'),     ("idsquery", 56),     ("limitquery", 56),     ("orderquery", 'orderquery_example'),     ("page_tokenquery", 'page_tokenquery_example'),     ("show_empty_accountsquery", True),     ("typequery", 'typequery_example'),     ("updated_sincequery", '2013-10-20T19:20:30+01:00'),     ("user_idquery", 56)]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
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
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_modified_sinc_eheader": '2013-10-20',
        "if_none_matc_hheader": 'if_none_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/bank_accounts/{id}.json".format(idpath=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_bank_account_update(client: TestClient):
    """Test case for bank_account_update

    Update a single BankAccount
    """
    bank_account_update_request = clio_mock.BankAccountUpdateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_matc_hheader": 'if_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/bank_accounts/{id}.json".format(idpath=56),
    #    headers=headers,
    #    json=bank_account_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

