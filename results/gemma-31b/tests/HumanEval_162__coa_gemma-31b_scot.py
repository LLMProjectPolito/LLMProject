
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import math


# Focus: Boundary Values
import hashlib

def test_string_to_md5_empty_string():
    assert string_to_md5("") is None

def test_string_to_md5_single_character():
    text = "a"
    expected = hashlib.md5(text.encode()).hexdigest()
    assert string_to_md5(text) == expected

def test_string_to_md5_very_long_string():
    text = "a" * 10**6
    expected = hashlib.md5(text.encode()).hexdigest()
    assert string_to_md5(text) == expected

# Focus: Type Scenarios
import pytest

def test_string_to_md5_return_type_string():
    """Test that a non-empty string input returns a string (the hash)."""
    assert isinstance(string_to_md5("Hello world"), str)

def test_string_to_md5_return_type_none():
    """Test that an empty string input returns None (NoneType)."""
    assert string_to_md5("") is None

def test_string_to_md5_invalid_input_type():
    """Test that non-string inputs raise a TypeError or AttributeError."""
    with pytest.raises((TypeError, AttributeError)):
        string_to_md5(123)

# Focus: Logic Branches
def test_string_to_md5_empty():
    assert string_to_md5("") is None

def test_string_to_md5_non_empty():
    assert string_to_md5("Hello world") == '3e25960a79dbc69b674cd4ec67a72c62'