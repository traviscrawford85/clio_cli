from enum import Enum


class RemindercreateJsonBodyDataSubjectType(str, Enum):
    CALENDARENTRY = "CalendarEntry"
    TASK = "Task"

    def __str__(self) -> str:
        return str(self.value)
