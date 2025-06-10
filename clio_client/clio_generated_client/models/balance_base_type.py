from enum import Enum


class BalanceBaseType(str, Enum):
    CLIENT = "Client"
    MATTER = "Matter"

    def __str__(self) -> str:
        return str(self.value)
