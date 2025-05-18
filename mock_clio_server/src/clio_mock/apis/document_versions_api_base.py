# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from clio_mock.models.activity_list import ActivityList


class BaseDocumentVersionsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDocumentVersionsApi.subclasses = BaseDocumentVersionsApi.subclasses + (cls,)
    async def document_version_index(
        self,
        idquery: Annotated[StrictInt, Field(description="The unique identifier for the DocumentVersion.")],
        idpath: Annotated[StrictInt, Field(description="The unique identifier for the Activity.")],
        x_api_versio_nheader: Annotated[Optional[StrictStr], Field(description="The [API minor version](#section/Minor-Versions). Default: latest version.")],
        fieldsquery: Annotated[Optional[StrictStr], Field(description="The fields to be returned. See response samples for what fields are available. For more information see the [fields section](#section/Fields).")],
        fully_uploadedquery: Annotated[Optional[StrictBool], Field(description="Filter DocumentVersion records to those with the given `fully_uploaded` status.")],
        limitquery: Annotated[Optional[StrictInt], Field(description="A limit on the number of Activity records to be returned. Limit can range between 1 and 200. Default: `200`.")],
        page_tokenquery: Annotated[Optional[StrictStr], Field(description="A token specifying which page to return.")],
    ) -> ActivityList:
        """Outlines the parameters, optional and required, used when requesting the data for all DocumentVersions"""
        ...
