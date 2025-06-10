from enum import Enum


class CalendarBaseType(str, Enum):
    ACCOUNTCALENDAR = "AccountCalendar"
    ADHOCCALENDAR = "AdhocCalendar"
    USERCALENDAR = "UserCalendar"

    def __str__(self) -> str:
        return str(self.value)
