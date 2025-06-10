from enum import Enum


class ExpenseCategorycreateJsonBodyDataEntryType(str, Enum):
    HARD_COST = "hard_cost"
    SOFT_COST = "soft_cost"
    UNASSOCIATED = "unassociated"

    def __str__(self) -> str:
        return str(self.value)
