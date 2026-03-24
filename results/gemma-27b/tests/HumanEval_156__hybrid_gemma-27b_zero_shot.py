
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

@pytest.mark.parametrize(
    "input_num, expected_roman",
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
        (51, "li"),
        (60, "lx"),
        (70, "lxx"),
        (80, "lxxx"),
        (90, "xc"),
        (91, "xci"),
        (92, "xcii"),
        (93, "xciii"),
        (94, "xciv"),
        (95, "xcv"),
        (96, "xcvi"),
        (97, "xcvii"),
        (98, "xcviii"),
        (99, "xcix"),
        (100, "c"),
        (101, "ci"),
        (149, "cxlix"),
        (150, "cl"),
        (152, "clii"),
        (194, "cxciv"),
        (200, "cc"),
        (300, "ccc"),
        (399, "cccxcix"),
        (400, "cd"),
        (426, "cdxxvi"),
        (444, "cdxliv"),
        (499, "cdxcix"),
        (500, "d"),
        (501, "di"),
        (555, "dlv"),
        (600, "dc"),
        (649, "dcxlix"),
        (700, "dcc"),
        (777, "dccclxxvii"),
        (800, "dccc"),
        (854, "dcccliv"),
        (900, "cm"),
        (901, "cmi"),
        (944, "cmxliv"),
        (999, "cmxcix"),
        (1000, "m"),
    ],
)
def test_int_to_mini_roman(input_num, expected_roman):
    assert int_to_mini_roman(input_num) == expected_roman

def test_invalid_input():
    with pytest.raises(TypeError):
        int_to_mini_roman("abc")
    with pytest.raises(TypeError):
        int_to_mini_roman(3.14)
    with pytest.raises(ValueError):
        int_to_mini_roman(0)
    with pytest.raises(ValueError):
        int_to_mini_roman(1001)