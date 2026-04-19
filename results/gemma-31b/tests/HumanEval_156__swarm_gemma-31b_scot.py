
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
import math

def test_int_to_mini_roman_complex_subtraction():
    """Test the most complex subtractive case within the allowed range (999)."""
    assert int_to_mini_roman(999) == 'cmxcix'

def test_int_to_mini_roman_upper_boundary():
    """Test the upper boundary constraint of the function (number = 1000)."""
    assert int_to_mini_roman(1000) == 'm'