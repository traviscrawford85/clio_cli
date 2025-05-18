# coding: utf-8

from fastapi.testclient import TestClient


from datetime import datetime  # noqa: F401
from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401


def test_interest_charge_destroy(client: TestClient):
    """Test case for interest_charge_destroy

    Delete a single InterestCharge
    """

    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/interest_charges/{id}.json".format(idpath=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_interest_charge_index(client: TestClient):
    """Test case for interest_charge_index

    Return the data for all InterestCharges
    """
    params = [("bill_idquery", 56),     ("created_sincequery", '2013-10-20T19:20:30+01:00'),     ("exclude_idsquery", 56),     ("fieldsquery", 'fieldsquery_example'),     ("idsquery", 56),     ("limitquery", 56),     ("page_tokenquery", 'page_tokenquery_example'),     ("updated_sincequery", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/interest_charges.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

