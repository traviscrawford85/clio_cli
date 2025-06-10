from enum import Enum


class CalendarcreateFilesBodyDataSource(str, Enum):
    MOBILE = "mobile"
    WEB = "web"

    def __str__(self) -> str:
        return str(self.value)
