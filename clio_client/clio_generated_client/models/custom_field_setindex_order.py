from enum import Enum


class CustomFieldSetindexOrder(str, Enum):
    IDASC = "id(asc)"
    IDDESC = "id(desc)"
    NAMEASC = "name(asc)"
    NAMEDESC = "name(desc)"
    PARENT_TYPEASC = "parent_type(asc)"
    PARENT_TYPEDESC = "parent_type(desc)"

    def __str__(self) -> str:
        return str(self.value)
