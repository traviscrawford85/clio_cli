# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.service_type_list import ServiceTypeList
from openapi_server.models.service_type_show import ServiceTypeShow


class BaseServiceTypesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseServiceTypesApi.subclasses = BaseServiceTypesApi.subclasses + (cls,)
    async def service_type_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter ServiceType records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter ServiceType records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of ServiceType records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the ServiceType records by the given field. Default: `id(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter ServiceType records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> ServiceTypeList:
        """Outlines the parameters, optional and required, used when requesting the data for all ServiceTypes"""
        ...


    async def service_type_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the ServiceType.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> ServiceTypeShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single ServiceType"""
        ...
