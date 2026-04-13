
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

def test_string_to_md5_empty_string():
    assert string_to_md5("") is None

def test_string_to_md5_hello_world():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_to_md5_single_character():
    assert string_to_md5("a") == "9709d29698944493933296269793693a"

def test_string_to_md5_multiple_spaces():
    assert string_to_md5("  ") == "29e1a3a56c9a15a797854446339e667a"

def test_string_to_md5_numbers():
    assert string_to_md5("12345") == "6b934237964363a3649969228983899a"

def test_string_to_md5_special_characters():
    assert string_to_md5("!@#$%^") == "886269679998999999999999999999999999999999999999"

def test_string_to_md5_mixed_characters():
    assert string_to_md5("Hello123!") == "6b934237964363a3649969228983899a"

def test_string_to_md5_unicode_characters():
    assert string_to_md5("你好世界") == "b9a39a899999999999999999999999999999999999999999"

def test_string_to_md5_long_string():
    long_string = "This is a very long string to test the function with a large input."
    expected_md5 = "896789999999999999999999999999999999999999999999"
    assert string_to_md5(long_string) == expected_md5