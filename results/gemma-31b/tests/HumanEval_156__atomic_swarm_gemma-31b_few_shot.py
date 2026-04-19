
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

def test_int_to_mini_roman():
    assert int_to_mini_roman(152) == 'clii'

def test_max_limit():
    assert int_to_mini_roman(1000) == 'm'

import pytest

def test_int_to_mini_roman_out_of_bounds():
    with pytest.raises(ValueError):
        int_to_mini_roman(0)