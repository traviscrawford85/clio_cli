# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class ConversationBase(BaseModel):
    archived: Optional[bool] = Field(
        None, description="Whether the conversation has been archived"
    )
    created_at: Optional[str] = Field(
        None,
        description="The time the *Conversation* was created (as a ISO-8601 timestamp)",
    )
    current_user_is_member: Optional[bool] = Field(
        None, description="Whether the current user is a member of this conversation"
    )
    etag: Optional[str] = Field(None, description="ETag for the *Conversation*")
    id: Optional[int] = Field(
        None, description="Unique identifier for the *Conversation*"
    )
    message_count: Optional[int] = Field(
        None, description="The number of messages in this conversation"
    )
    read: Optional[bool] = Field(
        None, description="Whether any messages in this conversation have been viewed"
    )
    read_only: Optional[bool] = Field(
        None, description="Whether the conversation is read only"
    )
    subject: Optional[str] = Field(
        None, description="The subject of the *Conversation*"
    )
    time_entries_count: Optional[int] = Field(
        None, description="The number of time entries applied to this conversation"
    )
    updated_at: Optional[str] = Field(
        None,
        description="The time the *Conversation* was last updated (as a ISO-8601 timestamp)",
    )
