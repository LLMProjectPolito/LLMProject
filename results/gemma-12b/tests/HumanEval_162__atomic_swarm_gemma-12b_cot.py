
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import math

def test_basic():
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_empty_string():
    """Test with an empty string input."""
    assert string_to_md5("") is None

def test_string_to_md5_wrong_type():
    """Test with a non-string input."""
    import hashlib
    try:
        string_to_md5(123)
        assert False, "Should have raised a TypeError"
    except TypeError:
        assert True