import pytest
import math

def test_find_max_typical():
    words = ["name", "of", "string"]
    assert find_max(words) == "string"

def test_empty_input():
    """Test with an empty list of words."""
    from solution import find_max
    assert find_max([]) == ""

def test_find_max_empty_list():
    """Test case: Empty list should return an empty string."""
    assert find_max([]) == ""

def test_find_max_list_with_empty_string():
    """Test case: List containing an empty string."""
    assert find_max([""]) == ""

def test_find_max_list_with_duplicate_unique_chars():
    """Test case: List with words having the same number of unique characters,
    lexicographical order should be considered."""
    assert find_max(["abc", "bca", "cab"]) == "abc"

def test_find_max_list_with_special_characters():
    """Test case: List with words containing special characters."""
    assert find_max(["!@#", "abc", "def"]) == "!@#"

def test_find_max_list_with_numbers():
    """Test case: List with words containing numbers."""
    assert find_max(["123", "abc", "def"]) == "abc"