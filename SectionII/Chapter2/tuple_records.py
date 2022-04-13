from typing import Tuple, List

if __name__ == '__main__':
    traveler_ids: List[Tuple[str, str]] = [
        ('USA', '31195855'),
        ('BRA', 'CE342567'),
        ('ESP', 'XDA205856')
    ]

    passport: Tuple[str, str]
    for passport in sorted(traveler_ids):
        print('%s/%s' % passport)