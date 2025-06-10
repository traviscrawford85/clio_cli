from enum import Enum


class DocumentCategoryindexQuery(str, Enum):
    NAME = "name"

    def __str__(self) -> str:
        return str(self.value)
