# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictInt, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.activity_show import ActivityShow  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401
from clio_mock.models.report_schedule_create_request import ReportScheduleCreateRequest  # noqa: F401
from clio_mock.models.report_schedule_update_request import ReportScheduleUpdateRequest  # noqa: F401


def test_report_schedule_create(client: TestClient):
    """Test case for report_schedule_create

    Create a new ReportSchedule
    """
    report_schedule_create_request = clio_mock.ReportScheduleCreateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
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
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/report_schedules/{id}.json".format(idpath=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_report_schedule_index(client: TestClient):
    """Test case for report_schedule_index

    Return the data for all ReportSchedules
    """
    params = [("created_sincequery", '2013-10-20T19:20:30+01:00'),     ("fieldsquery", 'fieldsquery_example'),     ("idsquery", 56),     ("limitquery", 56),     ("page_tokenquery", 'page_tokenquery_example'),     ("updated_sincequery", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
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
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_modified_sinc_eheader": '2013-10-20',
        "if_none_matc_hheader": 'if_none_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/report_schedules/{id}.json".format(idpath=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_report_schedule_update(client: TestClient):
    """Test case for report_schedule_update

    Update a single ReportSchedule
    """
    report_schedule_update_request = clio_mock.ReportScheduleUpdateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_matc_hheader": 'if_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/report_schedules/{id}.json".format(idpath=56),
    #    headers=headers,
    #    json=report_schedule_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

