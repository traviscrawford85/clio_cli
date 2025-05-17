# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.conversation_messages_api_base import BaseConversationMessagesApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from datetime import date, datetime
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.conversation_message_create_request import ConversationMessageCreateRequest
from openapi_server.models.conversation_message_list import ConversationMessageList
from openapi_server.models.conversation_message_show import ConversationMessageShow
from openapi_server.models.error import Error


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/conversation_messages.json",
    responses={
        201: {"model": ConversationMessageShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Conversation Messages"],
    summary="Create a new ConversationMessage",
    response_model_by_alias=True,
)
async def conversation_message_create(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    conversation_message_create_request: Annotated[Optional[ConversationMessageCreateRequest], Field(description="Request Body for Conversation Messages")] = Body(None, description="Request Body for Conversation Messages"),
) -> ConversationMessageShow:
    """Outlines the parameters and data fields used when creating a new ConversationMessage"""
    if not BaseConversationMessagesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseConversationMessagesApi.subclasses[0]().conversation_message_create(x_api_version, fields, conversation_message_create_request)


@router.get(
    "/conversation_messages.json",
    responses={
        200: {"model": ConversationMessageList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Conversation Messages"],
    summary="Return the data for all ConversationMessages",
    response_model_by_alias=True,
)
async def conversation_message_index(
    conversation_id: Annotated[StrictInt, Field(description="The unique identifier for a single Conversation. Use the keyword `null` to match those without a ConversationMessage. The list will be filtered to include only the ConversationMessage records with the matching property.")] = Query(None, description="The unique identifier for a single Conversation. Use the keyword &#x60;null&#x60; to match those without a ConversationMessage. The list will be filtered to include only the ConversationMessage records with the matching property.", alias="conversation_id"),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    created_since: Annotated[Optional[datetime], Field(description="Filter ConversationMessage records to those having the `created_at` field on the related Conversation after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter ConversationMessage records to those having the &#x60;created_at&#x60; field on the related Conversation after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter ConversationMessage records to those having the specified unique identifiers.")] = Query(None, description="Filter ConversationMessage records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of ConversationMessage records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of ConversationMessage records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the ConversationMessage records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the ConversationMessage records by the given field. Default: &#x60;id(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `body` matching a given string.")] = Query(None, description="Wildcard search for &#x60;body&#x60; matching a given string.", alias="query"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter ConversationMessage records to those having the `updated_at` field on the related Conversation after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter ConversationMessage records to those having the &#x60;updated_at&#x60; field on the related Conversation after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> ConversationMessageList:
    """Outlines the parameters, optional and required, used when requesting the data for all ConversationMessages"""
    if not BaseConversationMessagesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseConversationMessagesApi.subclasses[0]().conversation_message_index(conversation_id, x_api_version, created_since, fields, ids, limit, order, page_token, query, updated_since)


@router.get(
    "/conversation_messages/{id}.json",
    responses={
        200: {"model": ConversationMessageShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Conversation Messages"],
    summary="Return the data for a single ConversationMessage",
    response_model_by_alias=True,
)
async def conversation_message_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the ConversationMessage.")] = Path(..., description="The unique identifier for the ConversationMessage."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> ConversationMessageShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single ConversationMessage"""
    if not BaseConversationMessagesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseConversationMessagesApi.subclasses[0]().conversation_message_show(id, if_modified_since, if_none_match, x_api_version, fields)
