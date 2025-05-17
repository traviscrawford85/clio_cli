# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.interest_charges_api_base import BaseInterestChargesApi
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
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.interest_charge_list import InterestChargeList


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.delete(
    "/interest_charges/{id}.json",
    responses={
        204: {"description": "No Content"},
        403: {"model": Error, "description": "Forbidden"},
    },
    tags=["Interest Charges"],
    summary="Delete a single InterestCharge",
    response_model_by_alias=True,
)
async def interest_charge_destroy(
    id: Annotated[StrictInt, Field(description="The unique identifier for the InterestCharge.")] = Path(..., description="The unique identifier for the InterestCharge."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single InterestCharge"""
    if not BaseInterestChargesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseInterestChargesApi.subclasses[0]().interest_charge_destroy(id, x_api_version)


@router.get(
    "/interest_charges.json",
    responses={
        200: {"model": InterestChargeList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Interest Charges"],
    summary="Return the data for all InterestCharges",
    response_model_by_alias=True,
)
async def interest_charge_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    bill_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Bill. The keyword `null` is not valid for this field. The list will be filtered to include only the InterestCharge records with the matching property.")] = Query(None, description="The unique identifier for a single Bill. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the InterestCharge records with the matching property.", alias="bill_id"),
    created_since: Annotated[Optional[datetime], Field(description="Filter InterestCharge records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter InterestCharge records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    exclude_ids: Annotated[Optional[StrictInt], Field(description="Array containing *InterestCharge* identifiers that should be excluded from the query.")] = Query(None, description="Array containing *InterestCharge* identifiers that should be excluded from the query.", alias="exclude_ids[]"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter InterestCharge records to those having the specified unique identifiers.")] = Query(None, description="Filter InterestCharge records to those having the specified unique identifiers.", alias="ids[]"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of InterestCharge records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of InterestCharge records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter InterestCharge records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter InterestCharge records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> InterestChargeList:
    """Outlines the parameters, optional and required, used when requesting the data for all InterestCharges"""
    if not BaseInterestChargesApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseInterestChargesApi.subclasses[0]().interest_charge_index(x_api_version, bill_id, created_since, exclude_ids, fields, ids, limit, page_token, updated_since)
