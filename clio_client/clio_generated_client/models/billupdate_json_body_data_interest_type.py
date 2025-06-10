from enum import Enum


class BillupdateJsonBodyDataInterestType(str, Enum):
    COMPOUND = "compound"
    SIMPLE = "simple"

    def __str__(self) -> str:
        return str(self.value)
