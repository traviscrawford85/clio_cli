# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.communication_create_request import CommunicationCreateRequest
from openapi_server.models.communication_list import CommunicationList
from openapi_server.models.communication_show import CommunicationShow
from openapi_server.models.communication_update_request import CommunicationUpdateRequest
from openapi_server.models.error import Error


class BaseCommunicationsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseCommunicationsApi.subclasses = BaseCommunicationsApi.subclasses + (cls,)
    async def communication_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        communication_create_request: Annotated[Optional[CommunicationCreateRequest], Field(description="Request Body for Communications")],
    ) -> CommunicationShow:
        """Outlines the parameters and data fields used when creating a new Communication"""
        ...


    async def communication_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Communication.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single Communication"""
        ...


    async def communication_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        contact_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the Communication records with the matching property.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter Communication records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        var_date: Annotated[Optional[date], Field(description="Filter Communication records to those that occur on the specified date (Expects an ISO-8601 date).")],
        external_property_name: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given external property(s) name set.  e.g. `?external_property_name=Name` ")],
        external_property_value: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. `?external_property_name=Name&external_property_value=Value` ")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        having_time_entries: Annotated[Optional[StrictBool], Field(description="Filter Communication records to those that do or do not have time entries.")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter Communication records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Communication records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        matter_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Communication. The list will be filtered to include only the Communication records with the matching property.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the Communication records by the given field. Default: `date(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `body` or `subject` matching a given string.")],
        received_at: Annotated[Optional[datetime], Field(description="Filter Communication records to those that occur on the specified date (Expects an ISO-8601 date-time).")],
        received_before: Annotated[Optional[datetime], Field(description="Filter Communication records to those whose `date` is on or before the date provided (Expects an ISO-8601 date).")],
        received_since: Annotated[Optional[datetime], Field(description="Filter Communication records to those whose `date` is on or after the date provided (Expects an ISO-8601 date).")],
        type: Annotated[Optional[StrictStr], Field(description="Filter Communication records to those of the specified type.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter Communication records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        user_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. The keyword `null` is not valid for this field. The list will be filtered to include only the Communication records with the matching property.")],
    ) -> CommunicationList:
        """Outlines the parameters, optional and required, used when requesting the data for all Communications"""
        ...


    async def communication_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Communication.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> CommunicationShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single Communication"""
        ...


    async def communication_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Communication.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        communication_update_request: Annotated[Optional[CommunicationUpdateRequest], Field(description="Request Body for Communications")],
    ) -> CommunicationShow:
        """Outlines the parameters and data fields used when updating a single Communication"""
        ...
