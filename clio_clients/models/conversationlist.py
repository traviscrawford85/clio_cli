# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field
from clio_clients.models.conversation import Conversation


class ConversationList(BaseModel):
    data: List[Conversation] = Field(..., description="Conversation List Response")
