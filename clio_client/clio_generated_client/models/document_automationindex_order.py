from enum import Enum


class DocumentAutomationindexOrder(str, Enum):
    IDASC = "id(asc)"
    IDDESC = "id(desc)"

    def __str__(self) -> str:
        return str(self.value)
