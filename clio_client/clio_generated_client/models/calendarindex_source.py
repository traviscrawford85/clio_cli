from enum import Enum


class CalendarindexSource(str, Enum):
    MOBILE = "mobile"
    WEB = "web"

    def __str__(self) -> str:
        return str(self.value)
