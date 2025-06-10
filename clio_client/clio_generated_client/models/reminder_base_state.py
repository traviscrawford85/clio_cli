from enum import Enum


class ReminderBaseState(str, Enum):
    ATTEMPTING_DELIVERY = "attempting_delivery"
    DELIVERED = "delivered"
    DELIVERY_FAILED = "delivery_failed"
    DELIVERY_SKIPPED = "delivery_skipped"
    INITIALIZING = "initializing"
    INVALID_USER = "invalid_user"
    RESCHEDULING = "rescheduling"
    SCHEDULED = "scheduled"
    SCHEDULING = "scheduling"

    def __str__(self) -> str:
        return str(self.value)
