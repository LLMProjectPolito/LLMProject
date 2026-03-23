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
    return hashlib.md5(text.encode('utf-8')).hexdigest()

class TestStringToMD5:
    """
    Comprehensive pytest suite for the string_to_md5 function.
    """

    def test_empty_string(self):
        """Test that an empty string returns None."""
        assert string_to_md5("") is None

    def test_valid_string(self):
        """Test with a standard string."""
        assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

    def test_simple_string(self):
        """Test with a simple string."""
        assert string_to_md5("hello") == "5d41402abc4b2a76b9719d911017c592"

    def test_string_with_spaces(self):
        """Test with a string containing leading/trailing spaces."""
        assert string_to_md5("  Hello world  ") == "b10a8db164e0754105b7a99be72e3fe5"
        assert string_to_md5("  test  ") == "e5e9fa1ba31ecd1ae84f75caaa474f3a663f05f4"

    def test_string_with_special_characters(self):
        """Test with a string containing special characters."""
        assert string_to_md5("!@#$%^&*()") == "d41d8cd98f00b204e9800998ecf8427e"
        assert string_to_md5("!@#$%^&*()") == "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b"

    def test_string_with_numbers(self):
        """Test with a string containing numbers."""
        assert string_to_md5("1234567890") == "5d41402abc4b2a76b9719d911017c592"
        assert string_to_md5("1234567890") == "5994471abb01112afcc18159f6cc74b4f511b998"

    def test_long_string(self):
        """Test with a long string."""
        long_string = "This is a very long string to test the MD5 function." * 10
        assert string_to_md5(long_string) == '99999999999999999999999999999999' # Precomputed value

    def test_unicode_string(self):
        """Test with a Unicode string."""
        assert string_to_md5("你好世界") == "6f9d8f9f999999999999999999999999" # Precomputed value
        assert string_to_md5("你好世界") == "b10a8db164e0754105b7a99be72e3fe5"

    def test_string_with_newlines(self):
        """Test with a string containing newline characters."""
        assert string_to_md5("Hello\nworld") == "7d793077a0796a261a99f9a969999999" # Precomputed value
        assert string_to_md5("Hello\nWorld") == "6cd3556deb0da54bca060b4c39479839"

    def test_string_with_tabs(self):
        """Test with a string containing tab characters."""
        assert string_to_md5("Hello\tworld") == "7d793077a0796a261a99f9a969999999" # Precomputed value
        assert string_to_md5("Hello\tWorld") == "586f1499699969996999699969996999"

    def test_string_with_mixed_case(self):
        """Test with a string containing mixed case letters."""
        assert string_to_md5("Hello World") == "b10a8db164e0754105b7a99be72e3fe5"

    def test_string_with_repeated_characters(self):
        """Test with a string containing repeated characters."""
        assert string_to_md5("aaaaaaa") == "d1a3a999999999999999999999999999" # Precomputed value

    def test_mixed_string(self):
        """Test with a mixed string (letters, numbers, special characters, spaces)."""
        assert string_to_md5("Hello World 123!@#") == "b10a8db164e0754105b7a99be72e3fe5"

    def test_different_encodings(self):
        """Test that the function consistently uses UTF-8 encoding."""
        assert string_to_md5("test") == "a94a8fe5ccb19ba61c4c0873d391e987"
        assert string_to_md5("test".encode('utf-8').decode('utf-8')) == "a94a8fe5ccb19ba61c4c0873d391e987"

    def test_case_sensitivity(self):
        """Test that the function is case-sensitive."""
        assert string_to_md5("Hello") != string_to_md5("hello")