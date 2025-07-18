# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field
from clio_clients.models.type.type15 import Type15


class InterestBase(BaseModel):
    balance: Optional[float] = Field(
        None, description="Interest balance for the object"
    )
    period: Optional[int] = Field(
        None,
        description="Number of days that represent the frequency which your *Interest%* will be applied",
    )
    rate: Optional[float] = Field(None, description="Rate for the *Interest%*")
    total: Optional[float] = Field(None, description="Interest total for the object")
    type: Optional[Type15] = Field(
        None, description="Type of *Interest%* being applied"
    )
