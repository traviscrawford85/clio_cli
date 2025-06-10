from enum import Enum


class MatterDocketindexStatus(str, Enum):
    COMPLETED = "completed"
    FAILED = "failed,"
    IN_PROGRESS = "in_progress,"
    NOT_STARTED = "not_started,"

    def __str__(self) -> str:
        return str(self.value)
