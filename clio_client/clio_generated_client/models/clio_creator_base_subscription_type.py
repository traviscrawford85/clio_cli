from enum import Enum


class ClioCreatorBaseSubscriptionType(str, Enum):
    ATTORNEY = "Attorney"
    NONATTORNEY = "NonAttorney"

    def __str__(self) -> str:
        return str(self.value)
