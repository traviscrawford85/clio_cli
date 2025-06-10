from enum import Enum


class ActivityDescriptionindexType(str, Enum):
    CLIO = "clio"
    UTBMS = "utbms"

    def __str__(self) -> str:
        return str(self.value)
