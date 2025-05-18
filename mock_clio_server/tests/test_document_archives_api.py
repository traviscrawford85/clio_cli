# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date  # noqa: F401
from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.activity_show import ActivityShow  # noqa: F401
from clio_mock.models.document_archive_create_request import DocumentArchiveCreateRequest  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401


def test_document_archive_create(client: TestClient):
    """Test case for document_archive_create

    Create a new DocumentArchive
    """
    document_archive_create_request = clio_mock.DocumentArchiveCreateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
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
    #    "/document_archives/{id}/download.json".format(idpath=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_document_archive_show(client: TestClient):
    """Test case for document_archive_show

    Return the data for a single DocumentArchive
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
    #    "/document_archives/{id}.json".format(idpath=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

