from enum import Enum


class PaymentBaseSourceFundType(str, Enum):
    CLIENT = "Client"
    MATTER = "Matter"

    def __str__(self) -> str:
        return str(self.value)
