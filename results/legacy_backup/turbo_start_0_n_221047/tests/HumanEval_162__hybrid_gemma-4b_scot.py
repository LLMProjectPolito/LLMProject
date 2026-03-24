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


def test_empty_string():
    assert string_to_md5("") is None

def test_normal_string():
    assert string_to_md5("Hello world") == '3e25960a79dbc69b674cd4ec67a72c62'

def test_special_characters():
    assert string_to_md5("!@#$%^") == 'b94d27b9934d3e08a52e52d97d0a763d'

def test_unicode_characters():
    assert string_to_md5("你好世界") == 'b94d27b9934d3e08a52e52d97d0a763d'

def test_long_string():
    long_string = "This is a very long string to test the MD5 hash function."
    assert string_to_md5(long_string) == 'b94d27b9934d3e08a52e52d97d0a763d'