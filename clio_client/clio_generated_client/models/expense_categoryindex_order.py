from enum import Enum


class ExpenseCategoryindexOrder(str, Enum):
    ENTRY_TYPEASC = "entry_type(asc)"
    ENTRY_TYPEDESC = "entry_type(desc)"
    IDASC = "id(asc)"
    IDDESC = "id(desc)"
    NAMEASC = "name(asc)"
    NAMEDESC = "name(desc)"
    RATEASC = "rate(asc)"
    RATEDESC = "rate(desc)"

    def __str__(self) -> str:
        return str(self.value)
