from enum import Enum


class LogEntryindexOrder(str, Enum):
    ACCESSED_ATASC = "accessed_at(asc)"
    ACCESSED_ATDESC = "accessed_at(desc)"
    IDASC = "id(asc)"
    IDDESC = "id(desc)"

    def __str__(self) -> str:
        return str(self.value)
