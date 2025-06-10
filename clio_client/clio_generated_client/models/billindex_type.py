from enum import Enum


class BillindexType(str, Enum):
    REVENUE = "revenue"
    TRUST = "trust"

    def __str__(self) -> str:
        return str(self.value)
