import pytest
import hashlib

def test_string_to_md5_valid_input():
    """Test with a valid, non-empty string."""
    assert string_to_md5("Hello world") == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty_string():
    """Test with an empty string."""
    assert string_to_md5("") is None

def test_string_to_md5_different_string():
    """Test with a different string."""
    assert string_to_md5("This is a test") == '9f86d081884c7d659a2feaa0c55ad015'

def test_string_to_md5_string_with_numbers():
    """Test with a string containing numbers."""
    assert string_to_md5("12345") == 'e10adc3949ba59abbe56e057f20f883e'

def test_string_to_md5_string_with_special_characters():
    """Test with a string containing special characters."""
    assert string_to_md5("!@#$%^") == '9d019294999999999999999999999999'

def test_string_to_md5_unicode_string():
    """Test with a unicode string."""
    assert string_to_md5("你好世界") == 'b10a8db164e0754105b7a99be72e3fe5'

def test_string_to_md5_long_string():
    """Test with a long string."""
    long_string = "This is a very long string to test the function with. It should handle long strings without any issues."
    expected_md5 = hashlib.md5(long_string.encode('utf-8')).hexdigest()
    assert string_to_md5(long_string) == expected_md5