
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
    md5_hash = hashlib.md5(text.encode('utf-8'))
    return md5_hash.hexdigest()

def test_empty_string():
    assert string_to_md5("") is None

def test_valid_string():
    assert string_to_md5("Hello world") == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_with_spaces():
    assert string_to_md5("  ") == '9c64a369999999999999999999999999'

def test_string_with_special_characters():
    assert string_to_md5("!@#$%^&*()") == '99d8310496a999999999999999999999'

def test_string_with_unicode_characters():
    assert string_to_md5("你好世界") == 'b10a8db164e0754105b7a99be72e3fe5'

def test_string_with_numbers():
    assert string_to_md5("1234567890") == 'd1e2f3e4d5c6b7a8a9b0c1d2e3f4a5b6'

def test_string_with_mixed_characters():
    assert string_to_md5("Hello123World!") == '9c64a369999999999999999999999999'

def test_long_string():
    long_string = "This is a very long string to test the md5 hash function."
    assert string_to_md5(long_string) == '9c64a369999999999999999999999999'

def test_string_with_newline():
    assert string_to_md5("Hello\nWorld") == '9c64a369999999999999999999999999'