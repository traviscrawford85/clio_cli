# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.activity_show import ActivityShow  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401
from clio_mock.models.folder_create_request import FolderCreateRequest  # noqa: F401
from clio_mock.models.folder_update_request import FolderUpdateRequest  # noqa: F401


def test_folder_create(client: TestClient):
    """Test case for folder_create

    Create a new Folder
    """
    folder_create_request = clio_mock.FolderCreateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/folders.json",
    #    headers=headers,
    #    json=folder_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_folder_destroy(client: TestClient):
    """Test case for folder_destroy

    Delete a single Folder
    """

    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/folders/{id}.json".format(idpath=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_folder_index(client: TestClient):
    """Test case for folder_index

    Return the data for all Folders
    """
    params = [("contact_idquery", 56),     ("created_sincequery", '2013-10-20T19:20:30+01:00'),     ("document_category_idquery", 56),     ("external_property_namequery", 'external_property_namequery_example'),     ("external_property_valuequery", 'external_property_valuequery_example'),     ("fieldsquery", 'fieldsquery_example'),     ("idsquery", 56),     ("include_deletedquery", True),     ("limitquery", 56),     ("matter_idquery", 56),     ("orderquery", 'orderquery_example'),     ("page_tokenquery", 'page_tokenquery_example'),     ("parent_idquery", 56),     ("queryquery", 'queryquery_example'),     ("scopequery", 'scopequery_example'),     ("updated_sincequery", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/folders.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_folder_list(client: TestClient):
    """Test case for folder_list

    Return the data of the contents of a Folder
    """
    params = [("contact_idquery", 56),     ("created_sincequery", '2013-10-20T19:20:30+01:00'),     ("document_category_idquery", 56),     ("external_property_namequery", 'external_property_namequery_example'),     ("external_property_valuequery", 'external_property_valuequery_example'),     ("fieldsquery", 'fieldsquery_example'),     ("idsquery", 56),     ("include_deletedquery", True),     ("limitquery", 56),     ("matter_idquery", 56),     ("orderquery", 'orderquery_example'),     ("page_tokenquery", 'page_tokenquery_example'),     ("parent_idquery", 56),     ("queryquery", 'queryquery_example'),     ("scopequery", 'scopequery_example'),     ("show_uncompletedquery", True),     ("updated_sincequery", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/folders/list.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_folder_show(client: TestClient):
    """Test case for folder_show

    Return the data for a single Folder
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
    #    "/folders/{id}.json".format(idpath=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_folder_update(client: TestClient):
    """Test case for folder_update

    Update a single Folder
    """
    folder_update_request = clio_mock.FolderUpdateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_matc_hheader": 'if_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/folders/{id}.json".format(idpath=56),
    #    headers=headers,
    #    json=folder_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

