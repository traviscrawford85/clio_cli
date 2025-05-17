# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.utbms_codes_api_base import BaseUtbmsCodesApi
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
from openapi_server.models.utbms_code_list import UtbmsCodeList
from openapi_server.models.utbms_code_show import UtbmsCodeShow


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/utbms/codes.json",
    responses={
        200: {"model": UtbmsCodeList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Utbms Codes"],
    summary="Return the data for all UtbmsCodes",
    response_model_by_alias=True,
)
async def utbms_code_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    created_since: Annotated[Optional[datetime], Field(description="Filter UtbmsCode records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter UtbmsCode records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter UtbmsCode records to those having the specified unique identifiers.")] = Query(None, description="Filter UtbmsCode records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of UtbmsCode records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of UtbmsCode records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the UtbmsCode records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the UtbmsCode records by the given field. Default: &#x60;id(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    type: Annotated[Optional[StrictStr], Field(description="Filter UtbmsCode records to those of a given type.")] = Query(None, description="Filter UtbmsCode records to those of a given type.", alias="type"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter UtbmsCode records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter UtbmsCode records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
    utbms_set_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single UtbmsSet. Use the keyword `null` to match those without a UtbmsCode. The list will be filtered to include only the UtbmsCode records with the matching property.")] = Query(None, description="The unique identifier for a single UtbmsSet. Use the keyword &#x60;null&#x60; to match those without a UtbmsCode. The list will be filtered to include only the UtbmsCode records with the matching property.", alias="utbms_set_id"),
) -> UtbmsCodeList:
    """Outlines the parameters, optional and required, used when requesting the data for all UtbmsCodes"""
    if not BaseUtbmsCodesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUtbmsCodesApi.subclasses[0]().utbms_code_index(x_api_version, created_since, fields, ids, limit, order, page_token, type, updated_since, utbms_set_id)


@router.get(
    "/utbms/codes/{id}.json",
    responses={
        200: {"model": UtbmsCodeShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Utbms Codes"],
    summary="Return the data for a single UtbmsCode",
    response_model_by_alias=True,
)
async def utbms_code_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the UtbmsCode.")] = Path(..., description="The unique identifier for the UtbmsCode."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> UtbmsCodeShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single UtbmsCode"""
    if not BaseUtbmsCodesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUtbmsCodesApi.subclasses[0]().utbms_code_show(id, if_modified_since, if_none_match, x_api_version, fields)
