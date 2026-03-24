
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
    Uses UTF-8 encoding.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    md5_hash = hashlib.md5(text.encode('utf-8'))
    return md5_hash.hexdigest()

def test_empty_string():
    assert string_to_md5("") is None

def test_valid_string():
    expected_md5 = hashlib.md5("Hello world".encode('utf-8')).hexdigest()
    assert string_to_md5("Hello world") == expected_md5

def test_string_with_spaces():
    assert string_to_md5("  ") == hashlib.md5("  ".encode('utf-8')).hexdigest()

def test_string_with_special_characters():
    assert string_to_md5("!@#$%^&*()") == hashlib.md5("!@#$%^&*()".encode('utf-8')).hexdigest()

def test_string_with_unicode_characters():
    assert string_to_md5("你好世界") == hashlib.md5("你好世界".encode('utf-8')).hexdigest()

def test_string_with_numbers():
    assert string_to_md5("1234567890") == hashlib.md5("1234567890".encode('utf-8')).hexdigest()

def test_string_with_leading_and_trailing_whitespace():
    assert string_to_md5("  test  ") == hashlib.md5("  test  ".encode('utf-8')).hexdigest()

def test_string_with_control_characters():
    assert string_to_md5("test\tstring\n") == hashlib.md5("test\tstring\n".encode('utf-8')).hexdigest()

def test_case_sensitivity():
    assert string_to_md5("hello") == hashlib.md5("hello".encode('utf-8')).hexdigest()
    assert string_to_md5("Hello") == hashlib.md5("Hello".encode('utf-8')).hexdigest()

def test_long_string():
    long_string = "This is a very long string to test the md5 hash function with a significant amount of data."
    assert string_to_md5(long_string) == hashlib.md5(long_string.encode('utf-8')).hexdigest()

def test_invalid_input():
    with pytest.raises(TypeError):
        string_to_md5(123)