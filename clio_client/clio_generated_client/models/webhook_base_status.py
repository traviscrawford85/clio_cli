from enum import Enum


class WebhookBaseStatus(str, Enum):
    ENABLED = "enabled"
    PENDING = "pending"
    SUSPENDED = "suspended"

    def __str__(self) -> str:
        return str(self.value)
