from enum import Enum


class LineItemBaseKind(str, Enum):
    EXPENSE = "Expense"
    SERVICE = "Service"

    def __str__(self) -> str:
        return str(self.value)
