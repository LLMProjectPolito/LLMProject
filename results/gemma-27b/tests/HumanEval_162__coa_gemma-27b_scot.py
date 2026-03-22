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

def test_string_to_md5_empty_string():
    """Test with an empty string input."""
    assert string_to_md5("") is None

def test_string_to_md5_none_input():
    """Test with None input."""
    with pytest.raises(TypeError):
        string_to_md5(None)

def test_string_to_md5_whitespace_string():
    """Test with a string containing only whitespace."""
    assert string_to_md5("   ") is not None

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
    return hashlib.md5(text.encode()).hexdigest()

def test_valid_string_input_basic():
    """Test with a simple, valid string."""
    assert string_to_md5("test") == '098f6bcd4621d373cade4e832627b4f6'

def test_valid_string_input_with_spaces():
    """Test with a valid string containing spaces."""
    assert string_to_md5("Hello world") == '3e25960a79dbc69b674cd4ec67a72c62'

def test_valid_string_input_long_string():
    """Test with a longer, valid string."""
    long_string = "This is a very long string to test the MD5 function."
    assert string_to_md5(long_string) == 'd9b1b7a8f89999999999999999999999'

# Focus: Error Handling/Invalid Input Types
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

def test_string_to_md5_invalid_input_type_int():
    """Test with integer input."""
    with pytest.raises(TypeError):
        string_to_md5(123)

def test_string_to_md5_invalid_input_type_list():
    """Test with list input."""
    with pytest.raises(TypeError):
        string_to_md5([1, 2, 3])

def test_string_to_md5_invalid_input_type_none():
    """Test with None input."""
    with pytest.raises(TypeError):
        string_to_md5(None)