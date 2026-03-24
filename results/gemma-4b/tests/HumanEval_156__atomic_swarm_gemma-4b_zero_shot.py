
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

import pytest

def test_basic():
    assert int_to_mini_roman(19) == 'xix'

import pytest

def test_edge_zero():
    assert int_to_mini_roman(0) == ''

import pytest

def test_int_to_mini_roman_invalid_input():
    with pytest.raises(ValueError):
        int_to_mini_roman(0)
        int_to_mini_roman(-1)
        int_to_mini_roman(1001)