from enum import Enum


class MattercreateJsonBodyDataStatuteOfLimitationsStatus(str, Enum):
    COMPLETE = "complete"
    IN_PROGRESS = "in_progress"
    IN_REVIEW = "in_review"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
