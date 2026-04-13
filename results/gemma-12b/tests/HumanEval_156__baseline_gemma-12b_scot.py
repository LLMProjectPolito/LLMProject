
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
# - Numbers with different combinations of Roman numerals (I, V, X, L, C, D)
# - Numbers requiring subtractive notation (e.g., 4, 9, 40, 90, 400, 900)
# - Numbers with no subtractive notation
# - Invalid input (outside the range 1-1000) - although the prompt doesn't explicitly require this, it's good practice.

# STEP 2: PLAN
# Test functions:
# - test_valid_input_boundary_1: Test the boundary value 1.
# - test_valid_input_boundary_1000: Test the boundary value 1000.
# - test_valid_input_simple_numbers: Test simple numbers like 3, 4, 5, 9, 10.
# - test_valid_input_mixed_numbers: Test numbers with mixed Roman numerals (e.g., 15, 27, 42, 99).
# - test_valid_input_subtractive_notation: Test numbers requiring subtractive notation (e.g., 4, 9, 40, 90, 400, 900).
# - test_valid_input_larger_numbers: Test larger numbers (e.g., 152, 426, 987).
# - test_invalid_input_less_than_1: Test input less than 1.
# - test_invalid_input_greater_than_1000: Test input greater than 1000.

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
    i = 12
    result = ""

    while number != 0:
        if list(roman_map.keys())[i] <= number:
            result += list(roman_map.values())[i]
            number -= list(roman_map.keys())[i]
        else:
            i -= 1

    return result.lower()

class TestIntToMiniRoman:
    def test_valid_input_boundary_1(self):
        assert int_to_mini_roman(1) == "i"

    def test_valid_input_boundary_1000(self):
        assert int_to_mini_roman(1000) == "m"

    def test_valid_input_simple_numbers(self):
        assert int_to_mini_roman(3) == "iii"
        assert int_to_mini_roman(4) == "iv"
        assert int_to_mini_roman(5) == "v"
        assert int_to_mini_roman(9) == "ix"
        assert int_to_mini_roman(10) == "x"

    def test_valid_input_mixed_numbers(self):
        assert int_to_mini_roman(15) == "xv"
        assert int_to_mini_roman(27) == "xxvii"
        assert int_to_mini_roman(42) == "xlii"
        assert int_to_mini_roman(99) == "xciii"

    def test_valid_input_subtractive_notation(self):
        assert int_to_mini_roman(40) == "xl"
        assert int_to_mini_roman(90) == "xc"
        assert int_to_mini_roman(400) == "cd"
        assert int_to_mini_roman(900) == "cm"

    def test_valid_input_larger_numbers(self):
        assert int_to_mini_roman(152) == "clii"
        assert int_to_mini_roman(426) == "cdxxvi"
        assert int_to_mini_roman(987) == "cmlxxxvii"

    def test_invalid_input_less_than_1(self):
        assert int_to_mini_roman(0) == ""

    def test_invalid_input_greater_than_1000(self):
        assert int_to_mini_roman(1001) == ""