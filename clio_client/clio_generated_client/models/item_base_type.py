from enum import Enum


class ItemBaseType(str, Enum):
    DOCUMENT = "Document"
    FOLDER = "Folder"

    def __str__(self) -> str:
        return str(self.value)
