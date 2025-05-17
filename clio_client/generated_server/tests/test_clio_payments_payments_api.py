# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date  # noqa: F401
from pydantic import Field, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.clio_payments_payment_list import ClioPaymentsPaymentList  # noqa: F401
from openapi_server.models.clio_payments_payment_show import ClioPaymentsPaymentShow  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401


def test_clio_payments_payment_index(client: TestClient):
    """Test case for clio_payments_payment_index

    Return the data for all ClioPaymentsPayments
    """
    params = [("bill_id", 56),     ("contact_id", 56),     ("fields", 'fields_example'),     ("ids", 56),     ("limit", 56),     ("page_token", 'page_token_example'),     ("state", 'state_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/clio_payments/payments.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_clio_payments_payment_show(client: TestClient):
    """Test case for clio_payments_payment_show

    Return the data for a single ClioPaymentsPayment
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
    #    "/clio_payments/payments/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

