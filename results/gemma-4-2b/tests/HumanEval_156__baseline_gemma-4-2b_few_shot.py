
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
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    roman_map = { 1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xix', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}
    if number in roman_map:
        return roman_map[number]
    result = ''
    while number > 0:
        remainder = number % 10
        if remainder == 1:
            result += 'i'
            number //= 10
        elif remainder == 2:
            result += 'ii'
            number //= 10
        elif remainder == 3:
            result += 'iii'
            number //= 10
        elif remainder == 4:
            result += 'iv'
            number //= 10
        elif remainder == 5:
            result += 'v'
            number //= 10
        elif remainder == 6:
            result += 'vi'
            number //= 10
        elif remainder == 7:
            result += 'vii'
            number //= 10
        elif remainder == 8:
            result += 'viii'
            number //= 10
        elif remainder == 9:
            result += 'ix'
            number //= 10
        else:
            return None
    return result

import pytest

def test_int_to_mini_roman_basic():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(14) == 'xiv'
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(20) == 'xx'
    assert int_to_mini_roman(39) == 'xxxix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(44) == 'xliv'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(58) == 'lvviii'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(94) == 'xlii'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(109) == 'ciix'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(900) == 'cm'
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(0) == ''
    assert int_to_mini_roman(1000) == 'm'
    assert int_to_mini_roman(1001) == 'mci'

def test_int_to_mini_roman_larger_numbers():
    assert int_to_mini_roman(199) == 'xciix'
    assert int_to_mini_roman(399) == 'cccxix'
    assert int_to_mini_roman(499) == 'cccxcix'
    assert int_to_mini_roman(899) == 'lxcxcix'
    assert int_to_mini_roman(999) == 'cmxc'