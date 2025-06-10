from enum import Enum


class UserindexOrder(str, Enum):
    EMAILASC = "email(asc)"
    EMAILDESC = "email(desc)"
    ENABLEDASC = "enabled(asc)"
    ENABLEDDESC = "enabled(desc)"
    FIRST_NAMEASC = "first_name(asc)"
    FIRST_NAMEDESC = "first_name(desc)"
    IDASC = "id(asc)"
    IDDESC = "id(desc)"
    INITIALSASC = "initials(asc)"
    INITIALSDESC = "initials(desc)"
    LAST_NAMEASC = "last_name(asc)"
    LAST_NAMEDESC = "last_name(desc)"
    NAMEASC = "name(asc)"
    NAMEDESC = "name(desc)"
    SUBSCRIPTION_TYPEASC = "subscription_type(asc)"
    SUBSCRIPTION_TYPEDESC = "subscription_type(desc)"

    def __str__(self) -> str:
        return str(self.value)
