from enum import Enum


class DocumentupdateDataBodyDataParentType(str, Enum):
    CONTACT = "Contact"
    DOCUMENT = "Document"
    FOLDER = "Folder"
    MATTER = "Matter"

    def __str__(self) -> str:
        return str(self.value)
