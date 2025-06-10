from enum import Enum


class MatterindexCloseDate(str, Enum):
    VALUE_0 = ">DATE"
    VALUE_1 = ">=DATE"
    VALUE_2 = "=DATE"
    VALUE_3 = "<=DATE"
    VALUE_4 = "<DATE"

    def __str__(self) -> str:
        return str(self.value)
