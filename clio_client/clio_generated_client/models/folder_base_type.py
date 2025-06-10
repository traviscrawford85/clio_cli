from enum import Enum


class FolderBaseType(str, Enum):
    FOLDER = "Folder"

    def __str__(self) -> str:
        return str(self.value)
