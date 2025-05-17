# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date  # noqa: F401
from pydantic import Field, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.billing_setting_show import BillingSettingShow  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401


def test_billing_setting_show(client: TestClient):
    """Test case for billing_setting_show

    Return the billing settings
    """
    params = [("duration", 'duration_example'),     ("fields", 'fields_example')]
    headers = {
        "if_modified_since": '2013-10-20',
        "if_none_match": 'if_none_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/settings/billing.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

