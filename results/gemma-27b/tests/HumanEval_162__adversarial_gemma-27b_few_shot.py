
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
    return hashlib.md5(text.encode()).hexdigest()

def test_md5_basic():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_md5_empty():
    assert string_to_md5('') == None

def test_md5_single_char():
    assert string_to_md5('a') == '0cc175b9c0f1b6a831c399e269772661'

def test_md5_long_string():
    long_string = "This is a very long string to test the MD5 function."
    expected_md5 = '9f86d081884c7d659a2feaa0c55ad015'
    assert string_to_md5(long_string) == expected_md5

def test_md5_with_numbers():
    assert string_to_md5('12345') == '5994471abb01112afcc18159f6cc74b4'

def test_md5_with_special_chars():
    assert string_to_md5('!@#$%^') == 'b10a8db164e0754105b7a99be72e3fe5'

def test_md5_unicode():
    assert string_to_md5('你好世界') == '6f9d9999999999999999999999999999' # Example unicode string