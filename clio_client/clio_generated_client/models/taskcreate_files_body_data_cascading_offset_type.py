from enum import Enum


class TaskcreateFilesBodyDataCascadingOffsetType(str, Enum):
    AFTER = "After"
    BEFORE = "Before"

    def __str__(self) -> str:
        return str(self.value)
