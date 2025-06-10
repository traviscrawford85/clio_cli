from enum import Enum


class TaskcreateDataBodyDataCascadingOffsetType(str, Enum):
    AFTER = "After"
    BEFORE = "Before"

    def __str__(self) -> str:
        return str(self.value)
