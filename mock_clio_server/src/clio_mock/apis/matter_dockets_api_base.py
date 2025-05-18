# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from clio_mock.models.activity_list import ActivityList
from clio_mock.models.activity_show import ActivityShow
from clio_mock.models.matter_docket_create_request import MatterDocketCreateRequest


class BaseMatterDocketsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseMatterDocketsApi.subclasses = BaseMatterDocketsApi.subclasses + (cls,)
    async def matter_docket_create(
        self,
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        matter_docket_create_request: Annotated[Optional[MatterDocketCreateRequest], Field(description="Request Body for Matter Dockets")],
    ) -> ActivityShow:
        """Outlines the parameters and data fields used when creating a new MatterDocket"""
        ...


    async def matter_docket_destroy(
        self,
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single MatterDocket"""
        ...


    async def matter_docket_index(
        self,
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        created_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        idsquery: Annotated[Optional[StrictInt], Field(description="Filter Activity records to those having the specified unique identifiers.")],
        limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        matter_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")],
        matter_statusquery: Annotated[Optional[StrictStr], Field(description="Filter MatterDocket records to those with Matters having a specific status.")],
        orderquery: Annotated[Optional[StrictStr], Field(description="Orders the Activity records by the given field. Default: `id(asc)`.")],
        page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        queryquery: Annotated[Optional[StrictStr], Field(description="Wildcard search for `note` matching a given string.")],
        service_type_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single ServiceType. Use the keyword `null` to match those without a MatterDocket. The list will be filtered to include only the MatterDocket records with the matching property.")],
        statusquery: Annotated[Optional[StrictStr], Field(description="Filter Activity records to those that are draft, billed, unbilled or non-billable.")],
        updated_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> ActivityList:
        """Outlines the parameters, optional and required, used when requesting the data for all MatterDockets"""
        ...


    async def matter_docket_preview(
        self,
        jurisdictionidquery: Annotated[StrictInt, Field(description="The unique identifier for a single Jurisdiction. The keyword `null` is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property.")],
        service_typeidquery: Annotated[StrictInt, Field(description="The unique identifier for a single ServiceType. The keyword `null` is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property.")],
        start_timequery: Annotated[datetime, Field(description="The time the MatterDocket should start. (Expects an ISO-8601 timestamp).")],
        triggeridquery: Annotated[StrictInt, Field(description="The unique identifier for a single JurisdictionsToTrigger. The keyword `null` is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property.")],
        event_prefixquery: Annotated[Optional[StrictStr], Field(description="The prefix that will be added to the beginning of all court rule event titles")],
        start_datequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those whose `date` is on or after the date provided (Expects an ISO-8601 date).")],
    ) -> None:
        """Preview calendar dates for the docket"""
        ...


    async def matter_docket_show(
        self,
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
        if_modified_sinc_eheader: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> ActivityList:
        """Outlines the parameters, optional and required, used when requesting the data for a single MatterDocket"""
        ...
