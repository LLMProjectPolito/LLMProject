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
    assert string_to_md5("a") == '2598cb8b460b6f8b8873b3969636933e'

def test_string_to_md5_long_string():
    long_string = "This is a very long string to test the md5 function."
    expected_md5 = 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'
    assert string_to_md5(long_string) == expected_md5

def test_string_to_md5_with_numbers():
    assert string_to_md5("12345") == '6b9340a38081cf7ff5401d102116a841'

def test_string_to_md5_with_special_characters():
    assert string_to_md5("!@#$%^") == 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'

def test_string_to_md5_mixed_characters():
    assert string_to_md5("Hello123!@#") == 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'

def test_string_to_md5_unicode_characters():
    assert string_to_md5("你好世界") == 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'

def test_string_to_md5_empty_string_2():
    assert string_to_md5("   ") is None

def test_string_to_md5_whitespace_only():
    assert string_to_md5("   ") is None

def test_string_to_md5_newline_only():
    assert string_to_md5("\n") is None

def test_string_to_md5_tab_only():
    assert string_to_md5("\t") is None