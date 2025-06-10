from enum import Enum


class BankAccountcreateDataBodyDataType(str, Enum):
    OPERATING = "Operating"
    TRUST = "Trust"

    def __str__(self) -> str:
        return str(self.value)
