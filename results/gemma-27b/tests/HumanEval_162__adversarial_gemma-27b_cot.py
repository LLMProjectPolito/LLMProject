
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import hashlib
import pytest

def test_empty_string():
    assert string_to_md5("") is None

def test_valid_string():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_with_spaces():
    assert string_to_md5("  test  ") == "e5e9fa1ba31ecd1ae84f75caaa474f3a6"

def test_string_with_special_characters():
    assert string_to_md5("!@#$%^") == "96f99919961c99999999999999999999"

def test_string_with_numbers():
    assert string_to_md5("12345") == "5994471abb01112afcc18159f6cc74b4"

def test_long_string():
    long_string = "This is a very long string to test the md5 function." * 10
    assert string_to_md5(long_string) == 'f9999999999999999999999999999999'

def test_unicode_string():
    assert string_to_md5("你好世界") == "b10a8db164e0754105b7a99be72e3fe5"

def test_string_with_newlines():
    assert string_to_md5("test\nstring") == "5994471abb01112afcc18159f6cc74b4"

def test_string_with_tabs():
    assert string_to_md5("test\tstring") == "5994471abb01112afcc18159f6cc74b4"