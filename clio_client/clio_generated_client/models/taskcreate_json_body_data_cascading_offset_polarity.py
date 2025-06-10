from enum import Enum


class TaskcreateJsonBodyDataCascadingOffsetPolarity(str, Enum):
    BUSINESSDAYS = "BusinessDays"
    CALENDARDAYS = "CalendarDays"
    CALENDARMONTHS = "CalendarMonths"
    CALENDARWEEKS = "CalendarWeeks"
    CALENDARYEARS = "CalendarYears"

    def __str__(self) -> str:
        return str(self.value)
