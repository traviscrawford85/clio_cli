from enum import Enum


class MatterBaseStatus(str, Enum):
    CLOSED = "Closed"
    OPEN = "Open"
    PENDING = "Pending"

    def __str__(self) -> str:
        return str(self.value)
