# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictInt, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.my_event_list import MyEventList
from openapi_server.models.my_event_show import MyEventShow
from openapi_server.models.my_event_update_request import MyEventUpdateRequest


class BaseMyEventsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseMyEventsApi.subclasses = BaseMyEventsApi.subclasses + (cls,)
    async def my_event_destroy(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the MyEvent.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
    ) -> None:
        """Outlines the parameters, optional and required, used when deleting the record for a single MyEvent"""
        ...


    async def my_event_index(
        self,
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of MyEvent records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
    ) -> MyEventList:
        """Outlines the parameters, optional and required, used when requesting the data for all MyEvents"""
        ...


    async def my_event_update(
        self,
        id: Annotated[StrictInt, Field(description="The unique identifier for the MyEvent.")],
        if_match: Annotated[Optional[StrictStr], Field(description="The server will update the requested resource and send back a 200 status, but only if value in the header matches the existing resource's [ETag](#section/ETags).")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        my_event_update_request: Annotated[Optional[MyEventUpdateRequest], Field(description="Request Body for My Events")],
    ) -> MyEventShow:
        """Outlines the parameters and data fields used when updating a single MyEvent"""
        ...
