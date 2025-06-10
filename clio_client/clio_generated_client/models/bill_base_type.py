from enum import Enum


class BillBaseType(str, Enum):
    CLIENTBILL = "ClientBill"
    MATTERBILL = "MatterBill"

    def __str__(self) -> str:
        return str(self.value)
