# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.billing_settings_api_base import BaseBillingSettingsApi
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
from datetime import date
from pydantic import Field, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.billing_setting_show import BillingSettingShow
from openapi_server.models.error import Error


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/settings/billing.json",
    responses={
        200: {"model": BillingSettingShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Billing Settings"],
    summary="Return the billing settings",
    response_model_by_alias=True,
)
async def billing_setting_show(
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    duration: Annotated[Optional[StrictStr], Field(description="Duration string for time rounding, conforming to the Chronic date parser. For example: '3h' or '2:15'.")] = Query(None, description="Duration string for time rounding, conforming to the Chronic date parser. For example: &#39;3h&#39; or &#39;2:15&#39;.", alias="duration"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> BillingSettingShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single BillingSetting"""
    if not BaseBillingSettingsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseBillingSettingsApi.subclasses[0]().billing_setting_show(if_modified_since, if_none_match, x_api_version, duration, fields)
