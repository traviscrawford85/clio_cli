from enum import Enum


class CustomFieldindexOrder(str, Enum):
    DISPLAY_ORDERASC = "display_order(asc)"
    DISPLAY_ORDERDESC = "display_order(desc)"
    IDASC = "id(asc)"
    IDDESC = "id(desc)"
    NAMEASC = "name(asc)"
    NAMEDESC = "name(desc)"

    def __str__(self) -> str:
        return str(self.value)
