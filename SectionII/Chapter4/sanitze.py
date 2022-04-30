import string
import unicodedata


def shave_marks(txt: str) -> str:
    """Remove all diacritic marks"""
    norm_txt = unicodedata.normalize('NFD', txt)  # Decompose all characters into base characters and combining marks
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))  # Filter out all combining marks

    return unicodedata.normalize('NFC', shaved)  # Recompose all characters


def shave_marks_latin(txt: str) -> str:
    """Remove all diacritic marks from Latin base characters"""
    norm_txt = unicodedata.normalize('NFD', txt)  # 1. Decompose all characters into base characters and combining marks
    latin_base = False
    keepers = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:  # 2. Skip over combining marks when base character is Latin.
            continue  # ignore diacritic on Latin base  char

        keepers.append(c)  # 3.  Otherwise, keep current character.

        # if it isn't combining char, it's a new base char
        if not unicodedata.combining(c):  # 4. Detect new base character and determine if it's Latin.
            latin_base = c in string.ascii_letters

    shaved = ''.join(keepers)
    return unicodedata.normalize('NFC', shaved)  # 5. Recompose all characters.
