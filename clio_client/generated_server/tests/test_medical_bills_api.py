# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.medical_bill_show import MedicalBillShow  # noqa: F401
from openapi_server.models.medical_bill_update_request import MedicalBillUpdateRequest  # noqa: F401


def test_medical_bill_destroy(client: TestClient):
    """Test case for medical_bill_destroy

    Destroying a Medical Bill
    """

    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/medical_bills/{id}.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_medical_bill_update(client: TestClient):
    """Test case for medical_bill_update

    Updating a Medical Bill
    """
    medical_bill_update_request = openapi_server.MedicalBillUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/medical_bills/{id}.json".format(id=56),
    #    headers=headers,
    #    json=medical_bill_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

