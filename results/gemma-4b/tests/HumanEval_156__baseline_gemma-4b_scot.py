
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
# The function `int_to_mini_roman` converts a positive integer (1-1000) to its lowercase Roman numeral representation.
# We need to test various input values to ensure the function produces the correct Roman numeral string for each case.
# We should cover edge cases like 1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, and 1000.
# We also need to test numbers in between these values to cover the combinations of Roman numerals.

### STEP 2: PLAN
# Test cases:
# 1. Basic cases: 1, 4, 5, 9, 10
# 2. Cases involving combinations: 19, 20, 39, 40, 50, 60, 70, 80, 90, 100
# 3. Cases involving larger numbers: 152, 426, 943, 1994
# 4. Edge cases: 1, 1000
# 5. Numbers that require multiple Roman numeral symbols: 19, 426, 943

# Test functions:
# test_int_to_mini_roman_1_to_10
# test_int_to_mini_roman_11_to_20
# test_int_to_mini_roman_21_to_30
# test_int_to_mini_roman_31_to_40
# test_int_to_mini_roman_41_to_50
# test_int_to_mini_roman_51_to_60
# test_int_to_mini_roman_61_to_70
# test_int_to_mini_roman_71_to_80
# test_int_to_mini_roman_81_to_90
# test_int_to_mini_roman_91_to_100
# test_int_to_mini_roman_152
# test_int_to_mini_roman_426
# test_int_to_mini_roman_943
# test_int_to_mini_roman_1994
# test_int_to_mini_roman_1
# test_int_to_mini_roman_1000

### STEP 3: CODE
def test_int_to_mini_roman_1_to_10():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(10) == 'x'

def test_int_to_mini_roman_11_to_20():
    assert int_to_mini_roman(11) == 'xi'
    assert int_to_mini_roman(14) == 'xiv'
    assert int_to_mini_roman(15) == 'xv'
    assert int_to_mini_roman(19) == 'xix'

def test_int_to_mini_roman_21_to_30():
    assert int_to_mini_roman(21) == 'xxi'
    assert int_to_mini_roman(24) == 'xxiv'
    assert int_to_mini_roman(25) == 'xxv'
    assert int_to_mini_roman(29) == 'xxix'

def test_int_to_mini_roman_31_to_40():
    assert int_to_mini_roman(31) == 'xxxii'
    assert int_to_mini_roman(34) == 'xxxiv'
    assert int_to_mini_roman(35) == 'xxxv'
    assert int_to_mini_roman(39) == 'xxxix'

def test_int_to_mini_roman_41_to_50():
    assert int_to_mini_roman(41) == 'xl'
    assert int_to_mini_roman(44) == 'xliv'
    assert int_to_mini_roman(45) == 'xlv'
    assert int_to_mini_roman(49) == 'xlix'

def test_int_to_mini_roman_51_to_60():
    assert int_to_mini_roman(51) == 'li'
    assert int_to_mini_roman(54) == 'lv'
    assert int_to_mini_roman(55) == 'lvi'
    assert int_to_mini_roman(59) == 'lvix'

def test_int_to_mini_roman_61_to_70():
    assert int_to_mini_roman(61) == 'lxi'
    assert int_to_mini_roman(64) == 'lxiv'
    assert int_to_mini_roman(65) == 'lxv'
    assert int_to_mini_roman(69) == 'lxxix'

def test_int_to_mini_roman_71_to_80():
    assert int_to_mini_roman(71) == 'lxx'
    assert int_to_mini_roman(74) == 'lxxiv'
    assert int_to_mini_roman(75) == 'lxxv'
    assert int_to_mini_roman(79) == 'lxxix'

def test_int_to_mini_roman_81_to_90():
    assert int_to_mini_roman(81) == 'lxxx'
    assert int_to_mini_roman(84) == 'lxxxiv'
    assert int_to_mini_roman(85) == 'lxxxv'
    assert int_to_mini_roman(89) == 'lxxxix'

def test_int_to_mini_roman_91_to_100():
    assert int_to_mini_roman(91) == 'xc'
    assert int_to_mini_roman(94) == 'xciv'
    assert int_to_mini_roman(95) == 'xcv'
    assert int_to_mini_roman(99) == 'xcix'

def test_int_to_mini_roman_152():
    assert int_to_mini_roman(152) == 'clii'

def test_int_to_mini_roman_426():
    assert int_to_mini_roman(426) == 'cdxxvi'

def test_int_to_mini_roman_943():
    assert int_to_mini_roman(943) == 'cmxciii'

def test_int_to_mini_roman_1994():
    assert int_to_mini_roman(1994) == 'mcmxciv'

def test_int_to_mini_roman_1():
    assert int_to_mini_roman(1) == 'i'

def test_int_to_mini_roman_1000():
    assert int_to_mini_roman(1000) == 'm'