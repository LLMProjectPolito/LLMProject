
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib
from your_module import string_to_md5  # Replace 'your_module' with actual filename

@pytest.mark.parametrize("input_str, expected_hash", [
    ("Hello world", "3e25960a79dbc69b674cd4ec67a72c62"),
    ("a", "0cc175b9c0f1b6a831c399e269772661"),
    ("12345", "827ccb0eea8a706c4c34a16891f84e7b"),
    ("Python", "118e371390817c4c872e4685b4e62291"),
])
def test_known_mappings(input_str, expected_hash):
    """Verify specific, known string-to-md5 mappings to ensure ground-truth accuracy."""
    assert string_to_md5(input_str) == expected_hash

def test_empty_string_behavior():
    """Verify that an empty string returns None, as per specific business logic."""
    assert string_to_md5("") is None

@pytest.mark.parametrize("input_str", [
    " ",                          # Single space
    "   ",                        # Multiple spaces
    "\n\t\r",                     # Whitespace characters
    "1234567890",                 # Numeric string
    "Complex!@#$%^&*()_+",        # Special characters
    "Python testing 101",         # Sentence
    "こんにちは",                   # Japanese Unicode
    "你好",                       # Chinese Unicode
    "🚀✨🔥",                     # Emojis (Multi-byte)
    "a" * 1000,                   # Medium input
    "a" * 10000,                  # Large input
])
def test_string_variations_against_hashlib(input_str):
    """
    Verify a wide range of string types against the standard hashlib implementation.
    This ensures correct encoding (UTF-8) and handling of whitespace/special chars.
    """
    expected_hash = hashlib.md5(input_str.encode('utf-8')).hexdigest()
    assert string_to_md5(input_str) == expected_hash

@pytest.mark.parametrize("invalid_input", [
    123,                          # Integer
    None,                         # NoneType
    ["list", "of", "strings"],    # List
    {"key": "value"},             # Dictionary
    1.23,                         # Float
])
def test_invalid_input_types(invalid_input):
    """Verify that passing non-string types raises a TypeError."""
    with pytest.raises(TypeError):
        string_to_md5(invalid_input)  # type: ignore

def test_consistency():
    """Verify that the function is deterministic (idempotent)."""
    text = "consistency_test_string_123!@#"
    first_call = string_to_md5(text)
    second_call = string_to_md5(text)
    assert first_call == second_call
    assert first_call is not None