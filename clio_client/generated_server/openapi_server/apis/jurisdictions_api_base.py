# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.jurisdiction_list import JurisdictionList
from openapi_server.models.jurisdiction_show import JurisdictionShow


class BaseJurisdictionsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseJurisdictionsApi.subclasses = BaseJurisdictionsApi.subclasses + (cls,)
    async def jurisdiction_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter Jurisdiction records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        for_current_account: Annotated[Optional[StrictBool], Field(description="Filter Jurisdiction records to those set up for this account.")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter Jurisdiction records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Jurisdiction records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the Jurisdiction records by the given field. Default: `id(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        query: Annotated[Optional[StrictStr], Field(description="Wildcard search for `description` matching a given string.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter Jurisdiction records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> JurisdictionList:
        """Outlines the parameters, optional and required, used when requesting the data for all Jurisdictions"""
        ...


    async def jurisdiction_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Jurisdiction.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> JurisdictionShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single Jurisdiction"""
        ...
