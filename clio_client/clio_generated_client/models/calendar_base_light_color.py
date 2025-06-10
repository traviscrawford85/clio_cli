from enum import Enum


class CalendarBaseLightColor(str, Enum):
    VALUE_0 = "#5DA5C7"
    VALUE_1 = "#F95957"
    VALUE_10 = "#A3A2A2"
    VALUE_11 = "#84AB3B"
    VALUE_12 = "#B091EE"
    VALUE_13 = "#BD9E69"
    VALUE_14 = "#F2A000"
    VALUE_15 = "#00A5CA"
    VALUE_16 = "#CB5A3D"
    VALUE_17 = "#959CD0"
    VALUE_18 = "#B0B0B0"
    VALUE_19 = "#7BA6CD"
    VALUE_2 = "#209412"
    VALUE_3 = "#FF7715"
    VALUE_4 = "#DE649D"
    VALUE_5 = "#FF6B02"
    VALUE_6 = "#56C4FC"
    VALUE_7 = "#00B177"
    VALUE_8 = "#50D19B"
    VALUE_9 = "#F14A8C"

    def __str__(self) -> str:
        return str(self.value)
