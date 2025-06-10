from enum import Enum


class CalendarEntryupdateDataBodyDataConferenceMeetingType(str, Enum):
    ZOOM = "zoom"

    def __str__(self) -> str:
        return str(self.value)
