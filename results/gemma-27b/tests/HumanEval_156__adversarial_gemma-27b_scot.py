
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

@pytest.mark.parametrize("input_num, expected_roman", [
    (1, "i"),
    (10, "x"),
    (100, "c"),
    (1000, "m"),
    (4, "iv"),
    (9, "ix"),
    (40, "xl"),
    (90, "xc"),
    (400, "cd"),
    (900, "cm"),
    (5, "v"),
    (50, "l"),
    (500, "d"),
    (19, "xix"),
    (52, "lii"),
    (123, "cxxiii"),
    (687, "dclxxxvii"),
    (152, "clii"),
    (426, "cdxxvi"),
])
def test_int_to_mini_roman_valid_inputs(input_num, expected_roman):
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
    assert int_to_mini_roman(14) == "xiv"
    assert int_to_mini_roman(40) == "xl"
    assert int_to_mini_roman(90) == "xc"
    assert int_to_mini_roman(400) == "cd"
    assert int_to_mini_roman(900) == "cm"

def test_int_to_mini_roman_intermediate_values():
    assert int_to_mini_roman(19) == "xix"
    assert int_to_mini_roman(52) == "lii"
    assert int_to_mini_roman(123) == "cxxiii"
    assert int_to_mini_roman(687) == "dclxxxvii"

def test_int_to_mini_roman_invalid_input_less_than_min():
    assert int_to_mini_roman(0) == ""

def test_int_to_mini_roman_invalid_input_greater_than_max():
    assert int_to_mini_roman(1001) == "m"

def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(999) == "cmxcix"
    assert int_to_mini_roman(1001) == "m"