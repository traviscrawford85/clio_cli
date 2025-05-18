# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.activity_show import ActivityShow  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401
from clio_mock.models.task_create_request import TaskCreateRequest  # noqa: F401
from clio_mock.models.task_update_request import TaskUpdateRequest  # noqa: F401


def test_task_create(client: TestClient):
    """Test case for task_create

    Create a new Task
    """
    task_create_request = clio_mock.TaskCreateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
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
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/tasks/{id}.json".format(idpath=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_task_index(client: TestClient):
    """Test case for task_index

    Return the data for all Tasks
    """
    params = [("assignee_idquery", 56),     ("assignee_typequery", 'assignee_typequery_example'),     ("assigner_idquery", 56),     ("cascading_source_idquery", 56),     ("client_idquery", 56),     ("completequery", True),     ("created_sincequery", '2013-10-20T19:20:30+01:00'),     ("due_at_fromquery", '2013-10-20'),     ("due_at_presentquery", True),     ("due_at_toquery", '2013-10-20'),     ("fieldsquery", 'fieldsquery_example'),     ("idsquery", 56),     ("limitquery", 56),     ("matter_idquery", 56),     ("orderquery", 'orderquery_example'),     ("page_tokenquery", 'page_tokenquery_example'),     ("permissionquery", 'permissionquery_example'),     ("priorityquery", 'priorityquery_example'),     ("queryquery", 'queryquery_example'),     ("responsible_attorney_idquery", 56),     ("statusquery", 'statusquery_example'),     ("statusesquery", 'statusesquery_example'),     ("statute_of_limitationsquery", True),     ("task_type_idquery", 56),     ("time_entries_presentquery", True),     ("updated_sincequery", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
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
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_modified_sinc_eheader": '2013-10-20',
        "if_none_matc_hheader": 'if_none_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/tasks/{id}.json".format(idpath=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_task_update(client: TestClient):
    """Test case for task_update

    Update a single Task
    """
    task_update_request = clio_mock.TaskUpdateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_matc_hheader": 'if_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/tasks/{id}.json".format(idpath=56),
    #    headers=headers,
    #    json=task_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

