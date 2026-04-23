
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

### SCoT Steps:

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function `int_to_mini_roman` converts a positive integer (1 <= num <= 1000) to its lowercase Roman numeral representation.
# We need to test various input values to ensure the function produces the correct Roman numeral string for each case.
# We should cover edge cases like 1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, and 1000.
# We also need to test numbers that require combinations of Roman numerals (e.g., 19, 152, 426).

# STEP 2: PLAN - List test functions names and scenarios.
# test_int_to_mini_roman_basic: Test basic cases.
# test_int_to_mini_roman_edge_cases: Test edge cases (1, 4, 5, 9, 10, etc.).
# test_int_to_mini_roman_combinations: Test numbers requiring combinations of Roman numerals.
# test_int_to_mini_roman_large: Test a large number close to the limit (1000).

# STEP 3: CODE - Write the high-quality pytest suite.
###
# test_int_to_mini_roman_basic
def test_int_to_mini_roman_basic():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(9) == 'ix'

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
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(149) == 'cxlix'
    assert int_to_mini_roman(29) == 'xxix'

# test_int_to_mini_roman_large
def test_int_to_mini_roman_large():
    assert int_to_mini_roman(999) == 'cmlxix'
    assert int_to_mini_roman(1000) == 'm'