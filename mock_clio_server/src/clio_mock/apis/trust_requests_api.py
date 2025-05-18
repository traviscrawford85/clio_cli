# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from clio_mock.apis.trust_requests_api_base import BaseTrustRequestsApi
import clio_mock.impl

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

from clio_mock.models.extra_models import TokenModel  # noqa: F401
from pydantic import Field, StrictStr
from typing import Optional
from typing_extensions import Annotated
from clio_mock.models.activity_show import ActivityShow
from clio_mock.models.error import Error
from clio_mock.models.trust_request_create_request import TrustRequestCreateRequest


router = APIRouter()

ns_pkg = clio_mock.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/trust_requests.json",
    responses={
        201: {"model": ActivityShow, "description": "Created"},
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
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    trust_request_create_request: Annotated[Optional[TrustRequestCreateRequest], Field(description="Request Body for Trust Requests")] = Body(None, description="Request Body for Trust Requests"),
) -> ActivityShow:
    """Outlines the parameters and data fields used when creating a new TrustRequest"""
    if not BaseTrustRequestsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseTrustRequestsApi.subclasses[0]().trust_request_create(x_api_versio_nheader, fieldsquery, trust_request_create_request)
