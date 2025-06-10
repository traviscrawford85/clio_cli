from enum import Enum


class TextSnippetindexOrder(str, Enum):
    IDASC = "id(asc)"
    IDDESC = "id(desc)"
    PHRASEASC = "phrase(asc)"
    PHRASEDESC = "phrase(desc)"
    SNIPPETASC = "snippet(asc)"
    SNIPPETDESC = "snippet(desc)"
    WHOLE_WORDASC = "whole_word(asc)"
    WHOLE_WORDDESC = "whole_word(desc)"

    def __str__(self) -> str:
        return str(self.value)
