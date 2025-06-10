from enum import Enum


class TaskindexAssigneeType(str, Enum):
    CONTACT = "contact"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
