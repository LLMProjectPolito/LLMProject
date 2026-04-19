
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib

# The function string_to_md5 is assumed to be imported or defined in the environment.
# From the prompt, we are not redefining it here.

def get_expected_md5(text):
    """Helper to calculate ground truth MD5 hash."""
    return hashlib.md5(text.encode('utf-8')).hexdigest()

class TestStringToMd5:
    
    def test_provided_example(self):
        """Verify the example provided in the docstring."""
        input_text = 'Hello world'
        expected = '3e25960a79dbc69b674cd4ec67a72c62'
        assert string_to_md5(input_text) == expected

    def test_empty_string(self):
        """Verify that an empty string returns None as per requirements."""
        assert string_to_md5("") is None

    def test_case_sensitivity(self):
        """Verify that MD5 hashes are case-sensitive."""
        text_upper = "PYTHON"
        text_lower = "python"
        assert string_to_md5(text_upper) != string_to_md5(text_lower)
        assert string_to_md5(text_upper) == get_expected_md5(text_upper)
        assert string_to_md5(text_lower) == get_expected_md5(text_lower)

    @pytest.mark.parametrize("special_text", [
        " ",                # Single space
        "Hello\nWorld",     # Newline
        "Special characters: !@#$%^&*()_+", # Symbols
        "🚀 Emoji Test 🌟",  # Unicode/Emojis
        "中文测试",           # Non-Latin characters
    ])
    def test_special_characters(self, special_text):
        """Verify handling of various special characters and encodings."""
        assert string_to_md5(special_text) == get_expected_md5(special_text)

    def test_long_string(self):
        """Verify the function handles very large strings."""
        long_text = "a" * 10**6  # 1 million characters
        assert string_to_md5(long_text) == get_expected_md5(long_text)

    def test_consistency(self):
        """Verify that the function is deterministic."""
        text = "Consistency Check"
        result1 = string_to_md5(text)
        result2 = string_to_md5(text)
        assert result1 == result2

    @pytest.mark.parametrize("invalid_input", [
        None,
        123,
        45.67,
        ["list"],
        {"key": "val"},
    ])
    def test_invalid_input_types(self, invalid_input):
        """
        Verify that non-string inputs raise an appropriate error.
        Since the docstring says 'Given a string', passing other types 
        should typically raise a TypeError or AttributeError.
        """
        with pytest.raises((TypeError, AttributeError)):
            string_to_md5(invalid_input)