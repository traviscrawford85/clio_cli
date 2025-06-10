from enum import Enum


class UtbmsCodeBaseType(str, Enum):
    UTBMSACTIVITY = "UtbmsActivity"
    UTBMSEXPENSE = "UtbmsExpense"
    UTBMSTASK = "UtbmsTask"

    def __str__(self) -> str:
        return str(self.value)
