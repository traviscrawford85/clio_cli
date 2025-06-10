from enum import Enum


class InterestBaseType(str, Enum):
    COMPOUND = "compound"
    SIMPLE = "simple"

    def __str__(self) -> str:
        return str(self.value)
