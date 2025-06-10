from enum import Enum


class CustomFieldindexParentType(str, Enum):
    CONTACT = "contact"
    MATTER = "matter"

    def __str__(self) -> str:
        return str(self.value)
