
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

def test_find_max_basic():
    """Test basic functionality with provided examples."""
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

@pytest.mark.parametrize("words, expected", [
    # Tie-breaker: Lexicographical order
    (["apple", "pear"], "apple"),  # Both have 4 unique chars, 'apple' < 'pear'
    (["abc", "cba", "bac"], "abc"), # All have 3 unique chars, 'abc' is first
    (["zebra", "apple"], "zebra"),  # zebra(5) > apple(4)
    
    # Edge Case: Empty strings
    (["", ""], ""),
    (["", "a"], "a"),
    (["a", ""], "a"),
    
    # Edge Case: Single element list
    (["hello"], "hello"),
    ([""], ""),
    
    # Edge Case: All characters identical
    (["aaaaa", "bb", "ccc"], "aaaaa"), # All have 1 unique char, 'aaaaa' is first
    
    # Edge Case: Mixed lengths, same unique count
    (["abcdef", "abc"], "abcdef"), # abcdef(6) > abc(3)
    (["abc", "def"], "abc"),       # Both 3, 'abc' < 'def'
    
    # Case sensitivity (Python default: 'A' < 'a')
    (["Apple", "apple"], "Apple"), # Both 4 unique, 'Apple' < 'apple'
])
def test_find_max_parametrized(words, expected):
    assert find_max(words) == expected

def test_find_max_empty_list():
    """Test behavior with an empty list. 
    Depending on implementation, this might raise an error or return None/empty.
    Assuming the function should handle it or the input is guaranteed non-empty.
    """
    with pytest.raises(Exception):
        # Most implementations using max() on empty list without default will raise ValueError
        find_max([])

def test_find_max_special_characters():
    """Test with strings containing numbers or symbols."""
    assert find_max(["123", "abc", "!!!"], "!!!") # All 3 unique, '!!!' < '123' < 'abc'
    assert find_max(["a1b2", "c3d4"], "a1b2")     # Both 4 unique, 'a1b2' < 'c3d4'