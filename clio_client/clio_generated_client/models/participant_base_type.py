from enum import Enum


class ParticipantBaseType(str, Enum):
    COMPANY = "Company"
    PERSON = "Person"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
