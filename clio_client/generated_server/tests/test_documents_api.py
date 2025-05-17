# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.document_copy_request import DocumentCopyRequest  # noqa: F401
from openapi_server.models.document_create_request import DocumentCreateRequest  # noqa: F401
from openapi_server.models.document_list import DocumentList  # noqa: F401
from openapi_server.models.document_show import DocumentShow  # noqa: F401
from openapi_server.models.document_update_request import DocumentUpdateRequest  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401


def test_document_copy(client: TestClient):
    """Test case for document_copy

    Copy a Document
    """
    document_copy_request = openapi_server.DocumentCopyRequest()
    params = [("fields", 'fields_example')]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/documents/{id}/copy.json".format(id=56),
    #    headers=headers,
    #    json=document_copy_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_document_create(client: TestClient):
    """Test case for document_create

    Create a new Document
    """
    document_create_request = openapi_server.DocumentCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/documents.json",
    #    headers=headers,
    #    json=document_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_document_destroy(client: TestClient):
    """Test case for document_destroy

    Delete a single Document
    """

    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/documents/{id}.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_document_download(client: TestClient):
    """Test case for document_download

    Download the Document
    """
    params = [("document_version_id", 56)]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/documents/{id}/download.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_document_index(client: TestClient):
    """Test case for document_index

    Return the data for all Documents
    """
    params = [("contact_id", 56),     ("created_since", '2013-10-20T19:20:30+01:00'),     ("document_category_id", 56),     ("external_property_name", 'external_property_name_example'),     ("external_property_value", 'external_property_value_example'),     ("fields", 'fields_example'),     ("ids", 56),     ("include_deleted", True),     ("limit", 56),     ("matter_id", 56),     ("order", 'order_example'),     ("page_token", 'page_token_example'),     ("parent_id", 56),     ("query", 'query_example'),     ("scope", 'scope_example'),     ("show_uncompleted", True),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/documents.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_document_show(client: TestClient):
    """Test case for document_show

    Return the data for a single Document
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
    #    "/documents/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_document_update(client: TestClient):
    """Test case for document_update

    Update a single Document
    """
    document_update_request = openapi_server.DocumentUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/documents/{id}.json".format(id=56),
    #    headers=headers,
    #    json=document_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

