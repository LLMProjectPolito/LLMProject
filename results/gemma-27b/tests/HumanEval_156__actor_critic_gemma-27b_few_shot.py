
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

def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(1) == 'i'
    >>> int_to_mini_roman(3) == 'iii'
    >>> int_to_mini_roman(4) == 'iv'
    >>> int_to_mini_roman(5) == 'v'
    >>> int_to_mini_roman(9) == 'ix'
    >>> int_to_mini_roman(10) == 'x'
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(40) == 'xl'
    >>> int_to_mini_roman(50) == 'l'
    >>> int_to_mini_roman(90) == 'xc'
    >>> int_to_mini_roman(100) == 'c'
    >>> int_to_mini_roman(400) == 'cd'
    >>> int_to_mini_roman(500) == 'd'
    >>> int_to_mini_roman(900) == 'cm'
    >>> int_to_mini_roman(1000) == 'm'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    if not 1 <= number <= 1000:
        raise ValueError("Number must be between 1 and 1000")

    roman_map = { 1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}

    result = ""
    for value, numeral in sorted(roman_map.items(), reverse=True):
        while number >= value:
            result += numeral
            number -= value

    return result.lower()

import pytest

def test_int_to_mini_roman_basic():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(3) == 'iii'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(10) == 'x'

def test_int_to_mini_roman_complex():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(900) == 'cm'
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_combined():
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'

def test_int_to_mini_roman_boundary():
    assert int_to_mini_roman(999) == 'cmxcix'
    assert int_to_mini_roman(399) == 'cccxcix'

def test_int_to_mini_roman_out_of_range():
    with pytest.raises(ValueError):
        int_to_mini_roman(0)
    with pytest.raises(ValueError):
        int_to_mini_roman(1001)