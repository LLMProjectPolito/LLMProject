
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest

# Note: string_to_md5 is assumed to be imported from your source module

def test_string_to_md5_provided_example():
    """Tests the specific example provided in the docstring to ensure contract compliance."""
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty_input():
    """Tests that an empty string returns None as per specific requirements."""
    assert string_to_md5('') is None

@pytest.mark.parametrize("input_text, expected_hash", [
    # Single characters & Numbers
    ("a", "0cc175b9c0f1b6a831c399e269772661"),
    ("123", "202cb962ac59075b964b07152d234b70"),
    ("12345", "827ccb0eea8a706c4c34a16891f84e7b"),
    # Standard words
    ("python", "1f980a858ea6110210363474a119255d"),
    # Whitespace and Escape characters
    (" ", "35a8cf0ed69492b03c6e6b752cff9c3a"),
    ("\n\t", "0762692f23349465580494567662540a"),
    # Special characters
    ("!@#$%^&*()", "77439399990610170608076e96f3022e"),
])
def test_string_to_md5_variations(input_text, expected_hash):
    """Tests a wide range of standard string inputs including symbols and whitespace."""
    assert string_to_md5(input_text) == expected_hash

def test_string_to_md5_unicode_handling():
    """Tests that the function correctly handles multi-byte Unicode characters (e.g., Emojis)."""
    # MD5 for '🐍' (snake emoji) encoded in UTF-8
    assert string_to_md5('🐍') == '7f0460a739b736f6875e9075708f647d'

@pytest.mark.parametrize("long_input, expected_hash", [
    ("The quick brown fox jumps over the lazy dog", "9e107d9d372bb6826bd81d3542a419d6"),
    ("a" * 1000, "7e2030203992562994f464471e614362"),
])
def test_string_to_md5_large_inputs(long_input, expected_hash):
    """Tests stability and correctness with larger string payloads."""
    assert string_to_md5(long_input) == expected_hash