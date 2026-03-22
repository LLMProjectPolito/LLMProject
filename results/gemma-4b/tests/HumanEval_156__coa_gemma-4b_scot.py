import pytest
import math


# Focus: Boundary Values
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
### The function `int_to_mini_roman` converts an integer to its Roman numeral representation.
### Boundary values are 1 and 1000. We need to test these values to ensure the function handles them correctly.
### We also need to test values near the boundaries, such as 4, 9, 40, 90, 400, and 900.
### STEP 2: PLAN - List test functions names and scenarios.
### test_int_to_mini_roman_boundary_1
### test_int_to_mini_roman_boundary_1000
### test_int_to_mini_roman_near_boundary_4
### STEP 3: CODE - Write the high-quality pytest suite.
###
def test_int_to_mini_roman_boundary_1():
    assert int_to_mini_roman(1) == 'i'

def test_int_to_mini_roman_boundary_1000():
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_near_boundary_4():
    assert int_to_mini_roman(4) == 'iv'

# Focus: Type Scenarios
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
### The function `int_to_mini_roman` converts a positive integer to its Roman numeral representation (lowercase).
### The test functions should focus solely on the 'Type Scenarios' dimension, meaning they should test different input values to ensure the function works correctly across a range of valid inputs.
### STEP 2: PLAN - List test functions names and scenarios.
### test_int_to_mini_roman_small_numbers() - Test with small numbers (1-10)
### test_int_to_mini_roman_medium_numbers() - Test with medium numbers (11-100)
### test_int_to_mini_roman_large_numbers() - Test with larger numbers (101-1000)
### STEP 3: CODE - Write the high-quality pytest suite.

def test_int_to_mini_roman_small_numbers():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(2) == 'ii'
    assert int_to_mini_roman(3) == 'iii'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(6) == 'vi'
    assert int_to_mini_roman(7) == 'vii'
    assert int_to_mini_roman(8) == 'viii'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(10) == 'x'

def test_int_to_mini_roman_medium_numbers():
    assert int_to_mini_roman(11) == 'xi'
    assert int_to_mini_roman(14) == 'xiv'
    assert int_to_mini_roman(15) == 'xv'
    assert int_to_mini_roman(16) == 'xvi'
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(20) == 'xx'
    assert int_to_mini_roman(39) == 'xxxix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(44) == 'xliv'
    assert int_to_mini_roman(49) == 'xlix'
    assert int_to_mini_roman(50) == 'l'

def test_int_to_mini_roman_large_numbers():
    assert int_to_mini_roman(101) == 'ci'
    assert int_to_mini_roman(144) == 'cxliv'
    assert int_to_mini_roman(150) == 'cl'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(199) == 'cxcix'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(444) == 'cdxliv'
    assert int_to_mini_roman(499) == 'cdxcix'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(999) == 'cmxcix'

# Focus: Logic Branches
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
### The function `int_to_mini_roman` converts a positive integer to its Roman numeral representation.
### The test functions should focus on verifying the logic branches within the function, specifically how it handles different integer values and the subtraction rules (e.g., 4, 9, 40, 90, 400, 900).
### STEP 2: PLAN - List test functions names and scenarios.
### test_int_to_mini_roman_small_numbers() - Tests small numbers to ensure basic conversion works.
### test_int_to_mini_roman_subtraction() - Tests numbers that require subtraction to generate the correct Roman numeral.
### test_int_to_mini_roman_edge_cases() - Tests edge cases like 1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000.

### STEP 3: CODE - Write the high-quality pytest suite.
### CODE
def test_int_to_mini_roman_small_numbers():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(2) == 'ii'
    assert int_to_mini_roman(3) == 'iii'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(6) == 'vi'
    assert int_to_mini_roman(7) == 'vii'
    assert int_to_mini_roman(8) == 'viii'
    assert int_to_mini_roman(9) == 'ix'

def test_int_to_mini_roman_subtraction():
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(14) == 'xiv'
    assert int_to_mini_roman(16) == 'xix'
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(20) == 'xx'
    assert int_to_mini_roman(39) == 'xxxix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(44) == 'xliv'
    assert int_to_mini_roman(49) == 'xlii'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(94) == 'xciv'
    assert int_to_mini_roman(99) == 'xcix'

def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(900) == 'cm'
    assert int_to_mini_roman(1000) == 'm'
    assert int_to_mini_roman(1994) == 'mcmxciv'
    assert int_to_mini_roman(2023) == 'mcmxxiii'