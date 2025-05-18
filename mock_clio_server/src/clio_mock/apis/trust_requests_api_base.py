# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Optional
from typing_extensions import Annotated
from clio_mock.models.activity_show import ActivityShow
from clio_mock.models.trust_request_create_request import TrustRequestCreateRequest


class BaseTrustRequestsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseTrustRequestsApi.subclasses = BaseTrustRequestsApi.subclasses + (cls,)
    async def trust_request_create(
        self,
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        trust_request_create_request: Annotated[Optional[TrustRequestCreateRequest], Field(description="Request Body for Trust Requests")],
    ) -> ActivityShow:
        """Outlines the parameters and data fields used when creating a new TrustRequest"""
        ...
