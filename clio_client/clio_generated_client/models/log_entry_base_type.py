from enum import Enum


class LogEntryBaseType(str, Enum):
    CONTACTLOGENTRY = "ContactLogEntry"
    MATTERLOGENTRY = "MatterLogEntry"

    def __str__(self) -> str:
        return str(self.value)
