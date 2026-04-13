
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

def test_int_to_mini_roman_teens():
    assert int_to_mini_roman(11) == 'xi'
    assert int_to_mini_roman(12) == 'xii'
    assert int_to_mini_roman(13) == 'xiii'
    assert int_to_mini_roman(14) == 'xiv'
    assert int_to_mini_roman(15) == 'xv'
    assert int_to_mini_roman(16) == 'xvi'
    assert int_to_mini_roman(17) == 'xvii'
    assert int_to_mini_roman(18) == 'xviii'
    assert int_to_mini_roman(19) == 'xix'

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

def test_int_to_mini_roman_complex():
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(888) == 'dccclxxxviii'
    assert int_to_mini_roman(999) == 'cmxcix'
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_invalid_input():
    with pytest.raises(TypeError):
        int_to_mini_roman(1.5)
    with pytest.raises(TypeError):
        int_to_mini_roman("1")
    with pytest.raises(ValueError):
        int_to_mini_roman(0)
    with pytest.raises(ValueError):
        int_to_mini_roman(1001)