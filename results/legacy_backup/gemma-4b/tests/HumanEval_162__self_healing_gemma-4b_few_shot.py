import hashlib
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

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None

def test_string_to_md5_basic():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty():
    assert string_to_md5('') == None

def test_string_to_md5_case_insensitive():
    assert string_to_md5('Hello World') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_with_spaces():
    assert string_to_md5('  Hello   World  ') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_with_special_chars():
    assert string_to_md5('Hello!@#World') == '3e25960a79dbc69b674cd4ec67a72c62'