from enum import Enum


class CalendarupdateJsonBodyDataColor(str, Enum):
    VALUE_0 = "#367B9C"
    VALUE_1 = "#FFA5A4"
    VALUE_10 = "#616161"
    VALUE_11 = "#BBDA81"
    VALUE_12 = "#DFD3F8"
    VALUE_13 = "#D6C4A5"
    VALUE_14 = "#FFD478"
    VALUE_15 = "#6AC9DE"
    VALUE_16 = "#EABBB0"
    VALUE_17 = "#BFC2E1"
    VALUE_18 = "#DADADA"
    VALUE_19 = "#CDE2F5"
    VALUE_2 = "#83D17F"
    VALUE_3 = "#FFAC7B"
    VALUE_4 = "#8E3F64"
    VALUE_5 = "#C75300"
    VALUE_6 = "#009CEC"
    VALUE_7 = "#62D6B1"
    VALUE_8 = "#9EEDCB"
    VALUE_9 = "#F9A2C4"

    def __str__(self) -> str:
        return str(self.value)
