# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.activity_show import ActivityShow  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401
from clio_mock.models.matter_create_request import MatterCreateRequest  # noqa: F401
from clio_mock.models.matter_update_request import MatterUpdateRequest  # noqa: F401


def test_matter_create(client: TestClient):
    """Test case for matter_create

    Create a new Matter
    """
    matter_create_request = clio_mock.MatterCreateRequest()
    params = [("custom_field_idsquery", 56),     ("fieldsquery", 'fieldsquery_example')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/matters.json",
    #    headers=headers,
    #    json=matter_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_matter_destroy(client: TestClient):
    """Test case for matter_destroy

    Delete a single Matter
    """

    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/matters/{id}.json".format(idpath=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_matter_index(client: TestClient):
    """Test case for matter_index

    Return the data for all Matters
    """
    params = [("billablequery", True),     ("client_idquery", 56),     ("close_datequery", 'close_datequery_example'),     ("created_sincequery", '2013-10-20T19:20:30+01:00'),     ("custom_field_idsquery", 56),     ("custom_field_valuesquery", 'custom_field_valuesquery_example'),     ("fieldsquery", 'fieldsquery_example'),     ("grant_idquery", 56),     ("group_idquery", 56),     ("idsquery", 56),     ("limitquery", 56),     ("notification_event_subscriber_user_idquery", 56),     ("open_datequery", 'open_datequery_example'),     ("orderquery", 'orderquery_example'),     ("originating_attorney_idquery", 56),     ("page_tokenquery", 'page_tokenquery_example'),     ("pending_datequery", 'pending_datequery_example'),     ("practice_area_idquery", 56),     ("queryquery", 'queryquery_example'),     ("responsible_attorney_idquery", 56),     ("responsible_staff_idquery", 56),     ("statusquery", 'statusquery_example'),     ("subscriber_user_idquery", 56),     ("updated_sincequery", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/matters.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_matter_show(client: TestClient):
    """Test case for matter_show

    Return the data for a single Matter
    """
    params = [("custom_field_idsquery", 56),     ("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_modified_sinc_eheader": '2013-10-20',
        "if_none_matc_hheader": 'if_none_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/matters/{id}.json".format(idpath=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_matter_update(client: TestClient):
    """Test case for matter_update

    Update a single Matter
    """
    matter_update_request = clio_mock.MatterUpdateRequest()
    params = [("custom_field_idsquery", 56),     ("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_matc_hheader": 'if_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/matters/{id}.json".format(idpath=56),
    #    headers=headers,
    #    json=matter_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

