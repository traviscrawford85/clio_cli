# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.report_schedule_create_request import ReportScheduleCreateRequest  # noqa: F401
from openapi_server.models.report_schedule_list import ReportScheduleList  # noqa: F401
from openapi_server.models.report_schedule_show import ReportScheduleShow  # noqa: F401
from openapi_server.models.report_schedule_update_request import ReportScheduleUpdateRequest  # noqa: F401


def test_report_schedule_create(client: TestClient):
    """Test case for report_schedule_create

    Create a new ReportSchedule
    """
    report_schedule_create_request = openapi_server.ReportScheduleCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/report_schedules.json",
    #    headers=headers,
    #    json=report_schedule_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_report_schedule_destroy(client: TestClient):
    """Test case for report_schedule_destroy

    Delete a single ReportSchedule
    """

    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/report_schedules/{id}.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_report_schedule_index(client: TestClient):
    """Test case for report_schedule_index

    Return the data for all ReportSchedules
    """
    params = [("created_since", '2013-10-20T19:20:30+01:00'),     ("fields", 'fields_example'),     ("ids", 56),     ("limit", 56),     ("page_token", 'page_token_example'),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/report_schedules.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_report_schedule_show(client: TestClient):
    """Test case for report_schedule_show

    Return the data for a single ReportSchedule
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
    #    "/report_schedules/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_report_schedule_update(client: TestClient):
    """Test case for report_schedule_update

    Update a single ReportSchedule
    """
    report_schedule_update_request = openapi_server.ReportScheduleUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/report_schedules/{id}.json".format(id=56),
    #    headers=headers,
    #    json=report_schedule_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

