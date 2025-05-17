# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.matter_contacts_list import MatterContactsList


class BaseMatterContactsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseMatterContactsApi.subclasses = BaseMatterContactsApi.subclasses + (cls,)
    async def matter_contacts_index(
        self,
        matter_id: Annotated[StrictInt, Field(description="Filters contact data by matter.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        custom_field_ids: Annotated[Optional[StrictInt], Field(description="IDs of custom fields to include in results.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of MatterContacts records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the MatterContacts records by the given field. Note that `id` is ordered by the `id` of the nested Relationship record. Default: `is_client(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
    ) -> MatterContactsList:
        """Outlines the parameters, optional and required, used when requesting the data for all MatterContacts"""
        ...
