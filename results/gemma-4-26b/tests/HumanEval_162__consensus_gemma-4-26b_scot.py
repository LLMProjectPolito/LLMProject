
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib

@pytest.mark.parametrize("text, expected", [
    ("Hello world", "3e25960a79dbc69b674cd4ec67a72c62"),
    ("abc", "900150983cd24fb0d6963f7d28e17f72"),
    ("a", "0cc175b9c0f1b6a831c399e269772661"),
    (" ", "356a192b7913b6d86e8f540234f42112"),
    ("123", "202cb962ac59075b964b07152d234b70"),
    ("!@#$%^&*()", "389f61844793452690f23f30306b0361"),
    ("The quick brown fox jumps over the lazy dog", "9e107d9d372bb6826bd81d3542a419d6"),
])
def test_string_to_md5_scenarios(text, expected):
    """Test various standard string inputs with known MD5 hashes."""
    assert string_to_md5(text) == expected

def test_string_to_md5_empty_string():
    """Test that an empty string returns None."""
    assert string_to_md5("") is None

def test_string_to_md5_unicode():
    """Test with multi-byte Unicode characters to ensure encoding is handled correctly."""
    text = "こんにちは 🚀"
    expected = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected

def test_string_to_md5_large_input():
    """Test with a very large string to ensure stability."""
    text = "large_string" * 10000
    expected = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected

def test_string_to_md5_whitespace_control():
    """Test with whitespace control characters."""
    text = "\n\t\r"
    expected = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected

def test_string_to_md5_invalid_types():
    """Test that non-string inputs raise appropriate errors."""
    for invalid_input in [None, 123, ["hello"]]:
        with pytest.raises((TypeError, AttributeError)):
            string_to_md5(invalid_input)