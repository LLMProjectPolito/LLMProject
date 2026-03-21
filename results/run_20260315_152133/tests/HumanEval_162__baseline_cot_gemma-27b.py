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

def test_basic_functionality():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_empty_string():
    assert string_to_md5("") is None

def test_unicode_string():
    assert string_to_md5("你好世界") == "d41d8cd98f00b204e9800998ecf8427e"

def test_long_string():
    long_string = "a" * 1000
    assert string_to_md5(long_string) == '98a76199999999999999999999999999'

def test_special_characters():
    assert string_to_md5("Hello\nworld\t!") == "b10a8db164e0754105b7a99be72e3fe5"

def test_string_length_one():
    assert string_to_md5("a") == "0cc175b9c0f1b6a831c399e269772661"

def test_short_string():
    assert string_to_md5("ab") == "d2a84f18999999999999999999999999"

def test_case_sensitivity():
    assert string_to_md5("Hello world") != string_to_md5("hello world")

def test_whitespace():
    assert string_to_md5("  Hello world  ") == "6f8f9999999999999999999999999999"

def test_string_with_quotes():
    assert string_to_md5('"Hello world"') == "f9999999999999999999999999999999"