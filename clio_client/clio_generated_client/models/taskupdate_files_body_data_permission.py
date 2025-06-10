from enum import Enum


class TaskupdateFilesBodyDataPermission(str, Enum):
    PRIVATE = "private"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)
