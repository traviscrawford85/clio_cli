from enum import Enum


class DocumentAutomationcreateJsonBodyDataFormatsItem(str, Enum):
    ORIGINAL = "original"
    PDF = "pdf"

    def __str__(self) -> str:
        return str(self.value)
