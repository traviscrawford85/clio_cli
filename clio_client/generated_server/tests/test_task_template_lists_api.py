# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.task_template_list_copy_request import TaskTemplateListCopyRequest  # noqa: F401
from openapi_server.models.task_template_list_create_request import TaskTemplateListCreateRequest  # noqa: F401
from openapi_server.models.task_template_list_list import TaskTemplateListList  # noqa: F401
from openapi_server.models.task_template_list_show import TaskTemplateListShow  # noqa: F401
from openapi_server.models.task_template_list_update_request import TaskTemplateListUpdateRequest  # noqa: F401


def test_task_template_list_copy(client: TestClient):
    """Test case for task_template_list_copy

    Copy a TaskTemplateList
    """
    task_template_list_copy_request = openapi_server.TaskTemplateListCopyRequest()
    params = [("fields", 'fields_example')]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/task_template_lists/{id}/copy.json".format(id=56),
    #    headers=headers,
    #    json=task_template_list_copy_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_task_template_list_create(client: TestClient):
    """Test case for task_template_list_create

    Create a new TaskTemplateList
    """
    task_template_list_create_request = openapi_server.TaskTemplateListCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/task_template_lists.json",
    #    headers=headers,
    #    json=task_template_list_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_task_template_list_destroy(client: TestClient):
    """Test case for task_template_list_destroy

    Delete a single TaskTemplateList
    """

    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/task_template_lists/{id}.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_task_template_list_index(client: TestClient):
    """Test case for task_template_list_index

    Return the data for all TaskTemplateLists
    """
    params = [("created_since", '2013-10-20T19:20:30+01:00'),     ("empty", True),     ("fields", 'fields_example'),     ("ids", 56),     ("limit", 56),     ("order", 'order_example'),     ("page_token", 'page_token_example'),     ("practice_area_id", 56),     ("query", 'query_example'),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/task_template_lists.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_task_template_list_show(client: TestClient):
    """Test case for task_template_list_show

    Return the data for a single TaskTemplateList
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
    #    "/task_template_lists/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_task_template_list_update(client: TestClient):
    """Test case for task_template_list_update

    Update a single TaskTemplateList
    """
    task_template_list_update_request = openapi_server.TaskTemplateListUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/task_template_lists/{id}.json".format(id=56),
    #    headers=headers,
    #    json=task_template_list_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

