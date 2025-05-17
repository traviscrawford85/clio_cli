# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.note_create_request import NoteCreateRequest
from openapi_server.models.note_list import NoteList
from openapi_server.models.note_show import NoteShow
from openapi_server.models.note_update_request import NoteUpdateRequest


class BaseNotesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseNotesApi.subclasses = BaseNotesApi.subclasses + (cls,)
    async def note_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        note_create_request: Annotated[Optional[NoteCreateRequest], Field(description="Request Body for Notes")],
    ) -> NoteShow:
        """Outlines the parameters and data fields used when creating a new Note"""
        ...


    async def note_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Note.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single Note"""
        ...


    async def note_index(
        self,
        type: Annotated[StrictStr, Field(description="Filter Note records to those of the specified type.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        contact_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the Note records with the matching property.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter Note records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        has_time_entries: Annotated[Optional[StrictBool], Field(description="Filter Note records to those with or without associated time entries.")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter Note records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Note records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        matter_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. The keyword `null` is not valid for this field. The list will be filtered to include only the Note records with the matching property.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the Note records by the given field. Default: `id(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        query: Annotated[Optional[StrictStr], Field(description="Wildcard search across note subject and detail.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter Note records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> NoteList:
        """Outlines the parameters, optional and required, used when requesting the data for all Notes"""
        ...


    async def note_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Note.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> NoteShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single Note"""
        ...


    async def note_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Note.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        note_update_request: Annotated[Optional[NoteUpdateRequest], Field(description="Request Body for Notes")],
    ) -> NoteShow:
        """Outlines the parameters and data fields used when updating a single Note"""
        ...
