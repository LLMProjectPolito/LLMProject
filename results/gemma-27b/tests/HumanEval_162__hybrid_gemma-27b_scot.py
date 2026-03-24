
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

def test_empty_string():
    assert string_to_md5("") is None

def test_basic_string():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_special_characters():
    assert string_to_md5("!@#$%^&*()") == "9f86d081884c7d659a2feaa0c55ad015"

def test_long_string():
    long_string = "This is a very long string to test the MD5 hash function." * 10
    assert isinstance(string_to_md5(long_string), str)
    assert len(string_to_md5(long_string)) == 32

def test_unicode_string():
    assert string_to_md5("你好世界") == "b10a8db164e0754105b7a99be72e3fe5"

def test_case_sensitivity():
    assert string_to_md5("Hello world") != string_to_md5("hello world")

def test_string_with_numbers():
    assert string_to_md5("1234567890") == "5d41402abc4b2a76b9719d911017c592"