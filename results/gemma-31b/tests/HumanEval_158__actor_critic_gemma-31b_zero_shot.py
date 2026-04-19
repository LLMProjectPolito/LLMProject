
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
    Returns the word with the maximum number of unique characters. 
    If multiple strings have the same maximum, returns the lexicographically first one.
    """
    if not words:
        return None
    
    # Sort lexicographically first to ensure that max() returns the first 
    # occurrence among ties (since max() is stable in Python).
    sorted_words = sorted(words)
    return max(sorted_words, key=lambda w: len(set(w)))

@pytest.mark.parametrize("input_words, expected", [
    # Provided examples
    (["name", "of", "string"], "string"),
    (["name", "enam", "game"], "enam"),
    (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
    
    # Tie-breaking: Same unique count, different lexicographical order
    (["apple", "pear"], "apple"),  # both have 4 unique chars, 'apple' < 'pear'
    (["zebra", "apple"], "apple"), # both have 5 unique chars, 'apple' < 'zebra'
    
    # Edge Case: Empty strings
    (["", "a"], "a"),
    (["", ""], ""),
    
    # Edge Case: Single character strings
    (["a", "b", "c"], "a"),
    
    # Edge Case: Case sensitivity (A and a are different unique characters)
    (["Aa", "B"], "Aa"), # 'Aa' has 2 unique, 'B' has 1
    (["Apple", "apple"], "Apple"), # Both have 4 unique ('A','p','l','e' vs 'a','p','l','e'), 'Apple' < 'apple'
    
    # Edge Case: Special characters and numbers
    (["123", "abc"], "123"), # Both 3 unique, '123' < 'abc'
    (["!@#", "$%^"], "!@#"), # Both 3 unique, '!' < '$'
    
    # Edge Case: All words identical
    (["test", "test", "test"], "test"),
    
    # Edge Case: Words with all same characters but different lengths
    (["aaaaa", "bb"], "aaaaa"), # Both 1 unique, 'aaaaa' < 'bb'
])
def test_find_max_scenarios(input_words, expected):
    assert find_max(input_words) == expected

def test_find_max_empty_list():
    """Test behavior when an empty list is provided."""
    assert find_max([]) is None

def test_find_max_single_element():
    """Test behavior with a list containing only one element."""
    assert find_max(["hello"]) == "hello"