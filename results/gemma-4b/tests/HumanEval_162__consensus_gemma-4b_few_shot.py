
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
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def test_string_to_md5_empty_string():
    assert string_to_md5("") is None

def test_string_to_md5_hello_world():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_to_md5_single_character():
    assert string_to_md5("a") == "97099a99999999999999999999999999"

def test_string_to_md5_multiple_spaces():
    assert string_to_md5("  ") == "2f3b0569838669429999999999999999"

def test_string_to_md5_numbers():
    assert string_to_md5("12345") == "6b93423796b396639999999999999999"

def test_string_to_md5_special_characters():
    assert string_to_md5("!@#$%^") == "8e999999999999999999999999999999"

def test_string_to_md5_mixed_characters():
    assert string_to_md5("Hello123!") == "64999999999999999999999999999999"

def test_string_to_md5_unicode_characters():
    assert string_to_md5("你好世界") == "99999999999999999999999999999999"

def test_string_to_md5_long_string():
    long_string = "This is a very long string to test the function with a large input."
    expected_md5 = "89679999999999999999999999999999"
    assert string_to_md5(long_string) == expected_md5

def test_string_to_md5_with_newlines():
    assert string_to_md5("Hello\nWorld") == "3e25960a79dbc69b674cd4ec67a72c62"