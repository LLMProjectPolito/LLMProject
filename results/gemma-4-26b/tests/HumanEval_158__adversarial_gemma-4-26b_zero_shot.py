
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

import pytest

def find_max(words):
    """
    Implementation provided for context to allow the test suite to run.
    The actual implementation is what we are testing.
    """
    if not words:
        return None
    
    # Calculate unique character counts
    # Tie-breaker: Lexicographical order (min string)
    # We want max(unique_count), then min(lexicographical)
    # A common trick is to use a key that maximizes unique count and minimizes string value
    return max(words, key=lambda w: (len(set(w)), [-ord(c) for c in w])) 
    # Note: The above is a placeholder logic. The test suite is designed to 
    # catch if the implementation fails the specific requirements.

# --- Robust Pytest Suite ---

def test_docstring_examples():
    """Verify the examples provided in the problem description."""
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_empty_list():
    """Test behavior when the input list is empty."""
    # Depending on requirements, this could return None or raise ValueError.
    # A robust function should handle this gracefully.
    assert find_max([]) is None

def test_single_element():
    """Test a list containing only one string."""
    assert find_max(["hello"]) == "hello"
    assert find_max([""]) == ""

def test_all_empty_strings():
    """Test a list containing only empty strings."""
    assert find_max(["", "", ""]) == ""

def test_tie_breaker_lexicographical():
    """
    Test that if unique counts are equal, the lexicographically 
    smallest string is returned.
    """
    # All have 3 unique characters
    # "abc" < "def" < "ghi"
    assert find_max(["ghi", "def", "abc"]) == "abc"
    # "apple" (a,p,l,e = 4) vs "apply" (a,p,l,y = 4)
    # "apple" comes first lexicographically
    assert find_max(["apply", "apple"]) == "apple"

def test_tie_breaker_different_lengths_same_unique():
    """
    Test tie-breaking when strings have different lengths but 
    the same number of unique characters.
    """
    # "aabbcc" (3 unique) vs "abc" (3 unique)
    # "aabbcc" vs "abc" -> "aabbcc" is lexicographically smaller? 
    # No, 'a'=='a', 'a' < 'b', so "aabbcc" < "abc"
    assert find_max(["abc", "aabbcc"]) == "aabbcc"

def test_case_sensitivity():
    """
    Test that the function respects case sensitivity in lexicographical order.
    In ASCII, 'A' (65) < 'a' (97).
    """
    # Both have 1 unique character. 'A' < 'a'.
    assert find_max(["a", "A"]) == "A"
    # "Abc" (3 unique) vs "abc" (3 unique). "Abc" < "abc"
    assert find_max(["abc", "Abc"]) == "Abc"

def test_special_characters_and_numbers():
    """Test strings containing numbers and symbols."""
    # "123" (3 unique) vs "111" (1 unique)
    assert find_max(["111", "123"]) == "123"
    # "!@#" (3 unique) vs "#@!" (3 unique)
    # "!@#" comes first lexicographically
    assert find_max(["#@!", "!@#"]) == "!@#"

def test_large_input():
    """Test with a larger dataset to ensure performance and correctness."""
    words = ["a" * i for i in range(1, 100)] # 1 unique char each
    # All have 1 unique char. Lexicographically, "a" is the smallest.
    assert find_max(words) == "a"
    
    words_mixed = ["abcde", "fghij", "aaaaa", "bbbbb"]
    # "abcde" and "fghij" both have 5. "abcde" < "fghij".
    assert find_max(words_mixed) == "abcde"

def test_duplicate_words():
    """Test list containing duplicate words."""
    assert find_max(["apple", "banana", "apple"]) == "banana"
    assert find_max(["test", "test", "test"]) == "test"