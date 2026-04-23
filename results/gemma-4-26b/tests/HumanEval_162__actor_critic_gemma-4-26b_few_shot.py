
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest

# --- Problem 1: is_palindrome ---

@pytest.mark.parametrize("input_str, expected", [
    ("radar", True),          # Standard palindrome
    ("hello", False),         # Standard non-palindrome
    ("", True),               # Empty string
    ("a", True),              # Single character
    ("racecar", True),        # Standard palindrome
    ("Racecar", False),       # Case sensitivity check (standard behavior)
    ("12321", True),          # Numeric string
    ("step on no pets", True) # Palindrome with spaces
])
def test_is_palindrome(input_str, expected):
    """Tests various string patterns for palindrome properties."""
    from your_module import is_palindrome # Replace with actual import
    assert is_palindrome(input_str) == expected


# --- Problem 2: get_max ---

@pytest.mark.parametrize("input_list, expected", [
    ([1, 2, 3], 3),           # Positive integers
    ([1, 5, 3, 5], 5),        # Duplicate maximums
    ([-1, -5, -2], -1),       # All negative integers
    ([-10, 0, 10], 10),       # Mixed positive and negative
    ([42], 42),               # Single element
])
def test_get_max_valid_lists(input_list, expected):
    """Tests get_max with various valid integer lists."""
    from your_module import get_max
    assert get_max(input_list) == expected

def test_get_max_empty():
    """Tests that an empty list returns None."""
    from your_module import get_max
    assert get_max([]) is None


# --- Problem 3: string_to_md5 ---

@pytest.mark.parametrize("input_text, expected_hash", [
    ("Hello world", "3e25960a79dbc69b674cd4ec67a72c62"),
    ("python", "1f3870be274f6c49b3e31a0c6728957f"),
    (" ", "3f794d17ba8e44721b91001013002011"), # Space character
])
def test_string_to_md5_valid(input_text, expected_hash):
    """Tests standard string inputs against known MD5 hashes."""
    from your_module import string_to_md5
    assert string_to_md5(input_text) == expected_hash

def test_string_to_md5_empty():
    """Tests that an empty string returns None as per requirements."""
    from your_module import string_to_md5
    assert string_to_md5("") is None