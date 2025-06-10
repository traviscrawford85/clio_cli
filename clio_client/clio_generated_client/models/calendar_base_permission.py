from enum import Enum


class CalendarBasePermission(str, Enum):
    EDITOR = "editor"
    LIMITED_VIEWER = "limited_viewer"
    NONE = "none"
    OWNER = "owner"
    VIEWER = "viewer"

    def __str__(self) -> str:
        return str(self.value)
