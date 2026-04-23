
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

def test_basic():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(10) == 'x'

def test_tens():
    assert int_to_mini_roman(20) == 'xx'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(90) == 'xc'

def test_hundreds():
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(900) == 'cm'

def test_combined():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(44) == 'xliv'
    assert int_to_mini_roman(99) == 'xcix'
    assert int_to_mini_roman(149) == 'cxlix'
    assert int_to_mini_roman(444) == 'cdxliv'
    assert int_to_mini_roman(944) == 'cmxliv'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(888) == 'dccclxxxviii'

def test_max_value():
    assert int_to_mini_roman(3999) == 'mmmcmxcix'

def test_edge_cases():
    assert int_to_mini_roman(1000) == 'm'

def test_invalid_input():
    with pytest.raises(TypeError):
        int_to_mini_roman(1.5)
    with pytest.raises(TypeError):
        int_to_mini_roman("1")
    with pytest.raises(ValueError):
        int_to_mini_roman(0)
    with pytest.raises(ValueError):
        int_to_mini_roman(-1)
    with pytest.raises(ValueError):
        int_to_mini_roman(4000)
    with pytest.raises(TypeError):
        int_to_mini_roman(None)

def test_random_inputs():
    for _ in range(10):
        num = random.randint(1, 3999)
        int_to_mini_roman(num)  # Just check it doesn't raise an exception