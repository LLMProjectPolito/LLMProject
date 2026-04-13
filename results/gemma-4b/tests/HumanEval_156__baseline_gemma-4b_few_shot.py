
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

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

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

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None

def test_int_to_mini_roman_1():
    assert int_to_mini_roman(19) == 'xix'

def test_int_to_mini_roman_2():
    assert int_to_mini_roman(152) == 'clii'

def test_int_to_mini_roman_3():
    assert int_to_mini_roman(426) == 'cdxxvi'

def test_int_to_mini_roman_4():
    assert int_to_mini_roman(4) == 'iv'

def test_int_to_mini_roman_5():
    assert int_to_mini_roman(9) == 'ix'

def test_int_to_mini_roman_10():
    assert int_to_mini_roman(10) == 'x'

def test_int_to_mini_roman_100():
    assert int_to_mini_roman(100) == 'c'

def test_int_to_mini_roman_400():
    assert int_to_mini_roman(400) == 'cd'

def test_int_to_mini_roman_500():
    assert int_to_mini_roman(500) == 'd'

def test_int_to_mini_roman_900():
    assert int_to_mini_roman(900) == 'cm'

def test_int_to_mini_roman_1000():
    assert int_to_mini_roman(1000) == 'm'