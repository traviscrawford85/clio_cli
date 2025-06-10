from enum import Enum


class NotecreateDataBodyDataType(str, Enum):
    CONTACT = "Contact"
    MATTER = "Matter"

    def __str__(self) -> str:
        return str(self.value)
