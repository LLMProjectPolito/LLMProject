
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib
from your_module import string_to_md5

@pytest.mark.parametrize("input_text, expected_output", [
    ("Hello world", "3e25960a79dbc69b674cd4ec67a72c62"),
    ("", None),
    ("pytest", hashlib.md5("pytest".encode()).hexdigest()),
    ("1234567890", hashlib.md5("1234567890".encode()).hexdigest()),
    (" ", hashlib.md5(" ".encode()).hexdigest()),
    ("!@#$%^&*()_+", hashlib.md5("!@#$%^&*()_+".encode()).hexdigest()),
    ("Special characters: \n\t\r", hashlib.md5("Special characters: \n\t\r".encode()).hexdigest()),
    ("Unicode test: ⚡️🔥", hashlib.md5("Unicode test: ⚡️🔥".encode()).hexdigest()),
    ("A" * 1000, hashlib.md5(("A" * 1000).encode()).hexdigest()),
])
def test_string_to_md5_valid_cases(input_text, expected_output):
    """Test various string inputs including empty, special characters, and unicode."""
    assert string_to_md5(input_text) == expected_output

def test_string_to_md5_none_input():
    """Test how the function handles None input if passed, though docstring specifies string."""
    with pytest.raises(AttributeError):
        string_to_md5(None)

def test_string_to_md5_type_consistency():
    """Ensure the output is either a string or None."""
    result = string_to_md5("test")
    assert isinstance(result, str)
    
    result_empty = string_to_md5("")
    assert result_empty is None