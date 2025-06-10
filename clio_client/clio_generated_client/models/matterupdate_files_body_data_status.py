from enum import Enum


class MatterupdateFilesBodyDataStatus(str, Enum):
    CLOSED = "closed"
    OPEN = "open"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
