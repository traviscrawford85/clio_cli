# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.activity_show import ActivityShow  # noqa: F401
from clio_mock.models.document_copy_request import DocumentCopyRequest  # noqa: F401
from clio_mock.models.document_create_request import DocumentCreateRequest  # noqa: F401
from clio_mock.models.document_update_request import DocumentUpdateRequest  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401


def test_document_copy(client: TestClient):
    """Test case for document_copy

    Copy a Document
    """
    document_copy_request = clio_mock.DocumentCopyRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/documents/{id}/copy.json".format(idpath=56),
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
    document_create_request = clio_mock.DocumentCreateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
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
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/documents/{id}.json".format(idpath=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_document_download(client: TestClient):
    """Test case for document_download

    Download the Document
    """
    params = [("document_version_idquery", 56)]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/documents/{id}/download.json".format(idpath=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_document_index(client: TestClient):
    """Test case for document_index

    Return the data for all Documents
    """
    params = [("contact_idquery", 56),     ("created_sincequery", '2013-10-20T19:20:30+01:00'),     ("document_category_idquery", 56),     ("external_property_namequery", 'external_property_namequery_example'),     ("external_property_valuequery", 'external_property_valuequery_example'),     ("fieldsquery", 'fieldsquery_example'),     ("idsquery", 56),     ("include_deletedquery", True),     ("limitquery", 56),     ("matter_idquery", 56),     ("orderquery", 'orderquery_example'),     ("page_tokenquery", 'page_tokenquery_example'),     ("parent_idquery", 56),     ("queryquery", 'queryquery_example'),     ("scopequery", 'scopequery_example'),     ("show_uncompletedquery", True),     ("updated_sincequery", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
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
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_modified_sinc_eheader": '2013-10-20',
        "if_none_matc_hheader": 'if_none_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/documents/{id}.json".format(idpath=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_document_update(client: TestClient):
    """Test case for document_update

    Update a single Document
    """
    document_update_request = clio_mock.DocumentUpdateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_matc_hheader": 'if_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/documents/{id}.json".format(idpath=56),
    #    headers=headers,
    #    json=document_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

