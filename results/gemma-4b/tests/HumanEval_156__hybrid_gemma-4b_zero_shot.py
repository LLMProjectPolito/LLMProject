
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

class TestIntToMiniRoman:
    def test_basic(self):
        assert int_to_mini_roman(1) == 'i'
        assert int_to_mini_roman(2) == 'ii'
        assert int_to_mini_roman(3) == 'iii'
        assert int_to_mini_roman(4) == 'iv'
        assert int_to_mini_roman(5) == 'v'
        assert int_to_mini_roman(6) == 'vi'
        assert int_to_mini_roman(7) == 'vii'
        assert int_to_mini_roman(8) == 'viii'
        assert int_to_mini_roman(9) == 'ix'
        assert int_to_mini_roman(10) == 'x'

    def test_examples(self):
        assert int_to_mini_roman(19) == 'xix'
        assert int_to_mini_roman(152) == 'clii'
        assert int_to_mini_roman(426) == 'cdxxvi'
        assert int_to_mini_roman(94) == 'xciv'
        assert int_to_mini_roman(49) == 'xlix'

    def test_edge_cases(self):
        assert int_to_mini_roman(100) == 'c'
        assert int_to_mini_roman(400) == 'cd'
        assert int_to_mini_roman(900) == 'cm'
        assert int_to_mini_roman(1000) == 'm'

    def test_larger_numbers(self):
        assert int_to_mini_roman(20) == 'xx'
        assert int_to_mini_roman(39) == 'xxxix'
        assert int_to_mini_roman(499) == 'ubciii'
        assert int_to_mini_roman(500) == 'd'
        assert int_to_mini_roman(888) == 'ccclxxxviii'

    def test_mixed(self):
        assert int_to_mini_roman(14) == 'xiv'
        assert int_to_mini_roman(27) == 'xxvii'
        assert int_to_mini_roman(38) == 'xxxviii'
        assert int_to_mini_roman(44) == 'xliv'
        assert int_to_mini_roman(58) == 'lviii'
        assert int_to_mini_roman(64) == 'lxiv'
        assert int_to_mini_roman(79) == 'lxxix'
        assert int_to_mini_roman(84) == 'lxxxiv'
        assert int_to_mini_roman(94) == 'xciv'