
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib

# The function is assumed to be in the same module or imported
# from implementation import string_to_md5

def test_string_to_md5_standard_case():
    """Test the provided example in the docstring."""
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty_string():
    """Requirement: If 'text' is an empty string, return None."""
    assert string_to_md5('') is None

def test_string_to_md5_unicode_characters():
    """Test handling of multi-byte Unicode characters (UTF-8)."""
    text = "🚀 Blue Team 🛡️"
    expected = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected

def test_string_to_md5_special_characters():
    """Test strings with whitespace, newlines, and symbols."""
    text = "line1\nline2\tspace  !@#$%^&*()"
    expected = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected

def test_string_to_md5_large_input():
    """Test performance and correctness with a large string."""
    text = "a" * 1_000_000  # 1MB string
    expected = hashlib.md5(text.encode('utf-8')).hexdigest()
    assert string_to_md5(text) == expected

@pytest.mark.parametrize("invalid_input", [
    123,            # Integer
    None,           # NoneType
    ["string"],     # List
    {"key": "val"}, # Dict
    4.5             # Float
])
def test_string_to_md5_type_safety(invalid_input):
    """
    Blue Team Check: Ensure the function raises a TypeError 
    when non-string inputs are provided, preventing unexpected behavior.
    """
    with pytest.raises(TypeError):
        string_to_md5(invalid_input)

def test_string_to_md5_case_sensitivity():
    """MD5 is sensitive to case; ensure 'A' and 'a' produce different hashes."""
    hash_upper = string_to_md5("ABC")
    hash_lower = string_to_md5("abc")
    assert hash_upper != hash_lower