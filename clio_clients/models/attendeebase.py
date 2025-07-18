# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field
from clio_clients.models.type.type2 import Type2


class AttendeeBase(BaseModel):
    created_at: Optional[str] = Field(
        None,
        description="The time the *Attendee* was created (as a ISO-8601 timestamp)",
    )
    email: Optional[str] = Field(
        None,
        description="If the Attendee is a User, this is the User's email. If the Attendee is a contact, this is the Contact's primary email address.",
    )
    enabled: Optional[bool] = Field(
        None,
        description="If the Attendee is a user, represents whether the user is enabled or disabled. Returns null if attendee is a Contact.",
    )
    etag: Optional[str] = Field(None, description="ETag for the *Attendee*")
    id: Optional[int] = Field(None, description="Unique identifier for the *Attendee*")
    name: Optional[str] = Field(None, description="The name of the *Attendee*")
    type: Optional[Type2] = Field(None, description="The class name of the *Attendee*")
    updated_at: Optional[str] = Field(
        None,
        description="The time the *Attendee* was last updated (as a ISO-8601 timestamp)",
    )
