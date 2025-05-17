# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.report_preset_create_request import ReportPresetCreateRequest  # noqa: F401
from openapi_server.models.report_preset_list import ReportPresetList  # noqa: F401
from openapi_server.models.report_preset_show import ReportPresetShow  # noqa: F401
from openapi_server.models.report_preset_update_request import ReportPresetUpdateRequest  # noqa: F401
from openapi_server.models.report_show import ReportShow  # noqa: F401


def test_report_preset_create(client: TestClient):
    """Test case for report_preset_create

    Create a new ReportPreset
    """
    report_preset_create_request = openapi_server.ReportPresetCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
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
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/report_presets/{id}.json".format(id=56),
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
    #    "/report_presets/{id}/generate_report.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_report_preset_index(client: TestClient):
    """Test case for report_preset_index

    Return the data for all ReportPresets
    """
    params = [("category", 'category_example'),     ("created_since", '2013-10-20T19:20:30+01:00'),     ("fields", 'fields_example'),     ("has_schedule", True),     ("ids", 56),     ("limit", 56),     ("order", 'order_example'),     ("output_format", 'output_format_example'),     ("page_token", 'page_token_example'),     ("query", 'query_example'),     ("schedule_frequency", 'schedule_frequency_example'),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
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
    params = [("fields", 'fields_example')]
    headers = {
        "if_modified_since": '2013-10-20',
        "if_none_match": 'if_none_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/report_presets/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_report_preset_update(client: TestClient):
    """Test case for report_preset_update

    Update a single ReportPreset
    """
    report_preset_update_request = openapi_server.ReportPresetUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/report_presets/{id}.json".format(id=56),
    #    headers=headers,
    #    json=report_preset_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

