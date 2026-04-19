
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib
from your_module import string_to_md5

def test_string_to_md5_basic():
    """Test the example provided in the docstring."""
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

def test_string_to_md5_empty_string():
    """Test that an empty string returns None as per requirements."""
    assert string_to_md5('') is None

def test_string_to_md5_single_character():
    """Test a single character string."""
    # md5('a') = 0cc175b9c0f1b6a831c399e269772661
    assert string_to_md5('a') == '0cc175b9c0f1b6a831c399e269772661'

def test_string_to_md5_case_sensitivity():
    """Test that the hash is case sensitive."""
    hash_upper = string_to_md5('HELLO')
    hash_lower = string_to_md5('hello')
    assert hash_upper != hash_lower
    assert hash_upper == hashlib.md5('HELLO'.encode()).hexdigest()
    assert hash_lower == hashlib.md5('hello'.encode()).hexdigest()

def test_string_to_md5_numeric_string():
    """Test strings containing only numbers."""
    assert string_to_md5('1234567890') == hashlib.md5('1234567890'.encode()).hexdigest()

def test_string_to_md5_unicode_characters():
    """Test strings with unicode/special characters."""
    text = 'Pytest 🚀 Unicode Test'
    assert string_to_md5(text) == hashlib.md5(text.encode()).hexdigest()

def test_string_to_md5_long_string():
    """Test a very long string to ensure stability."""
    text = "a" * 10000
    assert string_to_md5(text) == hashlib.md5(text.encode()).hexdigest()

def test_string_to_md5_whitespace():
    """Test strings with various whitespace characters."""
    text = ' \t\n '
    assert string_to_md5(text) == hashlib.md5(text.encode()).hexdigest()

@pytest.mark.parametrize("input_text, expected_hash", [
    ("python", "64733333460126681469696969696969"), # This is a placeholder, using hashlib for dynamic check
])
def test_string_to_md5_parametrized(input_text, expected_hash):
    """Parametrized test for multiple inputs."""
    assert string_to_md5(input_text) == hashlib.md5(input_text.encode()).hexdigest()