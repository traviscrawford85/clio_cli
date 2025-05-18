# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_description_create_request import ActivityDescriptionCreateRequest  # noqa: F401
from clio_mock.models.activity_description_update_request import ActivityDescriptionUpdateRequest  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.activity_show import ActivityShow  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401


def test_activity_description_create(client: TestClient):
    """Test case for activity_description_create

    Create a new ActivityDescription
    """
    activity_description_create_request = clio_mock.ActivityDescriptionCreateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/activity_descriptions.json",
    #    headers=headers,
    #    json=activity_description_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_activity_description_destroy(client: TestClient):
    """Test case for activity_description_destroy

    Delete a single ActivityDescription
    """

    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/activity_descriptions/{id}.json".format(idpath=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_activity_description_index(client: TestClient):
    """Test case for activity_description_index

    Return the data for all ActivityDescriptions
    """
    params = [("created_sincequery", '2013-10-20T19:20:30+01:00'),     ("fieldsquery", 'fieldsquery_example'),     ("flat_ratequery", True),     ("idsquery", 56),     ("limitquery", 56),     ("page_tokenquery", 'page_tokenquery_example'),     ("rate_formatter_idquery", 56),     ("rate_foruser_idquery", 56),     ("typequery", 'typequery_example'),     ("updated_sincequery", '2013-10-20T19:20:30+01:00'),     ("user_idquery", 56)]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/activity_descriptions.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_activity_description_show(client: TestClient):
    """Test case for activity_description_show

    Return the data for a single ActivityDescription
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
    #    "/activity_descriptions/{id}.json".format(idpath=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_activity_description_update(client: TestClient):
    """Test case for activity_description_update

    Update a single ActivityDescription
    """
    activity_description_update_request = clio_mock.ActivityDescriptionUpdateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_matc_hheader": 'if_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/activity_descriptions/{id}.json".format(idpath=56),
    #    headers=headers,
    #    json=activity_description_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

