# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from clio_mock.models.activity_list import ActivityList
from clio_mock.models.activity_show import ActivityShow
from clio_mock.models.calendar_entry_create_request import CalendarEntryCreateRequest
from clio_mock.models.calendar_entry_update_request import CalendarEntryUpdateRequest


class BaseCalendarEntriesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseCalendarEntriesApi.subclasses = BaseCalendarEntriesApi.subclasses + (cls,)
    async def calendar_entry_create(
        self,
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        calendar_entry_create_request: Annotated[Optional[CalendarEntryCreateRequest], Field(description="Request Body for Calendar Entries")],
    ) -> ActivityShow:
        """Outlines the parameters and data fields used when creating a new CalendarEntry"""
        ...


    async def calendar_entry_destroy(
        self,
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single CalendarEntry"""
        ...


    async def calendar_entry_index(
        self,
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        calendar_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Calendar. The keyword `null` is not valid for this field. The list will be filtered to include only the CalendarEntry records with the matching property.")],
        created_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        expandedquery: Annotated[Optional[StrictBool], Field(description="Returns a record for each occurrence of a recurring calendar event.  Non-recurring calendar events are unaffected and returned as separate records regardless of the expanded setting.")],
        external_property_namequery: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given external property(s) name set.  e.g. `?external_property_name=Name` ")],
        external_property_valuequery: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given external property(s) value set. Requires external property name as well.  e.g. `?external_property_name=Name&external_property_value=Value` ")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        fromquery: Annotated[Optional[datetime], Field(description="Filter CalendarEntry records to those that end on or after the provided time (Expects an ISO-8601 timestamp).")],
        has_court_rulequery: Annotated[Optional[StrictBool], Field(description="Allows matching court rule on calendar entry.")],
        idsquery: Annotated[Optional[StrictInt], Field(description="Filter Activity records to those having the specified unique identifiers.")],
        is_all_dayquery: Annotated[Optional[StrictBool], Field(description="Filter CalendarEntry records to those that are marked as all day events.")],
        limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        matter_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")],
        owner_entries_across_all_usersquery: Annotated[Optional[StrictBool], Field(description="Returns CalendarEntry records for all users related to a matter. Requires matter id.")],
        page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        queryquery: Annotated[Optional[StrictStr], Field(description="Wildcard search for `note` matching a given string.")],
        sourcequery: Annotated[Optional[StrictStr], Field(description="Filter CalendarEntry records to those having a specific calendar visibility source (mobile, web).")],
        toquery: Annotated[Optional[datetime], Field(description="Filter CalendarEntry records to those that begin on or before the provided time (Expects an ISO-8601 timestamp).")],
        updated_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        visiblequery: Annotated[Optional[StrictBool], Field(description="Filter CalendarEntry records to those that are visible.")],
    ) -> ActivityList:
        """Outlines the parameters, optional and required, used when requesting the data for all CalendarEntries"""
        ...


    async def calendar_entry_show(
        self,
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
        if_modified_sinc_eheader: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> ActivityList:
        """Outlines the parameters, optional and required, used when requesting the data for a single CalendarEntry"""
        ...


    async def calendar_entry_update(
        self,
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
        if_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        calendar_entry_update_request: Annotated[Optional[CalendarEntryUpdateRequest], Field(description="Request Body for Calendar Entries")],
    ) -> ActivityList:
        """Outlines the parameters and data fields used when updating a single CalendarEntry"""
        ...
