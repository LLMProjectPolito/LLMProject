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

### SCoT Steps:

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `int_to_mini_roman` converts a positive integer (1 <= num <= 1000) to its lowercase Roman numeral representation.
# We need to test various input values within the specified range to ensure the function produces the correct Roman numeral string.
# Edge cases include 1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, and 1000.
# We also need to test combinations of Roman numerals to ensure correct subtraction.

# STEP 2: PLAN - List test functions names and scenarios.
# test_int_to_mini_roman_basic: Tests basic cases.
# test_int_to_mini_roman_edge_cases: Tests edge cases like 1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000.
# test_int_to_mini_roman_combinations: Tests combinations of Roman numerals to ensure correct subtraction.
# test_int_to_mini_roman_invalid_input: Tests invalid input (outside the range 1-1000) - although the problem states it's restricted, it's good to check.

# STEP 3: CODE - Write the high-quality pytest suite.
###
# test_int_to_mini_roman_basic
def test_int_to_mini_roman_basic():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(94) == 'xciv'
    assert int_to_mini_roman(3) == 'iii'

# test_int_to_mini_roman_edge_cases
def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(900) == 'cm'
    assert int_to_mini_roman(1000) == 'm'

# test_int_to_mini_roman_combinations
def test_int_to_mini_roman_combinations():
    assert int_to_mini_roman(14) == 'xiv'
    assert int_to_mini_roman(29) == 'xxix'
    assert int_to_mini_roman(44) == 'xliv'
    assert int_to_mini_roman(83) == 'lxxxiii'
    assert int_to_mini_roman(111) == 'cxxxiii'

# test_int_to_mini_roman_invalid_input
def test_int_to_mini_roman_invalid_input():
    with pytest.raises(Exception):  # Or a more specific exception if appropriate
        int_to_mini_roman(0)
    with pytest.raises(Exception):
        int_to_mini_roman(1001)