from enum import Enum


class AttendeeBaseType(str, Enum):
    CALENDAR = "Calendar"
    CONTACT = "Contact"

    def __str__(self) -> str:
        return str(self.value)
