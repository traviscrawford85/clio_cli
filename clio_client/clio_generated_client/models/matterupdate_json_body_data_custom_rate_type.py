from enum import Enum


class MatterupdateJsonBodyDataCustomRateType(str, Enum):
    CONTINGENCYFEE = "ContingencyFee"
    FLATRATE = "FlatRate"
    HOURLYRATE = "HourlyRate"

    def __str__(self) -> str:
        return str(self.value)
