from enum import Enum


class LineItemupdateJsonBodyDataKind(str, Enum):
    EXPENSE = "Expense"
    PRODUCT = "Product"
    SERVICE = "Service"

    def __str__(self) -> str:
        return str(self.value)
