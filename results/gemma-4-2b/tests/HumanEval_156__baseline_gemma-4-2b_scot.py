
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

# STEP 1: REASONING
# The function `int_to_mini_roman` converts a positive integer (1-1000) to its Roman numeral representation.
# We need to test various scenarios including single-digit numbers, numbers with combinations of Roman numerals,
# and edge cases like 1, 4, 5, 9, 10, 40, 50, 90, 100.
# We should also test invalid inputs (though the problem states 1 <= num <= 1000, we should still consider it).
# The output should be lowercase.

# STEP 2: PLAN
# Test cases:
# 1. Single-digit numbers (1-9)
# 2. Numbers with combinations of Roman numerals (e.g., 19, 42, 58, 99)
# 3. Numbers with subtractive notation (e.g., 4, 9, 40, 90, 400, 900)
# 4. Edge cases (1, 4, 5, 9, 10, 40, 50, 90, 100)
# 5. Invalid input (outside the range 1-1000) - although the problem specifies this is not allowed, it's good practice.

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
    roman_map = { 1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'x', 100: 'c'}
    result = ''
    if number in roman_map:
        result += roman_map[number]
        number = number // 10
    while number > 0:
        if number in roman_map:
            result += roman_map[number]
            number = number // 10
        else:
            result += str(number % 10)
            number = number // 10
    return result.lower()

def test_single_digit():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(2) == 'ii'
    assert int_to_mini_roman(3) == 'iii'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(6) == 'vi'
    assert int_to_mini_roman(7) == 'vii'
    assert int_to_mini_roman(8) == 'viii'
    assert int_to_mini_roman(9) == 'ix'

def test_combinations():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(42) == 'xlii'
    assert int_to_mini_roman(58) == 'lvviii'
    assert int_to_mini_roman(99) == 'xciii'

def test_edge_cases():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(100) == 'c'

def test_invalid_input():
    with pytest.raises(ValueError):
        int_to_mini_roman(0)
    with pytest.raises(ValueError):
        int_to_mini_roman(1001)