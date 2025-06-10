from enum import Enum


class BillupdateJsonBodyDataDiscountType(str, Enum):
    MONEY = "money"
    PERCENTAGE = "percentage"

    def __str__(self) -> str:
        return str(self.value)
