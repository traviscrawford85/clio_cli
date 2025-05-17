# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.line_item_list import LineItemList
from openapi_server.models.line_item_show import LineItemShow
from openapi_server.models.line_item_update_request import LineItemUpdateRequest


class BaseLineItemsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseLineItemsApi.subclasses = BaseLineItemsApi.subclasses + (cls,)
    async def line_item_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the LineItem.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """A LineItem can not be deleted if it&#39;s Bill is not editable"""
        ...


    async def line_item_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        activity_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Activity. Use the keyword `null` to match those without a LineItem. The list will be filtered to include only the LineItem records with the matching property.")],
        bill_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Bill. The keyword `null` is not valid for this field. The list will be filtered to include only the LineItem records with the matching property.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter LineItem records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        display: Annotated[Optional[StrictBool], Field(description="Set this flag to true to return only LineItems displayed on the bill.")],
        exclude_ids: Annotated[Optional[StrictInt], Field(description="Array containing LineItem identifiers that should be excluded from the query.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        group_ordering: Annotated[Optional[StrictInt], Field(description="Filters LineItem records to match given group ordering.")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter LineItem records to those having the specified unique identifiers.")],
        kind: Annotated[Optional[StrictStr], Field(description="The kind of LineItem.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of LineItem records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        matter_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a LineItem. The list will be filtered to include only the LineItem records with the matching property.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `description` or `note` matching a given string.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter LineItem records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> LineItemList:
        """Outlines the parameters, optional and required, used when requesting the data for all LineItems"""
        ...


    async def line_item_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the LineItem.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        line_item_update_request: Annotated[Optional[LineItemUpdateRequest], Field(description="Request Body for Line Items")],
    ) -> LineItemShow:
        """Outlines the parameters and data fields used when updating a single LineItem"""
        ...
