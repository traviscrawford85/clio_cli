from enum import Enum


class DamageupdateFilesBodyDataDamageType(str, Enum):
    GENERAL = "general"
    OTHER = "other"
    SPECIAL = "special"

    def __str__(self) -> str:
        return str(self.value)
