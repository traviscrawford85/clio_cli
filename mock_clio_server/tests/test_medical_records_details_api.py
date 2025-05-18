# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.activity_show import ActivityShow  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401
from clio_mock.models.medical_records_request_create_request import MedicalRecordsRequestCreateRequest  # noqa: F401
from clio_mock.models.medical_records_request_update_request import MedicalRecordsRequestUpdateRequest  # noqa: F401


def test_medical_records_request_create(client: TestClient):
    """Test case for medical_records_request_create

    Creating a Medical Records Detail, Medical Records and Medical Bills
    """
    medical_records_request_create_request = clio_mock.MedicalRecordsRequestCreateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
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
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/medical_records_details/{id}.json".format(idpath=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_medical_records_request_index(client: TestClient):
    """Test case for medical_records_request_index

    Return the data for all Medical Records Details
    """
    params = [("created_sincequery", '2013-10-20T19:20:30+01:00'),     ("fieldsquery", 'fieldsquery_example'),     ("idsquery", 56),     ("limitquery", 56),     ("page_tokenquery", 'page_tokenquery_example'),     ("treatment_end_datequery", '2013-10-20T19:20:30+01:00'),     ("treatment_start_datequery", '2013-10-20T19:20:30+01:00'),     ("updated_sincequery", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
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
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_modified_sinc_eheader": '2013-10-20',
        "if_none_matc_hheader": 'if_none_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/medical_records_details/{id}.json".format(idpath=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_medical_records_request_update(client: TestClient):
    """Test case for medical_records_request_update

    Updating a Medical Records Detail
    """
    medical_records_request_update_request = clio_mock.MedicalRecordsRequestUpdateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_matc_hheader": 'if_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/medical_records_details/{id}.json".format(idpath=56),
    #    headers=headers,
    #    json=medical_records_request_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

