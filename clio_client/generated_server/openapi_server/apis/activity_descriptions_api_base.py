# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.activity_description_create_request import ActivityDescriptionCreateRequest
from openapi_server.models.activity_description_list import ActivityDescriptionList
from openapi_server.models.activity_description_show import ActivityDescriptionShow
from openapi_server.models.activity_description_update_request import ActivityDescriptionUpdateRequest
from openapi_server.models.error import Error


class BaseActivityDescriptionsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseActivityDescriptionsApi.subclasses = BaseActivityDescriptionsApi.subclasses + (cls,)
    async def activity_description_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        activity_description_create_request: Annotated[Optional[ActivityDescriptionCreateRequest], Field(description="Request Body for Activity Descriptions")],
    ) -> ActivityDescriptionShow:
        """Outlines the parameters and data fields used when creating a new ActivityDescription"""
        ...


    async def activity_description_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the ActivityDescription.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single ActivityDescription"""
        ...


    async def activity_description_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter ActivityDescription records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        flat_rate: Annotated[Optional[StrictBool], Field(description="Filter ActivityDescription records to those that have a flat rate, or not.")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter ActivityDescription records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of ActivityDescription records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        rate_for_matter_id: Annotated[Optional[StrictInt], Field(description="Matter id for rate calculation.")],
        rate_for_user_id: Annotated[Optional[StrictInt], Field(description="User id for rate calculation. If not provided, the user associated to the API request is assumed.")],
        type: Annotated[Optional[StrictStr], Field(description="Filter ActivityDescription records to those of a specific type.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter ActivityDescription records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        user_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single User. The keyword `null` is not valid for this field. The list will be filtered to include only the ActivityDescription records with the matching property.")],
    ) -> ActivityDescriptionList:
        """Outlines the parameters, optional and required, used when requesting the data for all ActivityDescriptions"""
        ...


    async def activity_description_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the ActivityDescription.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> ActivityDescriptionShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single ActivityDescription"""
        ...


    async def activity_description_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the ActivityDescription.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        activity_description_update_request: Annotated[Optional[ActivityDescriptionUpdateRequest], Field(description="Request Body for Activity Descriptions")],
    ) -> ActivityDescriptionShow:
        """Outlines the parameters and data fields used when updating a single ActivityDescription"""
        ...
