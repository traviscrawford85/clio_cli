# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.matter_docket_create_request import MatterDocketCreateRequest  # noqa: F401
from openapi_server.models.matter_docket_list import MatterDocketList  # noqa: F401
from openapi_server.models.matter_docket_show import MatterDocketShow  # noqa: F401


def test_matter_docket_create(client: TestClient):
    """Test case for matter_docket_create

    Creates a matter docket
    """
    matter_docket_create_request = openapi_server.MatterDocketCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
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
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/court_rules/matter_dockets/{id}.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_matter_docket_index(client: TestClient):
    """Test case for matter_docket_index

    Return the data for all matter dockets
    """
    params = [("created_since", '2013-10-20T19:20:30+01:00'),     ("fields", 'fields_example'),     ("ids", 56),     ("limit", 56),     ("matter_id", 56),     ("matter_status", 'matter_status_example'),     ("order", 'order_example'),     ("page_token", 'page_token_example'),     ("query", 'query_example'),     ("service_type_id", 56),     ("status", 'status_example'),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
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
    params = [("event_prefix", 'event_prefix_example'),     ("jurisdiction_id", 56),     ("service_type_id", 56),     ("start_date", '2013-10-20T19:20:30+01:00'),     ("start_time", '2013-10-20T19:20:30+01:00'),     ("trigger_id", 56)]
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
    params = [("fields", 'fields_example')]
    headers = {
        "if_modified_since": '2013-10-20',
        "if_none_match": 'if_none_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/court_rules/matter_dockets/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

