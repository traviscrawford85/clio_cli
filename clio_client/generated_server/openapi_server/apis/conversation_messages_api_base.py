# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.conversation_message_create_request import ConversationMessageCreateRequest
from openapi_server.models.conversation_message_list import ConversationMessageList
from openapi_server.models.conversation_message_show import ConversationMessageShow
from openapi_server.models.error import Error


class BaseConversationMessagesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseConversationMessagesApi.subclasses = BaseConversationMessagesApi.subclasses + (cls,)
    async def conversation_message_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        conversation_message_create_request: Annotated[Optional[ConversationMessageCreateRequest], Field(description="Request Body for Conversation Messages")],
    ) -> ConversationMessageShow:
        """Outlines the parameters and data fields used when creating a new ConversationMessage"""
        ...


    async def conversation_message_index(
        self,
        conversation_id: Annotated[StrictInt, Field(description="The unique identifier for a single Conversation. Use the keyword `null` to match those without a ConversationMessage. The list will be filtered to include only the ConversationMessage records with the matching property.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter ConversationMessage records to those having the `created_at` field on the related Conversation after a specific time. (Expects an ISO-8601 timestamp).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter ConversationMessage records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of ConversationMessage records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the ConversationMessage records by the given field. Default: `id(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `body` matching a given string.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter ConversationMessage records to those having the `updated_at` field on the related Conversation after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> ConversationMessageList:
        """Outlines the parameters, optional and required, used when requesting the data for all ConversationMessages"""
        ...


    async def conversation_message_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the ConversationMessage.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> ConversationMessageShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single ConversationMessage"""
        ...
