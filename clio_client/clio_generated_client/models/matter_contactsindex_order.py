from enum import Enum


class MatterContactsindexOrder(str, Enum):
    IDASC = "id(asc)"
    IDDESC = "id(desc)"
    IS_CLIENTASC = "is_client(asc)"
    IS_CLIENTDESC = "is_client(desc)"

    def __str__(self) -> str:
        return str(self.value)
