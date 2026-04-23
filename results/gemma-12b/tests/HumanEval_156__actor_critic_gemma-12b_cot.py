
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
    def test_valid_input(self):
        assert int_to_mini_roman(1) == "i"  # Basic case
        assert int_to_mini_roman(4) == "iv"  # Subtractive case
        assert int_to_mini_roman(5) == "v"  # Basic case
        assert int_to_mini_roman(9) == "ix"  # Subtractive case
        assert int_to_mini_roman(10) == "x"  # Basic case
        assert int_to_mini_roman(19) == "xix" # Combination of basic and subtractive
        assert int_to_mini_roman(426) == "cdxxvi" # Complex combination
        assert int_to_mini_roman(152) == "clii" # Combination of basic and subtractive
        assert int_to_mini_roman(444) == "cdxliv" # Complex combination
        assert int_to_mini_roman(999) == "cmxciii" # Complex combination
        assert int_to_mini_roman(1000) == "m" # Maximum value
        assert int_to_mini_roman(3) == "iii" # Repeated symbols
        assert int_to_mini_roman(20) == "xx" # Repeated symbols
        assert int_to_mini_roman(300) == "ccc" # Repeated symbols
        assert int_to_mini_roman(40) == "xl" # Subtractive case
        assert int_to_mini_roman(50) == "l" # Basic case
        assert int_to_mini_roman(90) == "xc" # Subtractive case
        assert int_to_mini_roman(100) == "c" # Basic case
        assert int_to_mini_roman(400) == "cd" # Subtractive case
        assert int_to_mini_roman(500) == "d" # Basic case
        assert int_to_mini_roman(900) == "cm" # Subtractive case

    def test_invalid_input(self):
        with pytest.raises(TypeError):
            int_to_mini_roman("abc")  # Invalid type
        with pytest.raises(ValueError):
            int_to_mini_roman(0)  # Input below minimum
        with pytest.raises(ValueError):
            int_to_mini_roman(1001)  # Input above maximum
        with pytest.raises(ValueError):
            int_to_mini_roman(-1) # Negative input