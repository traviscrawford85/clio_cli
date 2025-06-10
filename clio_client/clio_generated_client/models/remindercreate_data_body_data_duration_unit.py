from enum import Enum


class RemindercreateDataBodyDataDurationUnit(str, Enum):
    DAYS = "days"
    HOURS = "hours"
    MINUTES = "minutes"
    WEEKS = "weeks"

    def __str__(self) -> str:
        return str(self.value)
