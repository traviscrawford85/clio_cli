# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date, datetime
from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.clio_payments_link_create_request import ClioPaymentsLinkCreateRequest
from openapi_server.models.clio_payments_link_list import ClioPaymentsLinkList
from openapi_server.models.clio_payments_link_show import ClioPaymentsLinkShow
from openapi_server.models.clio_payments_link_update_request import ClioPaymentsLinkUpdateRequest
from openapi_server.models.error import Error


class BaseClioPaymentsLinksApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseClioPaymentsLinksApi.subclasses = BaseClioPaymentsLinksApi.subclasses + (cls,)
    async def clio_payments_link_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        clio_payments_link_create_request: Annotated[Optional[ClioPaymentsLinkCreateRequest], Field(description="Request Body for Links")],
    ) -> ClioPaymentsLinkShow:
        """Outlines the parameters and data fields used when creating a new ClioPaymentsLink"""
        ...


    async def clio_payments_link_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        active: Annotated[Optional[StrictBool], Field(description="Filter ClioPaymentsLink records based on whether or not they have expired.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter ClioPaymentsLink records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter ClioPaymentsLink records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of ClioPaymentsLink records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter ClioPaymentsLink records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> ClioPaymentsLinkList:
        """Outlines the parameters, optional and required, used when requesting the data for all ClioPaymentsLinks"""
        ...


    async def clio_payments_link_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the ClioPaymentsLink.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> ClioPaymentsLinkShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single ClioPaymentsLink"""
        ...


    async def clio_payments_link_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the ClioPaymentsLink.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        clio_payments_link_update_request: Annotated[Optional[ClioPaymentsLinkUpdateRequest], Field(description="Request Body for Links")],
    ) -> ClioPaymentsLinkShow:
        """Outlines the parameters and data fields used when updating a single ClioPaymentsLink"""
        ...
