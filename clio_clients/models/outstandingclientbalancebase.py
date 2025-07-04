# generated by datamodel-codegen:
#   filename:  openapi_sdk.yaml

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class OutstandingClientBalanceBase(BaseModel):
    associated_matter_ids: Optional[List[int]] = Field(
        None,
        description="An array of Matter IDs associated with bills in the unpaid state",
    )
    created_at: Optional[str] = Field(
        None,
        description="The time the *OutstandingClientBalance* was created (as a ISO-8601 timestamp)",
    )
    etag: Optional[str] = Field(
        None, description="ETag for the *OutstandingClientBalance*"
    )
    id: Optional[int] = Field(
        None, description="Unique identifier for the *OutstandingClientBalance*"
    )
    last_payment_date: Optional[str] = Field(
        None,
        description="The date the most recent payment from the contact was received",
    )
    last_shared_date: Optional[str] = Field(
        None,
        description="The date of the most recently shared bills through the outstanding balance table",
    )
    newest_issued_bill_due_date: Optional[str] = Field(
        None, description="The due date of the contact's newest bill"
    )
    pending_payments_total: Optional[float] = Field(
        None,
        description="The sum of all online payments in a pending state on the outstanding bills",
    )
    reminders_enabled: Optional[bool] = Field(
        None, description="The status of automated reminders for this client"
    )
    total_outstanding_balance: Optional[float] = Field(
        None, description="The sum of all bills in the unpaid state"
    )
    updated_at: Optional[str] = Field(
        None,
        description="The time the *OutstandingClientBalance* was last updated (as a ISO-8601 timestamp)",
    )
