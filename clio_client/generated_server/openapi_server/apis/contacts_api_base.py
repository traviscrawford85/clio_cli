# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.contact_create_request import ContactCreateRequest
from openapi_server.models.contact_list import ContactList
from openapi_server.models.contact_show import ContactShow
from openapi_server.models.contact_update_request import ContactUpdateRequest
from openapi_server.models.error import Error


class BaseContactsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseContactsApi.subclasses = BaseContactsApi.subclasses + (cls,)
    async def contact_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        custom_field_ids: Annotated[Optional[StrictInt], Field(description="Filter Contact's custom_field_values to only include values for the given custom field unique identifiers.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        contact_create_request: Annotated[Optional[ContactCreateRequest], Field(description="Request Body for Contacts")],
    ) -> ContactShow:
        """Outlines the parameters and data fields used when creating a new Contact"""
        ...


    async def contact_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Contact.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single Contact"""
        ...


    async def contact_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        client_only: Annotated[Optional[StrictBool], Field(description="Filter Contact records to those that are clients.")],
        clio_connect_only: Annotated[Optional[StrictBool], Field(description="Filter Contact records to those that are Clio Connect users.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter Contact records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        custom_field_ids: Annotated[Optional[StrictInt], Field(description="Filter Contact's custom_field_values to only include values for the given custom field unique identifiers.")],
        custom_field_values: Annotated[Optional[StrictStr], Field(description="Filter records to only those with the given custom field(s) set. The value is compared using the operator provided, or, if the value type only supports one operator, the supported operator is used. In the latter case, no check for operator is performed on the input string. The key for the custom field value filter is the custom_field.id. e.g. `custom_field_values[12345]` If an operator is used for a type that does not support it, an `400 Bad Request` is returned.  *Supported operators:* * `checkbox`, `contact`, `matter`, `picklist` : `=`  e.g. `?custom_field_values[1]=42`  * `currency`, `date`, `time`, `numeric` : `=`, `<`, `>`, `<=`, `>=`  e.g. `?custom_field_values[1]=>=105.4`  * `email`, `text_area`, `text_line`, `url` : `=`  e.g. `?custom_field_values[1]=url_encoded`  *Multiple conditions for the same custom field:*  If you want to use more than one operator to filter a custom field, you can do so by passing in an array of values. e.g. `?custom_field_values[1]=[<=50, >=45]` ")],
        email_only: Annotated[Optional[StrictBool], Field(description="Filter Contact records to those that have email addresses.")],
        exclude_ids: Annotated[Optional[StrictInt], Field(description="Filter Contact records to those who are not included in the given list of unique identifiers.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter Contact records to those having the specified unique identifiers.")],
        initial: Annotated[Optional[StrictStr], Field(description="Filter Contact records to those where the last name or company name start with the given initial.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Contact records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the Contact records by the given field. Default: `id(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        query: Annotated[Optional[StrictStr], Field(description="Wildcard search for name, title, email address, address, phone number, web site, instant messenger address, custom fields, related matter name, or company name matching a given string. ")],
        shared_resource_id: Annotated[Optional[StrictInt], Field(description="Filter Contact records to those that currently have access to a given shared resource.")],
        type: Annotated[Optional[StrictStr], Field(description="Filter Contact records to those that match the given type.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter Contact records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> ContactList:
        """Outlines the parameters, optional and required, used when requesting the data for all Contacts"""
        ...


    async def contact_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Contact.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        custom_field_ids: Annotated[Optional[StrictInt], Field(description="Filter Contact's custom_field_values to only include values for the given custom field unique identifiers.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> ContactShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single Contact"""
        ...


    async def contact_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Contact.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        custom_field_ids: Annotated[Optional[StrictInt], Field(description="Filter Contact's custom_field_values to only include values for the given custom field unique identifiers.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        contact_update_request: Annotated[Optional[ContactUpdateRequest], Field(description="Request Body for Contacts")],
    ) -> ContactShow:
        """Outlines the parameters and data fields used when updating a single Contact"""
        ...
