# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.activity_show import ActivityShow  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401
from clio_mock.models.matter_docket_create_request import MatterDocketCreateRequest  # noqa: F401


def test_matter_docket_create(client: TestClient):
    """Test case for matter_docket_create

    Creates a matter docket
    """
    matter_docket_create_request = clio_mock.MatterDocketCreateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/court_rules/matter_dockets.json",
    #    headers=headers,
    #    json=matter_docket_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_matter_docket_destroy(client: TestClient):
    """Test case for matter_docket_destroy

    Deletes the requested matter docket
    """

    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/court_rules/matter_dockets/{id}.json".format(idpath=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_matter_docket_index(client: TestClient):
    """Test case for matter_docket_index

    Return the data for all matter dockets
    """
    params = [("created_sincequery", '2013-10-20T19:20:30+01:00'),     ("fieldsquery", 'fieldsquery_example'),     ("idsquery", 56),     ("limitquery", 56),     ("matter_idquery", 56),     ("matter_statusquery", 'matter_statusquery_example'),     ("orderquery", 'orderquery_example'),     ("page_tokenquery", 'page_tokenquery_example'),     ("queryquery", 'queryquery_example'),     ("service_type_idquery", 56),     ("statusquery", 'statusquery_example'),     ("updated_sincequery", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/court_rules/matter_dockets.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_matter_docket_preview(client: TestClient):
    """Test case for matter_docket_preview

    Preview calendar dates for the docket
    """
    params = [("event_prefixquery", 'event_prefixquery_example'),     ("jurisdictionidquery", 56),     ("service_typeidquery", 56),     ("start_datequery", '2013-10-20T19:20:30+01:00'),     ("start_timequery", '2013-10-20T19:20:30+01:00'),     ("triggeridquery", 56)]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/court_rules/matter_dockets/preview.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_matter_docket_show(client: TestClient):
    """Test case for matter_docket_show

    Return the data for the matter docket
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
    #    "/court_rules/matter_dockets/{id}.json".format(idpath=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

