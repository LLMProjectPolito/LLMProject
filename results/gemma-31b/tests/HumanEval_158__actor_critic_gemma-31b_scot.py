
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
from solution import find_max

@pytest.mark.parametrize("words, expected", [
    # Provided examples
    (["name", "of", "string"], "string"),
    (["name", "enam", "game"], "enam"),
    (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
    
    # Tie-break: Same unique count, different lexicographical order
    (["apple", "pear"], "apple"), # apple: {a,p,l,e}=4, pear: {p,e,a,r}=4. 'apple' < 'pear'
    (["abc", "abd", "abe"], "abc"), # All have 3 unique. 'abc' is smallest.
    
    # Logic Correction: Max unique count
    (["zebra", "apple"], "zebra"), # zebra: 5 unique, apple: 4 unique.
    
    # Single unique character variations
    (["zzzz", "yyyy", "xxxx"], "xxxx"), # All have 1 unique. 'xxxx' is smallest.
    (["a", "b", "c"], "a"),
    
    # Mixed lengths, same unique count (Redundancy removed)
    (["abcdef", "abcdefffff"], "abcdef"), # Both have 6 unique. 'abcdef' < 'abcdefffff'
    
    # Case sensitivity (Python sets treat 'A' and 'a' as different)
    (["Aa", "B"], "Aa"), # "Aa" has 2 unique, "B" has 1.
    (["aB", "Ab"], "Ab"), # Both have 2 unique. "Ab" < "aB" (Uppercase < Lowercase)
    
    # Logic Correction: Special characters and numbers
    (["123", "abc", "!!!"], "123"), # "123": 3, "abc": 3, "!!!": 1. '123' < 'abc'
    ([" ", "  ", "   "], " "), # All have 1 unique. " " is smallest.
    
    # Edge Case: Duplicate identical strings
    (["apple", "apple"], "apple"),
])
def test_find_max_scenarios(words, expected):
    """Tests various scenarios including provided examples, corrected logic, and edge cases."""
    assert find_max(words) == expected

def test_find_max_single_element():
    """Test with a list containing only one string."""
    assert find_max(["hello"]) == "hello"

def test_find_max_empty_string_in_list():
    """Test with lists containing empty strings."""
    # Empty string has 0 unique chars. "a" has 1.
    assert find_max(["", "a"]) == "a"
    # Both empty strings have 0 unique chars.
    assert find_max(["", ""]) == ""

def test_find_max_empty_list():
    """Test behavior with an empty list."""
    # Standard max() on empty sequence raises ValueError.
    with pytest.raises((ValueError, TypeError)):
        find_max([])