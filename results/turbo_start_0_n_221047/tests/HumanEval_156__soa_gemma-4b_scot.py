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
### The test suite needs to cover various input values, including edge cases (1, 1000), and numbers that utilize subtractive notation (4, 9, 40, 90, 400, 900).
### We need to test the function with a range of inputs to ensure it produces the correct Roman numeral string.

### STEP 2: PLAN - List test functions names and scenarios.
### test_int_to_mini_roman_basic() - Tests basic cases.
### test_int_to_mini_roman_subtractive() - Tests cases using subtractive notation.
### test_int_to_mini_roman_edge_cases() - Tests edge cases (1, 1000).
### test_int_to_mini_roman_mixed() - Tests a mix of additive and subtractive cases.

### STEP 3: CODE - Write the high-quality pytest suite.
### CODE
def test_int_to_mini_roman_basic():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(14) == 'xiv'
    assert int_to_mini_roman(16) == 'xvi'
    assert int_to_mini_roman(20) == 'xx'
    assert int_to_mini_roman(39) == 'xxxix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(900) == 'cm'

def test_int_to_mini_roman_subtractive():
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(44) == 'xliv'
    assert int_to_mini_roman(49) == 'xlix'
    assert int_to_mini_roman(94) == 'xciv'
    assert int_to_mini_roman(99) == 'xcix'

def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_mixed():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(944) == 'cxciv'
    assert int_to_mini_roman(1994) == 'mcmxciv'
    assert int_to_mini_roman(2023) == 'mmii'