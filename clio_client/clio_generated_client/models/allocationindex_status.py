from enum import Enum


class AllocationindexStatus(str, Enum):
    INVALID = "invalid"
    VALID = "valid"

    def __str__(self) -> str:
        return str(self.value)
