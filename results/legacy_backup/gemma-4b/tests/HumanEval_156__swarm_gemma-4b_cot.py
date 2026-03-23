import pytest
import math

def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    roman_map = { 1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}
    integers = list(roman_map)
    symbols = list(roman_map.values())

    i = 12
    result = ""

    while number != 0:
        if integers[i] <= number:
            result += symbols[i]
            number -= integers[i]
        else:
            i -= 1

    return result

@pytest.mark.parametrize("num, expected", [
    (1, "i"),
    (4, "iv"),
    (9, "ix"),
    (40, "xl"),
    (90, "xc"),
    (400, "cd"),
    (900, "cm"),
    (1000, "m"),
    (19, "xix"),
    (152, "clii"),
    (426, "cdxxvi"),
    (1994, "mcmxciv"),
    (3, "iii"),
    (58, "lviii"),
    (1999, "mcmxix")
])
def test_edge_cases(num, expected):
    assert int_to_mini_roman(num) == expected