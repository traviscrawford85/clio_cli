# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class CommunicationEmlFileBase(BaseModel):
    id: Optional[int] = Field(
        None, description="Unique identifier for the *CommunicationEmlFile*"
    )
