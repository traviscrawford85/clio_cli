from enum import Enum


class ClientBaseType(str, Enum):
    COMPANY = "Company"
    PERSON = "Person"

    def __str__(self) -> str:
        return str(self.value)
