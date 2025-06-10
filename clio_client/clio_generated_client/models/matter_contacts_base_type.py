from enum import Enum


class MatterContactsBaseType(str, Enum):
    COMPANY = "Company"
    PERSON = "Person"

    def __str__(self) -> str:
        return str(self.value)
