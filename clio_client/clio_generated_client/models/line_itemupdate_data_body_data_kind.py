from enum import Enum


class LineItemupdateDataBodyDataKind(str, Enum):
    EXPENSE = "Expense"
    PRODUCT = "Product"
    SERVICE = "Service"

    def __str__(self) -> str:
        return str(self.value)
