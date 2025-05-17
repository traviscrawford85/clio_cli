# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.calendar_create_request import CalendarCreateRequest
from openapi_server.models.calendar_list import CalendarList
from openapi_server.models.calendar_show import CalendarShow
from openapi_server.models.calendar_update_request import CalendarUpdateRequest
from openapi_server.models.error import Error


class BaseCalendarsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseCalendarsApi.subclasses = BaseCalendarsApi.subclasses + (cls,)
    async def calendar_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        calendar_create_request: Annotated[Optional[CalendarCreateRequest], Field(description="Request Body for Calendars")],
    ) -> CalendarShow:
        """Outlines the parameters and data fields used when creating a new Calendar"""
        ...


    async def calendar_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Calendar.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single Calendar"""
        ...


    async def calendar_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter Calendar records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        filter_inactive_users: Annotated[Optional[StrictBool], Field(description="Filter any shared UserCalendar records whose owner is inactive.")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter Calendar records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Calendar records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the Calendar records by the given field. Default: `id(asc)`.")],
        owner: Annotated[Optional[StrictBool], Field(description="Filter Calendar records to those that the user owns.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        source: Annotated[Optional[StrictStr], Field(description="Filter Calendar records to those having a specific calendar visibility source (mobile, web).")],
        type: Annotated[Optional[StrictStr], Field(description="Filter Calendar records to those of the specified type.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter Calendar records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        visible: Annotated[Optional[StrictBool], Field(description="Filter Calendar records to those that are visible.")],
        writeable: Annotated[Optional[StrictBool], Field(description="Filter Calendar records to those which the user can write to.")],
    ) -> CalendarList:
        """Outlines the parameters, optional and required, used when requesting the data for all Calendars"""
        ...


    async def calendar_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Calendar.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> CalendarShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single Calendar"""
        ...


    async def calendar_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Calendar.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        calendar_update_request: Annotated[Optional[CalendarUpdateRequest], Field(description="Request Body for Calendars")],
    ) -> CalendarShow:
        """Outlines the parameters and data fields used when updating a single Calendar"""
        ...
