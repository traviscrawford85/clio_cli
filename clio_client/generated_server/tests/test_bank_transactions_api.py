# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.bank_transaction_list import BankTransactionList  # noqa: F401
from openapi_server.models.bank_transaction_show import BankTransactionShow  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401


def test_bank_transaction_index(client: TestClient):
    """Test case for bank_transaction_index

    Return the data for all BankTransactions
    """
    params = [("bank_account_id", 56),     ("client_id", 56),     ("created_since", '2013-10-20T19:20:30+01:00'),     ("fields", 'fields_example'),     ("ids", 56),     ("limit", 56),     ("matter_id", 56),     ("order", 'order_example'),     ("page_token", 'page_token_example'),     ("type", 'type_example'),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/bank_transactions.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_bank_transaction_show(client: TestClient):
    """Test case for bank_transaction_show

    Return the data for a single BankTransaction
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
    #    "/bank_transactions/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

