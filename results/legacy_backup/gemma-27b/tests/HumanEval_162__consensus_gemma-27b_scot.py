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

def test_empty_string():
    assert string_to_md5("") is None

def test_valid_string():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_special_characters():
    assert string_to_md5("!@#$%^&*()") == "9f86d081884c7d659a2feaa0c55ad015"

def test_long_string():
    long_string = "This is a very long string to test the MD5 hash function."
    assert string_to_md5(long_string) == hashlib.md5(long_string.encode('utf-8')).hexdigest()

def test_unicode_string():
    assert string_to_md5("你好世界") == "b10a8db164e0754105b7a99be72e3fe5"

def test_return_type():
    assert isinstance(string_to_md5("test"), str)

def test_known_hash():
    assert string_to_md5("The quick brown fox jumps over the lazy dog") == "d41d8cd98f00b204e9800998ecf8427e"

def test_long_string_type():
    long_string = "a" * 1000
    assert isinstance(string_to_md5(long_string), str)

def test_different_case():
    assert string_to_md5("hello world") != string_to_md5("Hello world")