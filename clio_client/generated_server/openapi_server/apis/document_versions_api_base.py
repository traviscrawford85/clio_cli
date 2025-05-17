# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Optional
from fastapi import Query, Path, Header
from typing_extensions import Annotated
from openapi_server.models.document_version_list import DocumentVersionList
from openapi_server.models.error import Error


class BaseDocumentVersionsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDocumentVersionsApi.subclasses = BaseDocumentVersionsApi.subclasses + (cls,)
async def document_version_index(
    document_version_id: Annotated[StrictInt, Query(description="The unique identifier for the DocumentVersion.", alias="id")] = ...,
    document_id: Annotated[StrictInt, Path(description="ID of the Document")] = ...,
    x_api_version: Annotated[Optional[StrictStr], Header(description="The [API minor version](#section/Minor-Versions). Default: latest version.")] = None,
    fields: Annotated[Optional[StrictStr], Query(description="The fields to be returned. See response samples for what fields are available.", alias="fields")] = None,
    fully_uploaded: Annotated[Optional[StrictBool], Query(description="Filter DocumentVersion records to those with the given `fully_uploaded` status.", alias="fully_uploaded")] = None,
    limit: Annotated[Optional[StrictInt], Query(description="A limit on the number of DocumentVersion records to be returned.", alias="limit")] = None,
    page_token: Annotated[Optional[StrictStr], Query(description="A token specifying which page to return.", alias="page_token")] = None,
) -> DocumentVersionList:
    # Your function logic

        """Outlines the parameters, optional and required, used when requesting the data for all DocumentVersions"""
        ...
