import pytest
import hashlib

def test_string_to_md5_empty_string():
    """Test with an empty string to check for None return value."""
    assert string_to_md5("") is None

def test_string_to_md5_short_string():
    """Test with a short string to check for correct md5 hash."""
    short_string = "Hello world"
    expected_md5 = hashlib.md5(short_string.encode()).hexdigest()
    assert string_to_md5(short_string) == expected_md5

def test_string_to_md5_very_long_string():
    """Test with a very long string to check for potential performance issues or buffer overflows."""
    long_string = "a" * 10000
    expected_md5 = hashlib.md5(long_string.encode()).hexdigest()
    assert string_to_md5(long_string) == expected_md5