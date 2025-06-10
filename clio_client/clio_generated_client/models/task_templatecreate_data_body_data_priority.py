from enum import Enum


class TaskTemplatecreateDataBodyDataPriority(str, Enum):
    HIGH = "High"
    LOW = "Low"
    NORMAL = "Normal"

    def __str__(self) -> str:
        return str(self.value)
