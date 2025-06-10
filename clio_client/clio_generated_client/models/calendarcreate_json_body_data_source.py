from enum import Enum


class CalendarcreateJsonBodyDataSource(str, Enum):
    MOBILE = "mobile"
    WEB = "web"

    def __str__(self) -> str:
        return str(self.value)
