from enum import Enum


class TaskupdateJsonBodyDataAssigneeType(str, Enum):
    CONTACT = "Contact"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
