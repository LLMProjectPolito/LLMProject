
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
# The function `int_to_mini_roman` converts a positive integer (1-1000) to its mini-Roman numeral representation.
# The constraints specify the input range. We need to test various scenarios within this range, including:
# - Boundary values (1, 1000)
# - Numbers with common Roman numeral combinations (4, 9, 40, 90, 400, 900)
# - Numbers requiring subtractive notation
# - Numbers with repeated numerals
# - Numbers with mixed numerals
# - Invalid input (outside the range 1-1000) - although the prompt doesn't explicitly require this, it's good practice to consider.  We'll assume the function handles this gracefully (e.g., returns an empty string or raises an exception).

# STEP 2: PLAN
# Test functions:
# - test_valid_input_boundary_1: Test the lower boundary (1)
# - test_valid_input_boundary_1000: Test the upper boundary (1000)
# - test_valid_input_common_roman_4: Test the number 4
# - test_valid_input_common_roman_9: Test the number 9
# - test_valid_input_common_roman_40: Test the number 40
# - test_valid_input_common_roman_90: Test the number 90
# - test_valid_input_common_roman_400: Test the number 400
# - test_valid_input_common_roman_900: Test the number 900
# - test_valid_input_subtractive_notation: Test a number requiring subtractive notation (e.g., 19, 152, 426)
# - test_valid_input_repeated_numerals: Test a number with repeated numerals (e.g., 3, 33, 88)
# - test_valid_input_mixed_numerals: Test a number with mixed numerals (e.g., 27, 149)
# - test_valid_input_random_numbers: Test a range of random numbers within the valid range.
# - test_invalid_input_less_than_1: Test input less than 1
# - test_invalid_input_greater_than_1000: Test input greater than 1000

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

    return result.lower()


class TestIntToMiniRoman:
    def test_valid_input_boundary_1(self):
        assert int_to_mini_roman(1) == "i"

    def test_valid_input_boundary_1000(self):
        assert int_to_mini_roman(1000) == "m"

    def test_valid_input_common_roman_4(self):
        assert int_to_mini_roman(4) == "iv"

    def test_valid_input_common_roman_9(self):
        assert int_to_mini_roman(9) == "ix"

    def test_valid_input_common_roman_40(self):
        assert int_to_mini_roman(40) == "xl"

    def test_valid_input_common_roman_90(self):
        assert int_to_mini_roman(90) == "xc"

    def test_valid_input_common_roman_400(self):
        assert int_to_mini_roman(400) == "cd"

    def test_valid_input_common_roman_900(self):
        assert int_to_mini_roman(900) == "cm"

    def test_valid_input_subtractive_notation(self):
        assert int_to_mini_roman(19) == "xix"
        assert int_to_mini_roman(152) == "clii"
        assert int_to_mini_roman(426) == "cdxxvi"

    def test_valid_input_repeated_numerals(self):
        assert int_to_mini_roman(3) == "iii"
        assert int_to_mini_roman(33) == "xxxiii"
        assert int_to_mini_roman(88) == "lxxxviii"

    def test_valid_input_mixed_numerals(self):
        assert int_to_mini_roman(27) == "xxvii"
        assert int_to_mini_roman(149) == "cxlix"

    def test_valid_input_random_numbers(self):
        assert int_to_mini_roman(55) == "lv"
        assert int_to_mini_roman(204) == "cciv"
        assert int_to_mini_roman(789) == "dccxcix"

    def test_invalid_input_less_than_1(self):
        assert int_to_mini_roman(0) == ""

    def test_invalid_input_greater_than_1000(self):
        assert int_to_mini_roman(1001) == ""