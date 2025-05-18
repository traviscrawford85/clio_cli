# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from clio_mock.models.activity_list import ActivityList
from clio_mock.models.line_item_update_request import LineItemUpdateRequest


class BaseLineItemsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseLineItemsApi.subclasses = BaseLineItemsApi.subclasses + (cls,)
    async def line_item_destroy(
        self,
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """A LineItem can not be deleted if it&#39;s Bill is not editable"""
        ...


    async def line_item_index(
        self,
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        activity_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Activity. Use the keyword `null` to match those without a LineItem. The list will be filtered to include only the LineItem records with the matching property.")],
        bill_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Bill. The keyword `null` is not valid for this field. The list will be filtered to include only the Allocation records with the matching property.")],
        created_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        displayquery: Annotated[Optional[StrictBool], Field(description="Set this flag to true to return only LineItems displayed on the bill.")],
        exclude_idsquery: Annotated[Optional[StrictInt], Field(description="Filter Contact records to those who are not included in the given list of unique identifiers.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        group_orderingquery: Annotated[Optional[StrictInt], Field(description="Filters LineItem records to match given group ordering.")],
        idsquery: Annotated[Optional[StrictInt], Field(description="Filter Activity records to those having the specified unique identifiers.")],
        kindquery: Annotated[Optional[StrictStr], Field(description="The kind of LineItem.")],
        limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        matter_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")],
        page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        queryquery: Annotated[Optional[StrictStr], Field(description="Wildcard search for `note` matching a given string.")],
        updated_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> ActivityList:
        """Outlines the parameters, optional and required, used when requesting the data for all LineItems"""
        ...


    async def line_item_update(
        self,
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
        if_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        line_item_update_request: Annotated[Optional[LineItemUpdateRequest], Field(description="Request Body for Line Items")],
    ) -> ActivityList:
        """Outlines the parameters and data fields used when updating a single LineItem"""
        ...
