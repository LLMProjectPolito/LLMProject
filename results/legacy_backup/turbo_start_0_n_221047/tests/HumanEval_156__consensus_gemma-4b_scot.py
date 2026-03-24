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
### STEP 1: REASONING - Analyze functional goals and constraints.
### The function `int_to_mini_roman` converts a positive integer (1-1000) to its lowercase Roman numeral representation.
### The constraints are that the input number must be between 1 and 1000 inclusive.
### The function should handle edge cases like 4, 9, 40, 90, 400, and 900 correctly.
### The output should be in lowercase.

### STEP 2: PLAN - List test functions names and scenarios.
### test_int_to_mini_roman_basic() - Tests basic cases.
### test_int_to_mini_roman_edge_cases() - Tests edge cases (4, 9, 40, 90, 400, 900).
### test_int_to_mini_roman_small() - Tests small numbers.
### test_int_to_mini_roman_large() - Tests larger numbers within the range.
### test_int_to_mini_roman_boundary() - Tests the boundaries (1 and 1000).

### STEP 3: CODE - Write the high-quality pytest suite.
### STEP 3: CODE - Write the high-quality pytest suite.
def test_int_to_mini_roman_basic():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'

def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(900) == 'cm'

def test_int_to_mini_roman_small():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(3) == 'iii'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(8) == 'viii'

def test_int_to_mini_roman_large():
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(2023) == 'mcmxxiii'

def test_int_to_mini_roman_boundary():
    assert int_to_mini_roman(1000) == 'm'
    assert int_to_mini_roman(1) == 'i'