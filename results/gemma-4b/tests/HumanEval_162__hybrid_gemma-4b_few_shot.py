
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()


def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Racecar') == True
    assert is_palindrome('Was it a car or a cat I saw?') == True
    assert is_palindrome('Madam') == True
    assert is_palindrome('level') == True
    assert is_palindrome('rotor') == True
    assert is_palindrome('stats') == True
    assert is_palindrome('noon') == True
    assert is_palindrome('12321') == True
    assert is_palindrome('12345') == False

def test_is_palindrome_empty():
    assert is_palindrome('') == True

def test_is_palindrome_whitespace():
    assert is_palindrome('  ') == True
    assert is_palindrome(' a ') == True

def test_is_palindrome_mixed_case():
    assert is_palindrome('Racecar') == True
    assert is_palindrome('RaCeCaR') == True

def test_is_palindrome_with_punctuation():
    assert is_palindrome('A man, a plan, a canal: Panama') == True
    assert is_palindrome('Madam, I\'m Adam') == True

def test_max_positive():
    assert get_max([1, 2, 3]) == 3
    assert get_max([3, 2, 1]) == 3
    assert get_max([1, 3, 2]) == 3
    assert get_max([-1, 0, 1]) == 1
    assert get_max([5, 5, 5]) == 5

def test_max_empty():
    assert get_max([]) == None

def test_max_single_element():
    assert get_max([5]) == 5

def test_max_negative_numbers():
    assert get_max([-1, -2, -3]) == -1

def test_max_mixed_positive_negative():
    assert get_max([-1, 0, 1]) == 1
    assert get_max([-5, -2, 0, 3]) == 3

def test_string_to_md5_basic():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert string_to_md5('abc') == 'b10a8db164e0754105b7a99be72e3fe5'
    assert string_to_md5('') == None

def test_string_to_md5_empty():
    assert string_to_md5('') == None

def test_string_to_md5_unicode():
    assert string_to_md5('你好世界') == 'b94d27b9934d3e08a52e52d442038e5a'

def test_string_to_md5_special_characters():
    assert string_to_md5('!@#$%^') == '689679639477331339636363636363'

def test_string_to_md5_mixed():
    assert string_to_md5('Hello World!') == '6e2d1a49989999999999999999999999'

def test_string_to_md5_long_string():
    long_string = "This is a very long string to test the md5 function."
    expected_md5 = '89669393969396939693969396939693'
    assert string_to_md5(long_string) == expected_md5