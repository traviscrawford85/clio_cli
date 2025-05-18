# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.activity_show import ActivityShow  # noqa: F401
from clio_mock.models.communication_create_request import CommunicationCreateRequest  # noqa: F401
from clio_mock.models.communication_update_request import CommunicationUpdateRequest  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401


def test_communication_create(client: TestClient):
    """Test case for communication_create

    Create a new Communication
    """
    communication_create_request = clio_mock.CommunicationCreateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/communications.json",
    #    headers=headers,
    #    json=communication_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_communication_destroy(client: TestClient):
    """Test case for communication_destroy

    Delete a single Communication
    """

    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/communications/{id}.json".format(idpath=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_communication_index(client: TestClient):
    """Test case for communication_index

    Return the data for all Communications
    """
    params = [("contact_idquery", 56),     ("created_sincequery", '2013-10-20T19:20:30+01:00'),     ("datequery", '2013-10-20'),     ("external_property_namequery", 'external_property_namequery_example'),     ("external_property_valuequery", 'external_property_valuequery_example'),     ("fieldsquery", 'fieldsquery_example'),     ("having_time_entriesquery", True),     ("idsquery", 56),     ("limitquery", 56),     ("matter_idquery", 56),     ("orderquery", 'orderquery_example'),     ("page_tokenquery", 'page_tokenquery_example'),     ("queryquery", 'queryquery_example'),     ("received_atquery", '2013-10-20T19:20:30+01:00'),     ("received_beforequery", '2013-10-20T19:20:30+01:00'),     ("received_sincequery", '2013-10-20T19:20:30+01:00'),     ("typequery", 'typequery_example'),     ("updated_sincequery", '2013-10-20T19:20:30+01:00'),     ("user_idquery", 56)]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/communications.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_communication_show(client: TestClient):
    """Test case for communication_show

    Return the data for a single Communication
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
    #    "/communications/{id}.json".format(idpath=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_communication_update(client: TestClient):
    """Test case for communication_update

    Update a single Communication
    """
    communication_update_request = clio_mock.CommunicationUpdateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_matc_hheader": 'if_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/communications/{id}.json".format(idpath=56),
    #    headers=headers,
    #    json=communication_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

