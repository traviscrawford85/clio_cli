# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.reminder_create_request import ReminderCreateRequest
from openapi_server.models.reminder_list import ReminderList
from openapi_server.models.reminder_show import ReminderShow
from openapi_server.models.reminder_update_request import ReminderUpdateRequest


class BaseRemindersApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseRemindersApi.subclasses = BaseRemindersApi.subclasses + (cls,)
    async def reminder_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        reminder_create_request: Annotated[Optional[ReminderCreateRequest], Field(description="Request Body for Reminders")],
    ) -> ReminderShow:
        """Outlines the parameters and data fields used when creating a new Reminder"""
        ...


    async def reminder_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Reminder.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single Reminder"""
        ...


    async def reminder_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter Reminder records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter Reminder records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Reminder records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        notification_method_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single NotificationMethod. The keyword `null` is not valid for this field. The list will be filtered to include only the Reminder records with the matching property.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the Reminder records by the given field. Default: `id(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        state: Annotated[Optional[StrictStr], Field(description="Filter Reminder records to those with a given state.")],
        subject_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single CalendarEntry or Task. The keyword `null` is not valid for this field. The list will be filtered to include only the Reminder records with the matching property.")],
        subject_type: Annotated[Optional[StrictStr], Field(description="Filter Reminder records to those of a given subject type, required if using subject_id.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter Reminder records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        user_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. The keyword `null` is not valid for this field. The list will be filtered to include only the Reminder records with the matching property.")],
    ) -> ReminderList:
        """Outlines the parameters, optional and required, used when requesting the data for all Reminders"""
        ...


    async def reminder_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Reminder.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> ReminderShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single Reminder"""
        ...


    async def reminder_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Reminder.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        reminder_update_request: Annotated[Optional[ReminderUpdateRequest], Field(description="Request Body for Reminders")],
    ) -> ReminderShow:
        """Outlines the parameters and data fields used when updating a single Reminder"""
        ...
