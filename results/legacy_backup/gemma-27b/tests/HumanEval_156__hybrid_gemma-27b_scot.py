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

    return result.lower()

# STEP 1: REASONING
# The function `int_to_mini_roman` converts an integer between 1 and 1000 (inclusive) into its lowercase Roman numeral representation.
# The tests should cover boundary conditions (1, 1000), common values, and a variety of numbers within the valid range.
# Error handling is not explicitly required, but we should test inputs outside the range [1, 1000].

# STEP 2: PLAN
# 1. test_int_to_mini_roman_valid_input: Tests with valid inputs covering various scenarios.
# 2. test_int_to_mini_roman_boundary_conditions: Tests the boundary conditions of the input range (1 and 1000).
# 3. test_int_to_mini_roman_subtractive_notation: Tests cases that specifically utilize subtractive notation (4, 9, 40, 90, 400, 900).
# 4. test_int_to_mini_roman_edge_cases: Tests numbers close to the boundaries of subtractive notation.
# 5. test_int_to_mini_roman_invalid_input_less_than_one: Tests input less than 1.
# 6. test_int_to_mini_roman_invalid_input_greater_than_one_thousand: Tests input greater than 1000.

# STEP 3: CODE
def test_int_to_mini_roman_valid_input():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(2) == "ii"
    assert int_to_mini_roman(3) == "iii"
    assert int_to_mini_roman(19) == "xix"
    assert int_to_mini_roman(42) == "xlii"
    assert int_to_mini_roman(152) == "clii"
    assert int_to_mini_roman(426) == "cdxxvi"
    assert int_to_mini_roman(789) == "dccxcix"
    assert int_to_mini_roman(999) == "cmxcix"

def test_int_to_mini_roman_boundary_conditions():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(1000) == "m"

def test_int_to_mini_roman_subtractive_notation():
    assert int_to_mini_roman(4) == "iv"
    assert int_to_mini_roman(9) == "ix"
    assert int_to_mini_roman(40) == "xl"
    assert int_to_mini_roman(90) == "xc"
    assert int_to_mini_roman(400) == "cd"
    assert int_to_mini_roman(900) == "cm"

def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(3) == "iii"
    assert int_to_mini_roman(5) == "v"
    assert int_to_mini_roman(39) == "xxxix"
    assert int_to_mini_roman(41) == "xli"
    assert int_to_mini_roman(89) == "lxxxix"
    assert int_to_mini_roman(91) == "xci"
    assert int_to_mini_roman(399) == "cccxcix"
    assert int_to_mini_roman(401) == "cdi"

def test_int_to_mini_roman_invalid_input_less_than_one():
    assert int_to_mini_roman(0) == ""
    assert int_to_mini_roman(-1) == ""

def test_int_to_mini_roman_invalid_input_greater_than_one_thousand():
    assert int_to_mini_roman(1001) == ""
    assert int_to_mini_roman(2000) == ""