from enum import Enum


class ReminderindexSubjectType(str, Enum):
    CALENDAR_ENTRY = "calendar_entry"
    TASK = "task"

    def __str__(self) -> str:
        return str(self.value)
