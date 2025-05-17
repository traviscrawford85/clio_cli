# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.matter_stages_api_base import BaseMatterStagesApi
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
from datetime import datetime
from pydantic import Field, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.matter_stage_list import MatterStageList


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/matter_stages.json",
    responses={
        200: {"model": MatterStageList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Matter Stages"],
    summary="Return the data for all MatterStages",
    response_model_by_alias=True,
)
async def matter_stage_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    created_since: Annotated[Optional[datetime], Field(description="Filter MatterStage records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter MatterStage records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter MatterStage records to those having the specified unique identifiers.")] = Query(None, description="Filter MatterStage records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of MatterStage records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of MatterStage records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    practice_area_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single PracticeArea. The keyword `null` is not valid for this field. The list will be filtered to include only the MatterStage records with the matching property.")] = Query(None, description="The unique identifier for a single PracticeArea. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the MatterStage records with the matching property.", alias="practice_area_id"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter MatterStage records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter MatterStage records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> MatterStageList:
    """Outlines the parameters, optional and required, used when requesting the data for all MatterStages"""
    if not BaseMatterStagesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMatterStagesApi.subclasses[0]().matter_stage_index(x_api_version, created_since, fields, ids, limit, page_token, practice_area_id, updated_since)
