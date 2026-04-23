
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

def test_empty_string():
    assert string_to_md5("") is None

def test_valid_string():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_with_special_characters():
    assert string_to_md5("!@#$%^&*()") == "e29c990000000000000000000000000000000000000000000000000000"

def test_string_with_unicode():
    assert string_to_md5("你好世界") == "9679a2953e6648f66d00a065c0f2315e"

def test_long_string():
    long_string = "This is a very long string to test the function." * 100
    assert string_to_md5(long_string) == hashlib.md5(long_string.encode('utf-8')).hexdigest()

def test_string_with_numbers():
    assert string_to_md5("1234567890") == "29e9a809e55b8554f66f9432c9b7f001"

def test_string_with_mixed_characters():
    assert string_to_md5("a1b2c3d4e5f6") == "e5e9a8799a4f4b92d18e512087966032"