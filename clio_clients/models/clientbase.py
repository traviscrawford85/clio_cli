# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field
from clio_clients.models.type.type7 import Type7


class ClientBase(BaseModel):
    client_connect_user_id: Optional[int] = Field(
        None, description="The client connect ID of the contacts associated user"
    )
    created_at: Optional[str] = Field(
        None, description="The time the *Client* was created (as a ISO-8601 timestamp)"
    )
    date_of_birth: Optional[str] = Field(None, description="Date of Birth")
    first_name: Optional[str] = Field(None, description="First name of the Person")
    id: Optional[int] = Field(None, description="Unique identifier for the *Client*")
    initials: Optional[str] = Field(None, description="The initials of the *Client*")
    is_matter_client: Optional[bool] = Field(
        None, description="Whether or not the Client is also the client of the matter"
    )
    last_name: Optional[str] = Field(None, description="Last name of the Person")
    middle_name: Optional[str] = Field(None, description="Middle name of the Person")
    name: Optional[str] = Field(None, description="The full name of the *Client*")
    prefix: Optional[str] = Field(
        None, description="The prefix of the *Client* (Mr, Mrs, etc)"
    )
    primary_email_address: Optional[str] = Field(
        None, description="The primary email address of client"
    )
    primary_phone_number: Optional[str] = Field(
        None, description="The primary phone number of client"
    )
    title: Optional[str] = Field(
        None, description="The designated title of the *Client*"
    )
    type: Optional[Type7] = Field(None, description="The type of the *Client*")
    updated_at: Optional[str] = Field(
        None,
        description="The time the *Client* was last updated (as a ISO-8601 timestamp)",
    )
