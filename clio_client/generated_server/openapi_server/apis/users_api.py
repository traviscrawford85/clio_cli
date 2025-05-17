# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.users_api_base import BaseUsersApi
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
from openapi_server.models.error import Error
from openapi_server.models.user_list import UserList
from openapi_server.models.user_show import UserShow


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/users.json",
    responses={
        200: {"model": UserList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Users"],
    summary="Return the data for all Users",
    response_model_by_alias=True,
)
async def user_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    created_since: Annotated[Optional[datetime], Field(description="Filter User records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter User records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    enabled: Annotated[Optional[StrictBool], Field(description="Filter User records to those that are enabled or disabled.")] = Query(None, description="Filter User records to those that are enabled or disabled.", alias="enabled"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter User records to those having the specified unique identifiers.")] = Query(None, description="Filter User records to those having the specified unique identifiers.", alias="ids[]"),
    include_co_counsel: Annotated[Optional[StrictBool], Field(description="Filter User to include co-counsel users")] = Query(None, description="Filter User to include co-counsel users", alias="include_co_counsel"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of User records to be returned. Limit can range between 1 and 2000. Default: `2000`.")] = Query(None, description="A limit on the number of User records to be returned. Limit can range between 1 and 2000. Default: &#x60;2000&#x60;.", alias="limit"),
    name: Annotated[Optional[StrictStr], Field(description="Filter User records to those with the given name.")] = Query(None, description="Filter User records to those with the given name.", alias="name"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the User records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the User records by the given field. Default: &#x60;id(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    pending_setup: Annotated[Optional[StrictBool], Field(description="Filter User records based on whether or not they are still being setup.")] = Query(None, description="Filter User records based on whether or not they are still being setup.", alias="pending_setup"),
    role: Annotated[Optional[StrictStr], Field(description="Filter User records to those with a specific role.")] = Query(None, description="Filter User records to those with a specific role.", alias="role"),
    subscription_type: Annotated[Optional[StrictStr], Field(description="Filter User records to those with a specific subscription type.")] = Query(None, description="Filter User records to those with a specific subscription type.", alias="subscription_type"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter User records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter User records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> UserList:
    """Outlines the parameters, optional and required, used when requesting the data for all Users"""
    if not BaseUsersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUsersApi.subclasses[0]().user_index(x_api_version, created_since, enabled, fields, ids, include_co_counsel, limit, name, order, page_token, pending_setup, role, subscription_type, updated_since)


@router.get(
    "/users/{id}.json",
    responses={
        200: {"model": UserShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Users"],
    summary="Return the data for a single User",
    response_model_by_alias=True,
)
async def user_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the User.")] = Path(..., description="The unique identifier for the User."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> UserShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single User"""
    if not BaseUsersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUsersApi.subclasses[0]().user_show(id, if_modified_since, if_none_match, x_api_version, fields)


@router.get(
    "/users/who_am_i.json",
    responses={
        200: {"model": UserShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Users"],
    summary="Return the data for the current User",
    response_model_by_alias=True,
)
async def user_who_am_i(
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> UserShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single User"""
    if not BaseUsersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUsersApi.subclasses[0]().user_who_am_i(if_modified_since, if_none_match, x_api_version, fields)
