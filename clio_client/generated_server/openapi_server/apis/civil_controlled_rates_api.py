# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.civil_controlled_rates_api_base import BaseCivilControlledRatesApi
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
from typing import Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.lauk_civil_controlled_rate_list import LaukCivilControlledRateList


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/lauk_civil_controlled_rates.json",
    responses={
        200: {"model": LaukCivilControlledRateList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Civil Controlled Rates"],
    summary="List Civil Controlled Rates",
    response_model_by_alias=True,
)
async def lauk_civil_controlled_rate_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    activity: Annotated[Optional[StrictStr], Field(description="Filter by activity.")] = Query(None, description="Filter by activity.", alias="activity"),
    category_of_law: Annotated[Optional[StrictStr], Field(description="Filter by category of law.")] = Query(None, description="Filter by category of law.", alias="category_of_law"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    key: Annotated[Optional[StrictStr], Field(description="Filter by key.")] = Query(None, description="Filter by key.", alias="key"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of LaukCivilControlledRate records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of LaukCivilControlledRate records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    matter_type_1: Annotated[Optional[StrictInt], Field(description="Filter by matter type 1.")] = Query(None, description="Filter by matter type 1.", alias="matter_type_1"),
    matter_type_2: Annotated[Optional[StrictInt], Field(description="Filter by matter type 2.")] = Query(None, description="Filter by matter type 2.", alias="matter_type_2"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    rate_type: Annotated[Optional[StrictStr], Field(description="Filter by rate type.")] = Query(None, description="Filter by rate type.", alias="rate_type"),
    region: Annotated[Optional[StrictStr], Field(description="Filter by region.")] = Query(None, description="Filter by region.", alias="region"),
) -> LaukCivilControlledRateList:
    """Outlines the parameters, optional and required, used when requesting the data for all LaukCivilControlledRates"""
    if not BaseCivilControlledRatesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCivilControlledRatesApi.subclasses[0]().lauk_civil_controlled_rate_index(x_api_version, activity, category_of_law, fields, key, limit, matter_type_1, matter_type_2, page_token, rate_type, region)
