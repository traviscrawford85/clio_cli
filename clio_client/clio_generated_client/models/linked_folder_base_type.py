from enum import Enum


class LinkedFolderBaseType(str, Enum):
    FOLDER = "Folder"

    def __str__(self) -> str:
        return str(self.value)
