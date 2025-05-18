# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_show import ActivityShow  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401
from clio_mock.models.trust_request_create_request import TrustRequestCreateRequest  # noqa: F401


def test_trust_request_create(client: TestClient):
    """Test case for trust_request_create

    Create a new TrustRequest
    """
    trust_request_create_request = clio_mock.TrustRequestCreateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
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

