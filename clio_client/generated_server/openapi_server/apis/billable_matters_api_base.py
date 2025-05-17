# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Optional
from typing_extensions import Annotated
from openapi_server.models.billable_matter_list import BillableMatterList
from openapi_server.models.billable_matter_show import BillableMatterShow
from openapi_server.models.error import Error


class BaseBillableMattersApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseBillableMattersApi.subclasses = BaseBillableMattersApi.subclasses + (cls,)
    async def billable_matter_ids(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        client_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the BillableMatter records with the matching property.")],
        custom_field_values: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. `custom_field_values[12345]` If an operator is used for a type that does not support it, an `400 Bad Request` is returned.  *Supported operators:* * `checkbox`, `contact`, `matter`, `picklist` : `=`  e.g. `?custom_field_values[1]=42`  * `currency`, `date`, `time`, `numeric` : `=`, `<`, `>`, `<=`, `>=`  e.g. `?custom_field_values[1]=>=105.4`  * `email`, `text_area`, `text_line`, `url` : `=`  e.g. `?custom_field_values[1]=url_encoded`  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. `?custom_field_values[1]=[<=50, >=45]` ")],
        end_date: Annotated[Optional[date], Field(description="Filter BillableMatter records to those that have matters with unbilled activities on or before this date (Expects an ISO-8601 date).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of BillableMatter records to be returned. Limit can range between 1 and 1000. Default: `1000`.")],
        matter_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. The keyword `null` is not valid for this field. The list will be filtered to include only the BillableMatter records with the matching property.")],
        originating_attorney_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a BillableMatter. The list will be filtered to include only the BillableMatter records with the matching property.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `display_number` or `number` or `description` matching a given string.")],
        responsible_attorney_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a BillableMatter. The list will be filtered to include only the BillableMatter records with the matching property.")],
        start_date: Annotated[Optional[date], Field(description="Filter BillableMatter records to those that have matters with unbilled activities on or after this date (Expects an ISO-8601 date).")],
    ) -> BillableMatterShow:
        """This data is retrieved asynchronously"""
        ...


    async def billable_matter_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        client_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the BillableMatter records with the matching property.")],
        custom_field_values: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. `custom_field_values[12345]` If an operator is used for a type that does not support it, an `400 Bad Request` is returned.  *Supported operators:* * `checkbox`, `contact`, `matter`, `picklist` : `=`  e.g. `?custom_field_values[1]=42`  * `currency`, `date`, `time`, `numeric` : `=`, `<`, `>`, `<=`, `>=`  e.g. `?custom_field_values[1]=>=105.4`  * `email`, `text_area`, `text_line`, `url` : `=`  e.g. `?custom_field_values[1]=url_encoded`  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. `?custom_field_values[1]=[<=50, >=45]` ")],
        end_date: Annotated[Optional[date], Field(description="Filter BillableMatter records to those that have matters with unbilled activities on or before this date (Expects an ISO-8601 date).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of BillableMatter records to be returned. Limit can range between 1 and 1000. Default: `1000`.")],
        matter_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Matter. The keyword `null` is not valid for this field. The list will be filtered to include only the BillableMatter records with the matching property.")],
        originating_attorney_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a BillableMatter. The list will be filtered to include only the BillableMatter records with the matching property.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `display_number` or `number` or `description` matching a given string.")],
        responsible_attorney_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. Use the keyword `null` to match those without a BillableMatter. The list will be filtered to include only the BillableMatter records with the matching property.")],
        start_date: Annotated[Optional[date], Field(description="Filter BillableMatter records to those that have matters with unbilled activities on or after this date (Expects an ISO-8601 date).")],
    ) -> BillableMatterList:
        """Outlines the parameters, optional and required, used when requesting the data for all BillableMatters"""
        ...
