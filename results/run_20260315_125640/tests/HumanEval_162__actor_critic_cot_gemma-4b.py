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


def test_string_to_md5_empty_string():
    assert string_to_md5("") is None

def test_string_to_md5_simple_string():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_to_md5_single_character():
    assert string_to_md5("a") == "2aae6c71c3b4d158763186b2b9d8439a"

def test_string_to_md5_unicode_string():
    assert string_to_md5("你好世界") == "b9a8a9c789b789b789b789b789b789b7"

def test_string_to_md5_string_with_numbers():
    assert string_to_md5("12345") == "6b9340a8f7a34230864b829d3f514e3a"

def test_string_to_md5_string_with_special_characters():
    assert string_to_md5("!@#$%^") == "89663369999999999999999999999999"

def test_string_to_md5_long_string():
    long_string = "This is a very long string to test the md5 function."
    expected_md5 = "89663369999999999999999999999999"
    assert string_to_md5(long_string) == expected_md5

def test_string_to_md5_string_with_spaces():
    assert string_to_md5("  hello world  ") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_to_md5_string_with_newlines():
    assert string_to_md5("hello\nworld") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_to_md5_string_with_tabs():
    assert string_to_md5("hello\tworld") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_to_md5_mixed_characters():
    assert string_to_md5("Hello123!@#") == "3e25960a79dbc69b674cd4ec67a72c62"