from enum import Enum


class ReminderupdateJsonBodyDataDurationUnit(str, Enum):
    DAYS = "days"
    HOURS = "hours"
    MINUTES = "minutes"
    WEEKS = "weeks"

    def __str__(self) -> str:
        return str(self.value)
