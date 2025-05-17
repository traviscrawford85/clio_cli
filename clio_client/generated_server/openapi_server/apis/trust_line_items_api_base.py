# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import datetime
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.trust_line_item_list import TrustLineItemList
from openapi_server.models.trust_line_item_show import TrustLineItemShow
from openapi_server.models.trust_line_item_update_request import TrustLineItemUpdateRequest


class BaseTrustLineItemsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseTrustLineItemsApi.subclasses = BaseTrustLineItemsApi.subclasses + (cls,)
    async def trust_line_item_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        bill_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Bill. The keyword `null` is not valid for this field. The list will be filtered to include only the TrustLineItem records with the matching property.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter TrustLineItem records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter TrustLineItem records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of TrustLineItem records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        matter_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a TrustLineItem. The list will be filtered to include only the TrustLineItem records with the matching property.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the TrustLineItem records by the given field. Default: `id(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter TrustLineItem records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> TrustLineItemList:
        """Outlines the parameters, optional and required, used when requesting the data for all TrustLineItems"""
        ...


    async def trust_line_item_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the TrustLineItem.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        trust_line_item_update_request: Annotated[Optional[TrustLineItemUpdateRequest], Field(description="Request Body for Trust Line Items")],
    ) -> TrustLineItemShow:
        """Outlines the parameters and data fields used when updating a single TrustLineItem"""
        ...
