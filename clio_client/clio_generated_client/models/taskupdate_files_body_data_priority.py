from enum import Enum


class TaskupdateFilesBodyDataPriority(str, Enum):
    HIGH = "High"
    LOW = "Low"
    NORMAL = "Normal"

    def __str__(self) -> str:
        return str(self.value)
