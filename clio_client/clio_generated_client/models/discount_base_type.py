from enum import Enum


class DiscountBaseType(str, Enum):
    MONEY = "money"
    PERCENTAGE = "percentage"

    def __str__(self) -> str:
        return str(self.value)
