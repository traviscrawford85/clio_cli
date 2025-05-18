# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.activity_show import ActivityShow  # noqa: F401
from clio_mock.models.clio_payments_link_create_request import ClioPaymentsLinkCreateRequest  # noqa: F401
from clio_mock.models.clio_payments_link_update_request import ClioPaymentsLinkUpdateRequest  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401


def test_clio_payments_link_create(client: TestClient):
    """Test case for clio_payments_link_create

    Create a new ClioPaymentsLink
    """
    clio_payments_link_create_request = clio_mock.ClioPaymentsLinkCreateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/clio_payments/links.json",
    #    headers=headers,
    #    json=clio_payments_link_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_clio_payments_link_index(client: TestClient):
    """Test case for clio_payments_link_index

    Return the data for all ClioPaymentsLinks
    """
    params = [("activequery", True),     ("created_sincequery", '2013-10-20T19:20:30+01:00'),     ("fieldsquery", 'fieldsquery_example'),     ("idsquery", 56),     ("limitquery", 56),     ("page_tokenquery", 'page_tokenquery_example'),     ("updated_sincequery", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/clio_payments/links.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_clio_payments_link_show(client: TestClient):
    """Test case for clio_payments_link_show

    Return the data for a single ClioPaymentsLink
    """
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_modified_sinc_eheader": '2013-10-20',
        "if_none_matc_hheader": 'if_none_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/clio_payments/links/{id}.json".format(idpath=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_clio_payments_link_update(client: TestClient):
    """Test case for clio_payments_link_update

    Update a single ClioPaymentsLink
    """
    clio_payments_link_update_request = clio_mock.ClioPaymentsLinkUpdateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_matc_hheader": 'if_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/clio_payments/links/{id}.json".format(idpath=56),
    #    headers=headers,
    #    json=clio_payments_link_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

