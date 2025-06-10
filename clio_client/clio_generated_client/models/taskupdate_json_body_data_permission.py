from enum import Enum


class TaskupdateJsonBodyDataPermission(str, Enum):
    PRIVATE = "private"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)
