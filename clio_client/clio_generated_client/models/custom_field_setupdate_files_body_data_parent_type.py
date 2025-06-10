from enum import Enum


class CustomFieldSetupdateFilesBodyDataParentType(str, Enum):
    CONTACT = "Contact"
    MATTER = "Matter"

    def __str__(self) -> str:
        return str(self.value)
