# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictBool, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.document_version_list import DocumentVersionList  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401


def test_document_version_index(client: TestClient):
    """Test case for document_version_index

    Return the data for all DocumentVersions
    """
    params = [("fields", 'fields_example'),     ("fully_uploaded", True),     ("id", 56),     ("limit", 56),     ("page_token", 'page_token_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/documents/{id}/versions.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

