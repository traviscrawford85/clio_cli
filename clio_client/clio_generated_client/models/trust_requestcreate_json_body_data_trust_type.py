from enum import Enum


class TrustRequestcreateJsonBodyDataTrustType(str, Enum):
    CLIENT = "client"
    MATTER = "matter"

    def __str__(self) -> str:
        return str(self.value)
