# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from clio_mock.apis.event_metrics_api_base import BaseEventMetricsApi
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
from clio_mock.models.activity_list import ActivityList
from clio_mock.models.error import Error


router = APIRouter()

ns_pkg = clio_mock.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/internal_notifications/event_metrics.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Event Metrics"],
    summary="Unread in-app notification events",
    response_model_by_alias=True,
)
async def event_metrics_index(
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting Event Metrics"""
    if not BaseEventMetricsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseEventMetricsApi.subclasses[0]().event_metrics_index(x_api_versio_nheader, fieldsquery)
