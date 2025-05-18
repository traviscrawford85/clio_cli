# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.activity_show import ActivityShow  # noqa: F401
from clio_mock.models.contact_create_request import ContactCreateRequest  # noqa: F401
from clio_mock.models.contact_update_request import ContactUpdateRequest  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401


def test_contact_create(client: TestClient):
    """Test case for contact_create

    Create a new Contact
    """
    contact_create_request = clio_mock.ContactCreateRequest()
    params = [("custom_field_idsquery", 56),     ("fieldsquery", 'fieldsquery_example')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/contacts.json",
    #    headers=headers,
    #    json=contact_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_contact_destroy(client: TestClient):
    """Test case for contact_destroy

    Delete a single Contact
    """

    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/contacts/{id}.json".format(idpath=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_contact_index(client: TestClient):
    """Test case for contact_index

    Return the data for all Contacts
    """
    params = [("client_onlyquery", True),     ("clio_connect_onlyquery", True),     ("created_sincequery", '2013-10-20T19:20:30+01:00'),     ("custom_field_idsquery", 56),     ("custom_field_valuesquery", 'custom_field_valuesquery_example'),     ("email_onlyquery", True),     ("exclude_idsquery", 56),     ("fieldsquery", 'fieldsquery_example'),     ("idsquery", 56),     ("initialquery", 'initialquery_example'),     ("limitquery", 56),     ("orderquery", 'orderquery_example'),     ("page_tokenquery", 'page_tokenquery_example'),     ("queryquery", 'queryquery_example'),     ("shared_resource_idquery", 56),     ("typequery", 'typequery_example'),     ("updated_sincequery", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/contacts.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_contact_show(client: TestClient):
    """Test case for contact_show

    Return the data for a single Contact
    """
    params = [("custom_field_idsquery", 56),     ("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_modified_sinc_eheader": '2013-10-20',
        "if_none_matc_hheader": 'if_none_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/contacts/{id}.json".format(idpath=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_contact_update(client: TestClient):
    """Test case for contact_update

    Update a single Contact
    """
    contact_update_request = clio_mock.ContactUpdateRequest()
    params = [("custom_field_idsquery", 56),     ("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_matc_hheader": 'if_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/contacts/{id}.json".format(idpath=56),
    #    headers=headers,
    #    json=contact_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

