
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib

def get_expected_md5(text):
    """Helper to calculate expected MD5 for test verification."""
    return hashlib.md5(text.encode('utf-8')).hexdigest()

class TestStringToMd5:
    def test_standard_string(self):
        """Test a standard string with known output."""
        input_text = 'Hello world'
        expected = '3e25960a79dbc69b674cd4ec67a72c62'
        assert string_to_md5(input_text) == expected

    def test_empty_string(self):
        """Test that an empty string returns None as per requirements."""
        assert string_to_md5("") is None

    def test_whitespace_string(self):
        """Test that strings containing only whitespace are hashed and not treated as empty."""
        input_text = " "
        assert string_to_md5(input_text) == get_expected_md5(input_text)
        
        input_text_newline = "\n\t "
        assert string_to_md5(input_text_newline) == get_expected_md5(input_text_newline)

    def test_unicode_characters(self):
        """Test strings with non-ASCII characters (UTF-8 encoding check)."""
        input_text = "Python 🐍"
        assert string_to_md5(input_text) == get_expected_md5(input_text)
        
        input_text_chinese = "你好"
        assert string_to_md5(input_text_chinese) == get_expected_md5(input_text_chinese)

    def test_case_sensitivity(self):
        """Test that MD5 is case sensitive."""
        text_lower = "hello"
        text_upper = "HELLO"
        assert string_to_md5(text_lower) != string_to_md5(text_upper)

    def test_long_string(self):
        """Test a very long string to ensure stability."""
        input_text = "a" * 10**6  # 1 million characters
        result = string_to_md5(input_text)
        assert len(result) == 32
        assert result == get_expected_md5(input_text)

    @pytest.mark.parametrize("invalid_input", [None, 123, 45.67, [], {}])
    def test_invalid_types(self, invalid_input):
        """Test how the function handles non-string inputs (should typically raise TypeError)."""
        with pytest.raises((TypeError, AttributeError)):
            string_to_md5(invalid_input)

    def test_single_character(self):
        """Test a single character string."""
        input_text = "a"
        assert string_to_md5(input_text) == get_expected_md5(input_text)