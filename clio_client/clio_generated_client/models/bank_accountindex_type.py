from enum import Enum


class BankAccountindexType(str, Enum):
    OPERATINGACCOUNT = "OperatingAccount"
    TRUSTACCOUNT = "TrustAccount"

    def __str__(self) -> str:
        return str(self.value)
