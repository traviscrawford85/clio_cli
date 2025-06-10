from enum import Enum


class ActivityDescriptionRateBaseType(str, Enum):
    CUSTOM = "Custom"
    FLATRATE = "FlatRate"
    USER = "User"

    def __str__(self) -> str:
        return str(self.value)
