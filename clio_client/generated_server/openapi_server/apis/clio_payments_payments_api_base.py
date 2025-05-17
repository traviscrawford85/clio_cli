# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date
from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.clio_payments_payment_list import ClioPaymentsPaymentList
from openapi_server.models.clio_payments_payment_show import ClioPaymentsPaymentShow
from openapi_server.models.error import Error


class BaseClioPaymentsPaymentsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseClioPaymentsPaymentsApi.subclasses = BaseClioPaymentsPaymentsApi.subclasses + (cls,)
    async def clio_payments_payment_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        bill_id: Annotated[Optional[StrictInt], Field(description="Filter ClioPaymentsPayment records to those that are allocated to the specified bill.")],
        contact_id: Annotated[Optional[StrictInt], Field(description="Filter ClioPaymentsPayment records to those that are assigned to the specified contact.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter ClioPaymentsPayment records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of ClioPaymentsPayment records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        state: Annotated[Optional[StrictStr], Field(description="Filter ClioPaymentsPayment records to those in a given state.")],
    ) -> ClioPaymentsPaymentList:
        """Outlines the parameters, optional and required, used when requesting the data for all ClioPaymentsPayments"""
        ...


    async def clio_payments_payment_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the ClioPaymentsPayment.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> ClioPaymentsPaymentShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single ClioPaymentsPayment"""
        ...
