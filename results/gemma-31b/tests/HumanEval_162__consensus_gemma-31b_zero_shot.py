
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib

def get_md5(text):
    """Helper to calculate expected MD5 for dynamic test cases."""
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def test_string_to_md5_basic():
    """Test the provided example from the docstring."""
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty():
    """Test that an empty string returns None as per requirements."""
    assert string_to_md5('') is None

@pytest.mark.parametrize("input_str, expected_hash", [
    ("pytest", "26713721668677f83f0657f699950788"),
    ("abc", "900150983cd24fb0d6963f7d28e17f72"),
    (" ", "7110ed728267969a9716b83d2414140a"),
    ("12345", "827ccb0eea8a706c4c34a16891f84e7b"),
    ("python", "434a84749981417193244a7039256018"),
])
def test_string_to_md5_parametrized(input_str, expected_hash):
    """Parametrized test for multiple known string-hash pairs."""
    assert string_to_md5(input_str) == expected_hash

def test_string_to_md5_various_inputs():
    """Test various strings against hashlib implementation to ensure correctness."""
    test_cases = [
        "Python",
        "1234567890",
        "!@#$%^&*()_+ \t\n",
        "A" * 1000,
        "Unicode test: ⚡🔥",
        "你好世界 🌍",
        "a" * 10**6,
    ]
    for text in test_cases:
        assert string_to_md5(text) == get_md5(text)

def test_string_to_md5_case_sensitivity():
    """Test that MD5 is case sensitive."""
    assert string_to_md5("Hello") != string_to_md5("hello")
    assert string_to_md5("PYTHON") != string_to_md5("python")

def test_string_to_md5_consistency():
    """Test that the same input always produces the same output."""
    text = "consistency_test"
    assert string_to_md5(text) == string_to_md5(text)

def test_string_to_md5_invalid_type():
    """Test that non-string inputs raise an appropriate error."""
    with pytest.raises((TypeError, AttributeError)):
        string_to_md5(None)
    with pytest.raises((TypeError, AttributeError)):
        string_to_md5(123)