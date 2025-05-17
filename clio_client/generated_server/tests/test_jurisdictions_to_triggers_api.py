# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.jurisdictions_to_trigger_list import JurisdictionsToTriggerList  # noqa: F401
from openapi_server.models.jurisdictions_to_trigger_show import JurisdictionsToTriggerShow  # noqa: F401


def test_jurisdictions_to_trigger_index(client: TestClient):
    """Test case for jurisdictions_to_trigger_index

    Return the data for all triggers
    """
    params = [("created_since", '2013-10-20T19:20:30+01:00'),     ("fields", 'fields_example'),     ("ids", 56),     ("is_requirements_required", True),     ("is_served", True),     ("limit", 56),     ("order", 'order_example'),     ("page_token", 'page_token_example'),     ("query", 'query_example'),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/court_rules/jurisdictions/{jurisdiction_id}/triggers.json".format(jurisdiction_id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_jurisdictions_to_trigger_show(client: TestClient):
    """Test case for jurisdictions_to_trigger_show

    Return the data for the trigger
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
    #    "/court_rules/jurisdictions/{jurisdiction_id}/triggers/{id}.json".format(id=56, jurisdiction_id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

