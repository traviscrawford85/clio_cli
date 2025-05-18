# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from clio_mock.models.activity_list import ActivityList
from clio_mock.models.bill_update_request import BillUpdateRequest


class BaseBillsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseBillsApi.subclasses = BaseBillsApi.subclasses + (cls,)
    async def bill_destroy(
        self,
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """This endpoint will transition a bill to either its deleted or voided state. A bill can only be deleted or voided if it has no payments recorded and its current state is one of the following: * Draft * Pending Approval * Unpaid  A bill will automatically be moved to a deleted or void state based on its current state. The mappings for this are: * Draft -&gt; Deleted * Pending Approval -&gt; Deleted * Unpaid -&gt; Void """
        ...


    async def bill_index(
        self,
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        client_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the BankTransaction records with the matching property.")],
        created_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        currency_idquery: Annotated[Optional[StrictInt], Field(description="Filter Bill records to those of a specific currency.")],
        custom_field_valuesquery: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. `custom_field_values[12345]` If an operator is used for a type that does not support it, an `400 Bad Request` is returned.  *Supported operators:* * `checkbox`, `contact`, `matter`, `picklist` : `=`  e.g. `?custom_field_values[1]=42`  * `currency`, `date`, `time`, `numeric` : `=`, `<`, `>`, `<=`, `>=`  e.g. `?custom_field_values[1]=>=105.4`  * `email`, `text_area`, `text_line`, `url` : `=`  e.g. `?custom_field_values[1]=url_encoded`  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. `?custom_field_values[1]=[<=50, >=45]` ")],
        due_afterquery: Annotated[Optional[date], Field(description="Filter Bill records to those that have a `due_date` after the one provided (Expects an ISO-8601 date).")],
        due_atquery: Annotated[Optional[date], Field(description="Filter Bill records to those that have a specific `due_date` (Expects an ISO-8601 date).")],
        due_beforequery: Annotated[Optional[date], Field(description="Filter Bill records to those that have a `due_date` before the one provided (Expects an ISO-8601 date).")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        idsquery: Annotated[Optional[StrictInt], Field(description="Filter Activity records to those having the specified unique identifiers.")],
        issued_afterquery: Annotated[Optional[date], Field(description="Filter Bill records to those that have an `issue_date` after the one provided (Expects an ISO-8601 date).")],
        issued_beforequery: Annotated[Optional[date], Field(description="Filter Bill records to those that have an `issue_date` before the one provided (Expects an ISO-8601 date).")],
        last_sent_end_datequery: Annotated[Optional[date], Field(description="Filter Bill records for those whose bills have been sent before the specified date")],
        last_sent_start_datequery: Annotated[Optional[date], Field(description="Filter Bill records for those whose bills have been sent after the specified date")],
        limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        matter_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. Use the keyword `null` to match those without a Activity. The list will be filtered to include only the Activity records with the matching property.")],
        orderquery: Annotated[Optional[StrictStr], Field(description="Orders the Activity records by the given field. Default: `id(asc)`.")],
        originating_attorney_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a BillableClient. The list will be filtered to include only the BillableClient records with the matching property.")],
        overdue_onlyquery: Annotated[Optional[StrictBool], Field(description="Filter Bill records to those that are overdue.")],
        page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        queryquery: Annotated[Optional[StrictStr], Field(description="Wildcard search for `note` matching a given string.")],
        responsible_attorney_idquery: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a BillableClient. The list will be filtered to include only the BillableClient records with the matching property.")],
        statequery: Annotated[Optional[StrictStr], Field(description="Filter Bill records to those in a given state.")],
        statusquery: Annotated[Optional[StrictStr], Field(description="Filter Activity records to those that are draft, billed, unbilled or non-billable.")],
        typequery: Annotated[Optional[StrictStr], Field(description="Filter Activity records to those of a specific type.")],
        updated_sincequery: Annotated[Optional[datetime], Field(description="Filter Activity records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> ActivityList:
        """Outlines the parameters, optional and required, used when requesting the data for all Bills"""
        ...


    async def bill_preview(
        self,
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
    ) -> ActivityList:
        """This endpoint returns a pre-rendered HTML object that you can use to view a preview of your bills. The HTML provided contains all of the CSS rules it requires to show the bill correctly, as well as the DOCTYPE setting it requires. It&#39;s best to use an iframe, or similar object, to render the results of this endpoint. """
        ...


    async def bill_show(
        self,
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
        if_modified_sinc_eheader: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        navigation_nextquery: Annotated[Optional[StrictInt], Field(description="The id of the next *Bill* available for viewing")],
        navigation_previousquery: Annotated[Optional[StrictInt], Field(description="The id of the previous *Bill* available for viewing")],
    ) -> ActivityList:
        """Outlines the parameters, optional and required, used when requesting the data for a single Bill"""
        ...


    async def bill_update(
        self,
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
        if_matc_hheader: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        bill_update_request: Annotated[Optional[BillUpdateRequest], Field(description="Request Body for Bills")],
    ) -> ActivityList:
        """Outlines the parameters and data fields used when updating a single Bill"""
        ...
