# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.lauk_civil_controlled_rate_list import LaukCivilControlledRateList  # noqa: F401


def test_lauk_civil_controlled_rate_index(client: TestClient):
    """Test case for lauk_civil_controlled_rate_index

    List Civil Controlled Rates
    """
    params = [("activity", 'activity_example'),     ("category_of_law", 'category_of_law_example'),     ("fields", 'fields_example'),     ("key", 'key_example'),     ("limit", 56),     ("matter_type_1", 56),     ("matter_type_2", 56),     ("page_token", 'page_token_example'),     ("rate_type", 'rate_type_example'),     ("region", 'region_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/lauk_civil_controlled_rates.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

