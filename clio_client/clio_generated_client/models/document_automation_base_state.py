from enum import Enum


class DocumentAutomationBaseState(str, Enum):
    COMPLETED = "completed"
    EMPTY = "empty"
    FAILED = "failed"
    IN_PROGRESS = "in_progress"
    NOT_STARTED = "not_started"
    QUEUED = "queued"

    def __str__(self) -> str:
        return str(self.value)
