from enum import Enum


class AllocationindexOrder(str, Enum):
    DATEASC = "date(asc)"
    DATEDESC = "date(desc)"
    IDASC = "id(asc)"
    IDDESC = "id(desc)"

    def __str__(self) -> str:
        return str(self.value)
