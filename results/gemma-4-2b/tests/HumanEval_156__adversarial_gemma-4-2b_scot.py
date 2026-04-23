
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
    roman_map = { 1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'x', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}
    if number < 1 or number > 1000:
        raise ValueError("Number must be between 1 and 1000")

    result = ''
    while number > 0:
        remainder = number % 10
        if remainder == 1:
            result += 'i'
        elif remainder == 2:
            result += 'ii'
        elif remainder == 3:
            result += 'iii'
        elif remainder == 4:
            result += 'iv'
        elif remainder == 5:
            result += 'v'
        elif remainder == 6:
            result += 'vi'
        elif remainder == 7:
            result += 'vii'
        elif remainder == 8:
            result += 'viii'
        elif remainder == 9:
            result += 'ix'
        elif remainder == 10:
            result += 'x'
        elif remainder == 40:
            result += 'xl'
        elif remainder == 50:
            result += 'l'
        elif remainder == 90:
            result += 'x'
        elif remainder == 100:
            result += 'c'
        elif remainder == 400:
            result += 'cd'
        elif remainder == 500:
            result += 'd'
        elif remainder == 900:
            result += 'cm'
        elif remainder == 1000:
            result += 'm'
        number //= 10
    return result.lower()

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
        (30, "xxx"),
        (40, "xl"),
        (50, "l"),
        (60, "sixty"),
        (70, "seventy"),
        (80, "eighty"),
        (90, "ninety"),
        (100, "c"),
        (101, "ci"),
        (102, "cii"),
        (103, "ciii"),
        (104, "civ"),
        (105, "v"),
        (106, "vi"),
        (107, "vii"),
        (108, "viii"),
        (109, "ix"),
        (110, "xi"),
        (120, "lxx"),
        (130, "cxxx"),
        (140, "xiv"),
        (150, "一百五十"),
        (160, "一百六十"),
        (170, "一百七十"),
        (180, "一百八十"),
        (190, "一百九十"),
        (200, "ccc"),
        (300, "ccc"),
        (400, "cd"),
        (500, "d"),
        (600, "cdxc"),
        (700, "dcc"),
        (800, "dccviii"),
        (900, "cm"),
        (1000, "m"),
    ],
)
def test_int_to_mini_roman(number, expected):
    assert int_to_mini_roman(number) == expected

@pytest.mark.parametrize(
    "number",
    [1, 1000],
)
def test_edge_cases(number):
    assert int_to_mini_roman(number) == str(number)

@pytest.mark.parametrize(
    "number",
    [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],
)
def test_invalid_input(number):
    with pytest.raises(ValueError) as excinfo:
        int_to_mini_roman(number)
    assert "Number must be between 1 and 1000" in str(excinfo.value)