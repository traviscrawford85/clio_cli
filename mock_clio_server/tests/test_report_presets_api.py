# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.activity_show import ActivityShow  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401
from clio_mock.models.report_preset_create_request import ReportPresetCreateRequest  # noqa: F401
from clio_mock.models.report_preset_update_request import ReportPresetUpdateRequest  # noqa: F401


def test_report_preset_create(client: TestClient):
    """Test case for report_preset_create

    Create a new ReportPreset
    """
    report_preset_create_request = clio_mock.ReportPresetCreateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/report_presets.json",
    #    headers=headers,
    #    json=report_preset_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_report_preset_destroy(client: TestClient):
    """Test case for report_preset_destroy

    Delete a single ReportPreset
    """

    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/report_presets/{id}.json".format(idpath=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_report_preset_generate_report(client: TestClient):
    """Test case for report_preset_generate_report

    Generate a new report for a given preset
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/report_presets/{id}/generate_report.json".format(idpath=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_report_preset_index(client: TestClient):
    """Test case for report_preset_index

    Return the data for all ReportPresets
    """
    params = [("categoryquery", 'categoryquery_example'),     ("created_sincequery", '2013-10-20T19:20:30+01:00'),     ("fieldsquery", 'fieldsquery_example'),     ("has_schedulequery", True),     ("idsquery", 56),     ("limitquery", 56),     ("orderquery", 'orderquery_example'),     ("output_formatquery", 'output_formatquery_example'),     ("page_tokenquery", 'page_tokenquery_example'),     ("queryquery", 'queryquery_example'),     ("schedule_frequencyquery", 'schedule_frequencyquery_example'),     ("updated_sincequery", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/report_presets.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_report_preset_show(client: TestClient):
    """Test case for report_preset_show

    Return the data for a single ReportPreset
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
    #    "/report_presets/{id}.json".format(idpath=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_report_preset_update(client: TestClient):
    """Test case for report_preset_update

    Update a single ReportPreset
    """
    report_preset_update_request = clio_mock.ReportPresetUpdateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_matc_hheader": 'if_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/report_presets/{id}.json".format(idpath=56),
    #    headers=headers,
    #    json=report_preset_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

