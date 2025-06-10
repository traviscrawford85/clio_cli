from enum import Enum


class ActivityDescriptionRateBaseHierarchy(str, Enum):
    ACTIVITY = "Activity"
    CLIENT = "Client"
    DEFAULT = "Default"
    MATTER = "Matter"

    def __str__(self) -> str:
        return str(self.value)
