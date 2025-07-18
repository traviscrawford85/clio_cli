# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field
from clio_clients.models.cliopaymentslink import ClioPaymentsLink


class ClioPaymentsLinkList(BaseModel):
    data: List[ClioPaymentsLink] = Field(
        ..., description="ClioPaymentsLink List Response"
    )
