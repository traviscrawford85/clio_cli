# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.conversation_list import ConversationList
from openapi_server.models.conversation_show import ConversationShow
from openapi_server.models.conversation_update_request import ConversationUpdateRequest
from openapi_server.models.error import Error


class BaseConversationsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseConversationsApi.subclasses = BaseConversationsApi.subclasses + (cls,)
    async def conversation_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        archived: Annotated[Optional[StrictBool], Field(description="Filter archived Conversation records.")],
        contact_id: Annotated[Optional[StrictInt], Field(description="Filter Conversation records for the contact.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter Conversation records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        var_date: Annotated[Optional[date], Field(description="Filter Conversation records created on a given date. (Expects an ISO-8601 date).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        for_user: Annotated[Optional[StrictBool], Field(description="If set to true, filter Conversation records accessible to any groups of the user. Note that the user may not be member of the conversations.  If set to false, filter Conversation records of which the user is a member. ")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter Conversation records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Conversation records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        matter_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Conversation. The list will be filtered to include only the Conversation records with the matching property.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the Conversation records by the given field. Default: `id(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        read_status: Annotated[Optional[StrictBool], Field(description="Filter Conversation records to those which have been read.")],
        time_entries: Annotated[Optional[StrictBool], Field(description="Filter Conversation records to those with or without associated time entries.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter Conversation records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> ConversationList:
        """Outlines the parameters, optional and required, used when requesting the data for all Conversations"""
        ...


    async def conversation_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Conversation.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> ConversationShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single Conversation"""
        ...


    async def conversation_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Conversation.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        conversation_update_request: Annotated[Optional[ConversationUpdateRequest], Field(description="Request Body for Conversations")],
    ) -> ConversationShow:
        """Outlines the parameters and data fields used when updating a single Conversation"""
        ...
