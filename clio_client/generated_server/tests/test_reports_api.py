# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.report_create_request import ReportCreateRequest  # noqa: F401
from openapi_server.models.report_list import ReportList  # noqa: F401
from openapi_server.models.report_show import ReportShow  # noqa: F401


def test_report_create(client: TestClient):
    """Test case for report_create

    Create a new Report
    """
    report_create_request = openapi_server.ReportCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/reports.json",
    #    headers=headers,
    #    json=report_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_report_download(client: TestClient):
    """Test case for report_download

    Download the completed Report
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/reports/{id}/download.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_report_index(client: TestClient):
    """Test case for report_index

    Return the data for all Reports
    """
    params = [("category", 'category_example'),     ("created_before", '2013-10-20T19:20:30+01:00'),     ("created_since", '2013-10-20T19:20:30+01:00'),     ("fields", 'fields_example'),     ("ids", 56),     ("kind", 'kind_example'),     ("limit", 56),     ("output_format", 'output_format_example'),     ("page_token", 'page_token_example'),     ("query", 'query_example'),     ("source", 'source_example'),     ("state", 'state_example'),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/reports.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_report_show(client: TestClient):
    """Test case for report_show

    Return the data for a single Report
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
    #    "/reports/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

