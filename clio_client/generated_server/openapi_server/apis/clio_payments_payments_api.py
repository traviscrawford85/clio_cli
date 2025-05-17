# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.clio_payments_payments_api_base import BaseClioPaymentsPaymentsApi
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
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.clio_payments_payment_list import ClioPaymentsPaymentList
from openapi_server.models.clio_payments_payment_show import ClioPaymentsPaymentShow
from openapi_server.models.error import Error


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/clio_payments/payments.json",
    responses={
        200: {"model": ClioPaymentsPaymentList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Clio Payments Payments"],
    summary="Return the data for all ClioPaymentsPayments",
    response_model_by_alias=True,
)
async def clio_payments_payment_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    bill_id: Annotated[Optional[StrictInt], Field(description="Filter ClioPaymentsPayment records to those that are allocated to the specified bill.")] = Query(None, description="Filter ClioPaymentsPayment records to those that are allocated to the specified bill.", alias="bill_id"),
    contact_id: Annotated[Optional[StrictInt], Field(description="Filter ClioPaymentsPayment records to those that are assigned to the specified contact.")] = Query(None, description="Filter ClioPaymentsPayment records to those that are assigned to the specified contact.", alias="contact_id"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter ClioPaymentsPayment records to those having the specified unique identifiers.")] = Query(None, description="Filter ClioPaymentsPayment records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of ClioPaymentsPayment records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of ClioPaymentsPayment records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    state: Annotated[Optional[StrictStr], Field(description="Filter ClioPaymentsPayment records to those in a given state.")] = Query(None, description="Filter ClioPaymentsPayment records to those in a given state.", alias="state"),
) -> ClioPaymentsPaymentList:
    """Outlines the parameters, optional and required, used when requesting the data for all ClioPaymentsPayments"""
    if not BaseClioPaymentsPaymentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseClioPaymentsPaymentsApi.subclasses[0]().clio_payments_payment_index(x_api_version, bill_id, contact_id, fields, ids, limit, page_token, state)


@router.get(
    "/clio_payments/payments/{id}.json",
    responses={
        200: {"model": ClioPaymentsPaymentShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Clio Payments Payments"],
    summary="Return the data for a single ClioPaymentsPayment",
    response_model_by_alias=True,
)
async def clio_payments_payment_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the ClioPaymentsPayment.")] = Path(..., description="The unique identifier for the ClioPaymentsPayment."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> ClioPaymentsPaymentShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single ClioPaymentsPayment"""
    if not BaseClioPaymentsPaymentsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseClioPaymentsPaymentsApi.subclasses[0]().clio_payments_payment_show(id, if_modified_since, if_none_match, x_api_version, fields)
