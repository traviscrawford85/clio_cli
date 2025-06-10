from enum import Enum


class FolderindexScope(str, Enum):
    CHILDREN = "children"
    DESCENDANTS = "descendants"

    def __str__(self) -> str:
        return str(self.value)
