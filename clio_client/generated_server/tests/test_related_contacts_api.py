# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.related_contacts_list import RelatedContactsList  # noqa: F401


def test_related_contacts_index(client: TestClient):
    """Test case for related_contacts_index

    Return the related contact data for a single matter
    """
    params = [("fields", 'fields_example'),     ("limit", 56),     ("order", 'order_example'),     ("page_token", 'page_token_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/matters/{matter_id}/related_contacts.json".format(matter_id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

