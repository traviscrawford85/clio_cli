# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.activity_show import ActivityShow  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401
from clio_mock.models.practice_area_create_request import PracticeAreaCreateRequest  # noqa: F401
from clio_mock.models.practice_area_update_request import PracticeAreaUpdateRequest  # noqa: F401


def test_practice_area_create(client: TestClient):
    """Test case for practice_area_create

    Create a new PracticeArea
    """
    practice_area_create_request = clio_mock.PracticeAreaCreateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/practice_areas.json",
    #    headers=headers,
    #    json=practice_area_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_practice_area_destroy(client: TestClient):
    """Test case for practice_area_destroy

    Delete a single PracticeArea
    """

    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/practice_areas/{id}.json".format(idpath=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_practice_area_index(client: TestClient):
    """Test case for practice_area_index

    Return the data for all PracticeAreas
    """
    params = [("codequery", 'codequery_example'),     ("created_sincequery", '2013-10-20T19:20:30+01:00'),     ("fieldsquery", 'fieldsquery_example'),     ("idsquery", 56),     ("limitquery", 56),     ("matter_idquery", 56),     ("namequery", 'namequery_example'),     ("orderquery", 'orderquery_example'),     ("page_tokenquery", 'page_tokenquery_example'),     ("updated_sincequery", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/practice_areas.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_practice_area_show(client: TestClient):
    """Test case for practice_area_show

    Return the data for a single PracticeArea
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
    #    "/practice_areas/{id}.json".format(idpath=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_practice_area_update(client: TestClient):
    """Test case for practice_area_update

    Update a single PracticeArea
    """
    practice_area_update_request = clio_mock.PracticeAreaUpdateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_matc_hheader": 'if_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/practice_areas/{id}.json".format(idpath=56),
    #    headers=headers,
    #    json=practice_area_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

