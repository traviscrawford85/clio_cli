# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.matter_contacts_api_base import BaseMatterContactsApi
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
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.matter_contacts_list import MatterContactsList


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/matters/{matter_id}/contacts.json",
    responses={
        200: {"model": MatterContactsList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Matter Contacts"],
    summary="Return the related contact data for a single matter",
    response_model_by_alias=True,
)
async def matter_contacts_index(
    matter_id: Annotated[StrictInt, Field(description="Filters contact data by matter.")] = Path(..., description="Filters contact data by matter."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    custom_field_ids: Annotated[Optional[StrictInt], Field(description="IDs of custom fields to include in results.")] = Query(None, description="IDs of custom fields to include in results.", alias="custom_field_ids[]"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of MatterContacts records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of MatterContacts records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the MatterContacts records by the given field. Note that `id` is ordered by the `id` of the nested Relationship record. Default: `is_client(asc)`.")] = Query(None, description="Orders the MatterContacts records by the given field. Note that &#x60;id&#x60; is ordered by the &#x60;id&#x60; of the nested Relationship record. Default: &#x60;is_client(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
) -> MatterContactsList:
    """Outlines the parameters, optional and required, used when requesting the data for all MatterContacts"""
    if not BaseMatterContactsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMatterContactsApi.subclasses[0]().matter_contacts_index(matter_id, x_api_version, custom_field_ids, fields, limit, order, page_token)
