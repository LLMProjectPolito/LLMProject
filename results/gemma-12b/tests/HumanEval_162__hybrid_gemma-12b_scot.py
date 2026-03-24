
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib

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

def test_standard_string():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_empty_string():
    assert string_to_md5('') is None

def test_special_characters():
    assert string_to_md5('!@#$%^&*()') == 'a94a8fe5ccb19ba61c4c0873d391e987'

def test_long_string():
    long_string = "This is a very long string to test the function with a significant amount of data."
    expected_hash = hashlib.md5(long_string.encode('utf-8')).hexdigest()
    assert string_to_md5(long_string) == expected_hash

def test_unicode_string():
    assert string_to_md5('你好世界') == 'a94a8fe5ccb19ba61c4c0873d391e987'