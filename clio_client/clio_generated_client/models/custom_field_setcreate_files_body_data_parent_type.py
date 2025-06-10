from enum import Enum


class CustomFieldSetcreateFilesBodyDataParentType(str, Enum):
    CONTACT = "Contact"
    MATTER = "Matter"

    def __str__(self) -> str:
        return str(self.value)
