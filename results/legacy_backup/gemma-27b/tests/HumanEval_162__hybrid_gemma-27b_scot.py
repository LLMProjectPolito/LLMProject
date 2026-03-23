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

def test_hello_world():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_long_string():
    long_string = "This is a very long string to test the MD5 hashing function."
    expected_hash = "d2a96a8f199999999999999999999999" # Replace with actual hash
    assert string_to_md5(long_string) == "99999999999999999999999999999999"

def test_special_characters():
    special_string = "This string contains !@#$%^&*()_+=-`~[]\{}|;':\",./<>?"
    assert string_to_md5(special_string) == "99999999999999999999999999999999" # Replace with actual hash

def test_unicode_string():
    unicode_string = "你好世界"  # Hello world in Chinese
    assert string_to_md5(unicode_string) == "99999999999999999999999999999999" # Replace with actual hash