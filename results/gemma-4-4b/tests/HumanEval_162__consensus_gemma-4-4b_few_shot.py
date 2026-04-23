
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib
from your_module import string_to_md5  # Replace your_module

def test_empty_string():
    assert string_to_md5("") is None

def test_simple_string():
    assert string_to_md5("Hello world") == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_with_numbers():
    assert string_to_md5("1234567890") == 'e4d9194a43141323d55446a5a9f33d1a'

def test_string_with_special_characters():
    assert string_to_md5("!@#$%^&*()") == 'e537539f6e780683688f3503394885b3'

def test_string_with_unicode_characters():
    assert string_to_md5("你好世界") == 'e9e8a429e783865b42e0c6152795855b'

def test_long_string():
    long_string = "This is a very long string to test the hashing function." * 10
    md5_hash = hashlib.md5(long_string.encode()).hexdigest()
    assert string_to_md5(long_string) == md5_hash