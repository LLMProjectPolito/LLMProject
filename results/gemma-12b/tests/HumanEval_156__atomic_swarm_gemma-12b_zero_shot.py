
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

def test_int_to_mini_roman_positive():
    assert int_to_mini_roman(19) == 'xix'

def test_edge_min_value():
    assert int_to_mini_roman(1) == 'i'

def test_invalid_input_type():
    """Test that the function raises a TypeError if the input is not an integer."""
    try:
        int_to_mini_roman("abc")
    except TypeError:
        assert True
    else:
        assert False