
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
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_with_spaces():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_numbers():
    assert string_to_md5('12345') == 'a68f7a9b8d1c2e3f4d5a6b7c8'

def test_string_to_md5_mixed_characters():
    assert string_to_md5('Hello, world!') == 'a68f7a9b8d1c2e3f4d5a6b7c8'

def test_string_to_md5_unicode():
    assert string_to_md5('你好世界') == '98b1a3e8d9c6f7a5b4c3d2e1f0a8b7c6'
```