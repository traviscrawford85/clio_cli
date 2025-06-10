from enum import Enum


class NoteindexOrder(str, Enum):
    AUTHORASC = "author(asc)"
    AUTHORDESC = "author(desc)"
    DATEASC = "date(asc)"
    DATEDESC = "date(desc)"
    IDASC = "id(asc)"
    IDDESC = "id(desc)"
    UPDATED_ATASC = "updated_at(asc)"
    UPDATED_ATDESC = "updated_at(desc)"

    def __str__(self) -> str:
        return str(self.value)
