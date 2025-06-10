from enum import Enum


class CalendarEntryupdateFilesBodyDataConferenceMeetingType(str, Enum):
    ZOOM = "zoom"

    def __str__(self) -> str:
        return str(self.value)
