from enum import Enum


class RemindercreateDataBodyDataSubjectType(str, Enum):
    CALENDARENTRY = "CalendarEntry"
    TASK = "Task"

    def __str__(self) -> str:
        return str(self.value)
