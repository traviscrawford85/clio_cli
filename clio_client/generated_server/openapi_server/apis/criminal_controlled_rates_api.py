# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.criminal_controlled_rates_api_base import BaseCriminalControlledRatesApi
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
from openapi_server.models.lauk_criminal_controlled_rate_list import LaukCriminalControlledRateList


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/lauk_criminal_controlled_rates.json",
    responses={
        200: {"model": LaukCriminalControlledRateList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Criminal Controlled Rates"],
    summary="List Criminal Controlled Rates",
    response_model_by_alias=True,
)
async def lauk_criminal_controlled_rate_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    activity: Annotated[Optional[StrictStr], Field(description="Filter by activity.")] = Query(None, description="Filter by activity.", alias="activity"),
    category_of_law: Annotated[Optional[StrictStr], Field(description="Filter by category of law.")] = Query(None, description="Filter by category of law.", alias="category_of_law"),
    counsel: Annotated[Optional[StrictStr], Field(description="Filter by counsel.")] = Query(None, description="Filter by counsel.", alias="counsel"),
    court: Annotated[Optional[StrictStr], Field(description="Filter by court.")] = Query(None, description="Filter by court.", alias="court"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    key: Annotated[Optional[StrictStr], Field(description="Filter by key.")] = Query(None, description="Filter by key.", alias="key"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of LaukCriminalControlledRate records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of LaukCriminalControlledRate records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    rate_type: Annotated[Optional[StrictStr], Field(description="Filter by rate type.")] = Query(None, description="Filter by rate type.", alias="rate_type"),
    region: Annotated[Optional[StrictStr], Field(description="Filter by region.")] = Query(None, description="Filter by region.", alias="region"),
    solicitor_type: Annotated[Optional[StrictStr], Field(description="Filter by solicitor type.")] = Query(None, description="Filter by solicitor type.", alias="solicitor_type"),
    standard_fee_category: Annotated[Optional[StrictStr], Field(description="Filter by standard fee category.")] = Query(None, description="Filter by standard fee category.", alias="standard_fee_category"),
) -> LaukCriminalControlledRateList:
    """Outlines the parameters, optional and required, used when requesting the data for all LaukCriminalControlledRates"""
    if not BaseCriminalControlledRatesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCriminalControlledRatesApi.subclasses[0]().lauk_criminal_controlled_rate_index(x_api_version, activity, category_of_law, counsel, court, fields, key, limit, page_token, rate_type, region, solicitor_type, standard_fee_category)
