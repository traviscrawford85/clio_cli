from enum import Enum


class ServiceTypeindexOrder(str, Enum):
    DESCRIPTIONASC = "description(asc)"
    DESCRIPTIONDESC = "description(desc)"
    IDASC = "id(asc)"
    IDDESC = "id(desc)"

    def __str__(self) -> str:
        return str(self.value)
