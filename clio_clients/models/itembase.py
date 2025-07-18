# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field
from clio_clients.models.type.type16 import Type16


class ItemBase(BaseModel):
    created_at: Optional[str] = Field(
        None, description="The time the *Item* was created (as a ISO-8601 timestamp)"
    )
    deleted_at: Optional[str] = Field(
        None, description="The time the *Item* was deleted (as a ISO-8601 timestamp)"
    )
    etag: Optional[str] = Field(None, description="ETag for the *Item*")
    id: Optional[int] = Field(None, description="Unique identifier for the *Item*")
    locked: Optional[bool] = Field(
        None,
        description="Whether or not the Item is locked. Locked Item cannot be modified",
    )
    name: Optional[str] = Field(None, description="The name of the Item")
    type: Optional[Type16] = Field(None, description="The type of the *Item*")
    updated_at: Optional[str] = Field(
        None,
        description="The time the *Item* was last updated (as a ISO-8601 timestamp)",
    )
