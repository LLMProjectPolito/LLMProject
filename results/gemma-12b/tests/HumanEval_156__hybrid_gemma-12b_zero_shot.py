
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
from your_module import int_to_mini_roman  # Replace your_module

class TestIntToMiniRoman:
    """
    Pytest suite for the int_to_mini_roman function.
    """

    def test_valid_input_range(self):
        """
        Test that the function handles numbers within the valid range (1-1000).
        """
        assert int_to_mini_roman(1) == 'i'
        assert int_to_mini_roman(1000) == 'm'

    def test_single_digit_numbers(self):
        """
        Test single-digit numbers.
        """
        assert int_to_mini_roman(1) == 'i'
        assert int_to_mini_roman(2) == 'ii'
        assert int_to_mini_roman(3) == 'iii'
        assert int_to_mini_roman(4) == 'iv'
        assert int_to_mini_roman(5) == 'v'
        assert int_to_mini_roman(6) == 'vi'
        assert int_to_mini_roman(7) == 'vii'
        assert int_to_mini_roman(8) == 'viii'
        assert int_to_mini_roman(9) == 'ix'

    def test_tens_and_hundreds(self):
        """
        Test numbers involving tens and hundreds.
        """
        assert int_to_mini_roman(10) == 'x'
        assert int_to_mini_roman(20) == 'xx'
        assert int_to_mini_roman(30) == 'xxx'
        assert int_to_mini_roman(40) == 'xl'
        assert int_to_mini_roman(50) == 'l'
        assert int_to_mini_roman(60) == 'lx'
        assert int_to_mini_roman(70) == 'lxx'
        assert int_to_mini_roman(80) == 'lxxx'
        assert int_to_mini_roman(90) == 'xc'
        assert int_to_mini_roman(100) == 'c'
        assert int_to_mini_roman(200) == 'cc'
        assert int_to_mini_roman(300) == 'ccc'
        assert int_to_mini_roman(400) == 'cd'
        assert int_to_mini_roman(500) == 'd'
        assert int_to_mini_roman(600) == 'dc'
        assert int_to_mini_roman(700) == 'dcc'
        assert int_to_mini_roman(800) == 'dccc'
        assert int_to_mini_roman(900) == 'cm'

    def test_combined_numbers(self):
        """
        Test numbers that combine different values.
        """
        assert int_to_mini_roman(19) == 'xix'
        assert int_to_mini_roman(42) == 'xlii'
        assert int_to_mini_roman(99) == 'xciii'
        assert int_to_mini_roman(152) == 'clii'
        assert int_to_mini_roman(426) == 'cdxxvi'
        assert int_to_mini_roman(789) == 'dccclxxxix'
        assert int_to_mini_roman(944) == 'cmlxxxiiii'
        assert int_to_mini_roman(999) == 'cmxciii'

    def test_edge_cases(self):
        """
        Test edge cases and boundary conditions.
        """
        assert int_to_mini_roman(3) == 'iii'
        assert int_to_mini_roman(8) == 'viii'
        assert int_to_mini_roman(39) == 'xxxix'
        assert int_to_mini_roman(44) == 'xliv'
        assert int_to_mini_roman(49) == 'xlix'
        assert int_to_mini_roman(89) == 'lxxxix'
        assert int_to_mini_roman(94) == 'xciv'
        assert int_to_mini_roman(999) == 'cmxcix'

    def test_invalid_input_below_range(self):
        """
        Test that the function raises a ValueError for numbers below 1.
        """
        with pytest.raises(ValueError):
            int_to_mini_roman(0)
        with pytest.raises(ValueError):
            int_to_mini_roman(-5)

    def test_invalid_input_above_range(self):
        """
        Test that the function raises a ValueError for numbers above 1000.
        """
        with pytest.raises(ValueError):
            int_to_mini_roman(1001)
        with pytest.raises(ValueError):
            int_to_mini_roman(2000)

    def test_all_lowercase(self):
        """
        Test that the output is always in lowercase.
        """
        assert int_to_mini_roman(1) == 'i'
        assert int_to_mini_roman(10) == 'x'
        assert int_to_mini_roman(100) == 'c'
        assert int_to_mini_roman(1000) == 'm'
        assert int_to_mini_roman(426) == 'cdxxvi'