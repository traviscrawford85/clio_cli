from enum import Enum


class CalendarEntrycreateJsonBodyDataDeleted(str, Enum):
    FUTURE = "future"
    SINGLE = "single"

    def __str__(self) -> str:
        return str(self.value)
