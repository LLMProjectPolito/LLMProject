
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
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def test_string_to_md5_basic():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_to_md5_empty():
    assert string_to_md5("") is None

def test_string_to_md5_single_char():
    assert string_to_md5("a") == "5d41402abc4b2a76b9719d911017c592"

def test_string_to_md5_long_string():
    long_string = "This is a very long string to test the md5 hash."
    md5_hash = string_to_md5(long_string)
    assert len(md5_hash) == 32

def test_string_to_md5_special_chars():
    assert string_to_md5("!@#$%^&*()") == "e2d9e5858776385a32595a695628614c"

def test_string_to_md5_unicode():
    assert string_to_md5("你好世界") == "e535d94696a986383454d59299699194"