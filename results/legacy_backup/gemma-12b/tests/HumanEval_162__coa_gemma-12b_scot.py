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
    """Test with an empty string (boundary condition)."""
    assert string_to_md5("") is None

def test_single_character_boundary():
    """Test with a single character string (boundary condition)."""
    assert string_to_md5("a") == "ba7816bf8f01cfea414140de5dae2223"

def test_short_string_boundary():
    """Test with a short string (boundary condition)."""
    assert string_to_md5("abc") == "0cc175b9c0f1b6a831c399e269772661"

# Focus: Error Handling
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

def test_empty_string_returns_none():
    """Test that an empty string input returns None."""
    assert string_to_md5("") is None

def test_invalid_input_type_raises_typeerror():
    """Test that non-string input raises a TypeError."""
    with pytest.raises(TypeError):
        string_to_md5(123)

def test_none_input_returns_none():
    """Test that None input returns None."""
    assert string_to_md5(None) is None

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

def test_non_empty_string():
    assert string_to_md5("Hello world") == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_with_spaces():
    assert string_to_md5("  ") == '9c6a98d4695394a99999999999999999'