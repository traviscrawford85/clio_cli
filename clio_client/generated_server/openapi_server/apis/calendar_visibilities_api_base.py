# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictInt, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.calendar_visibility_list import CalendarVisibilityList
from openapi_server.models.calendar_visibility_show import CalendarVisibilityShow
from openapi_server.models.calendar_visibility_update_request import CalendarVisibilityUpdateRequest
from openapi_server.models.error import Error


class BaseCalendarVisibilitiesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseCalendarVisibilitiesApi.subclasses = BaseCalendarVisibilitiesApi.subclasses + (cls,)
    async def calendar_visibility_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter CalendarVisibility records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter CalendarVisibility records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of CalendarVisibility records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter CalendarVisibility records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> CalendarVisibilityList:
        """Outlines the parameters, optional and required, used when requesting the data for all CalendarVisibilities"""
        ...


    async def calendar_visibility_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the CalendarVisibility.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> CalendarVisibilityShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single CalendarVisibility"""
        ...


    async def calendar_visibility_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the CalendarVisibility.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        calendar_visibility_update_request: Annotated[Optional[CalendarVisibilityUpdateRequest], Field(description="Request Body for Task Calendars")],
    ) -> CalendarVisibilityShow:
        """Outlines the parameters and data fields used when updating a single CalendarVisibility"""
        ...
