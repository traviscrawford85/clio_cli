# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field
from clio_clients.models.type.type20 import Type20


class MatterContactsBase(BaseModel):
    client_connect_user_id: Optional[int] = Field(
        None, description="The client connect ID of the contacts associated user"
    )
    contact_created_at: Optional[str] = Field(
        None, description="Timestamp of the time the contact was created"
    )
    contact_updated_at: Optional[str] = Field(
        None, description="Timestamp of the time the contact was created"
    )
    created_at: Optional[str] = Field(
        None,
        description="The time the *MatterContacts* was created (as a ISO-8601 timestamp)",
    )
    description: Optional[str] = Field(None, description="Description of the matter")
    etag: Optional[str] = Field(None, description="ETag for the *MatterContacts*")
    first_name: Optional[str] = Field(None, description="First name of the Person")
    id: Optional[int] = Field(
        None, description="Unique identifier for the *MatterContacts*"
    )
    initials: Optional[str] = Field(
        None, description="The initials of the *MatterContacts*"
    )
    is_client: Optional[bool] = Field(
        None, description="Whether or not the MatterContacts is a client"
    )
    last_name: Optional[str] = Field(None, description="Last name of the Person")
    matter_id: Optional[int] = Field(None, description="ID of the matter")
    matter_number: Optional[str] = Field(None, description="Number of the matter")
    middle_name: Optional[str] = Field(None, description="Middle name of the Person")
    name: Optional[str] = Field(
        None, description="The full name of the *MatterContacts*"
    )
    prefix: Optional[str] = Field(
        None, description="The prefix of the *MatterContacts* (Mr, Mrs, etc)"
    )
    primary_email_address: Optional[str] = Field(
        None,
        description="The primary email address associated with this *MatterContacts*.",
    )
    primary_phone_number: Optional[str] = Field(
        None,
        description="The primary phone number associated with this *MatterContacts*.",
    )
    relationship_name: Optional[str] = Field(
        None,
        description='The description of the relation between the contact and the matter, or "Client" if the user is the client.',
    )
    secondary_email_address: Optional[str] = Field(
        None, description="The secondary email address of the contact"
    )
    secondary_phone_number: Optional[str] = Field(
        None, description="The secondary phone number of the contact"
    )
    title: Optional[str] = Field(
        None, description="The designated title of the *MatterContacts*"
    )
    type: Optional[Type20] = Field(None, description="The type of the *MatterContacts*")
    updated_at: Optional[str] = Field(
        None,
        description="The time the *MatterContacts* was last updated (as a ISO-8601 timestamp)",
    )
