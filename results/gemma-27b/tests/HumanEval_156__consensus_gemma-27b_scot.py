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

@pytest.mark.parametrize("input_num, expected_roman", [
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
    (60, "lx"),
    (70, "lxx"),
    (80, "lxxx"),
    (90, "xc"),
    (100, "c"),
    (110, "cx"),
    (120, "cxx"),
    (150, "cl"),
    (200, "cc"),
    (300, "ccc"),
    (400, "cd"),
    (500, "d"),
    (600, "dc"),
    (700, "dcc"),
    (800, "dccc"),
    (900, "cm"),
    (1000, "m"),
    (152, "clii"),
    (426, "cdxxvi"),
    (199, "cxcix"),
    (388, "cccLXXXVIII"),
    (944, "cmxliv"),
    (499, "cdxcix")
])
def test_int_to_mini_roman(input_num, expected_roman):
    assert int_to_mini_roman(input_num) == expected_roman

def test_edge_cases():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(1000) == "m"

def test_invalid_input():
    assert int_to_mini_roman(0) == ""
    assert int_to_mini_roman(1001) == "m"