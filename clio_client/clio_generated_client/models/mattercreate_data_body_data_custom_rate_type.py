from enum import Enum


class MattercreateDataBodyDataCustomRateType(str, Enum):
    CONTINGENCYFEE = "ContingencyFee"
    FLATRATE = "FlatRate"
    HOURLYRATE = "HourlyRate"

    def __str__(self) -> str:
        return str(self.value)
