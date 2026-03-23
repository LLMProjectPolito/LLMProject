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

def test_simple_string():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_with_spaces():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_with_special_characters():
    assert string_to_md5('Hello! world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_with_numbers():
    assert string_to_md5('1234567890') == 'a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0'

def test_string_with_unicode():
    assert string_to_md5('你好世界') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_long_string():
    assert string_to_md5('This is a very long string to test the function.') == 'a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0'