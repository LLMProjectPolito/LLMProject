
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import math

def test_string_to_md5_unicode_characters():
    """Tests the function with a string containing unicode characters."""
    assert string_to_md5("你好世界") == "95a07999996999999999999999999999"

def test_string_to_md5_unicode_characters_2():
    """Tests handling of Unicode characters in the input string."""
    assert string_to_md5("你好世界") == "59524439999999999999999999999999"

def test_string_to_md5_unicode_characters_3():
    """Tests the function with a string containing unicode characters."""
    assert string_to_md5("你好世界") == "92999999999999999999999999999999"