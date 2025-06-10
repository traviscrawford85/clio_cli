from enum import Enum


class ReminderupdateDataBodyDataDurationUnit(str, Enum):
    DAYS = "days"
    HOURS = "hours"
    MINUTES = "minutes"
    WEEKS = "weeks"

    def __str__(self) -> str:
        return str(self.value)
