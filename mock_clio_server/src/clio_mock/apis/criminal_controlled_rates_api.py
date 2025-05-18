# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from clio_mock.apis.criminal_controlled_rates_api_base import BaseCriminalControlledRatesApi
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
from pydantic import Field, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from clio_mock.models.activity_list import ActivityList
from clio_mock.models.error import Error


router = APIRouter()

ns_pkg = clio_mock.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/lauk_criminal_controlled_rates.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
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
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    activityquery: Annotated[Optional[StrictStr], Field(description="Filter by activity.")] = Query(None, description="Filter by activity.", alias="activityquery"),
    category_of_lawquery: Annotated[Optional[StrictStr], Field(description="Filter by category of law.")] = Query(None, description="Filter by category of law.", alias="category_of_lawquery"),
    counselquery: Annotated[Optional[StrictStr], Field(description="Filter by counsel.")] = Query(None, description="Filter by counsel.", alias="counselquery"),
    courtquery: Annotated[Optional[StrictStr], Field(description="Filter by court.")] = Query(None, description="Filter by court.", alias="courtquery"),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    keyquery: Annotated[Optional[StrictStr], Field(description="Filter by key.")] = Query(None, description="Filter by key.", alias="keyquery"),
    limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limitquery"),
    page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_tokenquery"),
    rate_typequery: Annotated[Optional[StrictStr], Field(description="Filter by rate type.")] = Query(None, description="Filter by rate type.", alias="rate_typequery"),
    regionquery: Annotated[Optional[StrictStr], Field(description="Filter by region.")] = Query(None, description="Filter by region.", alias="regionquery"),
    solicitor_typequery: Annotated[Optional[StrictStr], Field(description="Filter by solicitor type.")] = Query(None, description="Filter by solicitor type.", alias="solicitor_typequery"),
    standard_fee_categoryquery: Annotated[Optional[StrictStr], Field(description="Filter by standard fee category.")] = Query(None, description="Filter by standard fee category.", alias="standard_fee_categoryquery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for all LaukCriminalControlledRates"""
    if not BaseCriminalControlledRatesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCriminalControlledRatesApi.subclasses[0]().lauk_criminal_controlled_rate_index(x_api_versio_nheader, activityquery, category_of_lawquery, counselquery, courtquery, fieldsquery, keyquery, limitquery, page_tokenquery, rate_typequery, regionquery, solicitor_typequery, standard_fee_categoryquery)
