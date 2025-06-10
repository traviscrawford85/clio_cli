from enum import Enum


class ActivityupdateDataBodyDataType(str, Enum):
    EXPENSEENTRY = "ExpenseEntry"
    HARDCOSTENTRY = "HardCostEntry"
    SOFTCOSTENTRY = "SoftCostEntry"
    TIMEENTRY = "TimeEntry"

    def __str__(self) -> str:
        return str(self.value)
