from enum import Enum


class PaymentProfileBaseInterestType(str, Enum):
    COMPOUND = "compound"
    SIMPLE = "simple"

    def __str__(self) -> str:
        return str(self.value)
