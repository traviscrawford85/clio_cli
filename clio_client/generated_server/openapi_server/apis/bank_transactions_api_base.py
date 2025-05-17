# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.bank_transaction_list import BankTransactionList
from openapi_server.models.bank_transaction_show import BankTransactionShow
from openapi_server.models.error import Error


class BaseBankTransactionsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseBankTransactionsApi.subclasses = BaseBankTransactionsApi.subclasses + (cls,)
    async def bank_transaction_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        bank_account_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single BankAccount. The keyword `null` is not valid for this field. The list will be filtered to include only the BankTransaction records with the matching property.")],
        client_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the BankTransaction records with the matching property.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter BankTransaction records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter BankTransaction records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of BankTransaction records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        matter_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. The keyword `null` is not valid for this field. The list will be filtered to include only the BankTransaction records with the matching property.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the BankTransaction records by the given field. Default: `id(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        type: Annotated[Optional[StrictStr], Field(description="Filter BankTransaction records to those having a specific type.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter BankTransaction records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> BankTransactionList:
        """Outlines the parameters, optional and required, used when requesting the data for all BankTransactions"""
        ...


    async def bank_transaction_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the BankTransaction.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> BankTransactionShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single BankTransaction"""
        ...
