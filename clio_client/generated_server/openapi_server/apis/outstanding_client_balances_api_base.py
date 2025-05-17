# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date
from pydantic import Field, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.outstanding_client_balance_list import OutstandingClientBalanceList


class BaseOutstandingClientBalancesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseOutstandingClientBalancesApi.subclasses = BaseOutstandingClientBalancesApi.subclasses + (cls,)
    async def outstanding_client_balance_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        contact_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Contact. Use the keyword `null` to match those without a OutstandingClientBalance. The list will be filtered to include only the OutstandingClientBalance records with the matching property.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        last_paid_end_date: Annotated[Optional[date], Field(description="Filter OutstandingClientBalance records for those whose bills have been paid before the specified date")],
        last_paid_start_date: Annotated[Optional[date], Field(description="Filter OutstandingClientBalance records for those whose bills have been paid after the specified date")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of OutstandingClientBalance records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        newest_bill_due_end_date: Annotated[Optional[date], Field(description="Filter OutstandingClientBalance records for the contact's newest bill due date before the specified date")],
        newest_bill_due_start_date: Annotated[Optional[date], Field(description="Filter OutstandingClientBalance records for the contact's newest bill due date after the specified date")],
        originating_attorney_id: Annotated[Optional[StrictInt], Field(description="Filters OutstandingClientBalance records to those with matters that have a matching originating attorney.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        responsible_attorney_id: Annotated[Optional[StrictInt], Field(description="Filter OutstandingClientBalance records to those with matters that have a matching responsible attorney")],
    ) -> OutstandingClientBalanceList:
        """Outlines the parameters, optional and required, used when requesting the data for all OutstandingClientBalances"""
        ...
