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

def test_string_to_md5_empty_string():
    assert string_to_md5("") is None

def test_string_to_md5_hello_world():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_string_to_md5_single_character():
    assert string_to_md5("a") == "97099a986b79a8999999999999999999"

def test_string_to_md5_long_string():
    long_string = "This is a very long string to test the md5 function."
    expected_md5 = "b94d27b9934d3e08a52e52d9d3b0d196"
    assert string_to_md5(long_string) == expected_md5

def test_string_to_md5_with_numbers():
    assert string_to_md5("12345") == "6b934d08859d8fcd33d6e87a6663425a"

def test_string_to_md5_with_special_characters():
    assert string_to_md5("!@#$%^") == "b94d27b9934d3e08a52e52d9d3b0d196"

def test_string_to_md5_unicode_characters():
    assert string_to_md5("你好世界") == "b94d27b9934d3e08a52e52d9d3b0d196"

def test_string_to_md5_mixed_characters():
    assert string_to_md5("Hello, 世界!") == "3e25960a79dbc69b674cd4ec67a72c62b94d27b9934d3e08a52e52d9d3b0d196"