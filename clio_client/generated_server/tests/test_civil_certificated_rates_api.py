# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictBool, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.lauk_civil_certificated_rate_list import LaukCivilCertificatedRateList  # noqa: F401


def test_lauk_civil_certificated_rate_index(client: TestClient):
    """Test case for lauk_civil_certificated_rate_index

    List Civil Certificated Rates
    """
    params = [("activity", 'activity_example'),     ("activity_sub_category", 'activity_sub_category_example'),     ("attended_several_hearings_for_multiple_clients", True),     ("category_of_law", 'category_of_law_example'),     ("change_of_solicitor", True),     ("court", 'court_example'),     ("eligible_for_sqm", True),     ("fee_scheme", 'fee_scheme_example'),     ("fields", 'fields_example'),     ("first_conducting_solicitor", True),     ("key", 'key_example'),     ("limit", 56),     ("number_of_clients", 'number_of_clients_example'),     ("page_token", 'page_token_example'),     ("party", 'party_example'),     ("post_transfer_clients_represented", 'post_transfer_clients_represented_example'),     ("rate_type", 'rate_type_example'),     ("region", 'region_example'),     ("session_type", 'session_type_example'),     ("user_type", 'user_type_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/lauk_civil_certificated_rates.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

