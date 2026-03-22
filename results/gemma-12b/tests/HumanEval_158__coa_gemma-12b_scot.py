import pytest
import math


# Focus: Boundary Values
def test_find_max_empty_list():
    """Test with an empty list - boundary condition."""
    assert find_max([]) == ""

def test_find_max_single_word():
    """Test with a list containing only one word - boundary condition."""
    assert find_max(["hello"]) == "hello"

def test_find_max_same_unique_chars_lexicographical():
    """Test when multiple words have the same number of unique chars, check lexicographical order."""
    assert find_max(["abc", "bca", "cab"]) == "abc"

# Focus: Type Scenarios
def test_find_max_empty_list():
    """Test case: Empty list input."""
    assert find_max([]) == ""

def test_find_max_single_word():
    """Test case: List with a single word."""
    assert find_max(["hello"]) == "hello"

def test_find_max_multiple_words_different_unique_chars():
    """Test case: Multiple words with different number of unique characters."""
    assert find_max(["name", "of", "string"]) == "string"

# Focus: Logic Branches
def test_find_max_different_unique_chars():
    """Test case where words have different number of unique characters."""
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_same_unique_chars_lexicographical():
    """Test case where words have the same number of unique characters,
    lexicographical order should be considered."""
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_all_same_char():
    """Test case where all words have the same character repeated."""
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"