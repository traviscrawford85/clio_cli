# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import datetime
from pydantic import Field, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.grant_funding_source_create_request import GrantFundingSourceCreateRequest
from openapi_server.models.grant_funding_source_list import GrantFundingSourceList
from openapi_server.models.grant_funding_source_show import GrantFundingSourceShow


class BaseGrantFundingSourcesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseGrantFundingSourcesApi.subclasses = BaseGrantFundingSourcesApi.subclasses + (cls,)
    async def grant_funding_source_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        grant_funding_source_create_request: Annotated[Optional[GrantFundingSourceCreateRequest], Field(description="Request Body for Grant Funding Sources")],
    ) -> GrantFundingSourceShow:
        """Outlines the parameters and data fields used when creating a new GrantFundingSource"""
        ...


    async def grant_funding_source_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the GrantFundingSource.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        grant_funding_source_create_request: Annotated[Optional[GrantFundingSourceCreateRequest], Field(description="Request Body for Grant Funding Sources")],
    ) -> GrantFundingSourceShow:
        """Outlines the parameters and data fields used when updating a single GrantFundingSource"""
        ...


    async def grant_funding_source_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter GrantFundingSource records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter GrantFundingSource records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of GrantFundingSource records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        name: Annotated[Optional[StrictStr], Field(description="Filter GrantFundingSource records to those that match the given name.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter GrantFundingSource records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> GrantFundingSourceList:
        """Outlines the parameters, optional and required, used when requesting the data for all GrantFundingSources"""
        ...


    async def grant_funding_source_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the GrantFundingSource.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        grant_funding_source_create_request: Annotated[Optional[GrantFundingSourceCreateRequest], Field(description="Request Body for Grant Funding Sources")],
    ) -> GrantFundingSourceShow:
        """Outlines the parameters and data fields used when updating a single GrantFundingSource"""
        ...
