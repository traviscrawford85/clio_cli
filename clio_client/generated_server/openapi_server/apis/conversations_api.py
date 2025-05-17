# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.conversations_api_base import BaseConversationsApi
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
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.conversation_list import ConversationList
from openapi_server.models.conversation_show import ConversationShow
from openapi_server.models.conversation_update_request import ConversationUpdateRequest
from openapi_server.models.error import Error


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/conversations.json",
    responses={
        200: {"model": ConversationList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Conversations"],
    summary="Return the data for all Conversations",
    response_model_by_alias=True,
)
async def conversation_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    archived: Annotated[Optional[StrictBool], Field(description="Filter archived Conversation records.")] = Query(None, description="Filter archived Conversation records.", alias="archived"),
    contact_id: Annotated[Optional[StrictInt], Field(description="Filter Conversation records for the contact.")] = Query(None, description="Filter Conversation records for the contact.", alias="contact_id"),
    created_since: Annotated[Optional[datetime], Field(description="Filter Conversation records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Conversation records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    var_date: Annotated[Optional[date], Field(description="Filter Conversation records created on a given date. (Expects an ISO-8601 date).")] = Query(None, description="Filter Conversation records created on a given date. (Expects an ISO-8601 date).", alias="date"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    for_user: Annotated[Optional[StrictBool], Field(description="If set to true, filter Conversation records accessible to any groups of the user. Note that the user may not be member of the conversations.  If set to false, filter Conversation records of which the user is a member. ")] = Query(None, description="If set to true, filter Conversation records accessible to any groups of the user. Note that the user may not be member of the conversations.  If set to false, filter Conversation records of which the user is a member. ", alias="for_user"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter Conversation records to those having the specified unique identifiers.")] = Query(None, description="Filter Conversation records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Conversation records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Conversation records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    matter_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Conversation. The list will be filtered to include only the Conversation records with the matching property.")] = Query(None, description="The unique identifier for a single Matter. Use the keyword &#x60;null&#x60; to match those without a Conversation. The list will be filtered to include only the Conversation records with the matching property.", alias="matter_id"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the Conversation records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the Conversation records by the given field. Default: &#x60;id(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    read_status: Annotated[Optional[StrictBool], Field(description="Filter Conversation records to those which have been read.")] = Query(None, description="Filter Conversation records to those which have been read.", alias="read_status"),
    time_entries: Annotated[Optional[StrictBool], Field(description="Filter Conversation records to those with or without associated time entries.")] = Query(None, description="Filter Conversation records to those with or without associated time entries.", alias="time_entries"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter Conversation records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Conversation records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> ConversationList:
    """Outlines the parameters, optional and required, used when requesting the data for all Conversations"""
    if not BaseConversationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseConversationsApi.subclasses[0]().conversation_index(x_api_version, archived, contact_id, created_since, var_date, fields, for_user, ids, limit, matter_id, order, page_token, read_status, time_entries, updated_since)


@router.get(
    "/conversations/{id}.json",
    responses={
        200: {"model": ConversationShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Conversations"],
    summary="Return the data for a single Conversation",
    response_model_by_alias=True,
)
async def conversation_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Conversation.")] = Path(..., description="The unique identifier for the Conversation."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> ConversationShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single Conversation"""
    if not BaseConversationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseConversationsApi.subclasses[0]().conversation_show(id, if_modified_since, if_none_match, x_api_version, fields)


@router.patch(
    "/conversations/{id}.json",
    responses={
        200: {"model": ConversationShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["Conversations"],
    summary="Update a single Conversation",
    response_model_by_alias=True,
)
async def conversation_update(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Conversation.")] = Path(..., description="The unique identifier for the Conversation."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    conversation_update_request: Annotated[Optional[ConversationUpdateRequest], Field(description="Request Body for Conversations")] = Body(None, description="Request Body for Conversations"),
) -> ConversationShow:
    """Outlines the parameters and data fields used when updating a single Conversation"""
    if not BaseConversationsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseConversationsApi.subclasses[0]().conversation_update(id, if_match, x_api_version, fields, conversation_update_request)
