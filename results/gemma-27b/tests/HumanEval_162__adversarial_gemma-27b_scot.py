
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
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    if not text:
        return None
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    return md5_hash

def test_empty_string():
    assert string_to_md5("") is None

def test_valid_string():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_different_strings():
    assert string_to_md5("test") == "098f6bcd4621d373cade4e832627b4f6"
    assert string_to_md5("another test") == "6a2b89f1991999999999999999999999"
    assert string_to_md5("12345") == "5d41402abc4b2a76b9719d911017c592"

def test_string_with_spaces():
    assert string_to_md5("  leading and trailing spaces  ") == "9f86d081884c7d659a2feaa0c55ad015"

def test_string_with_special_characters():
    assert string_to_md5("!@#$%^&*()") == "9496e999999999999999999999999999"

def test_long_string():
    long_string = "a" * 1000
    assert len(string_to_md5(long_string)) == 32

def test_non_string_input():
    with pytest.raises(TypeError):
        string_to_md5(123)
    with pytest.raises(TypeError):
        string_to_md5([1, 2, 3])