
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
    thousands = number // 1000
    number %= 1000
    result += 'm' if thousands > 0 else ''
    hundreds = number // 100
    number %= 100
    result += 'c' if hundreds > 0 else ''
    tens = number // 10
    number %= 10
    result += 'x' if tens > 0 else ''
    ones = number
    result += 'i' if ones > 0 else ''
    return result


import pytest

def test_int_to_mini_roman_basic():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(90) == 'ix'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(900) == 'cm'
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(0) == ''
    assert int_to_mini_roman(1000) == 'm'
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(399) == 'cccxix'
    assert int_to_mini_roman(589) == 'dlxxix'
    assert int_to_mini_roman(999) == 'cmxccii'

def test_int_to_mini_roman_larger_numbers():
    assert int_to_mini_roman(1000) == 'm'
    assert int_to_mini_roman(10000) == 'x' #This is not within the range, but it's good to check
    assert int_to_mini_roman(100000) == 'c' #This is not within the range, but it's good to check
    assert int_to_mini_roman(1000000) == 'm' #This is not within the range, but it's good to check

def test_int_to_mini_roman_with_zero_values():
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(900) == 'cm'