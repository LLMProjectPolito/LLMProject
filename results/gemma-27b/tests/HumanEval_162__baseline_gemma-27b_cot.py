
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

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
    md5_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
    return md5_hash

def test_string_to_md5_empty_string():
    assert string_to_md5("") is None

def test_string_to_md5_hello_world():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_to_md5_single_character():
    assert string_to_md5("a") == "0cc175b9c0f1b6a831c399e269772661"

def test_string_to_md5_with_spaces():
    assert string_to_md5("  test  ") == "9f86d081884c7d659a2feaa0c55ad015"

def test_string_to_md5_with_numbers():
    assert string_to_md5("12345") == "827ccb0eea8a706c4c34a16891f84e7b"

def test_string_to_md5_with_special_characters():
    assert string_to_md5("!@#$%^") == "b10a8db164e0754105b7a99be72e3fe5"

def test_string_to_md5_long_string():
    long_string = "This is a very long string to test the md5 hash function."
    assert string_to_md5(long_string) == "9a39a919499994999499949994999499"

def test_string_to_md5_unicode_string():
    assert string_to_md5("你好世界") == "b10a8db164e0754105b7a99be72e3fe5"