# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.bank_account_create_request import BankAccountCreateRequest
from openapi_server.models.bank_account_list import BankAccountList
from openapi_server.models.bank_account_show import BankAccountShow
from openapi_server.models.bank_account_update_request import BankAccountUpdateRequest
from openapi_server.models.error import Error


class BaseBankAccountsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseBankAccountsApi.subclasses = BaseBankAccountsApi.subclasses + (cls,)
    async def bank_account_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        bank_account_create_request: Annotated[Optional[BankAccountCreateRequest], Field(description="Request Body for Bank Accounts")],
    ) -> BankAccountShow:
        """Outlines the parameters and data fields used when creating a new BankAccount"""
        ...


    async def bank_account_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the BankAccount.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single BankAccount"""
        ...


    async def bank_account_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter BankAccount records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter BankAccount records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of BankAccount records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the BankAccount records by the given field. Default: `id(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        show_empty_accounts: Annotated[Optional[StrictBool], Field(description="Filter BankAccount records to those having a zero or non zero balance.")],
        type: Annotated[Optional[StrictStr], Field(description="Filter BankAccount records to those having a specific type.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter BankAccount records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        user_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a BankAccount. The list will be filtered to include only the BankAccount records with the matching property.")],
    ) -> BankAccountList:
        """Outlines the parameters, optional and required, used when requesting the data for all BankAccounts"""
        ...


    async def bank_account_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the BankAccount.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> BankAccountShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single BankAccount"""
        ...


    async def bank_account_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the BankAccount.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        bank_account_update_request: Annotated[Optional[BankAccountUpdateRequest], Field(description="Request Body for Bank Accounts")],
    ) -> BankAccountShow:
        """Outlines the parameters and data fields used when updating a single BankAccount"""
        ...
