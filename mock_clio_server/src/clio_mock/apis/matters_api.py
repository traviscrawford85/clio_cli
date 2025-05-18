# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from clio_mock.apis.matters_api_base import BaseMattersApi
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
from clio_mock.models.error import Error
from clio_mock.models.matter_create_request import MatterCreateRequest
from clio_mock.models.matter_update_request import MatterUpdateRequest


router = APIRouter()

ns_pkg = clio_mock.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/matters.json",
    responses={
        201: {"model": ActivityShow, "description": "Created"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        422: {"model": Error, "description": "Unprocessable Entity"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Matters"],
    summary="Create a new Matter",
    response_model_by_alias=True,
)
async def matter_create(
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    custom_field_idsquery: Annotated[Optional[StrictInt], Field(description="Filter Contact's custom_field_values to only include values for the given custom field unique identifiers.")] = Query(None, description="Filter Contact&#39;s custom_field_values to only include values for the given custom field unique identifiers.", alias="custom_field_idsquery"),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    matter_create_request: Annotated[Optional[MatterCreateRequest], Field(description="Request Body for Matters")] = Body(None, description="Request Body for Matters"),
) -> ActivityShow:
    """Outlines the parameters and data fields used when creating a new Matter"""
    if not BaseMattersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMattersApi.subclasses[0]().matter_create(x_api_versio_nheader, custom_field_idsquery, fieldsquery, matter_create_request)


@router.delete(
    "/matters/{id}.json",
    responses={
        204: {"description": "No Content"},
        403: {"model": Error, "description": "Forbidden"},
    },
    tags=["Matters"],
    summary="Delete a single Matter",
    response_model_by_alias=True,
)
async def matter_destroy(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
) -> None:
    """Outlines the parameters, optional and required, used when deleting the record for a single Matter"""
    if not BaseMattersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMattersApi.subclasses[0]().matter_destroy(idpath, x_api_versio_nheader)


@router.get(
    "/matters.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Forbidden"},
        429: {"model": Error, "description": "Too Many Requests"},
    },
    tags=["Matters"],
    summary="Return the data for all Matters",
    response_model_by_alias=True,
)
async def matter_index(
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    billablequery: Annotated[Optional[StrictBool], Field(description="Filter Matter records to those which are billable.")] = Query(None, description="Filter Matter records to those which are billable.", alias="billablequery"),
    client_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the BankTransaction records with the matching property.")] = Query(None, description="The unique identifier for a single Contact. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the BankTransaction records with the matching property.", alias="client_idquery"),
    close_datequery: Annotated[Optional[StrictStr], Field(description="Filter Matter records by the close date. The date should be provided in the format YYYY-MM-DD.  e.g. `?close_date==2020-01-01`, `?close_date=<=2021-12-31`  You can provide more than one value to narrow the results of this filter. You can do so by passing several individual values and appending `[]` to the parameter name.  e.g. `?close_date[]=>=2020-01-01&close_date[]=<=2021-12-31`  Note that, when providing multiple values for this filter, only Matter records that meet *all* filter conditions will be returned. ")] = Query(None, description="Filter Matter records by the close date. The date should be provided in the format YYYY-MM-DD.  e.g. &#x60;?close_date&#x3D;&#x3D;2020-01-01&#x60;, &#x60;?close_date&#x3D;&lt;&#x3D;2021-12-31&#x60;  You can provide more than one value to narrow the results of this filter. You can do so by passing several individual values and appending &#x60;[]&#x60; to the parameter name.  e.g. &#x60;?close_date[]&#x3D;&gt;&#x3D;2020-01-01&amp;close_date[]&#x3D;&lt;&#x3D;2021-12-31&#x60;  Note that, when providing multiple values for this filter, only Matter records that meet *all* filter conditions will be returned. ", alias="close_datequery"),
    created_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;created_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="created_sincequery"),
    custom_field_idsquery: Annotated[Optional[StrictInt], Field(description="Filter Contact's custom_field_values to only include values for the given custom field unique identifiers.")] = Query(None, description="Filter Contact&#39;s custom_field_values to only include values for the given custom field unique identifiers.", alias="custom_field_idsquery"),
    custom_field_valuesquery: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. `custom_field_values[12345]` If an operator is used for a type that does not support it, an `400 Bad Request` is returned.  *Supported operators:* * `checkbox`, `contact`, `matter`, `picklist` : `=`  e.g. `?custom_field_values[1]=42`  * `currency`, `date`, `time`, `numeric` : `=`, `<`, `>`, `<=`, `>=`  e.g. `?custom_field_values[1]=>=105.4`  * `email`, `text_area`, `text_line`, `url` : `=`  e.g. `?custom_field_values[1]=url_encoded`  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. `?custom_field_values[1]=[<=50, >=45]` ")] = Query(None, description="Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. &#x60;custom_field_values[12345]&#x60; If an operator is used for a type that does not support it, an &#x60;400 Bad Request&#x60; is returned.  *Supported operators:* * &#x60;checkbox&#x60;, &#x60;contact&#x60;, &#x60;matter&#x60;, &#x60;picklist&#x60; : &#x60;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;42&#x60;  * &#x60;currency&#x60;, &#x60;date&#x60;, &#x60;time&#x60;, &#x60;numeric&#x60; : &#x60;&#x3D;&#x60;, &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;&gt;&#x3D;105.4&#x60;  * &#x60;email&#x60;, &#x60;text_area&#x60;, &#x60;text_line&#x60;, &#x60;url&#x60; : &#x60;&#x3D;&#x60;  e.g. &#x60;?custom_field_values[1]&#x3D;url_encoded&#x60;  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. &#x60;?custom_field_values[1]&#x3D;[&lt;&#x3D;50, &gt;&#x3D;45]&#x60; ", alias="custom_field_valuesquery"),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    grant_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Grant. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")] = Query(None, description="The unique identifier for a single Grant. Use the keyword &#x60;null&#x60; to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.", alias="grant_idquery"),
    group_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Group. The keyword `null` is not valid for this field. The list will be filtered to include only the Matter records with the matching property.")] = Query(None, description="The unique identifier for a single Group. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Matter records with the matching property.", alias="group_idquery"),
    idsquery: Annotated[Optional[StrictInt], Field(description="Filter Activity records to those having the specified unique identifiers.")] = Query(None, description="Filter Activity records to those having the specified unique identifiers.", alias="idsquery"),
    limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")] = Query(None, description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: &#x60;200&#x60;.", alias="limitquery"),
    notification_event_subscriber_user_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single NotificationEventSubscriber. Use the keyword `null` to match those without a Matter. The list will be filtered to include only the Matter records with the matching property.")] = Query(None, description="The unique identifier for a single NotificationEventSubscriber. Use the keyword &#x60;null&#x60; to match those without a Matter. The list will be filtered to include only the Matter records with the matching property.", alias="notification_event_subscriber_user_idquery"),
    open_datequery: Annotated[Optional[StrictStr], Field(description="Filter Matter records by the open date. The date should be provided in the format YYYY-MM-DD.  e.g. `?open_date==2020-01-01`, `?open_date=<=2021-12-31`  You can provide more than one value to narrow the results of this filter. You can do so by passing several individual values and appending `[]` to the parameter name.  e.g. `?open_date[]=>=2020-01-01&open_date[]=<=2021-12-31`  Note that, when providing multiple values for this filter, only Matter records that meet *all* filter conditions will be returned. ")] = Query(None, description="Filter Matter records by the open date. The date should be provided in the format YYYY-MM-DD.  e.g. &#x60;?open_date&#x3D;&#x3D;2020-01-01&#x60;, &#x60;?open_date&#x3D;&lt;&#x3D;2021-12-31&#x60;  You can provide more than one value to narrow the results of this filter. You can do so by passing several individual values and appending &#x60;[]&#x60; to the parameter name.  e.g. &#x60;?open_date[]&#x3D;&gt;&#x3D;2020-01-01&amp;open_date[]&#x3D;&lt;&#x3D;2021-12-31&#x60;  Note that, when providing multiple values for this filter, only Matter records that meet *all* filter conditions will be returned. ", alias="open_datequery"),
    orderquery: Annotated[Optional[StrictStr], Field(description="Orders the Activity records by the given field. Default: `id(asc)`.")] = Query(None, description="Orders the Activity records by the given field. Default: &#x60;id(asc)&#x60;.", alias="orderquery"),
    originating_attorney_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a BillableClient. The list will be filtered to include only the BillableClient records with the matching property.")] = Query(None, description="The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a BillableClient. The list will be filtered to include only the BillableClient records with the matching property.", alias="originating_attorney_idquery"),
    page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")] = Query(None, description="A token specifying which page to return.", alias="page_tokenquery"),
    pending_datequery: Annotated[Optional[StrictStr], Field(description="Filter Matter records by the pending date. The date should be provided in the format YYYY-MM-DD.  e.g. `?pending_date==2020-01-01`, `?pending_date=<=2021-12-31`  You can provide more than one value to narrow the results of this filter. You can do so by passing several individual values and appending `[]` to the parameter name.  e.g. `?pending_date[]=>=2020-01-01&pending_date[]=<=2021-12-31`  Note that, when providing multiple values for this filter, only Matter records that meet *all* filter conditions will be returned. ")] = Query(None, description="Filter Matter records by the pending date. The date should be provided in the format YYYY-MM-DD.  e.g. &#x60;?pending_date&#x3D;&#x3D;2020-01-01&#x60;, &#x60;?pending_date&#x3D;&lt;&#x3D;2021-12-31&#x60;  You can provide more than one value to narrow the results of this filter. You can do so by passing several individual values and appending &#x60;[]&#x60; to the parameter name.  e.g. &#x60;?pending_date[]&#x3D;&gt;&#x3D;2020-01-01&amp;pending_date[]&#x3D;&lt;&#x3D;2021-12-31&#x60;  Note that, when providing multiple values for this filter, only Matter records that meet *all* filter conditions will be returned. ", alias="pending_datequery"),
    practice_area_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single PracticeArea. The keyword `null` is not valid for this field. The list will be filtered to include only the Matter records with the matching property.")] = Query(None, description="The unique identifier for a single PracticeArea. The keyword &#x60;null&#x60; is not valid for this field. The list will be filtered to include only the Matter records with the matching property.", alias="practice_area_idquery"),
    queryquery: Annotated[Optional[StrictStr], Field(description="Wildcard search for `note` matching a given string.")] = Query(None, description="Wildcard search for &#x60;note&#x60; matching a given string.", alias="queryquery"),
    responsible_attorney_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a BillableClient. The list will be filtered to include only the BillableClient records with the matching property.")] = Query(None, description="The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a BillableClient. The list will be filtered to include only the BillableClient records with the matching property.", alias="responsible_attorney_idquery"),
    responsible_staff_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a Matter. The list will be filtered to include only the Matter records with the matching property.")] = Query(None, description="The unique identifier for a single User. Use the keyword &#x60;null&#x60; to match those without a Matter. The list will be filtered to include only the Matter records with the matching property.", alias="responsible_staff_idquery"),
    statusquery: Annotated[Optional[StrictStr], Field(description="Filter Activity records to those that are draft, billed, unbilled or non-billable.")] = Query(None, description="Filter Activity records to those that are draft, billed, unbilled or non-billable.", alias="statusquery"),
    subscriber_user_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single NotificationEventSubscriber. Use the keyword `null` to match those without a Matter. The list will be filtered to include only the Matter records with the matching property.")] = Query(None, description="The unique identifier for a single NotificationEventSubscriber. Use the keyword &#x60;null&#x60; to match those without a Matter. The list will be filtered to include only the Matter records with the matching property.", alias="subscriber_user_idquery"),
    updated_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")] = Query(None, description="Filter Activity records to those having the &#x60;updated_at&#x60; field after a specific time. (Expects an ISO-8601 timestamp).", alias="updated_sincequery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for all Matters"""
    if not BaseMattersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMattersApi.subclasses[0]().matter_index(x_api_versio_nheader, billablequery, client_idquery, close_datequery, created_sincequery, custom_field_idsquery, custom_field_valuesquery, fieldsquery, grant_idquery, group_idquery, idsquery, limitquery, notification_event_subscriber_user_idquery, open_datequery, orderquery, originating_attorney_idquery, page_tokenquery, pending_datequery, practice_area_idquery, queryquery, responsible_attorney_idquery, responsible_staff_idquery, statusquery, subscriber_user_idquery, updated_sincequery)


@router.get(
    "/matters/{id}.json",
    responses={
        200: {"model": ActivityList, "description": "Ok"},
        400: {"model": Error, "description": "Bad Request"},
        403: {"model": Error, "description": "Forbidden"},
        404: {"model": Error, "description": "Not Found"},
        401: {"model": Error, "description": "Unauthorized"},
        429: {"model": Error, "description": "Too Many Requests"},
        304: {"description": "Not Modified"},
    },
    tags=["Matters"],
    summary="Return the data for a single Matter",
    response_model_by_alias=True,
)
async def matter_show(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_modified_sinc_eheader: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")] = Header(None, description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp)."),
    if_none_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")] = Header(None, description="The server will send the requested resource with a 200 status, but only if the existing resource&#39;s [ETag](#section/ETags) doesn&#39;t match any of the values listed."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    custom_field_idsquery: Annotated[Optional[StrictInt], Field(description="Filter Contact's custom_field_values to only include values for the given custom field unique identifiers.")] = Query(None, description="Filter Contact&#39;s custom_field_values to only include values for the given custom field unique identifiers.", alias="custom_field_idsquery"),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
) -> ActivityList:
    """Outlines the parameters, optional and required, used when requesting the data for a single Matter"""
    if not BaseMattersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMattersApi.subclasses[0]().matter_show(idpath, if_modified_sinc_eheader, if_none_matc_hheader, x_api_versio_nheader, custom_field_idsquery, fieldsquery)


@router.patch(
    "/matters/{id}.json",
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
    tags=["Matters"],
    summary="Update a single Matter",
    response_model_by_alias=True,
)
async def matter_update(
    idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")] = Path(..., description="The unique identifier for the Activity."),
    if_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")] = Header(None, description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource&#39;s [ETag](#section/ETags)."),
    x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = Header(None, description="The [API minor version](#section/Minor-Versions). Default: latest version."),
    custom_field_idsquery: Annotated[Optional[StrictInt], Field(description="Filter Contact's custom_field_values to only include values for the given custom field unique identifiers.")] = Query(None, description="Filter Contact&#39;s custom_field_values to only include values for the given custom field unique identifiers.", alias="custom_field_idsquery"),
    fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")] = Query(None, description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).", alias="fieldsquery"),
    matter_update_request: Annotated[Optional[MatterUpdateRequest], Field(description="Request Body for Matters")] = Body(None, description="Request Body for Matters"),
) -> ActivityList:
    """Outlines the parameters and data fields used when updating a single Matter"""
    if not BaseMattersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseMattersApi.subclasses[0]().matter_update(idpath, if_matc_hheader, x_api_versio_nheader, custom_field_idsquery, fieldsquery, matter_update_request)
