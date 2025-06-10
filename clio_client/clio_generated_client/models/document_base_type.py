from enum import Enum


class DocumentBaseType(str, Enum):
    DOCUMENT = "Document"

    def __str__(self) -> str:
        return str(self.value)
