from enum import Enum


class ActivitycreateDataBodyDataType(str, Enum):
    EXPENSEENTRY = "ExpenseEntry"
    HARDCOSTENTRY = "HardCostEntry"
    SOFTCOSTENTRY = "SoftCostEntry"
    TIMEENTRY = "TimeEntry"

    def __str__(self) -> str:
        return str(self.value)
