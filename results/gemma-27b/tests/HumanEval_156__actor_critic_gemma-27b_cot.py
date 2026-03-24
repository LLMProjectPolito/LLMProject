
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
import random

def test_int_to_mini_roman_basic():
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

def test_int_to_mini_roman_tens():
    assert int_to_mini_roman(20) == 'xx'
    assert int_to_mini_roman(30) == 'xxx'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(60) == 'lx'
    assert int_to_mini_roman(70) == 'lxx'
    assert int_to_mini_roman(80) == 'lxxx'
    assert int_to_mini_roman(90) == 'xc'

def test_int_to_mini_roman_hundreds():
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(200) == 'cc'
    assert int_to_mini_roman(300) == 'ccc'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(600) == 'dc'
    assert int_to_mini_roman(700) == 'dcc'
    assert int_to_mini_roman(800) == 'dccc'
    assert int_to_mini_roman(900) == 'cm'

def test_int_to_mini_roman_combined():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(44) == 'xliv'
    assert int_to_mini_roman(99) == 'xcix'
    assert int_to_mini_roman(149) == 'cxlix'
    assert int_to_mini_roman(444) == 'cdxliv'
    assert int_to_mini_roman(944) == 'cmxliv'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(888) == 'dccclxxxviii'

def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_maximum():
    assert int_to_mini_roman(3999) == 'mmmcmxcix'

def test_int_to_mini_roman_zero():
    with pytest.raises(ValueError):
        int_to_mini_roman(0)

def test_int_to_mini_roman_negative():
    with pytest.raises(ValueError):
        int_to_mini_roman(-1)

def test_int_to_mini_roman_invalid_input():
    pytest.mark.parametrize(
        "invalid_input",
        [1.5, "1", 4000, -10, 0]
    )
    def test_invalid(invalid_input):
        if isinstance(invalid_input, float):
            with pytest.raises(TypeError):
                int_to_mini_roman(invalid_input)
        elif isinstance(invalid_input, str):
            with pytest.raises(TypeError):
                int_to_mini_roman(invalid_input)
        else:
            with pytest.raises(ValueError):
                int_to_mini_roman(invalid_input)

def test_int_to_mini_roman_random():
    for _ in range(10):
        num = random.randint(1, 3999)
        int_to_mini_roman(num)