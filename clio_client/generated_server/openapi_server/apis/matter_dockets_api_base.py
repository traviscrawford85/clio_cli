# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.matter_docket_create_request import MatterDocketCreateRequest
from openapi_server.models.matter_docket_list import MatterDocketList
from openapi_server.models.matter_docket_show import MatterDocketShow


class BaseMatterDocketsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseMatterDocketsApi.subclasses = BaseMatterDocketsApi.subclasses + (cls,)
    async def matter_docket_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        matter_docket_create_request: Annotated[Optional[MatterDocketCreateRequest], Field(description="Request Body for Matter Dockets")],
    ) -> MatterDocketShow:
        """Outlines the parameters and data fields used when creating a new MatterDocket"""
        ...


    async def matter_docket_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the MatterDocket.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single MatterDocket"""
        ...


    async def matter_docket_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter MatterDocket records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter MatterDocket records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of MatterDocket records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        matter_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. The keyword `null` is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property.")],
        matter_status: Annotated[Optional[StrictStr], Field(description="Filter MatterDocket records to those with Matters having a specific status.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the MatterDocket records by the given field. Default: `id(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `name` matching a given string.")],
        service_type_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single ServiceType. Use the keyword `null` to match those without a MatterDocket. The list will be filtered to include only the MatterDocket records with the matching property.")],
        status: Annotated[Optional[StrictStr], Field(description="Filter MatterDocket records to those having a specific status.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter MatterDocket records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> MatterDocketList:
        """Outlines the parameters, optional and required, used when requesting the data for all MatterDockets"""
        ...


    async def matter_docket_preview(
        self,
        jurisdiction_id: Annotated[StrictInt, Field(description="The unique identifier for a single Jurisdiction. The keyword `null` is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property.")],
        service_type_id: Annotated[StrictInt, Field(description="The unique identifier for a single ServiceType. The keyword `null` is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property.")],
        start_date: Annotated[datetime, Field(description="The date the MatterDocket should start. (Expects an ISO-8601 date).")],
        start_time: Annotated[datetime, Field(description="The time the MatterDocket should start. (Expects an ISO-8601 timestamp).")],
        trigger_id: Annotated[StrictInt, Field(description="The unique identifier for a single JurisdictionsToTrigger. The keyword `null` is not valid for this field. The list will be filtered to include only the MatterDocket records with the matching property.")],
        event_prefix: Annotated[Optional[StrictStr], Field(description="The prefix that will be added to the beginning of all court rule event titles")],
    ) -> None:
        """Preview calendar dates for the docket"""
        ...


    async def matter_docket_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the MatterDocket.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> MatterDocketShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single MatterDocket"""
        ...
