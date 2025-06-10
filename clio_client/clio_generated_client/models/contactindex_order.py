from enum import Enum


class ContactindexOrder(str, Enum):
    IDASC = "id(asc)"
    IDDESC = "id(desc)"
    NAMEASC = "name(asc)"
    NAMEDESC = "name(desc)"
    SHARED_ATASC = "shared_at(asc)"
    SHARED_ATDESC = "shared_at(desc)"

    def __str__(self) -> str:
        return str(self.value)
