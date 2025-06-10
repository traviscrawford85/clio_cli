from enum import Enum


class BankAccountindexOrder(str, Enum):
    ACCOUNT_NUMBERASC = "account_number(asc)"
    ACCOUNT_NUMBERDESC = "account_number(desc)"
    CURRENCYASC = "currency(asc)"
    CURRENCYDESC = "currency(desc)"
    IDASC = "id(asc)"
    IDDESC = "id(desc)"
    INSTITUTIONASC = "institution(asc)"
    INSTITUTIONDESC = "institution(desc)"
    NAMEASC = "name(asc)"
    NAMEDESC = "name(desc)"
    TRANSIT_NUMBERASC = "transit_number(asc)"
    TRANSIT_NUMBERDESC = "transit_number(desc)"
    TYPEASC = "type(asc)"
    TYPEDESC = "type(desc)"
    UPDATED_ATASC = "updated_at(asc)"
    UPDATED_ATDESC = "updated_at(desc)"

    def __str__(self) -> str:
        return str(self.value)
