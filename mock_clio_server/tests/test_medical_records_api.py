# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401
from clio_mock.models.medical_record_update_request import MedicalRecordUpdateRequest  # noqa: F401


def test_medical_record_destroy(client: TestClient):
    """Test case for medical_record_destroy

    Destroying a Medical Record
    """

    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/medical_records/{id}.json".format(idpath=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_medical_record_update(client: TestClient):
    """Test case for medical_record_update

    Updating a Medical Record
    """
    medical_record_update_request = clio_mock.MedicalRecordUpdateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_matc_hheader": 'if_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/medical_records/{id}.json".format(idpath=56),
    #    headers=headers,
    #    json=medical_record_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

