# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_create_request import ActivityCreateRequest  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.activity_show import ActivityShow  # noqa: F401
from clio_mock.models.activity_update_request import ActivityUpdateRequest  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401


def test_activity_create(client: TestClient):
    """Test case for activity_create

    Create a new Activity
    """
    activity_create_request = clio_mock.ActivityCreateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/activities.json",
    #    headers=headers,
    #    json=activity_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_activity_destroy(client: TestClient):
    """Test case for activity_destroy

    Delete a single Activity
    """

    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/activities/{id}.json".format(idpath=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_activity_index(client: TestClient):
    """Test case for activity_index

    Return the data for all Activities
    """
    params = [("activity_description_idquery", 56),     ("calendar_entry_idquery", 56),     ("communication_idquery", 56),     ("contact_note_idquery", 56),     ("created_sincequery", '2013-10-20T19:20:30+01:00'),     ("end_datequery", '2013-10-20T19:20:30+01:00'),     ("expense_category_idquery", 56),     ("fieldsquery", 'fieldsquery_example'),     ("flat_ratequery", True),     ("grant_idquery", 56),     ("idsquery", 56),     ("limitquery", 56),     ("matter_idquery", 56),     ("matter_note_idquery", 56),     ("only_unaccounted_forquery", True),     ("orderquery", 'orderquery_example'),     ("page_tokenquery", 'page_tokenquery_example'),     ("queryquery", 'queryquery_example'),     ("start_datequery", '2013-10-20T19:20:30+01:00'),     ("statusquery", 'statusquery_example'),     ("task_idquery", 56),     ("typequery", 'typequery_example'),     ("updated_sincequery", '2013-10-20T19:20:30+01:00'),     ("user_idquery", 56)]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/activities.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_activity_show(client: TestClient):
    """Test case for activity_show

    Return the data for a single Activity
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
    #    "/activities/{id}.json".format(idpath=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_activity_update(client: TestClient):
    """Test case for activity_update

    Update a single Activity
    """
    activity_update_request = clio_mock.ActivityUpdateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_matc_hheader": 'if_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/activities/{id}.json".format(idpath=56),
    #    headers=headers,
    #    json=activity_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

