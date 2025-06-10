from enum import Enum


class BillindexStatus(str, Enum):
    ALL = "all"
    OVERDUE = "overdue"

    def __str__(self) -> str:
        return str(self.value)
