
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
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def test_normal_string():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_empty_string():
    assert string_to_md5("") is None

def test_unicode_string():
    assert string_to_md5("你好世界") == "b10a8db164e0754105b7a99be72e3fe5"

def test_long_string():
    long_string = "a" * 1000
    assert string_to_md5(long_string) == "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3"

def test_special_characters():
    assert string_to_md5("Hello\nworld\t!") == "6cd3556deb0da54bca060b4c39479839"

def test_whitespace_string():
    assert string_to_md5("   ") == "7f9173d89c6999999999999999999999"

def test_emoji():
    assert string_to_md5("Hello 😊 world") == "99999999999999999999999999999999"

def test_large_string():
    large_string = "a" * 1000000
    assert string_to_md5(large_string) == "b10a8db164e0754105b7a99be72e3fe5"