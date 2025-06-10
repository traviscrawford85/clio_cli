from enum import Enum


class CustomFieldcreateFilesBodyDataParentType(str, Enum):
    CONTACT = "Contact"
    MATTER = "Matter"

    def __str__(self) -> str:
        return str(self.value)
