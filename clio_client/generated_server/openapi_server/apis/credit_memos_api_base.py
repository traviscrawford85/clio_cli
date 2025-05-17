# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.credit_memo_list import CreditMemoList
from openapi_server.models.credit_memo_show import CreditMemoShow
from openapi_server.models.error import Error


class BaseCreditMemosApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseCreditMemosApi.subclasses = BaseCreditMemosApi.subclasses + (cls,)
    async def credit_memo_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        contact_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the CreditMemo records with the matching property.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter CreditMemo records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter CreditMemo records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of CreditMemo records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the CreditMemo records by the given field. Default: `date(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter CreditMemo records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> CreditMemoList:
        """Outlines the parameters, optional and required, used when requesting the data for all CreditMemos"""
        ...


    async def credit_memo_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the CreditMemo.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> CreditMemoShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single CreditMemo"""
        ...
