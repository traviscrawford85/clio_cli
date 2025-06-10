from enum import Enum


class CalendarVisibilityBaseColor(str, Enum):
    VALUE_0 = "#658CDA"
    VALUE_1 = "#DA6666"
    VALUE_10 = "#BFBF4B"
    VALUE_11 = "#8BBF3C"
    VALUE_12 = "#B473B4"
    VALUE_13 = "#A7A77D"
    VALUE_14 = "#F2A53D"
    VALUE_15 = "#658CB3"
    VALUE_16 = "#BE9494"
    VALUE_17 = "#A992A9"
    VALUE_18 = "#8897A5"
    VALUE_19 = "#93A2BE"
    VALUE_2 = "#49B050"
    VALUE_3 = "#E7804C"
    VALUE_4 = "#8C66DA"
    VALUE_5 = "#C4A882"
    VALUE_6 = "#64AD88"
    VALUE_7 = "#84AAA5"
    VALUE_8 = "#56BFB3"
    VALUE_9 = "#E77399"

    def __str__(self) -> str:
        return str(self.value)
