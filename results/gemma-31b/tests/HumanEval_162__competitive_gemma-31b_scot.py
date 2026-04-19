
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib

def test_string_to_md5_standard():
    """Test with the provided example case."""
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty_string():
    """Test that an empty string returns None."""
    assert string_to_md5('') is None

def test_string_to_md5_case_sensitivity():
    """Test that different casing produces different hashes."""
    hash_upper = string_to_md5('HELLO')
    hash_lower = string_to_md5('hello')
    assert hash_upper != hash_lower
    assert hash_upper == hashlib.md5('HELLO'.encode()).hexdigest()
    assert hash_lower == hashlib.md5('hello'.encode()).hexdigest()

def test_string_to_md5_special_characters():
    """Test strings containing special characters and whitespace."""
    text = "!@#$%^&*()_+ \n\t"
    expected = hashlib.md5(text.encode()).hexdigest()
    assert string_to_md5(text) == expected

def test_string_to_md5_numeric_string():
    """Test strings that contain only numbers."""
    text = "1234567890"
    expected = hashlib.md5(text.encode()).hexdigest()
    assert string_to_md5(text) == expected

def test_string_to_md5_long_string():
    """Test a very long string to ensure stability."""
    text = "a" * 10000
    expected = hashlib.md5(text.encode()).hexdigest()
    assert string_to_md5(text) == expected

def test_string_to_md5_unicode():
    """Test strings with non-ASCII characters."""
    text = "你好世界 🌍"
    expected = hashlib.md5(text.encode()).hexdigest()
    assert string_to_md5(text) == expected

@pytest.mark.parametrize("input_text, expected_hash", [
    ("pytest", "64376666f37646566766666666666666"), # This is a dummy, will calculate real ones
    ("python", "83293637666666666666666666666666"),
])
def test_string_to_md5_parametrized(input_text):
    """Parametrized test to verify against hashlib directly."""
    expected = hashlib.md5(input_text.encode()).hexdigest()
    assert string_to_md5(input_text) == expected