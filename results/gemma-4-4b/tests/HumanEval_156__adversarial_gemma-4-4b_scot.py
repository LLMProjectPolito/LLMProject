
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

    return result

import pytest

# STEP 1: REASONING
# The function `int_to_mini_roman` converts an integer to its Roman numeral representation.
# The constraints are 1 <= number <= 1000.
# The function should return the Roman numeral string in lowercase.
# We need to test various cases, including:
# - Single-digit numbers (1-9)
# - Numbers in the teens (10-19)
# - Numbers in the twenties (20-29)
# - Numbers in the thirties (30-39)
# - Numbers in the forties (40-49)
# - Numbers in the fifties (50-59)
# - Numbers in the sixties (60-69)
# - Numbers in the seventies (70-79)
# - Numbers in the eighties (80-89)
# - Numbers in the nineties (90-99)
# - Numbers in the hundreds (100-999)
# - Edge cases like 4, 9, 40, 90, 400, 900, 1000.
# - Invalid input (although the problem statement specifies 1 <= number <= 1000, it's good to check).

# STEP 2: PLAN
# Test functions:
# - test_single_digit_numbers: Test numbers 1-9
# - test_teen_numbers: Test numbers 10-19
# - test_twenties_to_eighties: Test numbers 20-89
# - test_ninenties: Test numbers 90-99
# - test_hundreds: Test numbers 100-999
# - test_edge_cases: Test 4, 9, 40, 90, 400, 900, 1000
# - test_invalid_input: Test numbers outside the range 1-1000 (optional, but good practice)

# STEP 3: CODE
class TestIntToMiniRoman:
    def test_single_digit_numbers(self):
        assert int_to_mini_roman(1) == 'i'
        assert int_to_mini_roman(2) == 'ii'
        assert int_to_mini_roman(3) == 'iii'
        assert int_to_mini_roman(4) == 'iv'
        assert int_to_mini_roman(5) == 'v'
        assert int_to_mini_roman(6) == 'vi'
        assert int_to_mini_roman(7) == 'vii'
        assert int_to_mini_roman(8) == 'viii'
        assert int_to_mini_roman(9) == 'ix'

    def test_teen_numbers(self):
        assert int_to_mini_roman(10) == 'x'
        assert int_to_mini_roman(11) == 'xi'
        assert int_to_mini_roman(12) == 'xii'
        assert int_to_mini_roman(13) == 'xiii'
        assert int_to_mini_roman(14) == 'xiv'
        assert int_to_mini_roman(15) == 'xv'
        assert int_to_mini_roman(16) == 'xvi'
        assert int_to_mini_roman(17) == 'xvii'
        assert int_to_mini_roman(18) == 'xviii'
        assert int_to_mini_roman(19) == 'xix'

    def test_twenties_to_eighties(self):
        assert int_to_mini_roman(20) == 'xx'
        assert int_to_mini_roman(30) == 'xxx'
        assert int_to_mini_roman(40) == 'xl'
        assert int_to_mini_roman(50) == 'l'
        assert int_to_mini_roman(60) == 'lx'
        assert int_to_mini_roman(70) == 'lxx'
        assert int_to_mini_roman(80) == 'lxxx'

    def test_nineties(self):
        assert int_to_mini_roman(90) == 'xc'
        assert int_to_mini_roman(100) == 'c'
        assert int_to_mini_roman(110) == 'cxi'
        assert int_to_mini_roman(120) == 'cxx'
        assert int_to_mini_roman(130) == 'cxxx'
        assert int_to_mini_roman(140) == 'cxl'
        assert int_to_mini_roman(150) == 'cl'
        assert int_to_mini_roman(160) == 'clx'
        assert int_to_mini_roman(170) == 'clxx'
        assert int_to_mini_roman(180) == 'clxxx'
        assert int_to_mini_roman(190) == 'cxix'

    def test_hundreds(self):
        assert int_to_mini_roman(400) == 'cd'
        assert int_to_mini_roman(500) == 'd'
        assert int_to_mini_roman(600) == 'dc'
        assert int_to_mini_roman(700) == 'dcc'
        assert int_to_mini_roman(800) == 'dccx'
        assert int_to_mini_roman(900) == 'cm'
        assert int_to_mini_roman(1000) == 'm'

    def test_edge_cases(self):
        assert int_to_mini_roman(4) == 'iv'
        assert int_to_mini_roman(9) == 'ix'
        assert int_to_mini_roman(40) == 'xl'
        assert int_to_mini_roman(90) == 'xc'
        assert int_to_mini_roman(400) == 'cd'
        assert int_to_mini_roman(900) == 'cm'
        assert int_to_mini_roman(1000) == 'm'

    def test_invalid_input(self):
        with pytest.raises(AssertionError):
            int_to_mini_roman(0)
        with pytest.raises(AssertionError):
            int_to_mini_roman(1001)