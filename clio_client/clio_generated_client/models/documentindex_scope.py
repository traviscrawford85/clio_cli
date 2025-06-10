from enum import Enum


class DocumentindexScope(str, Enum):
    CHILDREN = "children"
    DESCENDANTS = "descendants"

    def __str__(self) -> str:
        return str(self.value)
