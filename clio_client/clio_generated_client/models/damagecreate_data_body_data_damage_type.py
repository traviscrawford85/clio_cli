from enum import Enum


class DamagecreateDataBodyDataDamageType(str, Enum):
    GENERAL = "general"
    OTHER = "other"
    SPECIAL = "special"

    def __str__(self) -> str:
        return str(self.value)
