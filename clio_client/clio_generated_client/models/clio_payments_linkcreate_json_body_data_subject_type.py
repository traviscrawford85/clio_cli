from enum import Enum


class ClioPaymentsLinkcreateJsonBodyDataSubjectType(str, Enum):
    BANKACCOUNT = "BankAccount"
    BILL = "Bill"
    CONTACT = "Contact"

    def __str__(self) -> str:
        return str(self.value)
