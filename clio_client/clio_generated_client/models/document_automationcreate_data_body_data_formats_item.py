from enum import Enum


class DocumentAutomationcreateDataBodyDataFormatsItem(str, Enum):
    ORIGINAL = "original"
    PDF = "pdf"

    def __str__(self) -> str:
        return str(self.value)
