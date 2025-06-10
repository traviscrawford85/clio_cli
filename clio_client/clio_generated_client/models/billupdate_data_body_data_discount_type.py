from enum import Enum


class BillupdateDataBodyDataDiscountType(str, Enum):
    MONEY = "money"
    PERCENTAGE = "percentage"

    def __str__(self) -> str:
        return str(self.value)
