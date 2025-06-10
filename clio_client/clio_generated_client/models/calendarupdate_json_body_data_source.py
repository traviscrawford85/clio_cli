from enum import Enum


class CalendarupdateJsonBodyDataSource(str, Enum):
    MOBILE = "mobile"
    WEB = "web"

    def __str__(self) -> str:
        return str(self.value)
