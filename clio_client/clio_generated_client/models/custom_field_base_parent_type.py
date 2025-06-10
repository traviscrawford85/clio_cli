from enum import Enum


class CustomFieldBaseParentType(str, Enum):
    CONTACT = "Contact"
    MATTER = "Matter"

    def __str__(self) -> str:
        return str(self.value)
