# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from datetime import datetime
from pydantic import Field, StrictInt, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.interest_charge_list import InterestChargeList


class BaseInterestChargesApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseInterestChargesApi.subclasses = BaseInterestChargesApi.subclasses + (cls,)
    async def interest_charge_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the InterestCharge.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single InterestCharge"""
        ...


    async def interest_charge_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        bill_id: Annotated[Optional[StrictInt], Field(description="The unique identifier for a single Bill. The keyword `null` is not valid for this field. The list will be filtered to include only the InterestCharge records with the matching property.")],
        created_since: Annotated[Optional[datetime], Field(description="Filter InterestCharge records to those having the `created_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
        exclude_ids: Annotated[Optional[StrictInt], Field(description="Array containing *InterestCharge* identifiers that should be excluded from the query.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        ids: Annotated[Optional[StrictInt], Field(description="Filter InterestCharge records to those having the specified unique identifiers.")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of InterestCharge records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
        updated_since: Annotated[Optional[datetime], Field(description="Filter InterestCharge records to those having the `updated_at` field after a specific time. (Expects an ISO-8601 timestamp).")],
    ) -> InterestChargeList:
        """Outlines the parameters, optional and required, used when requesting the data for all InterestCharges"""
        ...
