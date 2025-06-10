from enum import Enum


class GroupindexOrder(str, Enum):
    IDASC = "id(asc)"
    IDDESC = "id(desc)"
    NAMEASC = "name(asc)"
    NAMEDESC = "name(desc)"

    def __str__(self) -> str:
        return str(self.value)
