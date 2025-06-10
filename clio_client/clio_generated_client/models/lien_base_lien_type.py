from enum import Enum


class LienBaseLienType(str, Enum):
    GENERAL = "general"
    MEDICAL_PAYER = "medical_payer"
    MEDICAL_PROVIDER = "medical_provider"

    def __str__(self) -> str:
        return str(self.value)
