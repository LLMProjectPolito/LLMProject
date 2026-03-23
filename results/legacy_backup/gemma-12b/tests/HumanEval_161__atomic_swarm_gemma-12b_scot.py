import pytest
import math

def test_lowercase_letters():
    assert solve("abc") == "ABC"

def test_empty_string():
    """Test with an empty string as input."""
    assert solve("") == ""

def test_solve_empty_string():
    """Test case: Empty string should return an empty string."""
    assert solve("") == ""

def test_solve_string_with_only_numbers():
    """Test case: String with only numbers should return the reversed string."""
    assert solve("12345") == "54321"

def test_solve_string_with_only_symbols():
    """Test case: String with only symbols should return the reversed string."""
    assert solve("@#$%^") == "^%$#@"

def test_solve_string_with_mixed_letters_numbers_symbols():
    """Test case: String with mixed letters, numbers, and symbols."""
    assert solve("a1@b2#c") == "A1@B2#C"

def test_solve_string_with_uppercase_letters():
    """Test case: String with only uppercase letters."""
    assert solve("ABC") == "abc"

def test_solve_string_with_lowercase_letters():
    """Test case: String with only lowercase letters."""
    assert solve("abc") == "ABC"

def test_solve_string_with_special_characters():
    """Test case: String with special characters and letters."""
    assert solve("#a@C") == "#A@c"

def test_solve_string_with_spaces():
    """Test case: String with spaces."""
    assert solve("a b c") == "A B C"