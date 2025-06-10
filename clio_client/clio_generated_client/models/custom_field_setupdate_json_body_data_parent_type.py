from enum import Enum


class CustomFieldSetupdateJsonBodyDataParentType(str, Enum):
    CONTACT = "Contact"
    MATTER = "Matter"

    def __str__(self) -> str:
        return str(self.value)
