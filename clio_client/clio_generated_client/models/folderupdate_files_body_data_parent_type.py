from enum import Enum


class FolderupdateFilesBodyDataParentType(str, Enum):
    CONTACT = "Contact"
    FOLDER = "Folder"
    MATTER = "Matter"

    def __str__(self) -> str:
        return str(self.value)
