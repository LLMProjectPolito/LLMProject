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
# 5. Numbers that require subtraction: 4, 9, 40, 90, 400, 900

### STEP 3: CODE
def test_int_to_mini_roman_1():
    assert int_to_mini_roman(1) == 'i'

def test_int_to_mini_roman_4():
    assert int_to_mini_roman(4) == 'iv'

def test_int_to_mini_roman_5():
    assert int_to_mini_roman(5) == 'v'

def test_int_to_mini_roman_9():
    assert int_to_mini_roman(9) == 'ix'

def test_int_to_mini_roman_10():
    assert int_to_mini_roman(10) == 'x'

def test_int_to_mini_roman_19():
    assert int_to_mini_roman(19) == 'xix'

def test_int_to_mini_roman_152():
    assert int_to_mini_roman(152) == 'clii'

def test_int_to_mini_roman_426():
    assert int_to_mini_roman(426) == 'cdxxvi'

def test_int_to_mini_roman_943():
    assert int_to_mini_roman(943) == 'cxliii'

def test_int_to_mini_roman_1994():
    assert int_to_mini_roman(1994) == 'mcmxciv'

def test_int_to_mini_roman_1000():
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_2():
    assert int_to_mini_roman(2) == 'ii'

def test_int_to_mini_roman_3():
    assert int_to_mini_roman(3) == 'iii'

def test_int_to_mini_roman_6():
    assert int_to_mini_roman(6) == 'vi'

def test_int_to_mini_roman_7():
    assert int_to_mini_roman(7) == 'vii'

def test_int_to_mini_roman_8():
    assert int_to_mini_roman(8) == 'viii'

def test_int_to_mini_roman_11():
    assert int_to_mini_roman(11) == 'xi'

def test_int_to_mini_roman_41():
    assert int_to_mini_roman(41) == 'xli'

def test_int_to_mini_roman_54():
    assert int_to_mini_roman(54) == 'lvii'