# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.task_template_create_request import TaskTemplateCreateRequest  # noqa: F401
from openapi_server.models.task_template_list import TaskTemplateList  # noqa: F401
from openapi_server.models.task_template_show import TaskTemplateShow  # noqa: F401
from openapi_server.models.task_template_update_request import TaskTemplateUpdateRequest  # noqa: F401


def test_task_template_create(client: TestClient):
    """Test case for task_template_create

    Create a new TaskTemplate
    """
    task_template_create_request = openapi_server.TaskTemplateCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/task_templates.json",
    #    headers=headers,
    #    json=task_template_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_task_template_destroy(client: TestClient):
    """Test case for task_template_destroy

    Delete a single TaskTemplate
    """

    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/task_templates/{id}.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_task_template_index(client: TestClient):
    """Test case for task_template_index

    Return the data for all TaskTemplates
    """
    params = [("created_since", '2013-10-20T19:20:30+01:00'),     ("fields", 'fields_example'),     ("ids", 56),     ("limit", 56),     ("order", 'order_example'),     ("page_token", 'page_token_example'),     ("priority", 'priority_example'),     ("query", 'query_example'),     ("task_template_list_id", 56),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/task_templates.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_task_template_show(client: TestClient):
    """Test case for task_template_show

    Return the data for a single TaskTemplate
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
    #    "/task_templates/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_task_template_update(client: TestClient):
    """Test case for task_template_update

    Update a single TaskTemplate
    """
    task_template_update_request = openapi_server.TaskTemplateUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/task_templates/{id}.json".format(id=56),
    #    headers=headers,
    #    json=task_template_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

