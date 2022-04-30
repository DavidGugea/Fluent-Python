from unicodedata import normalize, name

if __name__ == '__main__':
    """
    s1 = "café"
    s2 = "cafe\u0301"
    print(s1, s2)
    print(len(s1), len(s2))
    print(len(normalize('NFC', s1)), len(normalize('NFC', s2)))
    print(normalize("NFC", s1) == normalize("NFC", s2))
    print(normalize("NFD", s1) == normalize("NFD", s2))
    print(s1 == s2)
    """

    ohm = '\u2126'
    print(name(ohm))
    ohm_c = normalize('NFC', ohm)
    print(name(ohm_c))
    print(ohm == ohm_c)
    print(normalize('NFC', ohm) == normalize('NFC', ohm_c))