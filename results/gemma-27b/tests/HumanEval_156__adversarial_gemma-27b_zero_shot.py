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
    "input_num, expected_output",
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
        (51, "li"),
        (54, "liv"),
        (55, "lv"),
        (59, "lix"),
        (60, "lx"),
        (64, "lxiv"),
        (65, "lxv"),
        (69, "lxix"),
        (70, "lxx"),
        (74, "lxxiv"),
        (75, "lxxv"),
        (79, "lxxix"),
        (80, "lxxx"),
        (84, "lxxxiv"),
        (85, "lxxxv"),
        (89, "lxxxix"),
        (90, "xc"),
        (91, "xci"),
        (94, "xciv"),
        (95, "xcv"),
        (99, "xcix"),
        (100, "c"),
        (101, "ci"),
        (104, "civ"),
        (105, "cv"),
        (109, "cix"),
        (110, "cx"),
        (149, "cxlix"),
        (150, "cl"),
        (152, "clii"),
        (199, "cxciix"),
        (200, "cc"),
        (300, "ccc"),
        (400, "cd"),
        (426, "cdxxvi"),
        (444, "cdxliv"),
        (499, "cdxcix"),
        (500, "d"),
        (501, "di"),
        (549, "div"),
        (600, "dc"),
        (700, "dcc"),
        (800, "dccc"),
        (900, "cm"),
        (944, "cmxliv"),
        (999, "cmxcix"),
        (1000, "m"),
    ],
)
def test_int_to_mini_roman(input_num, expected_output):
    assert int_to_mini_roman(input_num) == expected_output

def test_invalid_input_less_than_1():
    with pytest.raises(TypeError):
        int_to_mini_roman(0)

def test_invalid_input_greater_than_1000():
    with pytest.raises(TypeError):
        int_to_mini_roman(1001)

def test_invalid_input_type():
    with pytest.raises(TypeError):
        int_to_mini_roman("1")
    with pytest.raises(TypeError):
        int_to_mini_roman(1.5)