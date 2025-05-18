# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from clio_mock.apis.outstanding_client_balances_api_base import BaseOutstandingClientBalancesApi
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
from datetime import date
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
    "/outstanding_client_balances.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Outstanding Client Balances"],
    summary="Return the data for all OutstandingClientBalances",
    response_model_by_alias=True,
)
async def outstanding_client_balance_index(
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    contact_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the ActivityRate records with the matching property.")] = Query(None, description="The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the ActivityRate records with the matching property.", alias="contact_idquery"),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    last_paid_end_datequery: Annotated[Optional[date], Field(description="Filter OutstandingClientBalance records for those whose bills have been paid before the specified date")] = Query(None, description="Filter OutstandingClientBalance records for those whose bills have been paid before the specified date", alias="last_paid_end_datequery"),
    last_paid_start_datequery: Annotated[Optional[date], Field(description="Filter OutstandingClientBalance records for those whose bills have been paid after the specified date")] = Query(None, description="Filter OutstandingClientBalance records for those whose bills have been paid after the specified date", alias="last_paid_start_datequery"),
    limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limitquery"),
    newest_bill_due_end_datequery: Annotated[Optional[date], Field(description="Filter OutstandingClientBalance records for the contact's newest bill due date before the specified date")] = Query(None, description="Filter OutstandingClientBalance records for the contact&#39;s newest bill due date before the specified date", alias="newest_bill_due_end_datequery"),
    newest_bill_due_start_datequery: Annotated[Optional[date], Field(description="Filter OutstandingClientBalance records for the contact's newest bill due date after the specified date")] = Query(None, description="Filter OutstandingClientBalance records for the contact&#39;s newest bill due date after the specified date", alias="newest_bill_due_start_datequery"),
    originating_attorney_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a BillableClient. The list will be filtered to include only the BillableClient records with the matching property.")] = Query(None, description="The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a BillableClient. The list will be filtered to include only the BillableClient records with the matching property.", alias="originating_attorney_idquery"),
    page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_tokenquery"),
    responsible_attorney_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a BillableClient. The list will be filtered to include only the BillableClient records with the matching property.")] = Query(None, description="The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a BillableClient. The list will be filtered to include only the BillableClient records with the matching property.", alias="responsible_attorney_idquery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for all OutstandingClientBalances"""
    if not BaseOutstandingClientBalancesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseOutstandingClientBalancesApi.subclasses[0]().outstanding_client_balance_index(x_api_versio_nheader, contact_idquery, fieldsquery, last_paid_end_datequery, last_paid_start_datequery, limitquery, newest_bill_due_end_datequery, newest_bill_due_start_datequery, originating_attorney_idquery, page_tokenquery, responsible_attorney_idquery)
