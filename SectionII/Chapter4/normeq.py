from unicodedata import normalize


def nfc_equal(str1: str, str2: str) -> bool:
    return normalize('NFC', str1) == normalize('NFC', str2)


def fold_equal(str1: str, str2: str) -> bool:
    return normalize('NFC', str1).casefold() == \
           normalize('NFC', str2).casefold()
