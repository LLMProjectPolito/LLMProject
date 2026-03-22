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
# STEP 1: REASONING - The function converts a positive integer to its Roman numeral representation in lowercase.
# The input is restricted to be between 1 and 1000 inclusive.
# We need to test various input values to ensure the function produces the correct Roman numeral string.
# We should test edge cases like 1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000.
# We should also test numbers in between these values to cover different combinations of Roman numerals.

# STEP 2: PLAN -
# test_int_to_mini_roman_1: Test with a simple number (19)
# test_int_to_mini_roman_2: Test with a number containing multiple Roman numerals (152)
# test_int_to_mini_roman_3: Test with a number containing more complex Roman numerals (426)
# test_int_to_mini_roman_4: Test with the minimum value (1)
# test_int_to_mini_roman_5: Test with the maximum value (1000)
# test_int_to_mini_roman_6: Test a number with repeating numerals (e.g., 3)
# test_int_to_mini_roman_7: Test a number with a mix of numerals (e.g., 27)
# test_int_to_mini_roman_8: Test a number that requires subtraction (e.g., 4)
# test_int_to_mini_roman_9: Test a number that requires subtraction twice (e.g., 9)


# STEP 3: CODE -
###
def test_int_to_mini_roman_1():
    assert int_to_mini_roman(19) == 'xix'

def test_int_to_mini_roman_2():
    assert int_to_mini_roman(152) == 'clii'

def test_int_to_mini_roman_3():
    assert int_to_mini_roman(426) == 'cdxxvi'

def test_int_to_mini_roman_4():
    assert int_to_mini_roman(1) == 'i'

def test_int_to_mini_roman_5():
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_6():
    assert int_to_mini_roman(3) == 'iii'

def test_int_to_mini_roman_7():
    assert int_to_mini_roman(27) == 'xxvii'

def test_int_to_mini_roman_8():
    assert int_to_mini_roman(4) == 'iv'

def test_int_to_mini_roman_9():
    assert int_to_mini_roman(9) == 'ix'