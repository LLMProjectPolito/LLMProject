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
    assert string_to_md5("你好世界") == "b10a8db164e0754105b7a99be72e3fe5"

def test_long_string():
    long_string = "a" * 1000
    assert string_to_md5(long_string) == "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3"

def test_special_characters():
    assert string_to_md5("Hello\nworld\t!") == "6cd3556deb0da54bca060b4c39479839"

def test_string_length_one():
    assert string_to_md5("a") == "0cc175b9c0f1b6a831c399e269772661"

def test_short_string():
    assert string_to_md5("ab") == "d2a96531699996969996969696969696"

def test_case_sensitivity():
    assert string_to_md5("Hello world") != string_to_md5("hello world")

def test_whitespace():
    assert string_to_md5("  Hello world  ") == "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b"

def test_string_with_numbers():
    assert string_to_md5("Hello123world") == "5994471abb01112afcc18159f6cc74b4"