# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import date
from pydantic import Field, StrictInt, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.bank_transfer_show import BankTransferShow
from openapi_server.models.error import Error


class BaseBankTransfersApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseBankTransfersApi.subclasses = BaseBankTransfersApi.subclasses + (cls,)
    async def bank_transfer_show(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the BankTransfer.")],
        if_modified_since: Annotated[Optional[date], Field(description="The server will send the requested resource with a 200 status, but only if it has been modified after the given date. (Expects an RFC 2822 timestamp).")],
        if_none_match: Annotated[Optional[StrictStr], Field(description="The server will send the requested resource with a 200 status, but only if the existing resource's [ETag](#section/ETags) doesn't match any of the values listed.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
    ) -> BankTransferShow:
        """Outlines the parameters, optional and required, used when requesting the data for a single BankTransfer"""
        ...
