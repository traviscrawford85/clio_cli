from enum import Enum


class MatterupdateDataBodyDataStatus(str, Enum):
    CLOSED = "closed"
    OPEN = "open"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
