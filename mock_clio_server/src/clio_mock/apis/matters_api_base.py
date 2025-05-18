# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from clio_mock.models.activity_list import ActivityList
from clio_mock.models.activity_show import ActivityShow
from clio_mock.models.matter_create_request import MatterCreateRequest
from clio_mock.models.matter_update_request import MatterUpdateRequest


class BaseMattersApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseMattersApi.subclasses = BaseMattersApi.subclasses + (cls,)
    async def matter_create(
        self,
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        custom_field_idsquery: Annotated[Optional[StrictInt], Field(description="Filter Contact's custom_field_values to only include values for the given custom field unique identifiers.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        matter_create_request: Annotated[Optional[MatterCreateRequest], Field(description="Request Body for Matters")],
    ) -> ActivityShow:
        """Outlines the parameters and data fields used when creating a new Matter"""
        ...


    async def matter_destroy(
        self,
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single Matter"""
        ...


    async def matter_index(
        self,
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        billablequery: Annotated[Optional[StrictBool], Field(description="Filter Matter records to those which are billable.")],
        client_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the BankTransaction records with the matching property.")],
        close_datequery: Annotated[Optional[StrictStr], Field(description="Filter Matter records by the close date. The date should be provided in the format YYYY-MM-DD.  e.g. `?close_date==2020-01-01`, `?close_date=<=2021-12-31`  You can provide more than one value to narrow the results of this filter. You can do so by passing several individual values and appending `[]` to the parameter name.  e.g. `?close_date[]=>=2020-01-01&close_date[]=<=2021-12-31`  Note that, when providing multiple values for this filter, only Matter records that meet *all* filter conditions will be returned. ")],
        created_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        custom_field_idsquery: Annotated[Optional[StrictInt], Field(description="Filter Contact's custom_field_values to only include values for the given custom field unique identifiers.")],
        custom_field_valuesquery: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. `custom_field_values[12345]` If an operator is used for a type that does not support it, an `400 Bad Request` is returned.  *Supported operators:* * `checkbox`, `contact`, `matter`, `picklist` : `=`  e.g. `?custom_field_values[1]=42`  * `currency`, `date`, `time`, `numeric` : `=`, `<`, `>`, `<=`, `>=`  e.g. `?custom_field_values[1]=>=105.4`  * `email`, `text_area`, `text_line`, `url` : `=`  e.g. `?custom_field_values[1]=url_encoded`  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. `?custom_field_values[1]=[<=50, >=45]` ")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        grant_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Grant. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")],
        group_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Group. The keyword `null` is not valid for this field. The list will be filtered to include only the Matter records with the matching property.")],
        idsquery: Annotated[Optional[StrictInt], Field(description="Filter Activity records to those having the specified unique identifiers.")],
        limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        notification_event_subscriber_user_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single NotificationEventSubscriber. Use the keyword `null` to match those without a Matter. The list will be filtered to include only the Matter records with the matching property.")],
        open_datequery: Annotated[Optional[StrictStr], Field(description="Filter Matter records by the open date. The date should be provided in the format YYYY-MM-DD.  e.g. `?open_date==2020-01-01`, `?open_date=<=2021-12-31`  You can provide more than one value to narrow the results of this filter. You can do so by passing several individual values and appending `[]` to the parameter name.  e.g. `?open_date[]=>=2020-01-01&open_date[]=<=2021-12-31`  Note that, when providing multiple values for this filter, only Matter records that meet *all* filter conditions will be returned. ")],
        orderquery: Annotated[Optional[StrictStr], Field(description="Orders the Activity records by the given field. Default: `id(asc)`.")],
        originating_attorney_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a BillableClient. The list will be filtered to include only the BillableClient records with the matching property.")],
        page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        pending_datequery: Annotated[Optional[StrictStr], Field(description="Filter Matter records by the pending date. The date should be provided in the format YYYY-MM-DD.  e.g. `?pending_date==2020-01-01`, `?pending_date=<=2021-12-31`  You can provide more than one value to narrow the results of this filter. You can do so by passing several individual values and appending `[]` to the parameter name.  e.g. `?pending_date[]=>=2020-01-01&pending_date[]=<=2021-12-31`  Note that, when providing multiple values for this filter, only Matter records that meet *all* filter conditions will be returned. ")],
        practice_area_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single PracticeArea. The keyword `null` is not valid for this field. The list will be filtered to include only the Matter records with the matching property.")],
        queryquery: Annotated[Optional[StrictStr], Field(description="Wildcard search for `note` matching a given string.")],
        responsible_attorney_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a BillableClient. The list will be filtered to include only the BillableClient records with the matching property.")],
        responsible_staff_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a Matter. The list will be filtered to include only the Matter records with the matching property.")],
        statusquery: Annotated[Optional[StrictStr], Field(description="Filter Activity records to those that are draft, billed, unbilled or non-billable.")],
        subscriber_user_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single NotificationEventSubscriber. Use the keyword `null` to match those without a Matter. The list will be filtered to include only the Matter records with the matching property.")],
        updated_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> ActivityList:
        """Outlines the parameters, optional and required, used when requesting the data for all Matters"""
        ...


    async def matter_show(
        self,
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
        if_modified_sinc_eheader: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        custom_field_idsquery: Annotated[Optional[StrictInt], Field(description="Filter Contact's custom_field_values to only include values for the given custom field unique identifiers.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> ActivityList:
        """Outlines the parameters, optional and required, used when requesting the data for a single Matter"""
        ...


    async def matter_update(
        self,
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
        if_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        custom_field_idsquery: Annotated[Optional[StrictInt], Field(description="Filter Contact's custom_field_values to only include values for the given custom field unique identifiers.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        matter_update_request: Annotated[Optional[MatterUpdateRequest], Field(description="Request Body for Matters")],
    ) -> ActivityList:
        """Outlines the parameters and data fields used when updating a single Matter"""
        ...
