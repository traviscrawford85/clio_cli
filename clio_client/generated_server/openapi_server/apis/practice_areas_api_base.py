# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.practice_area_create_request import PracticeAreaCreateRequest
from openapi_server.models.practice_area_list import PracticeAreaList
from openapi_server.models.practice_area_show import PracticeAreaShow
from openapi_server.models.practice_area_update_request import PracticeAreaUpdateRequest


class BasePracticeAreasApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BasePracticeAreasApi.subclasses = BasePracticeAreasApi.subclasses + (cls,)
    async def practice_area_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        practice_area_create_request: Annotated[Optional[PracticeAreaCreateRequest], Field(description="Request Body for Practice Areas")],
    ) -> PracticeAreaShow:
        """Outlines the parameters and data fields used when creating a new PracticeArea"""
        ...


    async def practice_area_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the PracticeArea.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single PracticeArea"""
        ...


    async def practice_area_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        code: Annotated[Optional[StrictStr], Field(description="Filter PracticeArea records to those that match the given code.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter PracticeArea records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter PracticeArea records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of PracticeArea records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        matter_id: Annotated[Optional[StrictInt], Field(description="Filter PracticeArea records to exclude Legal Aid UK Practice Areas when activities exist on the matter.")],
        name: Annotated[Optional[StrictStr], Field(description="Filter PracticeArea records to those that match the given name.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the PracticeArea records by the given field. Default: `id(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter PracticeArea records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> PracticeAreaList:
        """Outlines the parameters, optional and required, used when requesting the data for all PracticeAreas"""
        ...


    async def practice_area_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the PracticeArea.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> PracticeAreaShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single PracticeArea"""
        ...


    async def practice_area_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the PracticeArea.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        practice_area_update_request: Annotated[Optional[PracticeAreaUpdateRequest], Field(description="Request Body for Practice Areas")],
    ) -> PracticeAreaShow:
        """Outlines the parameters and data fields used when updating a single PracticeArea"""
        ...
