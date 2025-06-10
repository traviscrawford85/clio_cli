from enum import Enum


class DocumentAutomationBaseExportFormats(str, Enum):
    ORIGINAL = "original"
    PDF = "pdf"

    def __str__(self) -> str:
        return str(self.value)
