from enum import Enum


class BillupdateFilesBodyDataDiscountType(str, Enum):
    MONEY = "money"
    PERCENTAGE = "percentage"

    def __str__(self) -> str:
        return str(self.value)
