# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.my_events_api_base import BaseMyEventsApi
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
from pydantic import Field, StrictInt, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.my_event_list import MyEventList
from openapi_server.models.my_event_show import MyEventShow
from openapi_server.models.my_event_update_request import MyEventUpdateRequest


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.delete(
    "/internal_notifications/my_events/{id}.json",
    responses={
        204: {"description": "No Content"},
        403: {"model": Error, "description": "Forbidden"},
    },
    tags=["My Events"],
    summary="Clear (delete) a single in-app notification event",
    response_model_by_alias=True,
)
async def my_event_destroy(
    id: Annotated[StrictInt, Field(description="The unique identifier for the MyEvent.")] = Path(..., description="The unique identifier for the MyEvent."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single MyEvent"""
    if not BaseMyEventsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMyEventsApi.subclasses[0]().my_event_destroy(id, x_api_version)


@router.get(
    "/internal_notifications/my_events.json",
    responses={
        200: {"model": MyEventList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["My Events"],
    summary="Return the data for all of my in-app notification events",
    response_model_by_alias=True,
)
async def my_event_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of MyEvent records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of MyEvent records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
) -> MyEventList:
    """Outlines the parameters, optional and required, used when requesting the data for all MyEvents"""
    if not BaseMyEventsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMyEventsApi.subclasses[0]().my_event_index(x_api_version, fields, limit, page_token)


@router.patch(
    "/internal_notifications/my_events/{id}.json",
    responses={
        200: {"model": MyEventShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["My Events"],
    summary="Mark a single in-app notification event as read/unread",
    response_model_by_alias=True,
)
async def my_event_update(
    id: Annotated[StrictInt, Field(description="The unique identifier for the MyEvent.")] = Path(..., description="The unique identifier for the MyEvent."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    my_event_update_request: Annotated[Optional[MyEventUpdateRequest], Field(description="Request Body for My Events")] = Body(None, description="Request Body for My Events"),
) -> MyEventShow:
    """Outlines the parameters and data fields used when updating a single MyEvent"""
    if not BaseMyEventsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMyEventsApi.subclasses[0]().my_event_update(id, if_match, x_api_version, fields, my_event_update_request)
