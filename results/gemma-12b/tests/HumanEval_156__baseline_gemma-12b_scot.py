
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
# The constraints are crucial: the input must be within the range [1, 1000].
# The output must be a lowercase string.
# We need to test various scenarios, including:
# - Single-digit numbers (1-9)
# - Numbers with tens (10-99)
# - Numbers with hundreds (100-999)
# - Boundary values (1, 1000)
# - Numbers requiring subtractive notation (4, 9, 40, 90, 400, 900)
# - Numbers with combinations of these (e.g., 19, 426)
# - Invalid input (outside the range 1-1000) - although the prompt doesn't specify how to handle this, we'll test for it.

# STEP 2: PLAN
# Test functions:
# - test_single_digit_numbers: Tests numbers from 1 to 9.
# - test_tens: Tests numbers from 10 to 99.
# - test_hundreds: Tests numbers from 100 to 999.
# - test_boundary_values: Tests 1 and 1000.
# - test_subtractive_notation: Tests numbers requiring subtractive notation (4, 9, 40, 90, 400, 900).
# - test_combined_numbers: Tests numbers with combinations of single digits, tens, and hundreds (e.g., 19, 426).
# - test_invalid_input: Tests numbers outside the range [1, 1000].  We'll expect a ValueError.

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
    def test_single_digit_numbers(self):
        assert int_to_mini_roman(1) == "i"
        assert int_to_mini_roman(2) == "ii"
        assert int_to_mini_roman(3) == "iii"
        assert int_to_mini_roman(4) == "iv"
        assert int_to_mini_roman(5) == "v"
        assert int_to_mini_roman(6) == "vi"
        assert int_to_mini_roman(7) == "vii"
        assert int_to_mini_roman(8) == "viii"
        assert int_to_mini_roman(9) == "ix"

    def test_tens(self):
        assert int_to_mini_roman(10) == "x"
        assert int_to_mini_roman(20) == "xx"
        assert int_to_mini_roman(30) == "xxx"
        assert int_to_mini_roman(40) == "xl"
        assert int_to_mini_roman(50) == "l"
        assert int_to_mini_roman(60) == "lx"
        assert int_to_mini_roman(70) == "lxx"
        assert int_to_mini_roman(80) == "lxxx"
        assert int_to_mini_roman(90) == "xc"

    def test_hundreds(self):
        assert int_to_mini_roman(100) == "c"
        assert int_to_mini_roman(200) == "cc"
        assert int_to_mini_roman(300) == "ccc"
        assert int_to_mini_roman(400) == "cd"
        assert int_to_mini_roman(500) == "d"
        assert int_to_mini_roman(600) == "dc"
        assert int_to_mini_roman(700) == "dcc"
        assert int_to_mini_roman(800) == "dccc"
        assert int_to_mini_roman(900) == "cm"

    def test_boundary_values(self):
        assert int_to_mini_roman(1) == "i"
        assert int_to_mini_roman(1000) == "m"

    def test_subtractive_notation(self):
        assert int_to_mini_roman(4) == "iv"
        assert int_to_mini_roman(9) == "ix"
        assert int_to_mini_roman(40) == "xl"
        assert int_to_mini_roman(90) == "xc"
        assert int_to_mini_roman(400) == "cd"
        assert int_to_mini_roman(900) == "cm"

    def test_combined_numbers(self):
        assert int_to_mini_roman(19) == "xix"
        assert int_to_mini_roman(426) == "cdxxvi"
        assert int_to_mini_roman(152) == "clii"
        assert int_to_mini_roman(999) == "cmxciX"

    def test_invalid_input(self):
        with pytest.raises(ValueError):
            int_to_mini_roman(0)
        with pytest.raises(ValueError):
            int_to_mini_roman(1001)
        with pytest.raises(ValueError):
            int_to_mini_roman(-1)