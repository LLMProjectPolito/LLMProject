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

def test_empty_string():
    assert string_to_md5("") is None

def test_valid_string():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_special_characters():
    assert string_to_md5("!@#$%^&*()") == "9496498e999999999999999999999999" or string_to_md5("!@#$%^&*()") == "9a6a9969999999999999999999999999"

def test_long_string():
    long_string = "This is a very long string to test the MD5 hash function." * 10
    assert len(string_to_md5(long_string)) == 32

def test_unicode_string():
    assert string_to_md5("你好世界") == "b10a8db164e0754105b7a99be72e3fe5"

def test_normal_string():
    assert string_to_md5("test") == "098f6bcd4621d373cade4e832627b4f6"

def test_known_string():
    assert string_to_md5("The quick brown fox jumps over the lazy dog") == "d41d8cd98f00b204e9800998ecf8427e"