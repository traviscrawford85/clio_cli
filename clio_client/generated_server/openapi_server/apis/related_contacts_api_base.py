# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Optional
from typing_extensions import Annotated
from openapi_server.models.error import Error
from openapi_server.models.related_contacts_list import RelatedContactsList


class BaseRelatedContactsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseRelatedContactsApi.subclasses = BaseRelatedContactsApi.subclasses + (cls,)
    async def related_contacts_index(
        self,
        matter_id: Annotated[StrictInt, Field(description="Filters RelatedContacts data by matter.")],
        x_api_version: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fields: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        limit: Annotated[Optional[StrictInt], Field(description="A limit on the number of RelatedContacts records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        order: Annotated[Optional[StrictStr], Field(description="Orders the RelatedContacts records by the given field. Note that `id` is ordered by the `id` of the nested Relationship record. Default: `id(asc)`.")],
        page_token: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
    ) -> RelatedContactsList:
        """Outlines the parameters, optional and required, used when requesting the data for all RelatedContacts"""
        ...
