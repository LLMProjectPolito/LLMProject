
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
    roman_map = { 1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}
    integers = list(roman_map)
    symbols = list(roman_map.values())

    i = 12
    result = ""

    while number != 0:
        if integers[i] <= number:
            result += symbols[i]
            number -= integers[i]
        else:
            i -= 1

    return result

def test_edge_zero():
    assert int_to_mini_roman(0) == ""

def test_zero():
    assert int_to_mini_roman(0) == ""

def test_9():
    assert int_to_mini_roman(9) == 'ix'

def test_1():
    assert int_to_mini_roman(1) == 'i'

def test_4():
    assert int_to_mini_roman(4) == 'iv'

def test_5():
    assert int_to_mini_roman(5) == 'v'

def test_10():
    assert int_to_mini_roman(10) == 'x'

def test_40():
    assert int_to_mini_roman(40) == 'xl'

def test_50():
    assert int_to_mini_roman(50) == 'l'

def test_90():
    assert int_to_mini_roman(90) == 'xc'

def test_100():
    assert int_to_mini_roman(100) == 'c'

def test_400():
    assert int_to_mini_roman(400) == 'cd'

def test_500():
    assert int_to_mini_roman(500) == 'd'

def test_900():
    assert int_to_mini_roman(900) == 'cm'

def test_1000():
    assert int_to_mini_roman(1000) == 'm'

def test_19():
    assert int_to_mini_roman(19) == 'xix'

def test_152():
    assert int_to_mini_roman(152) == 'clii'

def test_426():
    assert int_to_mini_roman(426) == 'cdxxvi'