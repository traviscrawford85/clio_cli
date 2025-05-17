# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictInt, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.activity_rate_create_request import ActivityRateCreateRequest
from openapi_server.models.activity_rate_list import ActivityRateList
from openapi_server.models.activity_rate_show import ActivityRateShow
from openapi_server.models.error import Error


class BaseActivityRatesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseActivityRatesApi.subclasses = BaseActivityRatesApi.subclasses + (cls,)
    async def activity_rate_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        activity_rate_create_request: Annotated[Optional[ActivityRateCreateRequest], Field(description="Request Body for Activity Rates")],
    ) -> ActivityRateShow:
        """Outlines the parameters and data fields used when creating a new ActivityRate"""
        ...


    async def activity_rate_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the ActivityRate.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single ActivityRate"""
        ...


    async def activity_rate_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        co_counsel_contact_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the ActivityRate records with the matching property.")],
        contact_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. The keyword `null` is not valid for this field. The list will be filtered to include only the ActivityRate records with the matching property.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter ActivityRate records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter ActivityRate records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of ActivityRate records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter ActivityRate records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> ActivityRateList:
        """Outlines the parameters, optional and required, used when requesting the data for all ActivityRates"""
        ...


    async def activity_rate_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the ActivityRate.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> ActivityRateShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single ActivityRate"""
        ...


    async def activity_rate_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the ActivityRate.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        activity_rate_create_request: Annotated[Optional[ActivityRateCreateRequest], Field(description="Request Body for Activity Rates")],
    ) -> ActivityRateShow:
        """Outlines the parameters and data fields used when updating a single ActivityRate"""
        ...
