import pytest
import math


# Focus: Empty/Null Input
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
    return hashlib.md5(text.encode()).hexdigest()

def test_empty_string():
    assert string_to_md5("") is None

def test_none_input():
    with pytest.raises(TypeError):
        string_to_md5(None)

def test_whitespace_string():
    assert string_to_md5("   ") == 'd41d8cd98f00b204e9800998ecf8427e'

# Focus: Valid String Input
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

def test_valid_string_input_normal_case():
    assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

def test_valid_string_input_with_spaces():
    assert string_to_md5("  test string  ") == "5a105e8b9d40e1329780d62ea2265d8a"

def test_valid_string_input_with_special_characters():
    assert string_to_md5("!@#$%^&*()") == "9f86d081884c7d659a2feaa0c55ad015"

# Focus: Error/Exception Handling (for potentially very large strings)
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

def test_string_to_md5_large_string():
    large_string = "a" * 1000000
    assert isinstance(string_to_md5(large_string), str)
    assert len(string_to_md5(large_string)) == 32

def test_string_to_md5_unicode_string():
    unicode_string = "你好世界"
    assert isinstance(string_to_md5(unicode_string), str)
    assert len(string_to_md5(unicode_string)) == 32