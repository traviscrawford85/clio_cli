from enum import Enum


class CalendarupdateDataBodyDataSource(str, Enum):
    MOBILE = "mobile"
    WEB = "web"

    def __str__(self) -> str:
        return str(self.value)
