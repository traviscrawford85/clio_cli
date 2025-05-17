# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.folder_create_request import FolderCreateRequest  # noqa: F401
from openapi_server.models.folder_list import FolderList  # noqa: F401
from openapi_server.models.folder_show import FolderShow  # noqa: F401
from openapi_server.models.folder_update_request import FolderUpdateRequest  # noqa: F401
from openapi_server.models.item_list import ItemList  # noqa: F401


def test_folder_create(client: TestClient):
    """Test case for folder_create

    Create a new Folder
    """
    folder_create_request = openapi_server.FolderCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
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
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/folders/{id}.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_folder_index(client: TestClient):
    """Test case for folder_index

    Return the data for all Folders
    """
    params = [("contact_id", 56),     ("created_since", '2013-10-20T19:20:30+01:00'),     ("document_category_id", 56),     ("external_property_name", 'external_property_name_example'),     ("external_property_value", 'external_property_value_example'),     ("fields", 'fields_example'),     ("ids", 56),     ("include_deleted", True),     ("limit", 56),     ("matter_id", 56),     ("order", 'order_example'),     ("page_token", 'page_token_example'),     ("parent_id", 56),     ("query", 'query_example'),     ("scope", 'scope_example'),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
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
    params = [("contact_id", 56),     ("created_since", '2013-10-20T19:20:30+01:00'),     ("document_category_id", 56),     ("external_property_name", 'external_property_name_example'),     ("external_property_value", 'external_property_value_example'),     ("fields", 'fields_example'),     ("ids", 56),     ("include_deleted", True),     ("limit", 56),     ("matter_id", 56),     ("order", 'order_example'),     ("page_token", 'page_token_example'),     ("parent_id", 56),     ("query", 'query_example'),     ("scope", 'scope_example'),     ("show_uncompleted", True),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
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
    params = [("fields", 'fields_example')]
    headers = {
        "if_modified_since": '2013-10-20',
        "if_none_match": 'if_none_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/folders/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_folder_update(client: TestClient):
    """Test case for folder_update

    Update a single Folder
    """
    folder_update_request = openapi_server.FolderUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/folders/{id}.json".format(id=56),
    #    headers=headers,
    #    json=folder_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

