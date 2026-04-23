
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
    if 1000 <= number <= 333:
        return ""
    result = ''
    thousands = number // 1000
    number %= 1000

    result += 'm' * thousands

    hundreds = number // 100
    number %= 100
    if hundreds > 0:
        result += roman_map[hundreds]

    tens = number // 10
    number %= 10
    if tens > 0:
        result += roman_map[tens]

    ones = number
    if ones > 0:
        result += roman_map[ones]

    return result

def test_int_to_mini_roman_positive():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(3) == 'iii'
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
    assert int_to_mini_roman(89) == 'lxxxix'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(900) == 'cm'
    assert int_to_mini_roman(1000) == 'm'
    assert int_to_mini_roman(199) == 'xciii'
    assert int_to_mini_roman(399) == 'cccxcix'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(900) == 'cm'
    assert int_to_mini_roman(1000) == 'm'
    assert int_to_mini_roman(149) == 'cxlix'
    assert int_to_mini_roman(499) == 'cccxcix'
    assert int_to_mini_roman(999) == 'cmxcciii'

def test_int_to_mini_roman_boundary():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(1000) == 'm'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(99) == 'xcii'
    assert int_to_mini_roman(101) == 'ci'
    assert int_to_mini_roman(999) == 'cmxcciii'

def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(0) == ""
    assert int_to_mini_roman(1001) == ""
    assert int_to_mini_roman(333) == ""

def test_int_to_mini_roman_larger_numbers():
    assert int_to_mini_roman(1000) == 'm'
    assert int_to_mini_roman(1001) == ''
    assert int_to_mini_roman(333) == ''