
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

def test_single_digit_conversions():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(2) == 'ii'
    assert int_to_mini_roman(3) == 'iii'
    assert int_to_mini_roman(4) == 'iiii'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(6) == 'vi'
    assert int_to_mini_roman(7) == 'vii'
    assert int_to_mini_roman(8) == 'viii'
    assert int_to_mini_roman(9) == 'ix'

def test_tens_conversions():
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(20) == 'xx'
    assert int_to_mini_roman(30) == 'xxx'
    assert int_to_mini_roman(40) == 'xxxx'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(60) == 'lx'
    assert int_to_mini_roman(70) == 'lxx'
    assert int_to_mini_roman(80) == 'lxxx'
    assert int_to_mini_roman(90) == 'lxxxx'

def test_hundreds_conversions():
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(200) == 'cc'
    assert int_to_mini_roman(300) == 'ccc'
    assert int_to_mini_roman(400) == 'cccc'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(600) == 'dc'
    assert int_to_mini_roman(700) == 'dcc'
    assert int_to_mini_roman(800) == 'dccc'
    assert int_to_mini_roman(900) == 'dcccc'

def test_edge_case_conversions():
    assert int_to_mini_roman(399) == 'ccccxcii'
    assert int_to_mini_roman(400) == 'cccc'
    assert int_to_mini_roman(499) == 'ccccxcii'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(501) == 'diiii'
    assert int_to_mini_roman(899) == 'dcccxcii'
    assert int_to_mini_roman(900) == 'dcccc'
    assert int_to_mini_roman(999) == 'dcccxcix'
    assert int_to_mini_roman(1000) == 'm'

def test_mixed_value_conversions():
    assert int_to_mini_roman(15) == 'xv'
    assert int_to_mini_roman(27) == 'xxvii'
    assert int_to_mini_roman(142) == 'ccxlii'
    assert int_to_mini_roman(456) == 'cdlvvi'
    assert int_to_mini_roman(149) == 'ccxcii'
    assert int_to_mini_roman(488) == 'ccccxxxviii'
    assert int_to_mini_roman(941) == 'dcccxcix'

def test_invalid_input():
    with pytest.raises(ValueError):
        int_to_mini_roman(0)
    with pytest.raises(ValueError):
        int_to_mini_roman(-1)
    with pytest.raises(ValueError):
        int_to_mini_roman(1001)

def test_zero_input():
    with pytest.raises(ValueError):
        int_to_mini_roman(0)