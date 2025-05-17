# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.medical_records_request_create_request import MedicalRecordsRequestCreateRequest  # noqa: F401
from openapi_server.models.medical_records_request_list import MedicalRecordsRequestList  # noqa: F401
from openapi_server.models.medical_records_request_show import MedicalRecordsRequestShow  # noqa: F401
from openapi_server.models.medical_records_request_update_request import MedicalRecordsRequestUpdateRequest  # noqa: F401


def test_medical_records_request_create(client: TestClient):
    """Test case for medical_records_request_create

    Creating a Medical Records Detail, Medical Records and Medical Bills
    """
    medical_records_request_create_request = openapi_server.MedicalRecordsRequestCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/medical_records_details.json",
    #    headers=headers,
    #    json=medical_records_request_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_medical_records_request_destroy(client: TestClient):
    """Test case for medical_records_request_destroy

    Destroying a Medical Records Detail
    """

    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/medical_records_details/{id}.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_medical_records_request_index(client: TestClient):
    """Test case for medical_records_request_index

    Return the data for all Medical Records Details
    """
    params = [("created_since", '2013-10-20T19:20:30+01:00'),     ("fields", 'fields_example'),     ("ids", 56),     ("limit", 56),     ("page_token", 'page_token_example'),     ("treatment_end_date", '2013-10-20T19:20:30+01:00'),     ("treatment_start_date", '2013-10-20T19:20:30+01:00'),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/medical_records_details.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_medical_records_request_show(client: TestClient):
    """Test case for medical_records_request_show

    Return the data for a single Medical Records Detail
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
    #    "/medical_records_details/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_medical_records_request_update(client: TestClient):
    """Test case for medical_records_request_update

    Updating a Medical Records Detail
    """
    medical_records_request_update_request = openapi_server.MedicalRecordsRequestUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/medical_records_details/{id}.json".format(id=56),
    #    headers=headers,
    #    json=medical_records_request_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

