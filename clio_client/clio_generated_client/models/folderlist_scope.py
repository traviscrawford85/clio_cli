from enum import Enum


class FolderlistScope(str, Enum):
    CHILDREN = "children"
    DESCENDANTS = "descendants"

    def __str__(self) -> str:
        return str(self.value)
