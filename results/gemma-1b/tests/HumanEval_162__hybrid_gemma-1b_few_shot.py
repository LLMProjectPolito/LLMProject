
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import hashlib
import pytest

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    return md5_hash

def test_string_to_md5_positive():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty():
    assert string_to_md5('') is None

def test_string_to_md5_single_char():
    assert string_to_md5('a') == '7f4a9893937a7f4a98937a7f4a98937'

def test_string_to_md5_mixed_case():
    assert string_to_md5('Hello World') == '7f4a9893937a7f4a98937a7f4a98937'

def test_string_to_md5_numbers():
    assert string_to_md5('12345') == '7f4a9893937a7f4a98937a7f4a98937'

def test_string_to_md5_symbols():
    assert string_to_md5('!@#$%^') == '7f4a9893937a7f4a98937a7f4a98937'

def test_is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    return s == s[::-1]

def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_is_palindrome_mixed_case():
    assert is_palindrome('Racecar') == True
    assert is_palindrome('hello') == False

def test_is_palindrome_numbers():
    assert is_palindrome('12345') == True
    assert is_palindrome('12345') == True

def test_is_palindrome_symbols():
    assert is_palindrome('!@#$%^') == True
    assert is_palindrome('!@#$%^') == True