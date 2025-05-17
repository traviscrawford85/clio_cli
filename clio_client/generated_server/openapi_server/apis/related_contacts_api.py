# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.related_contacts_api_base import BaseRelatedContactsApi
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
from openapi_server.models.related_contacts_list import RelatedContactsList


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/matters/{matter_id}/related_contacts.json",
    responses={
        200: {"model": RelatedContactsList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Related Contacts"],
    summary="Return the related contact data for a single matter",
    response_model_by_alias=True,
)
async def related_contacts_index(
    matter_id: Annotated[StrictInt, Field(description="Filters RelatedContacts data by matter.")] = Path(..., description="Filters RelatedContacts data by matter."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of RelatedContacts records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of RelatedContacts records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the RelatedContacts records by the given field. Note that `id` is ordered by the `id` of the nested Relationship record. Default: `id(asc)`.")] = Query(None, description="Orders the RelatedContacts records by the given field. Note that &#x60;id&#x60; is ordered by the &#x60;id&#x60; of the nested Relationship record. Default: &#x60;id(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
) -> RelatedContactsList:
    """Outlines the parameters, optional and required, used when requesting the data for all RelatedContacts"""
    if not BaseRelatedContactsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseRelatedContactsApi.subclasses[0]().related_contacts_index(matter_id, x_api_version, fields, limit, order, page_token)
