# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from clio_mock.apis.civil_certificated_rates_api_base import BaseCivilCertificatedRatesApi
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
from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from clio_mock.models.activity_list import ActivityList
from clio_mock.models.error import Error


router = APIRouter()

ns_pkg = clio_mock.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/lauk_civil_certificated_rates.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Civil Certificated Rates"],
    summary="List Civil Certificated Rates",
    response_model_by_alias=True,
)
async def lauk_civil_certificated_rate_index(
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    activityquery: Annotated[Optional[StrictStr], Field(description="Filter by activity.")] = Query(None, description="Filter by activity.", alias="activityquery"),
    activity_sub_categoryquery: Annotated[Optional[StrictStr], Field(description="Filter by activity sub-category.")] = Query(None, description="Filter by activity sub-category.", alias="activity_sub_categoryquery"),
    attended_several_hearings_for_multiple_clientsquery: Annotated[Optional[StrictBool], Field(description="Filter by whether multiple hearings were attended for multiple clients.")] = Query(None, description="Filter by whether multiple hearings were attended for multiple clients.", alias="attended_several_hearings_for_multiple_clientsquery"),
    category_of_lawquery: Annotated[Optional[StrictStr], Field(description="Filter by category of law.")] = Query(None, description="Filter by category of law.", alias="category_of_lawquery"),
    change_of_solicitorquery: Annotated[Optional[StrictBool], Field(description="Filter by change of solicitor status.")] = Query(None, description="Filter by change of solicitor status.", alias="change_of_solicitorquery"),
    courtquery: Annotated[Optional[StrictStr], Field(description="Filter by court.")] = Query(None, description="Filter by court.", alias="courtquery"),
    eligible_for_sqmquery: Annotated[Optional[StrictBool], Field(description="Filter by SQM eligibility.")] = Query(None, description="Filter by SQM eligibility.", alias="eligible_for_sqmquery"),
    fee_schemequery: Annotated[Optional[StrictStr], Field(description="Fee scheme")] = Query(None, description="Fee scheme", alias="fee_schemequery"),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    first_conducting_solicitorquery: Annotated[Optional[StrictBool], Field(description="Filter by first conducting solicitor status.")] = Query(None, description="Filter by first conducting solicitor status.", alias="first_conducting_solicitorquery"),
    keyquery: Annotated[Optional[StrictStr], Field(description="Filter by key.")] = Query(None, description="Filter by key.", alias="keyquery"),
    limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limitquery"),
    number_of_clientsquery: Annotated[Optional[StrictStr], Field(description="Filter by number of clients.")] = Query(None, description="Filter by number of clients.", alias="number_of_clientsquery"),
    page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_tokenquery"),
    partyquery: Annotated[Optional[StrictStr], Field(description="Filter by party.")] = Query(None, description="Filter by party.", alias="partyquery"),
    post_transfer_clients_representedquery: Annotated[Optional[StrictStr], Field(description="Filter by post-transfer clients represented.")] = Query(None, description="Filter by post-transfer clients represented.", alias="post_transfer_clients_representedquery"),
    rate_typequery: Annotated[Optional[StrictStr], Field(description="Filter by rate type.")] = Query(None, description="Filter by rate type.", alias="rate_typequery"),
    regionquery: Annotated[Optional[StrictStr], Field(description="Filter by region.")] = Query(None, description="Filter by region.", alias="regionquery"),
    session_typequery: Annotated[Optional[StrictStr], Field(description="Filter by session type.")] = Query(None, description="Filter by session type.", alias="session_typequery"),
    user_typequery: Annotated[Optional[StrictStr], Field(description="Filter by user type.")] = Query(None, description="Filter by user type.", alias="user_typequery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for all LaukCivilCertificatedRates"""
    if not BaseCivilCertificatedRatesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseCivilCertificatedRatesApi.subclasses[0]().lauk_civil_certificated_rate_index(x_api_versio_nheader, activityquery, activity_sub_categoryquery, attended_several_hearings_for_multiple_clientsquery, category_of_lawquery, change_of_solicitorquery, courtquery, eligible_for_sqmquery, fee_schemequery, fieldsquery, first_conducting_solicitorquery, keyquery, limitquery, number_of_clientsquery, page_tokenquery, partyquery, post_transfer_clients_representedquery, rate_typequery, regionquery, session_typequery, user_typequery)
