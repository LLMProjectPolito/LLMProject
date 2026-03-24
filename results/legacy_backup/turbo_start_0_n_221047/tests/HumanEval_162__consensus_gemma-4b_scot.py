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
    assert string_to_md5("Hello world") == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_single_character():
    assert string_to_md5("a") == '2aae6c71c3bdf16a8b704468c74a9c71'

def test_string_to_md5_long_string():
    long_string = "This is a very long string to test the md5 function."
    expected_md5 = 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'
    assert string_to_md5(long_string) == expected_md5

def test_string_to_md5_with_numbers():
    assert string_to_md5("12345") == '6b934d08e9a3d1c794a7b7984699999a'

def test_string_to_md5_with_special_characters():
    assert string_to_md5("!@#$%^") == '8966339999999999999999999999999999999999999999999999999999999999'

def test_string_to_md5_unicode_characters():
    assert string_to_md5("你好世界") == 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'

def test_string_to_md5_mixed_characters():
    assert string_to_md5("Hello, world!") == '6b934d08e9a3d1c794a7b7984699999a'

def test_string_to_md5_case_sensitive():
    assert string_to_md5("Hello") != 'hello'