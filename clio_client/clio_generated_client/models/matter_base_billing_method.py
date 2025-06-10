from enum import Enum


class MatterBaseBillingMethod(str, Enum):
    CONTINGENCY = "contingency"
    FLAT = "flat"
    HOURLY = "hourly"

    def __str__(self) -> str:
        return str(self.value)
