# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401


def test_lauk_criminal_controlled_rate_index(client: TestClient):
    """Test case for lauk_criminal_controlled_rate_index

    List Criminal Controlled Rates
    """
    params = [("activityquery", 'activityquery_example'),     ("category_of_lawquery", 'category_of_lawquery_example'),     ("counselquery", 'counselquery_example'),     ("courtquery", 'courtquery_example'),     ("fieldsquery", 'fieldsquery_example'),     ("keyquery", 'keyquery_example'),     ("limitquery", 56),     ("page_tokenquery", 'page_tokenquery_example'),     ("rate_typequery", 'rate_typequery_example'),     ("regionquery", 'regionquery_example'),     ("solicitor_typequery", 'solicitor_typequery_example'),     ("standard_fee_categoryquery", 'standard_fee_categoryquery_example')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
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

