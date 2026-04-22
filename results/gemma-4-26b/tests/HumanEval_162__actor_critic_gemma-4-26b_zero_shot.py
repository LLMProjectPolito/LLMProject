
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import hashlib
import pytest

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    if text == "":
        return None
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def test_string_to_md5_empty_string():
    """Test that an empty string returns None."""
    assert string_to_md5('') is None

def test_string_to_md5_whitespace():
    """Test strings consisting only of whitespace (should not be None)."""
    space = " "
    expected = hashlib.md5(space.encode('utf-8')).hexdigest()
    assert string_to_md5(space) == expected
    
    newline = "\n"
    expected_newline = hashlib.md5(newline.encode('utf-8')).hexdigest()
    assert string_to_md5(newline) == expected_newline

@pytest.mark.parametrize("input_text", [
    "1234567890",
    "!@#$%^&*()_+~`|}{[]:;?><,./",
    "MixedCaseWithNumbers123",
])
def test_string_to_md5_various_contents(input_text):
    """Test various types of string content using parametrization."""
    expected = hashlib.md5(input_text.encode('utf-8')).hexdigest()
    assert string_to_md5(input_text) == expected

def test_string_to_md5_unicode():
    """Test strings containing Unicode/Emoji characters."""
    unicode_text = "Python 🐍 is awesome! 🚀"
    expected = hashlib.md5(unicode_text.encode('utf-8')).hexdigest()
    assert string_to_md5(unicode_text) == expected

def test_string_to_md5_large_input():
    """Test a very large string of multi-byte characters to ensure stability."""
    large_text = "🐍" * 10**5  # 100,000 emojis
    expected = hashlib.md5(large_text.encode('utf-8')).hexdigest()
    assert string_to_md5(large_text) == expected

def test_string_to_md5_null_byte():
    """Test a string containing only a null byte."""
    null_char = "\0"
    expected = hashlib.md5(null_char.encode('utf-8')).hexdigest()
    assert string_to_md5(null_char) == expected

@pytest.mark.parametrize("invalid_input", [None, 123, b"bytes"])
def test_string_to_md5_invalid_inputs(invalid_input):
    """
    Test that non-string inputs raise a TypeError.
    Testing for TypeError ensures we are testing semantic correctness 
    rather than implementation details like .encode() behavior.
    """
    with pytest.raises(TypeError):
        string_to_md5(invalid_input)