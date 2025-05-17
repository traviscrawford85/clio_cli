# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.contacts_api_base import BaseContactsApi
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
from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.contact_create_request import ContactCreateRequest
from openapi_server.models.contact_list import ContactList
from openapi_server.models.contact_show import ContactShow
from openapi_server.models.contact_update_request import ContactUpdateRequest
from openapi_server.models.error import Error


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/contacts.json",
    responses={
        201: {"model": ContactShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Contacts"],
    summary="Create a new Contact",
    response_model_by_alias=True,
)
async def contact_create(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    custom_field_ids: Annotated[Optional[StrictInt], Field(description="Filter Contact's custom_field_values to only include values for the given custom field unique identifiers.")] = Query(None, description="Filter Contact&#39;s custom_field_values to only include values for the given custom field unique identifiers.", alias="custom_field_ids[]"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    contact_create_request: Annotated[Optional[ContactCreateRequest], Field(description="Request Body for Contacts")] = Body(None, description="Request Body for Contacts"),
) -> ContactShow:
    """Outlines the parameters and data fields used when creating a new Contact"""
    if not BaseContactsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseContactsApi.subclasses[0]().contact_create(x_api_version, custom_field_ids, fields, contact_create_request)


@router.delete(
    "/contacts/{id}.json",
    responses={
        204: {"description": "No Content"},
        403: {"model": Error, "description": "Forbidden"},
    },
    tags=["Contacts"],
    summary="Delete a single Contact",
    response_model_by_alias=True,
)
async def contact_destroy(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Contact.")] = Path(..., description="The unique identifier for the Contact."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single Contact"""
    if not BaseContactsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseContactsApi.subclasses[0]().contact_destroy(id, x_api_version)


@router.get(
    "/contacts.json",
    responses={
        200: {"model": ContactList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Contacts"],
    summary="Return the data for all Contacts",
    response_model_by_alias=True,
)
async def contact_index(
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    client_only: Annotated[Optional[StrictBool], Field(description="Filter Contact records to those that are clients.")] = Query(None, description="Filter Contact records to those that are clients.", alias="client_only"),
    clio_connect_only: Annotated[Optional[StrictBool], Field(description="Filter Contact records to those that are Clio Connect users.")] = Query(None, description="Filter Contact records to those that are Clio Connect users.", alias="clio_connect_only"),
    created_since: Annotated[Optional[datetime], Field(description="Filter Contact records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Contact records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_since"),
    custom_field_ids: Annotated[Optional[StrictInt], Field(description="Filter Contact's custom_field_values to only include values for the given custom field unique identifiers.")] = Query(None, description="Filter Contact&#39;s custom_field_values to only include values for the given custom field unique identifiers.", alias="custom_field_ids[]"),
    custom_field_values: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. `custom_field_values[12345]` If an operator is used for a type that does not support it, an `400 Bad Request` is returned.  *Supported operators:* * `checkbox`, `contact`, `matter`, `picklist` : `=`  e.g. `?custom_field_values[1]=42`  * `currency`, `date`, `time`, `numeric` : `=`, `<`, `>`, `<=`, `>=`  e.g. `?custom_field_values[1]=>=105.4`  * `email`, `text_area`, `text_line`, `url` : `=`  e.g. `?custom_field_values[1]=url_encoded`  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. `?custom_field_values[1]=[<=50, >=45]` ")] = Query(None, description="Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. &#x60;custom_field_values[12345]&#x60; If an operator is used for a type that does not support it, an &#x60;400 Bad Request&#x60; is returned.  *Supported operators:* * &#x60;checkbox&#x60;, &#x60;contact&#x60;, &#x60;matter&#x60;, &#x60;picklist&#x60; : &#x60;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;42&#x60;  * &#x60;currency&#x60;, &#x60;date&#x60;, &#x60;time&#x60;, &#x60;numeric&#x60; : &#x60;&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;&gt;&#x3D;105.4&#x60;  * &#x60;email&#x60;, &#x60;text_area&#x60;, &#x60;text_line&#x60;, &#x60;url&#x60; : &#x60;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;url_encoded&#x60;  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. &#x60;?custom_field_values[1]&#x3D;[&lt;&#x3D;50, &gt;&#x3D;45]&#x60; ", alias="custom_field_values"),
    email_only: Annotated[Optional[StrictBool], Field(description="Filter Contact records to those that have email addresses.")] = Query(None, description="Filter Contact records to those that have email addresses.", alias="email_only"),
    exclude_ids: Annotated[Optional[StrictInt], Field(description="Filter Contact records to those who are not included in the given list of unique identifiers.")] = Query(None, description="Filter Contact records to those who are not included in the given list of unique identifiers.", alias="exclude_ids[]"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    ids: Annotated[Optional[StrictInt], Field(description="Filter Contact records to those having the specified unique identifiers.")] = Query(None, description="Filter Contact records to those having the specified unique identifiers.", alias="ids[]"),
    initial: Annotated[Optional[StrictStr], Field(description="Filter Contact records to those where the last name or company name start with the given initial.")] = Query(None, description="Filter Contact records to those where the last name or company name start with the given initial.", alias="initial"),
    limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Contact records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Contact records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limit"),
    order: Annotated[Optional[StrictStr], Field(description="Orders the Contact records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the Contact records by the given field. Default: &#x60;id(asc)&#x60;.", alias="order"),
    page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_token"),
    query: Annotated[Optional[StrictStr], Field(description="Wildcard search for name, title, email address, address, phone number, web site, instant messenger address, custom fields, related matter name, or company name matching a given string. ")] = Query(None, description="Wildcard search for name, title, email address, address, phone number, web site, instant messenger address, custom fields, related matter name, or company name matching a given string. ", alias="query"),
    shared_resource_id: Annotated[Optional[StrictInt], Field(description="Filter Contact records to those that currently have access to a given shared resource.")] = Query(None, description="Filter Contact records to those that currently have access to a given shared resource.", alias="shared_resource_id"),
    type: Annotated[Optional[StrictStr], Field(description="Filter Contact records to those that match the given type.")] = Query(None, description="Filter Contact records to those that match the given type.", alias="type"),
    updated_since: Annotated[Optional[datetime], Field(description="Filter Contact records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Contact records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_since"),
) -> ContactList:
    """Outlines the parameters, optional and required, used when requesting the data for all Contacts"""
    if not BaseContactsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseContactsApi.subclasses[0]().contact_index(x_api_version, client_only, clio_connect_only, created_since, custom_field_ids, custom_field_values, email_only, exclude_ids, fields, ids, initial, limit, order, page_token, query, shared_resource_id, type, updated_since)


@router.get(
    "/contacts/{id}.json",
    responses={
        200: {"model": ContactShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Contacts"],
    summary="Return the data for a single Contact",
    response_model_by_alias=True,
)
async def contact_show(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Contact.")] = Path(..., description="The unique identifier for the Contact."),
    if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    custom_field_ids: Annotated[Optional[StrictInt], Field(description="Filter Contact's custom_field_values to only include values for the given custom field unique identifiers.")] = Query(None, description="Filter Contact&#39;s custom_field_values to only include values for the given custom field unique identifiers.", alias="custom_field_ids[]"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
) -> ContactShow:
    """Outlines the parameters, optional and required, used when requesting the data for a single Contact"""
    if not BaseContactsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseContactsApi.subclasses[0]().contact_show(id, if_modified_since, if_none_match, x_api_version, custom_field_ids, fields)


@router.patch(
    "/contacts/{id}.json",
    responses={
        200: {"model": ContactShow, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        412: {"model": Error, "description": "Precondition Failed"},
    },
    tags=["Contacts"],
    summary="Update a single Contact",
    response_model_by_alias=True,
)
async def contact_update(
    id: Annotated[StrictInt, Field(description="The unique identifier for the Contact.")] = Path(..., description="The unique identifier for the Contact."),
    if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    custom_field_ids: Annotated[Optional[StrictInt], Field(description="Filter Contact's custom_field_values to only include values for the given custom field unique identifiers.")] = Query(None, description="Filter Contact&#39;s custom_field_values to only include values for the given custom field unique identifiers.", alias="custom_field_ids[]"),
    fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fields"),
    contact_update_request: Annotated[Optional[ContactUpdateRequest], Field(description="Request Body for Contacts")] = Body(None, description="Request Body for Contacts"),
) -> ContactShow:
    """Outlines the parameters and data fields used when updating a single Contact"""
    if not BaseContactsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseContactsApi.subclasses[0]().contact_update(id, if_match, x_api_version, custom_field_ids, fields, contact_update_request)
