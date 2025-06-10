from enum import Enum


class RelatedContactsindexOrder(str, Enum):
    IDASC = "id(asc)"
    IDDESC = "id(desc)"

    def __str__(self) -> str:
        return str(self.value)
