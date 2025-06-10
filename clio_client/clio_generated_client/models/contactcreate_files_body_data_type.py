from enum import Enum


class ContactcreateFilesBodyDataType(str, Enum):
    COMPANY = "Company"
    PERSON = "Person"

    def __str__(self) -> str:
        return str(self.value)
