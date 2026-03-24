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
    assert string_to_md5("a") == "9709d296989443969a87669669999999"

def test_string_to_md5_long_string():
    long_string = "This is a very long string to test the function."
    expected_md5 = "8966339999999999999999999999999999999999999999999999999999999999"
    assert string_to_md5(long_string) == expected_md5

def test_string_to_md5_with_spaces():
    assert string_to_md5("  test  ") == "596f7034397e2d0d6a38383a3338383a"

def test_string_to_md5_with_special_characters():
    assert string_to_md5("!@#$%^&*()") == "8f8349656f70d396498a963369647636965"

def test_string_to_md5_unicode_characters():
    assert string_to_md5("你好世界") == "b9a3669696429999999999999999999999999999999999999999999999999999"

def test_string_to_md5_numbers_and_letters():
    assert string_to_md5("1234567890") == "6299999999999999999999999999999999999999999999999999999999999999"

def test_string_to_md5_mixed_characters():
    assert string_to_md5("Hello123World!") == "6499999999999999999999999999999999999999999999999999999999999999"