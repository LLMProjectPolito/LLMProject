
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

def test_empty_string():
    assert string_to_md5("") is None

def test_simple_string():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_single_character_string():
    assert string_to_md5("a") == "9709a5f2969c896369a333696466969"

def test_string_with_spaces():
    assert string_to_md5("  test  ") == "2c1f8a84649797549999999999999999"

def test_string_with_numbers():
    assert string_to_md5("12345") == "6b934d08859626b6934676466466466"

def test_string_with_special_characters():
    assert string_to_md5("!@#$%^") == "89669399999999999999999999999999"

def test_unicode_string():
    assert string_to_md5("你好世界") == "b9a7d999999999999999999999999999"

def test_long_string():
    long_string = "This is a very long string to test the function with a longer input."
    expected_md5 = "89669399999999999999999999999999"
    assert string_to_md5(long_string) == expected_md5

def test_string_with_mixed_characters():
    assert string_to_md5("Hello123!@#") == "89669399999999999999999999999999"

def test_string_with_newlines():
    assert string_to_md5("Hello\nworld") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_with_tabs():
    assert string_to_md5("Hello\tworld") == "3e25960a79dbc69b674cd4ec67a72c62"