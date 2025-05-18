# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.bill_update_request import BillUpdateRequest  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401


def test_bill_destroy(client: TestClient):
    """Test case for bill_destroy

    Delete or void a Bill
    """

    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/bills/{id}.json".format(idpath=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_bill_index(client: TestClient):
    """Test case for bill_index

    Return the data for all Bills
    """
    params = [("client_idquery", 56),     ("created_sincequery", '2013-10-20T19:20:30+01:00'),     ("currency_idquery", 56),     ("custom_field_valuesquery", 'custom_field_valuesquery_example'),     ("due_afterquery", '2013-10-20'),     ("due_atquery", '2013-10-20'),     ("due_beforequery", '2013-10-20'),     ("fieldsquery", 'fieldsquery_example'),     ("idsquery", 56),     ("issued_afterquery", '2013-10-20'),     ("issued_beforequery", '2013-10-20'),     ("last_sent_end_datequery", '2013-10-20'),     ("last_sent_start_datequery", '2013-10-20'),     ("limitquery", 56),     ("matter_idquery", 56),     ("orderquery", 'orderquery_example'),     ("originating_attorney_idquery", 56),     ("overdue_onlyquery", True),     ("page_tokenquery", 'page_tokenquery_example'),     ("queryquery", 'queryquery_example'),     ("responsible_attorney_idquery", 56),     ("statequery", 'statequery_example'),     ("statusquery", 'statusquery_example'),     ("typequery", 'typequery_example'),     ("updated_sincequery", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/bills.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_bill_preview(client: TestClient):
    """Test case for bill_preview

    Returns the pre-rendered html for the Bill
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/bills/{id}/preview.json".format(idpath=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_bill_show(client: TestClient):
    """Test case for bill_show

    Return the data for a single Bill
    """
    params = [("fieldsquery", 'fieldsquery_example'),     ("navigation_nextquery", 56),     ("navigation_previousquery", 56)]
    headers = {
        "if_modified_sinc_eheader": '2013-10-20',
        "if_none_matc_hheader": 'if_none_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/bills/{id}.json".format(idpath=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_bill_update(client: TestClient):
    """Test case for bill_update

    Update a single Bill
    """
    bill_update_request = clio_mock.BillUpdateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_matc_hheader": 'if_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/bills/{id}.json".format(idpath=56),
    #    headers=headers,
    #    json=bill_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

