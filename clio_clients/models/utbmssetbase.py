# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class UtbmsSetBase(BaseModel):
    created_at: Optional[str] = Field(
        None,
        description="The time the *UtbmsSet* was created (as a ISO-8601 timestamp)",
    )
    enabled: Optional[bool] = Field(
        None, description="Whether the *UtbmsSet* is enabled for the current account."
    )
    etag: Optional[str] = Field(None, description="ETag for the *UtbmsSet*")
    id: Optional[int] = Field(None, description="Unique identifier for the *UtbmsSet*")
    name: Optional[str] = Field(None, description="The name of the *UtbmsSet*")
    updated_at: Optional[str] = Field(
        None,
        description="The time the *UtbmsSet* was last updated (as a ISO-8601 timestamp)",
    )
