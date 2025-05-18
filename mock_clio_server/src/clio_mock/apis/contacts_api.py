# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from clio_mock.apis.contacts_api_base import BaseContactsApi
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
from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from clio_mock.models.activity_list import ActivityList
from clio_mock.models.activity_show import ActivityShow
from clio_mock.models.contact_create_request import ContactCreateRequest
from clio_mock.models.contact_update_request import ContactUpdateRequest
from clio_mock.models.error import Error


router = APIRouter()

ns_pkg = clio_mock.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/contacts.json",
    responses={
        201: {"model": ActivityShow, "description": "Created"},
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
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    custom_field_idsquery: Annotated[Optional[StrictInt], Field(description="Filter Contact's custom_field_values to only include values for the given custom field unique identifiers.")] = Query(None, description="Filter Contact&#39;s custom_field_values to only include values for the given custom field unique identifiers.", alias="custom_field_idsquery"),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    contact_create_request: Annotated[Optional[ContactCreateRequest], Field(description="Request Body for Contacts")] = Body(None, description="Request Body for Contacts"),
) -> ActivityShow:
    """Outlines the parameters and data fields used when creating a new Contact"""
    if not BaseContactsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseContactsApi.subclasses[0]().contact_create(x_api_versio_nheader, custom_field_idsquery, fieldsquery, contact_create_request)


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
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single Contact"""
    if not BaseContactsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseContactsApi.subclasses[0]().contact_destroy(idpath, x_api_versio_nheader)


@router.get(
    "/contacts.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
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
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    client_onlyquery: Annotated[Optional[StrictBool], Field(description="Filter Contact records to those that are clients.")] = Query(None, description="Filter Contact records to those that are clients.", alias="client_onlyquery"),
    clio_connect_onlyquery: Annotated[Optional[StrictBool], Field(description="Filter Contact records to those that are Clio Connect users.")] = Query(None, description="Filter Contact records to those that are Clio Connect users.", alias="clio_connect_onlyquery"),
    created_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_sincequery"),
    custom_field_idsquery: Annotated[Optional[StrictInt], Field(description="Filter Contact's custom_field_values to only include values for the given custom field unique identifiers.")] = Query(None, description="Filter Contact&#39;s custom_field_values to only include values for the given custom field unique identifiers.", alias="custom_field_idsquery"),
    custom_field_valuesquery: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. `custom_field_values[12345]` If an operator is used for a type that does not support it, an `400 Bad Request` is returned.  *Supported operators:* * `checkbox`, `contact`, `matter`, `picklist` : `=`  e.g. `?custom_field_values[1]=42`  * `currency`, `date`, `time`, `numeric` : `=`, `<`, `>`, `<=`, `>=`  e.g. `?custom_field_values[1]=>=105.4`  * `email`, `text_area`, `text_line`, `url` : `=`  e.g. `?custom_field_values[1]=url_encoded`  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. `?custom_field_values[1]=[<=50, >=45]` ")] = Query(None, description="Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. &#x60;custom_field_values[12345]&#x60; If an operator is used for a type that does not support it, an &#x60;400 Bad Request&#x60; is returned.  *Supported operators:* * &#x60;checkbox&#x60;, &#x60;contact&#x60;, &#x60;matter&#x60;, &#x60;picklist&#x60; : &#x60;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;42&#x60;  * &#x60;currency&#x60;, &#x60;date&#x60;, &#x60;time&#x60;, &#x60;numeric&#x60; : &#x60;&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;&gt;&#x3D;105.4&#x60;  * &#x60;email&#x60;, &#x60;text_area&#x60;, &#x60;text_line&#x60;, &#x60;url&#x60; : &#x60;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;url_encoded&#x60;  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. &#x60;?custom_field_values[1]&#x3D;[&lt;&#x3D;50, &gt;&#x3D;45]&#x60; ", alias="custom_field_valuesquery"),
    email_onlyquery: Annotated[Optional[StrictBool], Field(description="Filter Contact records to those that have email addresses.")] = Query(None, description="Filter Contact records to those that have email addresses.", alias="email_onlyquery"),
    exclude_idsquery: Annotated[Optional[StrictInt], Field(description="Filter Contact records to those who are not included in the given list of unique identifiers.")] = Query(None, description="Filter Contact records to those who are not included in the given list of unique identifiers.", alias="exclude_idsquery"),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    idsquery: Annotated[Optional[StrictInt], Field(description="Filter Activity records to those having the specified unique identifiers.")] = Query(None, description="Filter Activity records to those having the specified unique identifiers.", alias="idsquery"),
    initialquery: Annotated[Optional[StrictStr], Field(description="Filter Contact records to those where the last name or company name start with the given initial.")] = Query(None, description="Filter Contact records to those where the last name or company name start with the given initial.", alias="initialquery"),
    limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limitquery"),
    orderquery: Annotated[Optional[StrictStr], Field(description="Orders the Activity records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the Activity records by the given field. Default: &#x60;id(asc)&#x60;.", alias="orderquery"),
    page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_tokenquery"),
    queryquery: Annotated[Optional[StrictStr], Field(description="Wildcard search for `note` matching a given string.")] = Query(None, description="Wildcard search for &#x60;note&#x60; matching a given string.", alias="queryquery"),
    shared_resource_idquery: Annotated[Optional[StrictInt], Field(description="Filter Contact records to those that currently have access to a given shared resource.")] = Query(None, description="Filter Contact records to those that currently have access to a given shared resource.", alias="shared_resource_idquery"),
    typequery: Annotated[Optional[StrictStr], Field(description="Filter Activity records to those of a specific type.")] = Query(None, description="Filter Activity records to those of a specific type.", alias="typequery"),
    updated_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_sincequery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for all Contacts"""
    if not BaseContactsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseContactsApi.subclasses[0]().contact_index(x_api_versio_nheader, client_onlyquery, clio_connect_onlyquery, created_sincequery, custom_field_idsquery, custom_field_valuesquery, email_onlyquery, exclude_idsquery, fieldsquery, idsquery, initialquery, limitquery, orderquery, page_tokenquery, queryquery, shared_resource_idquery, typequery, updated_sincequery)


@router.get(
    "/contacts/{id}.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
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
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_modified_sinc_eheader: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    custom_field_idsquery: Annotated[Optional[StrictInt], Field(description="Filter Contact's custom_field_values to only include values for the given custom field unique identifiers.")] = Query(None, description="Filter Contact&#39;s custom_field_values to only include values for the given custom field unique identifiers.", alias="custom_field_idsquery"),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for a single Contact"""
    if not BaseContactsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseContactsApi.subclasses[0]().contact_show(idpath, if_modified_sinc_eheader, if_none_matc_hheader, x_api_versio_nheader, custom_field_idsquery, fieldsquery)


@router.patch(
    "/contacts/{id}.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
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
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    custom_field_idsquery: Annotated[Optional[StrictInt], Field(description="Filter Contact's custom_field_values to only include values for the given custom field unique identifiers.")] = Query(None, description="Filter Contact&#39;s custom_field_values to only include values for the given custom field unique identifiers.", alias="custom_field_idsquery"),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    contact_update_request: Annotated[Optional[ContactUpdateRequest], Field(description="Request Body for Contacts")] = Body(None, description="Request Body for Contacts"),
) -> ActivityList:
    """Outlines the parameters and data fields used when updating a single Contact"""
    if not BaseContactsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseContactsApi.subclasses[0]().contact_update(idpath, if_matc_hheader, x_api_versio_nheader, custom_field_idsquery, fieldsquery, contact_update_request)
