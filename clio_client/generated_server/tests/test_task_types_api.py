# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.task_type_create_request import TaskTypeCreateRequest  # noqa: F401
from openapi_server.models.task_type_list import TaskTypeList  # noqa: F401
from openapi_server.models.task_type_show import TaskTypeShow  # noqa: F401
from openapi_server.models.task_type_update_request import TaskTypeUpdateRequest  # noqa: F401


def test_task_type_create(client: TestClient):
    """Test case for task_type_create

    Create a new TaskType
    """
    task_type_create_request = openapi_server.TaskTypeCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/task_types.json",
    #    headers=headers,
    #    json=task_type_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_task_type_index(client: TestClient):
    """Test case for task_type_index

    Return the data for all TaskTypes
    """
    params = [("created_since", '2013-10-20T19:20:30+01:00'),     ("enabled", True),     ("fields", 'fields_example'),     ("ids", 56),     ("limit", 56),     ("name", 'name_example'),     ("order", 'order_example'),     ("page_token", 'page_token_example'),     ("query", 'query_example'),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/task_types.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_task_type_show(client: TestClient):
    """Test case for task_type_show

    Return the data for a single TaskType
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
    #    "/task_types/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_task_type_update(client: TestClient):
    """Test case for task_type_update

    Update a single TaskType
    """
    task_type_update_request = openapi_server.TaskTypeUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/task_types/{id}.json".format(id=56),
    #    headers=headers,
    #    json=task_type_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

