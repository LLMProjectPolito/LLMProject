
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
    i = 12
    result = ""

    while number != 0:
        if list(roman_map.keys())[i] <= number:
            result += list(roman_map.values())[i]
            number -= list(roman_map.keys())[i]
        else:
            i -= 1

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
        (12, "xii"),
        (13, "xiii"),
        (14, "xiv"),
        (15, "xv"),
        (16, "xvi"),
        (17, "xvii"),
        (18, "xviii"),
        (19, "xix"),
        (20, "xx"),
        (39, "xxxix"),
        (40, "xl"),
        (41, "xli"),
        (42, "xlii"),
        (43, "xliii"),
        (44, "xliv"),
        (45, "xlv"),
        (46, "xlvi"),
        (47, "xlvii"),
        (48, "xlviii"),
        (49, "xlix"),
        (50, "l"),
        (90, "xc"),
        (100, "c"),
        (400, "cd"),
        (500, "d"),
        (900, "cm"),
        (1000, "m"),
        (1, "i"),
        (1000, "m"),
        (1999, "mcmxcix"),
        (2023, "mmxxiii"),
        (101, "ci"),
        (111, "cxi"),
        (121, "cxxi"),
        (131, "cxxxi"),
        (141, "cxlvi"),
        (151, "cli"),
        (161, "clxi"),
        (171, "clxxi"),
        (181, "clxxi"),
        (191, "clxxi"),
        (299, "cccxcix"),
        (399, "cccxciii"),
        (499, "cdxcix"),
        (599, "dxcix"),
        (699, "dcxix"),
        (799, "dccxix"),
        (899, "dccxix"),
        (999, "cmxcix"),
    ],
)
def test_int_to_mini_roman(number, expected):
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize(
    "number",
    [0, -1, 1001],
)
def test_invalid_input(number):
    with pytest.raises(AssertionError):
        int_to_mini_roman(number)