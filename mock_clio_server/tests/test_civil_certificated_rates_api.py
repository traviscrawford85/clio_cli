# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictBool, StrictInt, StrictStr  # noqa: F401
from typing import Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401


def test_lauk_civil_certificated_rate_index(client: TestClient):
    """Test case for lauk_civil_certificated_rate_index

    List Civil Certificated Rates
    """
    params = [("activityquery", 'activityquery_example'),     ("activity_sub_categoryquery", 'activity_sub_categoryquery_example'),     ("attended_several_hearings_for_multiple_clientsquery", True),     ("category_of_lawquery", 'category_of_lawquery_example'),     ("change_of_solicitorquery", True),     ("courtquery", 'courtquery_example'),     ("eligible_for_sqmquery", True),     ("fee_schemequery", 'fee_schemequery_example'),     ("fieldsquery", 'fieldsquery_example'),     ("first_conducting_solicitorquery", True),     ("keyquery", 'keyquery_example'),     ("limitquery", 56),     ("number_of_clientsquery", 'number_of_clientsquery_example'),     ("page_tokenquery", 'page_tokenquery_example'),     ("partyquery", 'partyquery_example'),     ("post_transfer_clients_representedquery", 'post_transfer_clients_representedquery_example'),     ("rate_typequery", 'rate_typequery_example'),     ("regionquery", 'regionquery_example'),     ("session_typequery", 'session_typequery_example'),     ("user_typequery", 'user_typequery_example')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
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

