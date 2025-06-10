from enum import Enum


class ClioPaymentsPaymentindexState(str, Enum):
    AUTHORIZED = "authorized"
    CANCELED = "canceled"
    COMPLETED = "completed"
    COMPLETED_REQUIRING_ALLOCATION = "completed_requiring_allocation"
    FAILED = "failed"
    PENDING = "pending"
    REQUIRES_CONFIRMATION = "requires_confirmation"
    VOIDED = "voided"

    def __str__(self) -> str:
        return str(self.value)
