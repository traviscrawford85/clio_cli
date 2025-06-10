from enum import Enum


class DocumentAutomationcreateFilesBodyDataFormatsItem(str, Enum):
    ORIGINAL = "original"
    PDF = "pdf"

    def __str__(self) -> str:
        return str(self.value)
