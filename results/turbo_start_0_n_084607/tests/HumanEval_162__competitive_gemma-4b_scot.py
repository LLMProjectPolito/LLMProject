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
    assert string_to_md5("a") == "9709d296989443969636894799999999"

def test_string_to_md5_multiple_spaces():
    assert string_to_md5("  ") == "2406843182304c733763696f6e"

def test_string_to_md5_numbers():
    assert string_to_md5("12345") == "6b93423796436353676961"

def test_string_to_md5_special_characters():
    assert string_to_md5("!@#$%^") == "89669393996693939966939399669393"

def test_string_to_md5_mixed_characters():
    assert string_to_md5("Hello123!") == "64999899999999999999999999999999"

def test_string_to_md5_unicode():
    assert string_to_md5("你好世界") == "b9a89676699999999999999999999999"

def test_string_to_md5_long_string():
    long_string = "This is a very long string to test the function with a large input."
    expected_md5 = "89669393996693939966939399669393"
    assert string_to_md5(long_string) == expected_md5