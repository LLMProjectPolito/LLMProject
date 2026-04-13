
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

def test_string_to_md5_simple_string():
    assert string_to_md5("Hello") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_to_md5_with_spaces():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_to_md5_numbers():
    assert string_to_md5("12345") == "a68f8f7a9f8b7a6d5c4e3f2b1a"

def test_string_to_md5_mixed_characters():
    assert string_to_md5("Hello!@#") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_to_md5_unicode():
    assert string_to_md5("你好世界") == "3e25960a79dbc69b674cd4ec67a72c62" #Example of unicode

def test_string_to_md5_long_string():
    assert string_to_md5("This is a very long string to test the md5 hash function.") == "a68f8f7a9f8b7a6d5c4e3f2b1a"