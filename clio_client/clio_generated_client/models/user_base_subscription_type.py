from enum import Enum


class UserBaseSubscriptionType(str, Enum):
    ATTORNEY = "Attorney"
    NONATTORNEY = "NonAttorney"

    def __str__(self) -> str:
        return str(self.value)
