from enum import Enum


class CustomFieldcreateJsonBodyDataParentType(str, Enum):
    CONTACT = "Contact"
    MATTER = "Matter"

    def __str__(self) -> str:
        return str(self.value)
