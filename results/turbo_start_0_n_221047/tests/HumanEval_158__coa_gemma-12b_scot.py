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
    """Test when multiple words have the same number of unique chars,
    lexicographical order should be considered - boundary condition."""
    assert find_max(["abc", "bca", "cab"]) == "abc"

# Focus: Type Scenarios
def test_find_max_empty_list():
    """Test case: Empty list input."""
    assert find_max([]) == ""

def test_find_max_single_word():
    """Test case: List with a single word."""
    assert find_max(["hello"]) == "hello"

def test_find_max_multiple_words_different_unique_chars():
    """Test case: Multiple words with different unique character counts."""
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_multiple_words_same_unique_chars_lexicographical():
    """Test case: Multiple words with the same unique character count, lexicographical order."""
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_words_with_repeated_chars():
    """Test case: Words with repeated characters."""
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"

# Focus: Logic Branches
def test_find_max_different_unique_chars():
    """Test case where words have different numbers of unique characters."""
    words = ["name", "of", "string"]
    assert find_max(words) == "string"

def test_find_max_same_unique_chars_lexicographical():
    """Test case where words have the same number of unique characters,
    but lexicographical order matters."""
    words = ["name", "enam", "game"]
    assert find_max(words) == "enam"

def test_find_max_all_same_char():
    """Test case where all words have the same character repeated."""
    words = ["aaaaaaa", "bb", "cc"]
    assert find_max(words) == "aaaaaaa"