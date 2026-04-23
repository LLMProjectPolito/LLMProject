
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib
import uuid

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

def test_normal_string():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_with_spaces():
    assert string_to_md5("This is a test string") == "a1b2c3d4e5f678901234567890abcdef"

def test_string_with_punctuation():
    assert string_to_md5("Hello, world!") == "b1a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1"

def test_string_with_numbers():
    assert string_to_md5("1234567890") == "a98a78a337385b93d64653a2d73046e2"

def test_mixed_string():
    assert string_to_md5("This is a mixed string with numbers and punctuation.") == "e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0"

def test_long_string():
    long_string = "This is a very long string to test the function's performance and correctness." * 100
    assert string_to_md5(long_string) == "a98a78a337385b93d64653a2d73046e2" # MD5 hash is consistent

def test_unicode_string():
    assert string_to_md5("你好世界") == "e5e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e5a6e"

def test_ascii_string():
    assert string_to_md5("This is an ASCII string") == "e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1"

def test_latin1_string():
    assert string_to_md5("This is a Latin-1 string") == "e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1"