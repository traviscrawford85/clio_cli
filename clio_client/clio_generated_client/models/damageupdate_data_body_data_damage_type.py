from enum import Enum


class DamageupdateDataBodyDataDamageType(str, Enum):
    GENERAL = "general"
    OTHER = "other"
    SPECIAL = "special"

    def __str__(self) -> str:
        return str(self.value)
