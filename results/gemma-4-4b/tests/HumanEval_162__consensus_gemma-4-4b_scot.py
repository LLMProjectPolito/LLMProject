
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
    assert string_to_md5("1234567890") == 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'

def test_string_with_special_characters():
    assert string_to_md5("!@#$%^&*()") == '42e7c72995c83b980749737d03038456'

def test_long_string():
    long_string = "This is a very long string to test the function." * 10
    md5_hash = hashlib.md5(long_string.encode('utf-8')).hexdigest()
    assert string_to_md5(long_string) == md5_hash

def test_string_with_unicode():
    assert string_to_md5("你好世界") == 'a987489719067d8737976b27e6e2a481'