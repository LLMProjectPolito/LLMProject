
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

### STEP 1: REASONING
# The function `int_to_mini_roman` converts a positive integer (1 <= num <= 1000) to its lowercase Roman numeral representation.
# We need to test various input values to ensure the function produces the correct Roman numeral string for each case.
# We should cover edge cases like 1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, and 1000.
# We also need to test numbers in between these values to cover the combinations of Roman numerals.

### STEP 2: PLAN
# Test cases:
# 1. Basic cases: 1, 4, 5, 9, 10
# 2. Cases involving combinations: 19, 20, 39, 40, 50, 69, 70, 89, 90, 100
# 3. Cases involving larger numbers: 152, 426, 943, 1994
# 4. Edge cases: 1, 1000
# 5. Numbers that require subtraction: 4, 9, 40, 90, 400, 900

### STEP 3: CODE
def test_int_to_mini_roman():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(20) == 'xx'
    assert int_to_mini_roman(39) == 'xxxix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(69) == 'lxix'
    assert int_to_mini_roman(70) == 'lxx'
    assert int_to_mini_roman(89) == 'lxxxix'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(943) == 'cxliii'
    assert int_to_mini_roman(1994) == 'mcmxciv'
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(1000) == 'm'
    assert int_to_mini_roman(3) == 'iii'
    assert int_to_mini_roman(7) == 'vii'
    assert int_to_mini_roman(11) == 'xi'
    assert int_to_mini_roman(14) == 'xiv'
    assert int_to_mini_roman(16) == 'xvi'
    assert int_to_mini_roman(23) == 'xxiii'
    assert int_to_mini_roman(29) == 'xxix'
    assert int_to_mini_roman(31) == 'xxi'
    assert int_to_mini_roman(37) == 'xxxvii'
    assert int_to_mini_roman(41) == 'xli'
    assert int_to_mini_roman(43) == 'xlii'
    assert int_to_mini_roman(47) == 'xlvii'
    assert int_to_mini_roman(53) == 'lxxxiii'
    assert int_to_mini_roman(59) == 'lxxxix'
    assert int_to_mini_roman(67) == 'lxxvii'
    assert int_to_mini_roman(73) == 'lxxiii'
    assert int_to_mini_roman(79) == 'lxxix'
    assert int_to_mini_roman(83) == 'lxxxiii'
    assert int_to_mini_roman(89) == 'lxxxix'
    assert int_to_mini_roman(97) == 'xcii'
    assert int_to_mini_roman(99) == 'xciii'