# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.activity_show import ActivityShow  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401
from clio_mock.models.task_template_list_copy_request import TaskTemplateListCopyRequest  # noqa: F401
from clio_mock.models.task_template_list_create_request import TaskTemplateListCreateRequest  # noqa: F401
from clio_mock.models.task_template_list_update_request import TaskTemplateListUpdateRequest  # noqa: F401


def test_task_template_list_copy(client: TestClient):
    """Test case for task_template_list_copy

    Copy a TaskTemplateList
    """
    task_template_list_copy_request = clio_mock.TaskTemplateListCopyRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/task_template_lists/{id}/copy.json".format(idpath=56),
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
    task_template_list_create_request = clio_mock.TaskTemplateListCreateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
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
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/task_template_lists/{id}.json".format(idpath=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_task_template_list_index(client: TestClient):
    """Test case for task_template_list_index

    Return the data for all TaskTemplateLists
    """
    params = [("created_sincequery", '2013-10-20T19:20:30+01:00'),     ("emptyquery", True),     ("fieldsquery", 'fieldsquery_example'),     ("idsquery", 56),     ("limitquery", 56),     ("orderquery", 'orderquery_example'),     ("page_tokenquery", 'page_tokenquery_example'),     ("practice_area_idquery", 56),     ("queryquery", 'queryquery_example'),     ("updated_sincequery", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
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
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_modified_sinc_eheader": '2013-10-20',
        "if_none_matc_hheader": 'if_none_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/task_template_lists/{id}.json".format(idpath=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_task_template_list_update(client: TestClient):
    """Test case for task_template_list_update

    Update a single TaskTemplateList
    """
    task_template_list_update_request = clio_mock.TaskTemplateListUpdateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_matc_hheader": 'if_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/task_template_lists/{id}.json".format(idpath=56),
    #    headers=headers,
    #    json=task_template_list_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

