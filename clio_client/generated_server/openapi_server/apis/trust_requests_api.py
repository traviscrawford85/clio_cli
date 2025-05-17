# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.trust_requests_api_base import BaseTrustRequestsApi
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
from pydantic import Field, StrictStr
from typing import Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.trust_request_create_request import TrustRequestCreateRequest
from openapi_server.models.trust_request_show import TrustRequestShow


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/trust_requests.json",
    responses={
        201: {"model": TrustRequestShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Trust Requests"],
    summary="Create a new TrustRequest",
    response_model_by_alias=True,
)
async def trust_request_create(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    trust_request_create_request: Annotated[Optional[TrustRequestCreateRequest], Field(description="Request Body for Trust Requests")] = Body(None, description="Request Body for Trust Requests"),
) -> TrustRequestShow:
    """Outlines the parameters and data fields used when creating a new TrustRequest"""
    if not BaseTrustRequestsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTrustRequestsApi.subclasses[0]().trust_request_create(x_api_version, fields, trust_request_create_request)
