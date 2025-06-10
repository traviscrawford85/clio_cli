from enum import Enum


class WebhookBaseEventsItem(str, Enum):
    CREATED = "created"
    DELETED = "deleted"
    MATTER_CLOSED = "matter_closed"
    MATTER_OPENED = "matter_opened"
    MATTER_PENDED = "matter_pended"
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
