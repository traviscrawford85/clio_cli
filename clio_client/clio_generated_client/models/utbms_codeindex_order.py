from enum import Enum


class UtbmsCodeindexOrder(str, Enum):
    IDASC = "id(asc)"
    IDDESC = "id(desc)"
    NAMEASC = "name(asc)"
    NAMEDESC = "name(desc)"
    SETASC = "set(asc)"
    SETDESC = "set(desc)"

    def __str__(self) -> str:
        return str(self.value)
