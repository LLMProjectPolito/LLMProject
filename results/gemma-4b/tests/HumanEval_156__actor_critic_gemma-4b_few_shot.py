
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

def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_is_palindrome_empty():
    assert is_palindrome('') == True
    assert is_palindrome(' ') == True
    assert is_palindrome('a') == True

def test_is_palindrome_mixed_case():
    assert is_palindrome('RaDaR') == True
    assert is_palindrome('Hello') == False

def test_is_palindrome_with_punctuation():
    assert is_palindrome('Madam, I\'m Adam') == True
    assert is_palindrome('Was it a car or a cat I saw?') == True

def test_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([5, 2, 8, 1]) == 8
    assert get_max([10, 5, 20, 15]) == 20

def test_max_empty():
    assert get_max([]) == None

def test_max_single_element():
    assert get_max([7]) == 7

def test_max_negative_and_positive():
    assert get_max([-1, 2, -3, 4]) == 4

def test_max_all_negative():
    assert get_max([-1, -2, -3]) == -1

def test_int_to_mini_roman_1():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(9) == 'ix'

def test_int_to_mini_roman_10():
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(90) == 'xc'

def test_int_to_mini_roman_100():
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(900) == 'cm'

def test_int_to_mini_roman_1000():
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_19():
    assert int_to_mini_roman(19) == 'xix'

def test_int_to_mini_roman_152():
    assert int_to_mini_roman(152) == 'clii'

def test_int_to_mini_roman_426():
    assert int_to_mini_roman(426) == 'cdxxvi'

def test_int_to_mini_roman_999():
    assert int_to_mini_roman(999) == 'cmlxix'

def test_int_to_mini_roman_1000():
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_8():
    assert int_to_mini_roman(8) == 'viii'

def test_int_to_mini_roman_6():
    assert int_to_mini_roman(6) == 'vi'