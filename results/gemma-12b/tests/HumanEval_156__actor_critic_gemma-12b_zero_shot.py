
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
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    if not 1 <= number <= 1000:
        raise ValueError("Input must be between 1 and 1000.")

    roman_map = { 1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}
    integers = tuple(roman_map.keys())
    symbols = tuple(roman_map.values())

    i = len(integers) - 1
    result = ""

    while number != 0:
        if integers[i] <= number:
            result += symbols[i]
            number -= integers[i]
        else:
            i -= 1

    return result.lower()


class TestIntToMiniRoman:
    def test_positive_integers_within_range(self):
        assert int_to_mini_roman(1) == 'i'
        assert int_to_mini_roman(2) == 'ii'
        assert int_to_mini_roman(3) == 'iii'
        assert int_to_mini_roman(4) == 'iv'
        assert int_to_mini_roman(5) == 'v'
        assert int_to_mini_roman(9) == 'ix'
        assert int_to_mini_roman(10) == 'x'
        assert int_to_mini_roman(19) == 'xix'
        assert int_to_mini_roman(42) == 'xlii'
        assert int_to_mini_roman(44) == 'xliv'
        assert int_to_mini_roman(49) == 'xlix'
        assert int_to_mini_roman(50) == 'l'
        assert int_to_mini_roman(90) == 'xc'
        assert int_to_mini_roman(100) == 'c'
        assert int_to_mini_roman(141) == 'cxlxi'
        assert int_to_mini_roman(152) == 'clii'
        assert int_to_mini_roman(426) == 'cdxxvi'
        assert int_to_mini_roman(444) == 'cdxliv'
        assert int_to_mini_roman(499) == 'cdxciii'
        assert int_to_mini_roman(500) == 'd'
        assert int_to_mini_roman(900) == 'cm'
        assert int_to_mini_roman(999) == 'cmxciii'
        assert int_to_mini_roman(1000) == 'm'
        assert int_to_mini_roman(899) == 'dccxcix'
        assert int_to_mini_roman(949) == 'cmxlix'
        assert int_to_mini_roman(998) == 'cmxciii'

    def test_edge_cases(self):
        assert int_to_mini_roman(1) == 'i'
        assert int_to_mini_roman(1000) == 'm'
        assert int_to_mini_roman(399) == 'cccxcix'
        assert int_to_mini_roman(501) == 'di'
        assert int_to_mini_roman(901) == 'cmi'

    def test_invalid_input(self):
        with pytest.raises(TypeError):
            int_to_mini_roman("abc")
        with pytest.raises(ValueError):
            int_to_mini_roman(0)
        with pytest.raises(ValueError):
            int_to_mini_roman(1001)
        with pytest.raises(TypeError):
            int_to_mini_roman(1.5)
        with pytest.raises(TypeError):
            int_to_mini_roman([1])