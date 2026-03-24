
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib
import math

def test_empty_string_returns_none():
    """Test that an empty string input returns None."""
    from your_module import string_to_md5  # Replace your_module
    assert string_to_md5("") is None