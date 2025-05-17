# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.task_create_request import TaskCreateRequest  # noqa: F401
from openapi_server.models.task_list import TaskList  # noqa: F401
from openapi_server.models.task_show import TaskShow  # noqa: F401
from openapi_server.models.task_update_request import TaskUpdateRequest  # noqa: F401


def test_task_create(client: TestClient):
    """Test case for task_create

    Create a new Task
    """
    task_create_request = openapi_server.TaskCreateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/tasks.json",
    #    headers=headers,
    #    json=task_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_task_destroy(client: TestClient):
    """Test case for task_destroy

    Delete a single Task
    """

    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/tasks/{id}.json".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_task_index(client: TestClient):
    """Test case for task_index

    Return the data for all Tasks
    """
    params = [("assignee_id", 56),     ("assignee_type", 'assignee_type_example'),     ("assigner_id", 56),     ("cascading_source_id", 56),     ("client_id", 56),     ("complete", True),     ("created_since", '2013-10-20T19:20:30+01:00'),     ("due_at_from", '2013-10-20'),     ("due_at_present", True),     ("due_at_to", '2013-10-20'),     ("fields", 'fields_example'),     ("ids", 56),     ("limit", 56),     ("matter_id", 56),     ("order", 'order_example'),     ("page_token", 'page_token_example'),     ("permission", 'permission_example'),     ("priority", 'priority_example'),     ("query", 'query_example'),     ("responsible_attorney_id", 56),     ("status", 'status_example'),     ("statuses", 'statuses_example'),     ("statute_of_limitations", True),     ("task_type_id", 56),     ("time_entries_present", True),     ("updated_since", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/tasks.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_task_show(client: TestClient):
    """Test case for task_show

    Return the data for a single Task
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
    #    "/tasks/{id}.json".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_task_update(client: TestClient):
    """Test case for task_update

    Update a single Task
    """
    task_update_request = openapi_server.TaskUpdateRequest()
    params = [("fields", 'fields_example')]
    headers = {
        "if_match": 'if_match_example',
        "x_api_version": 'x_api_version_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/tasks/{id}.json".format(id=56),
    #    headers=headers,
    #    json=task_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

