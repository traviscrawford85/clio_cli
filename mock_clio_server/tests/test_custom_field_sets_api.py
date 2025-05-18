# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.activity_show import ActivityShow  # noqa: F401
from clio_mock.models.custom_field_set_create_request import CustomFieldSetCreateRequest  # noqa: F401
from clio_mock.models.custom_field_set_update_request import CustomFieldSetUpdateRequest  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401


def test_custom_field_set_create(client: TestClient):
    """Test case for custom_field_set_create

    Create a new CustomFieldSet
    """
    custom_field_set_create_request = clio_mock.CustomFieldSetCreateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/custom_field_sets.json",
    #    headers=headers,
    #    json=custom_field_set_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_custom_field_set_destroy(client: TestClient):
    """Test case for custom_field_set_destroy

    Delete a single CustomFieldSet
    """

    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/custom_field_sets/{id}.json".format(idpath=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_custom_field_set_index(client: TestClient):
    """Test case for custom_field_set_index

    Return the data for all CustomFieldSets
    """
    params = [("created_sincequery", '2013-10-20T19:20:30+01:00'),     ("displayedquery", True),     ("fieldsquery", 'fieldsquery_example'),     ("idsquery", 56),     ("limitquery", 56),     ("orderquery", 'orderquery_example'),     ("page_tokenquery", 'page_tokenquery_example'),     ("parent_typequery", 56),     ("queryquery", 'queryquery_example'),     ("updated_sincequery", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/custom_field_sets.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_custom_field_set_show(client: TestClient):
    """Test case for custom_field_set_show

    Return the data for a single CustomFieldSet
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
    #    "/custom_field_sets/{id}.json".format(idpath=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_custom_field_set_update(client: TestClient):
    """Test case for custom_field_set_update

    Update a single CustomFieldSet
    """
    custom_field_set_update_request = clio_mock.CustomFieldSetUpdateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_matc_hheader": 'if_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/custom_field_sets/{id}.json".format(idpath=56),
    #    headers=headers,
    #    json=custom_field_set_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

