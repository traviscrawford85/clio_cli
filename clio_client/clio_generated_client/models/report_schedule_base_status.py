from enum import Enum


class ReportScheduleBaseStatus(str, Enum):
    COMPLETED = "completed"
    FAILED = "failed"
    INITIAL = "initial"
    PROCESSING = "processing"
    QUEUED = "queued"

    def __str__(self) -> str:
        return str(self.value)
