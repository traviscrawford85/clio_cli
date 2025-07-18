# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from typing import List, Optional

from clio_clients.models.documentversionbase import DocumentVersionBase
from pydantic import Field
from clio_clients.models.cliocreatorbase import ClioCreatorBase
from clio_clients.models.multipart import Multipart
from clio_clients.models.multipartheaderbase import MultipartHeaderBase


class DocumentVersion(DocumentVersionBase):
    creator: Optional[ClioCreatorBase] = None
    multiparts: Optional[List[Multipart]] = Field(None, description="Multipart")
    put_headers: Optional[List[MultipartHeaderBase]] = Field(
        None, description="MultipartHeader"
    )
