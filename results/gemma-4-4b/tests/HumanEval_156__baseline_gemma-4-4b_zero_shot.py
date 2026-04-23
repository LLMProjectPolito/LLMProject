
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

import pytest

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
    i = 1
    result = ''
    while number > 0:
        if i in roman_map and i <= number:
            result += roman_map[i]
            number -= i
        else:
            i *= 10
    return result

@pytest.mark.parametrize(
    "number, expected",
    [
        (1, "i"),
        (2, "ii"),
        (3, "iii"),
        (4, "iv"),
        (5, "v"),
        (6, "vi"),
        (7, "vii"),
        (8, "viii"),
        (9, "ix"),
        (10, "x"),
        (11, "xi"),
        (14, "xiv"),
        (15, "xv"),
        (16, "xvi"),
        (19, "xix"),
        (20, "xx"),
        (39, "xxxix"),
        (40, "xl"),
        (41, "xli"),
        (44, "xliv"),
        (45, "xlv"),
        (49, "xlix"),
        (50, "l"),
        (90, "xc"),
        (100, "c"),
        (400, "cd"),
        (500, "d"),
        (900, "cm"),
        (1000, "m"),
        (152, "clii"),
        (426, "cdxxvi"),
        (944, "cxliv"),
        (999, "cmxcix"),
        (1001, "m"),
        (1000, "m"),
        (1, "i"),
        (3, "iii"),
        (5, "v"),
        (10, "x"),
        (50, "l"),
        (100, "c"),
        (500, "d"),
        (1000, "m"),
        (1994, "mcmxciv"),
        (2023, "mmxxiii"),
    ],
)
def test_int_to_mini_roman(number, expected):
    assert int_to_mini_roman(number) == expected