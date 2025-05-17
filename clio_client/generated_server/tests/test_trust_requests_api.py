# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.trust_request_create_request import TrustRequestCreateRequest  # noqa: F401
from openapi_server.models.trust_request_show import TrustRequestShow  # noqa: F401


def test_trust_request_create(client: TestClient):
    """Test case for trust_request_create

    Create a new TrustRequest
    """
    trust_request_create_request = openapi_server.TrustRequestCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/trust_requests.json",
    #    headers=headers,
    #    json=trust_request_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

