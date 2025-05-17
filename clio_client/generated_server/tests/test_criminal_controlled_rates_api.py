# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.lauk_criminal_controlled_rate_list import LaukCriminalControlledRateList  # noqa: F401


def test_lauk_criminal_controlled_rate_index(client: TestClient):
    """Test case for lauk_criminal_controlled_rate_index

    List Criminal Controlled Rates
    """
    params = [("activity", 'activity_example'),     ("category_of_law", 'category_of_law_example'),     ("counsel", 'counsel_example'),     ("court", 'court_example'),     ("fields", 'fields_example'),     ("key", 'key_example'),     ("limit", 56),     ("page_token", 'page_token_example'),     ("rate_type", 'rate_type_example'),     ("region", 'region_example'),     ("solicitor_type", 'solicitor_type_example'),     ("standard_fee_category", 'standard_fee_category_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/lauk_criminal_controlled_rates.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

