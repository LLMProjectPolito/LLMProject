# STEP 1: REASONING
# The function `int_to_mini_roman` converts an integer between 1 and 1000 (inclusive) to its mini-roman numeral representation (lowercase).
# We need to test various cases:
# - Boundary values (1, 1000)
# - Single digit values (1-9)
# - Tens (10, 20, ..., 90)
# - Hundreds (100, 200, ..., 900)
# - Combinations of digits (e.g., 19, 42, 152, 426, 888, 999)
# - Special cases like 4, 9, 40, 90, 400, 900 which use subtractive notation.
# - Invalid input (numbers outside the range 1-1000) should ideally raise an exception, but the prompt doesn't specify this. We'll test for correct behavior within the specified range.

# STEP 2: PLAN
# 1. test_int_to_mini_roman_boundary_1: Test with input 1.
# 2. test_int_to_mini_roman_boundary_1000: Test with input 1000.
# 3. test_int_to_mini_roman_single_digits: Test with single digits 1-9.
# 4. test_int_to_mini_roman_tens: Test with multiples of 10 (10, 20, ..., 90).
# 5. test_int_to_mini_roman_hundreds: Test with multiples of 100 (100, 200, ..., 900).
# 6. test_int_to_mini_roman_combinations: Test with various combinations of digits.
# 7. test_int_to_mini_roman_subtractive_cases: Test cases using subtractive notation (4, 9, 40, 90, 400, 900).
# 8. test_int_to_mini_roman_examples: Test with the examples provided in the docstring.

# STEP 3: CODE
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

def test_int_to_mini_roman_boundary_1():
    assert int_to_mini_roman(1) == 'i'

def test_int_to_mini_roman_boundary_1000():
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_single_digits():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(2) == 'ii'
    assert int_to_mini_roman(3) == 'iii'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(6) == 'vi'
    assert int_to_mini_roman(7) == 'vii'
    assert int_to_mini_roman(8) == 'viii'
    assert int_to_mini_roman(9) == 'ix'

def test_int_to_mini_roman_tens():
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(20) == 'xx'
    assert int_to_mini_roman(30) == 'xxx'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(60) == 'lx'
    assert int_to_mini_roman(70) == 'lxx'
    assert int_to_mini_roman(80) == 'lxxx'
    assert int_to_mini_roman(90) == 'xc'

def test_int_to_mini_roman_hundreds():
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(200) == 'cc'
    assert int_to_mini_roman(300) == 'ccc'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(600) == 'dc'
    assert int_to_mini_roman(700) == 'dcc'
    assert int_to_mini_roman(800) == 'dccc'
    assert int_to_mini_roman(900) == 'cm'

def test_int_to_mini_roman_combinations():
    assert int_to_mini_roman(12) == 'xii'
    assert int_to_mini_roman(35) == 'xxxv'
    assert int_to_mini_roman(149) == 'cxlix'
    assert int_to_mini_roman(278) == 'ccLxxviii'
    assert int_to_mini_roman(567) == 'dLvii'
    assert int_to_mini_roman(899) == 'cmxcix'

def test_int_to_mini_roman_subtractive_cases():
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(900) == 'cm'

def test_int_to_mini_roman_examples():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'