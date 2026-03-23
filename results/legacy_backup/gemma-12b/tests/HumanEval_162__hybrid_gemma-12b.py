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


class TestStringtoMD5:
    """
    Pytest suite for the string_to_md5 function.
    """

    def test_valid_string(self):
        """Test with a standard string."""
        assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

    def test_empty_string(self):
        """Test with an empty string - should return None."""
        assert string_to_md5("") is None

    def test_string_with_spaces(self):
        """Test with a string containing only spaces."""
        assert string_to_md5("   ") == "d41d8cd98f00b204e9800998ecf8427e"

    def test_string_with_special_characters(self):
        """Test with a string containing special characters."""
        assert string_to_md5("!@#$%^&*()") == "9469a999999999999999999999999999"

    def test_string_with_unicode_characters(self):
        """Test with a string containing Unicode characters."""
        assert string_to_md5("你好世界") == "a94a8fe5ccb19ba61c4c0873d391e987"

    def test_string_with_numbers(self):
        """Test with a string containing numbers."""
        assert string_to_md5("1234567890") == "d1e2f3e4d5e6f7e8d9e0f1e2d3e4f5e6"

    def test_string_with_mixed_characters(self):
        """Test with a string containing a mix of characters."""
        assert string_to_md5("Hello123World!") == "92999999999999999999999999999999"

    def test_long_string(self):
        """Test with a long string to ensure no buffer issues."""
        long_string = "This is a very long string to test the function with.  It should handle it without any errors." * 10
        expected_md5 = hashlib.md5(long_string.encode('utf-8')).hexdigest()
        assert string_to_md5(long_string) == expected_md5

    def test_string_with_newline_characters(self):
        """Test with a string containing newline characters."""
        assert string_to_md5("Hello\nWorld") == "1d995399334169996153639999999999"

    def test_string_with_tab_characters(self):
        """Test with a string containing tab characters."""
        assert string_to_md5("Hello\tWorld") == "99999999999999999999999999999999"

    def test_string_with_carriage_return(self):
        """Test with a string containing carriage return characters."""
        assert string_to_md5("Hello\rWorld") == "99999999999999999999999999999999"

    def test_string_with_utf8_encoded_characters(self):
        """Test with a string that is already UTF-8 encoded."""
        encoded_string = "Test string".encode('utf-8').decode('utf-8')
        assert string_to_md5(encoded_string) == "e5d7a999999999999999999999999999"

    def test_string_with_leading_and_trailing_whitespace(self):
        """Test with a string that has leading and trailing whitespace."""
        assert string_to_md5("  Test string  ") == "99999999999999999999999999999999"