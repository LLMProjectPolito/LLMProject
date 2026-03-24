
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

def test_numbers_1_to_999():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(123) == 'ccxxxi'
    assert int_to_mini_roman(789) == 'ddccclxxxix'
    assert int_to_mini_roman(999) == 'dcccxcix'
    assert int_to_mini_roman(998) == 'dcccxcviiii'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(200) == 'cc'
    assert int_to_mini_roman(300) == 'ccc'
    assert int_to_mini_roman(400) == 'cccc'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(600) == 'dc'
    assert int_to_mini_roman(700) == 'dcc'
    assert int_to_mini_roman(800) == 'dccc'
    assert int_to_mini_roman(900) == 'dcccc'
    assert int_to_mini_roman(15) == 'xv'
    assert int_to_mini_roman(27) == 'xxvii'
    assert int_to_mini_roman(142) == 'cxlii'
    assert int_to_mini_roman(456) == 'cdlvii'
    assert int_to_mini_roman(999) == 'dcccxcix'


def test_edge_cases_and_zero():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(999) == 'dcccxcix'
    assert int_to_mini_roman(0) == '' # Explicitly test zero.  The function should return an empty string.


def test_invalid_input():
    with pytest.raises(ValueError):
        int_to_mini_roman(0)
    with pytest.raises(ValueError):
        int_to_mini_roman(1000)
    with pytest.raises(ValueError):
        int_to_mini_roman(-1)