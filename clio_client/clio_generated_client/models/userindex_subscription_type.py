from enum import Enum


class UserindexSubscriptionType(str, Enum):
    ATTORNEY = "attorney"
    NONATTORNEY = "nonattorney"

    def __str__(self) -> str:
        return str(self.value)
