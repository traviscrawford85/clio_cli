# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.activity_show import ActivityShow  # noqa: F401
from clio_mock.models.custom_field_create_request import CustomFieldCreateRequest  # noqa: F401
from clio_mock.models.custom_field_update_request import CustomFieldUpdateRequest  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401


def test_custom_field_create(client: TestClient):
    """Test case for custom_field_create

    Create a new CustomField
    """
    custom_field_create_request = clio_mock.CustomFieldCreateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/custom_fields.json",
    #    headers=headers,
    #    json=custom_field_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_custom_field_destroy(client: TestClient):
    """Test case for custom_field_destroy

    Delete a single CustomField
    """

    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/custom_fields/{id}.json".format(idpath=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_custom_field_index(client: TestClient):
    """Test case for custom_field_index

    Return the data for all CustomFields
    """
    params = [("created_sincequery", '2013-10-20T19:20:30+01:00'),     ("deletedquery", True),     ("field_typequery", 'field_typequery_example'),     ("fieldsquery", 'fieldsquery_example'),     ("idsquery", 56),     ("limitquery", 56),     ("orderquery", 'orderquery_example'),     ("page_tokenquery", 'page_tokenquery_example'),     ("parent_typequery", 56),     ("queryquery", 'queryquery_example'),     ("updated_sincequery", '2013-10-20T19:20:30+01:00'),     ("visible_and_requiredquery", True)]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/custom_fields.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_custom_field_show(client: TestClient):
    """Test case for custom_field_show

    Return the data for a single CustomField
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
    #    "/custom_fields/{id}.json".format(idpath=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_custom_field_update(client: TestClient):
    """Test case for custom_field_update

    Update a single CustomField
    """
    custom_field_update_request = clio_mock.CustomFieldUpdateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_matc_hheader": 'if_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/custom_fields/{id}.json".format(idpath=56),
    #    headers=headers,
    #    json=custom_field_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

