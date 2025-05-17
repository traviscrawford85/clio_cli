# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.expense_category_create_request import ExpenseCategoryCreateRequest
from openapi_server.models.expense_category_list import ExpenseCategoryList
from openapi_server.models.expense_category_show import ExpenseCategoryShow
from openapi_server.models.expense_category_update_request import ExpenseCategoryUpdateRequest
from openapi_server.models.lauk_expense_category_list import LaukExpenseCategoryList


class BaseExpenseCategoriesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseExpenseCategoriesApi.subclasses = BaseExpenseCategoriesApi.subclasses + (cls,)
    async def expense_category_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        expense_category_create_request: Annotated[Optional[ExpenseCategoryCreateRequest], Field(description="Request Body for Expense Categories")],
    ) -> ExpenseCategoryShow:
        """Outlines the parameters and data fields used when creating a new ExpenseCategory"""
        ...


    async def expense_category_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the ExpenseCategory.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single ExpenseCategory"""
        ...


    async def expense_category_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter ExpenseCategory records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        entry_type: Annotated[Optional[StrictStr], Field(description="Filter ExpenseCategory records to those that match the given type.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of ExpenseCategory records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the ExpenseCategory records by the given field. Default: `id(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        query: Annotated[Optional[StrictStr], Field(description="Allows matching search on expense category name.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter ExpenseCategory records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> ExpenseCategoryList:
        """Outlines the parameters, optional and required, used when requesting the data for all ExpenseCategories"""
        ...


    async def expense_category_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the ExpenseCategory.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> ExpenseCategoryShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single ExpenseCategory"""
        ...


    async def expense_category_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the ExpenseCategory.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        expense_category_update_request: Annotated[Optional[ExpenseCategoryUpdateRequest], Field(description="Request Body for Expense Categories")],
    ) -> ExpenseCategoryShow:
        """Outlines the parameters and data fields used when updating a single ExpenseCategory"""
        ...


    async def lauk_expense_category_index(
        self,
        region: Annotated[StrictStr, Field(description="Sets the expense rate returned based on the region. If the region is set to London, it will return the London rate; otherwise, it will return the non-London rate.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        key: Annotated[Optional[StrictStr], Field(description="Filter by key.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of LaukExpenseCategory records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        name: Annotated[Optional[StrictStr], Field(description="Filter by expense name.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        practice_area: Annotated[Optional[StrictStr], Field(description="Filter by expense practice area.")],
    ) -> LaukExpenseCategoryList:
        """Outlines the parameters, optional and required, used when requesting the data for all LaukExpenseCategories"""
        ...
