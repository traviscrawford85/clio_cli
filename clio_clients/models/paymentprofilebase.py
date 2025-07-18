# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field
from clio_clients.models.interesttype import InterestType


class PaymentProfileBase(BaseModel):
    billing_setting_id: Optional[int] = Field(
        None, description="The unique identifier for the *PaymentProfile"
    )
    created_at: Optional[str] = Field(
        None,
        description="The time the *PaymentProfile* was created (as a ISO-8601 timestamp)",
    )
    discount_period: Optional[int] = Field(
        None, description="The early payment discount period for the *PaymentProfile"
    )
    discount_rate: Optional[float] = Field(
        None, description="The early payment discount rate for the *PaymentProfile"
    )
    etag: Optional[str] = Field(None, description="ETag for the *PaymentProfile*")
    id: Optional[int] = Field(
        None, description="Unique identifier for the *PaymentProfile*"
    )
    interest_period: Optional[int] = Field(
        None, description="The interest period interval for the *PaymentProfile"
    )
    interest_rate: Optional[float] = Field(
        None, description="The interest rate for the *PaymentProfile"
    )
    interest_type: Optional[InterestType] = Field(
        None,
        description="The type of interest to be calculated for the *PaymentProfile (Simple or Compound)",
    )
    name: Optional[str] = Field(None, description="The name of the *PaymentProfile")
    terms: Optional[int] = Field(
        None, description="The total grace period for the *PaymentProfile"
    )
    updated_at: Optional[str] = Field(
        None,
        description="The time the *PaymentProfile* was last updated (as a ISO-8601 timestamp)",
    )
