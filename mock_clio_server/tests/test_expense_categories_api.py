# coding: utf-8

from fastapi.testclient import TestClient


from datetime import date, datetime  # noqa: F401
from pydantic import Field, StrictInt, StrictStr, field_validator  # noqa: F401
from typing import Any, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from clio_mock.models.activity_list import ActivityList  # noqa: F401
from clio_mock.models.activity_show import ActivityShow  # noqa: F401
from clio_mock.models.error import Error  # noqa: F401
from clio_mock.models.expense_category_create_request import ExpenseCategoryCreateRequest  # noqa: F401
from clio_mock.models.expense_category_update_request import ExpenseCategoryUpdateRequest  # noqa: F401


def test_expense_category_create(client: TestClient):
    """Test case for expense_category_create

    Create a new ExpenseCategory
    """
    expense_category_create_request = clio_mock.ExpenseCategoryCreateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/expense_categories.json",
    #    headers=headers,
    #    json=expense_category_create_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_expense_category_destroy(client: TestClient):
    """Test case for expense_category_destroy

    Delete a single ExpenseCategory
    """

    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/expense_categories/{id}.json".format(idpath=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_expense_category_index(client: TestClient):
    """Test case for expense_category_index

    Return the data for all ExpenseCategories
    """
    params = [("created_sincequery", '2013-10-20T19:20:30+01:00'),     ("entry_typequery", 'entry_typequery_example'),     ("fieldsquery", 'fieldsquery_example'),     ("limitquery", 56),     ("orderquery", 'orderquery_example'),     ("page_tokenquery", 'page_tokenquery_example'),     ("queryquery", 'queryquery_example'),     ("updated_sincequery", '2013-10-20T19:20:30+01:00')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/expense_categories.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_expense_category_show(client: TestClient):
    """Test case for expense_category_show

    Return the data for a single ExpenseCategory
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
    #    "/expense_categories/{id}.json".format(idpath=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_expense_category_update(client: TestClient):
    """Test case for expense_category_update

    Update a single ExpenseCategory
    """
    expense_category_update_request = clio_mock.ExpenseCategoryUpdateRequest()
    params = [("fieldsquery", 'fieldsquery_example')]
    headers = {
        "if_matc_hheader": 'if_matc_hheader_example',
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PATCH",
    #    "/expense_categories/{id}.json".format(idpath=56),
    #    headers=headers,
    #    json=expense_category_update_request,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_lauk_expense_category_index(client: TestClient):
    """Test case for lauk_expense_category_index

    List Expense Categories
    """
    params = [("fieldsquery", 'fieldsquery_example'),     ("keyquery", 'keyquery_example'),     ("limitquery", 56),     ("namequery", 'namequery_example'),     ("page_tokenquery", 'page_tokenquery_example'),     ("practice_areaquery", 'practice_areaquery_example'),     ("regionquery", 'regionquery_example')]
    headers = {
        "x_api_versio_nheader": 'x_api_versio_nheader_example',
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/lauk_expense_categories.json",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

