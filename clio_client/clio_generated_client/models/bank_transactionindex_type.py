from enum import Enum


class BankTransactionindexType(str, Enum):
    ASSET = "asset"
    LIABILITY = "liability"

    def __str__(self) -> str:
        return str(self.value)
