
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
    roman_map = { 1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}
    i = 12
    result = ""

    while number != 0:
        if list(roman_map.keys())[i] <= number:
            result += list(roman_map.values())[i]
            number -= list(roman_map.keys())[i]
        else:
            i -= 1

    return result.lower()

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


def test_mini_roman_basic():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(1000) == 'm'

def test_mini_roman_combinations():
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(900) == 'cm'

def test_mini_roman_examples():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(1994) == 'mcmxciv'
    assert int_to_mini_roman(3) == 'iii'
    assert int_to_mini_roman(8) == 'viii'
    assert int_to_mini_roman(88) == 'lxxxviii'
    assert int_to_mini_roman(399) == 'cccxcix'

def test_mini_roman_edge_cases():
    assert int_to_mini_roman(1001) == 'm'
    assert int_to_mini_roman(0) == ''
    assert int_to_mini_roman(2023) == 'mmxxiii'
    assert int_to_mini_roman(1000) == 'm'
    assert int_to_mini_roman(1) == 'i'

def test_mini_roman_complex():
    assert int_to_mini_roman(399) == 'cccxcix'
    assert int_to_mini_roman(789) == 'dccLxxxix'
    assert int_to_mini_roman(649) == 'dcxlix'

def test_mini_roman_mid_range():
    assert int_to_mini_roman(250) == 'ccL'
    assert int_to_mini_roman(333) == 'cccxxxiii'
    assert int_to_mini_roman(666) == 'dclxvi'

def test_mini_roman_large_numbers():
    assert int_to_mini_roman(888) == 'dccclxxxviii'
    assert int_to_mini_roman(999) == 'cmxcix'

def test_mini_roman_random_numbers():
    assert int_to_mini_roman(7) == 'vii'
    assert int_to_mini_roman(23) == 'xxiii'
    assert int_to_mini_roman(68) == 'lxviii'
    assert int_to_mini_roman(144) == 'cxliv'
    assert int_to_mini_roman(345) == 'cccxlv'
    assert int_to_mini_roman(678) == 'dclxxviii'
    assert int_to_mini_roman(999) == 'cmxcix'

def test_mini_roman_boundary_values():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(1000) == 'm'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(100) == 'c'

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None