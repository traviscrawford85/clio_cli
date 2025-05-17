# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.webhooks_api_base import BaseWebhooksApi
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
from openapi_server.models.error import Error
from openapi_server.models.webhook_create_request import WebhookCreateRequest
from openapi_server.models.webhook_list import WebhookList
from openapi_server.models.webhook_show import WebhookShow
from openapi_server.models.webhook_update_request import WebhookUpdateRequest


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/webhooks.json",
    responses={
        201: {"model": WebhookShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Webhooks"],
    summary="Create a new Webhook",
    response_model_by_alias=True,
)
async def webhook_create(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    webhook_create_request: Annotated[Optional[WebhookCreateRequest], Field(description="Request Body for Webhooks")] = Body(None, description="Request Body for Webhooks"),
) -> WebhookShow:
    """Outlines the parameters and data fields used when creating a new Webhook"""
    if not BaseWebhooksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWebhooksApi.subclasses[0]().webhook_create(x_api_version, fields, webhook_create_request)


@router.delete(
    "/webhooks/{id}.json",
    responses={
        204: {"description": "No Content"},
        403: {"model": Error, "description": "Forbidden"},
    },
    tags=["Webhooks"],
    summary="Delete a single Webhook",
    response_model_by_alias=True,
)
async def webhook_destroy(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Webhook.")] = Path(..., description="The unique identifier for the Webhook."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single Webhook"""
    if not BaseWebhooksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWebhooksApi.subclasses[0]().webhook_destroy(id, x_api_version)


@router.get(
    "/webhooks.json",
    responses={
        200: {"model": WebhookList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Webhooks"],
    summary="Return the data for all Webhooks",
    response_model_by_alias=True,
)
async def webhook_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    created_since: Annotated[Optional[datetime], Field(description="Filter Webhook records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Webhook records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter Webhook records to those having the specified unique identifiers.")] = Query(None, description="Filter Webhook records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Webhook records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Webhook records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the Webhook records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the Webhook records by the given field. Default: &#x60;id(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter Webhook records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Webhook records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> WebhookList:
    """Outlines the parameters, optional and required, used when requesting the data for all Webhooks"""
    if not BaseWebhooksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWebhooksApi.subclasses[0]().webhook_index(x_api_version, created_since, fields, ids, limit, order, page_token, updated_since)


@router.get(
    "/webhooks/{id}.json",
    responses={
        200: {"model": WebhookShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Webhooks"],
    summary="Return the data for a single Webhook",
    response_model_by_alias=True,
)
async def webhook_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Webhook.")] = Path(..., description="The unique identifier for the Webhook."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> WebhookShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single Webhook"""
    if not BaseWebhooksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWebhooksApi.subclasses[0]().webhook_show(id, if_modified_since, if_none_match, x_api_version, fields)


@router.patch(
    "/webhooks/{id}.json",
    responses={
        200: {"model": WebhookShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["Webhooks"],
    summary="Update a single Webhook",
    response_model_by_alias=True,
)
async def webhook_update(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Webhook.")] = Path(..., description="The unique identifier for the Webhook."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    webhook_update_request: Annotated[Optional[WebhookUpdateRequest], Field(description="Request Body for Webhooks")] = Body(None, description="Request Body for Webhooks"),
) -> WebhookShow:
    """Outlines the parameters and data fields used when updating a single Webhook"""
    if not BaseWebhooksApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseWebhooksApi.subclasses[0]().webhook_update(id, if_match, x_api_version, fields, webhook_update_request)
