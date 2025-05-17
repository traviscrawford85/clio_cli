# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.trust_request_create_request import TrustRequestCreateRequest
from openapi_server.models.trust_request_show import TrustRequestShow


class BaseTrustRequestsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseTrustRequestsApi.subclasses = BaseTrustRequestsApi.subclasses + (cls,)
    async def trust_request_create(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        trust_request_create_request: Annotated[Optional[TrustRequestCreateRequest], Field(description="Request Body for Trust Requests")],
    ) -> TrustRequestShow:
        """Outlines the parameters and data fields used when creating a new TrustRequest"""
        ...
