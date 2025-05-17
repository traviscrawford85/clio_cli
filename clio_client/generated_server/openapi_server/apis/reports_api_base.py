# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.report_create_request import ReportCreateRequest
from openapi_server.models.report_list import ReportList
from openapi_server.models.report_show import ReportShow


class BaseReportsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseReportsApi.subclasses = BaseReportsApi.subclasses + (cls,)
    async def report_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        report_create_request: Annotated[Optional[ReportCreateRequest], Field(description="Request Body for Reports")],
    ) -> ReportShow:
        """Outlines the parameters and data fields used when creating a new Report"""
        ...


    async def report_download(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Report.")],
    ) -> None:
        """Download the completed Report"""
        ...


    async def report_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        category: Annotated[Optional[StrictStr], Field(description="Filters Report data by category.")],
        created_before: Annotated[Optional[datetime], Field(description="Filters Report data by date. (Expects an ISO-8601 date).")],
        created_since: Annotated[Optional[datetime], Field(description="Filter Report records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter Report records to those having the specified unique identifiers.")],
        kind: Annotated[Optional[StrictStr], Field(description="Filters Report data by kind.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of Report records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        output_format: Annotated[Optional[StrictStr], Field(description="Filters Report data by format.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        query: Annotated[Optional[StrictStr], Field(description="Wildcard search for Report name.")],
        source: Annotated[Optional[StrictStr], Field(description="Filters Report data by source.")],
        state: Annotated[Optional[StrictStr], Field(description="Filters Report data by state.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter Report records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> ReportList:
        """Outlines the parameters, optional and required, used when requesting the data for all Reports"""
        ...


    async def report_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the Report.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> ReportShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single Report"""
        ...
