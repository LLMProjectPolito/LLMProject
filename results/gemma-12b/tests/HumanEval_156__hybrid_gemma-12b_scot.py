
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

    return result.lower()


class TestIntToMiniRoman:
    def test_valid_input_range(self):
        assert int_to_mini_roman(50) == 'l'
        assert int_to_mini_roman(250) == 'cccl'
        assert int_to_mini_roman(777) == 'cccclxxvii'
        assert int_to_mini_roman(999) == 'dcccxcix'

    def test_boundary_values(self):
        assert int_to_mini_roman(1) == 'i'
        assert int_to_mini_roman(1000) == 'm'

    def test_simple_numbers(self):
        assert int_to_mini_roman(1) == 'i'
        assert int_to_mini_roman(5) == 'v'
        assert int_to_mini_roman(10) == 'x'
        assert int_to_mini_roman(50) == 'l'
        assert int_to_mini_roman(100) == 'c'

    def test_numbers_with_repetitions(self):
        assert int_to_mini_roman(3) == 'iii'
        assert int_to_mini_roman(20) == 'xx'
        assert int_to_mini_roman(80) == 'lxxx'
        assert int_to_mini_roman(300) == 'ccc'

    def test_numbers_with_mixed_symbols(self):
        assert int_to_mini_roman(7) == 'vii'
        assert int_to_mini_roman(35) == 'xxxv'
        assert int_to_mini_roman(147) == 'cxlvii'

    def test_typical_numbers(self):
        assert int_to_mini_roman(19) == 'xix'
        assert int_to_mini_roman(152) == 'clii'
        assert int_to_mini_roman(426) == 'cdxxvi'

    def test_invalid_input_less_than_1(self):
        with pytest.raises(TypeError):
            int_to_mini_roman(0)

    def test_invalid_input_greater_than_1000(self):
        with pytest.raises(TypeError):
            int_to_mini_roman(1001)

    def test_zero_input(self):
        with pytest.raises(TypeError):
            int_to_mini_roman(0)