from enum import Enum


class PracticeAreaindexOrder(str, Enum):
    CATEGORYASC = "category(asc)"
    CATEGORYDESC = "category(desc)"
    CODEASC = "code(asc)"
    CODEDESC = "code(desc)"
    IDASC = "id(asc)"
    IDDESC = "id(desc)"
    NAMEASC = "name(asc)"
    NAMEDESC = "name(desc)"

    def __str__(self) -> str:
        return str(self.value)
