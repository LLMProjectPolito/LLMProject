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


def test_empty_string():
    assert string_to_md5("") is None

def test_simple_string():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_single_character_string():
    assert string_to_md5("a") == "2aae6c71c39beca499a99c64b9b0c841"

def test_string_with_spaces():
    assert string_to_md5("  test  ") == "26a85490399996969696969696969696"

def test_string_with_numbers():
    assert string_to_md5("12345") == "6b934237964363a36463636364636363"

def test_string_with_special_characters():
    assert string_to_md5("!@#$%^") == "89663369999999999999999999999999"

def test_unicode_string():
    assert string_to_md5("你好世界") == "b9a7d999999999999999999999999999"

def test_long_string():
    long_string = "This is a very long string to test the function with a large input."
    expected_md5 = "89663369999999999999999999999999"
    assert string_to_md5(long_string) == expected_md5

def test_string_with_mixed_characters():
    assert string_to_md5("Hello123!@#") == "89663369999999999999999999999999"