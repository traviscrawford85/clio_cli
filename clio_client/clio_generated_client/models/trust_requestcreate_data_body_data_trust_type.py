from enum import Enum


class TrustRequestcreateDataBodyDataTrustType(str, Enum):
    CLIENT = "client"
    MATTER = "matter"

    def __str__(self) -> str:
        return str(self.value)
