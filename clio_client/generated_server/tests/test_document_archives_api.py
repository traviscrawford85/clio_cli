# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date  # noqa: F401
from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.document_archive_create_request import DocumentArchiveCreateRequest  # noqa: F401
from openapi_server.models.document_archive_show import DocumentArchiveShow  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401


def test_document_archive_create(client: TestClient):
    """Test case for document_archive_create

    Create a new DocumentArchive
    """
    document_archive_create_request = openapi_server.DocumentArchiveCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/document_archives.json",
    #    headers=headers,
    #    json=document_archive_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_document_archive_download(client: TestClient):
    """Test case for document_archive_download

    Download the DocumentArchive
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/document_archives/{id}/download.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_document_archive_show(client: TestClient):
    """Test case for document_archive_show

    Return the data for a single DocumentArchive
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
    #    "/document_archives/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

