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

@pytest.mark.parametrize("input_num, expected_roman", [
    (1, "i"),
    (3, "iii"),
    (4, "iv"),
    (5, "v"),
    (9, "ix"),
    (10, "x"),
    (14, "xiv"),
    (15, "xv"),
    (16, "xvi"),
    (19, "xix"),
    (40, "xl"),
    (44, "xliv"),
    (50, "l"),
    (90, "xc"),
    (100, "c"),
    (400, "cd"),
    (500, "d"),
    (900, "cm"),
    (1000, "m"),
    (1994, "mcmxciv"),
    (152, "clii"),
    (426, "cdxxvi"),
    (888, "dccclxxxviii")
])
def test_int_to_mini_roman(input_num, expected_roman):
    assert int_to_mini_roman(input_num) == expected_roman

def test_int_to_mini_roman_boundary_min():
    assert int_to_mini_roman(1) == "i"

def test_int_to_mini_roman_boundary_max():
    assert int_to_mini_roman(1000) == "m"

def test_int_to_mini_roman_single_symbols():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(5) == "v"
    assert int_to_mini_roman(10) == "x"
    assert int_to_mini_roman(50) == "l"
    assert int_to_mini_roman(100) == "c"
    assert int_to_mini_roman(500) == "d"

def test_int_to_mini_roman_combinations():
    assert int_to_mini_roman(4) == "iv"
    assert int_to_mini_roman(9) == "ix"
    assert int_to_mini_roman(40) == "xl"
    assert int_to_mini_roman(90) == "xc"
    assert int_to_mini_roman(400) == "cd"
    assert int_to_mini_roman(900) == "cm"

def test_int_to_mini_roman_intermediate_values():
    assert int_to_mini_roman(19) == "xix"
    assert int_to_mini_roman(52) == "lii"
    assert int_to_mini_roman(123) == "cxxiii"
    assert int_to_mini_roman(687) == "dclxxxvii"

def test_int_to_mini_roman_invalid_input_below():
    assert int_to_mini_roman(0) == ""

def test_int_to_mini_roman_invalid_input_above():
    assert int_to_mini_roman(1001) == "m"

def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(999) == "cmxcix"
    assert int_to_mini_roman(1001) == "m"