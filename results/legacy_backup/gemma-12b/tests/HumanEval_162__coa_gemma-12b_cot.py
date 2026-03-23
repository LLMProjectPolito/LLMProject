import pytest
import math


# Focus: Boundary Values
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
    md5_hash = hashlib.md5(text.encode('utf-8'))
    return md5_hash.hexdigest()

def test_empty_string_boundary():
    assert string_to_md5("") is None

def test_single_character_boundary():
    assert string_to_md5("a") == "0cc175b9c0f1b6a831c399e269772661"

def test_max_length_string_boundary():
    max_length = 256
    long_string = 'A' * max_length
    expected_md5 = hashlib.md5(long_string.encode('utf-8')).hexdigest()
    assert string_to_md5(long_string) == expected_md5

# Focus: Error Handling
import pytest
from your_module import string_to_md5  # Replace your_module

def test_empty_string_returns_none():
    """Test that an empty string input returns None."""
    assert string_to_md5("") is None

def test_invalid_input_type_raises_typeerror():
    """Test that non-string input raises a TypeError."""
    with pytest.raises(TypeError):
        string_to_md5(123)

def test_none_input_raises_typeerror():
    """Test that None input raises a TypeError."""
    with pytest.raises(TypeError):
        string_to_md5(None)

# Focus: Logic Branches
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
    md5_hash = hashlib.md5(text.encode('utf-8'))
    return md5_hash.hexdigest()

def test_empty_string():
    assert string_to_md5("") is None

def test_valid_string():
    assert string_to_md5("Hello world") == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_with_unicode():
    assert string_to_md5("你好世界") == 'a94a8fe5ccb19ba61c4c0873d391e987'